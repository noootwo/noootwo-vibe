#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path

from validate_noootwo_readiness import validate_capture_file


PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
USER_DELEGATED_RE = re.compile(r"user delegated choice to agent\s*:\s*(?:yes|true|delegated)", re.IGNORECASE)
APPROVED_RE = re.compile(r"approved by user\s*:\s*(?:yes|true|approved)", re.IGNORECASE)
PLAN_APPROVED_RE = re.compile(r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)", re.IGNORECASE)
INTERVENTION_VALUES = {"leave simple", "craft only", "add moment"}
COMPARED_DIRECTION_RE = re.compile(
    r"^##\s+Compared Direction\s+\d+\s*\n(.*?)(?=^##\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
SOURCE_BLOCK_RE = re.compile(r"^##\s+(?:Optional\s+)?Source\b.*$", re.IGNORECASE | re.MULTILINE)


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_unresolved(content: str) -> bool:
    return bool(PENDING_RE.search(content) or TBD_RE.search(content) or not content.strip())


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def has_value(content: str, label: str) -> bool:
    pattern = re.compile(
        rf"^\s*-\s*{re.escape(label)}\s*:\s*(?!\s*(?:TBD|pending|none|no|blocked|not selected yet)\s*$).+\S",
        re.IGNORECASE | re.MULTILINE,
    )
    return bool(pattern.search(content))


def field_value(content: str, label: str) -> str | None:
    pattern = re.compile(
        rf"^\s*-\s*{re.escape(label)}\s*:\s*(.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(content)
    if not match:
        return None
    return match.group(1).strip()


def has_recorded_value(content: str, label: str) -> bool:
    value = (field_value(content, label) or "").strip()
    return bool(value) and "TBD" not in value.upper() and value.lower() not in {"pending", "blocked"}


def local_artifact_exists(root: Path, value: str) -> bool:
    clean = value.strip().strip("`")
    if re.match(r"^https?://", clean, re.IGNORECASE):
        return True
    return (root / clean).exists()


def validate_direction_sample_records(root: Path, directions: str) -> list[str]:
    errors: list[str] = []
    blocks = list(COMPARED_DIRECTION_RE.finditer(directions))
    require(errors, len(blocks) >= 3, "directions compare fewer than 3 paths")
    for index, match in enumerate(blocks, start=1):
        block = match.group(1)
        sample_path = (field_value(block, "Low-cost sample path") or "").strip()
        sample_proves = (field_value(block, "What the sample proves") or "").strip()
        inspected = (field_value(block, "Sample inspected") or "").strip().lower()
        require(errors, bool(sample_path) and "TBD" not in sample_path.upper(), f"direction {index} missing low-cost sample path")
        require(errors, bool(sample_proves) and "TBD" not in sample_proves.upper(), f"direction {index} missing what the sample proves")
        require(errors, inspected.startswith(("yes", "viewed")), f"direction {index} sample was not inspected")
        if sample_path:
            require(errors, local_artifact_exists(root, sample_path), f"direction {index} sample path does not exist: {sample_path}")
    return errors


def validate_source_records(root: Path, board: str) -> list[str]:
    errors: list[str] = []
    blocks = SOURCE_BLOCK_RE.split(board)[1:]
    require(errors, len(blocks) >= 3, "reference board has fewer than 3 sources")
    for index, block in enumerate(blocks, start=1):
        for label in ("Same-medium fit", "Artifact inspected", "Observed evidence", "Borrowed mechanism"):
            require(errors, has_recorded_value(block, label), f"reference source {index} missing {label.lower()}")
        inspected = (field_value(block, "Artifact inspected") or "").strip().lower()
        capture = (field_value(block, "Capture path") or "").strip().strip("`")
        if capture and capture.lower() not in {"unreachable", "none", "url-only", "url only", "blocked", "login required"}:
            capture_error = validate_capture_file((root / capture).resolve())
            require(errors, capture_error is None, f"reference source {index} capture {capture_error or 'is invalid'}: {capture}")
            require(errors, inspected.startswith("yes"), f"reference source {index} capture was not inspected")
    return errors


def validate_aesthetic_review(review: str) -> list[str]:
    errors: list[str] = []
    safety = (field_value(review, "Safety hard-gate result") or "").strip()
    evidence = (field_value(review, "Evidence of harm or intentional use") or "").strip()
    require(errors, bool(safety) and "TBD" not in safety.upper(), "review missing safety hard-gate result")
    require(errors, has_recorded_value(review, "Aesthetic flags"), "review missing aesthetic flags")
    require(errors, bool(evidence) and "TBD" not in evidence.upper(), "review missing aesthetic harm or intentional-use evidence")

    decision = (field_value(review, "Decision") or "").strip().lower()
    ready = decision.startswith("ready")
    if ready:
        require(errors, safety.lower().startswith("pass"), "ready review cannot fail the safety hard gate")
        lowered = evidence.lower()
        harmful = bool(
            re.search(r"(observed|demonstrated|confirmed|actual)\s+(harm|damage)", lowered)
            or re.search(r"(breaks?|damages?|weakens?)\s+(hierarchy|readability|brand fit|cohesion)", lowered)
        )
        negated = "no demonstrated harm" in lowered or "no observed harm" in lowered or "without harm" in lowered
        require(errors, not harmful or negated, "ready review records aesthetic harm without a passing resolution")
    return errors


def intervention_value(review: str) -> str:
    return (field_value(review, "Intervention decision") or "").strip().lower()


def validate_intervention_record(review: str, expected: str) -> list[str]:
    errors: list[str] = []
    decision = intervention_value(review)
    user_intent = (field_value(review, "User motion intent") or "").strip().lower()
    accepted_no_motion = (field_value(review, "User accepted no authored motion") or "").strip().lower()
    require(errors, decision in INTERVENTION_VALUES, "review intervention decision must be leave simple, craft only, or add moment")
    require(errors, decision == expected, f"review intervention decision must be {expected}")
    require(errors, user_intent in {"requested", "not requested", "declined"}, "review user motion intent must be requested, not requested, or declined")
    require(errors, accepted_no_motion in {"yes", "no", "not applicable", "n/a"}, "review user accepted no authored motion must be yes, no, or not applicable")
    require(
        errors,
        not (user_intent == "requested" and decision != "add moment" and accepted_no_motion != "yes"),
        f"review explicit motion request cannot use {decision or 'an invalid decision'} without the user accepting no authored motion",
    )
    require(errors, has_value(review, "Decision rationale"), "review missing intervention decision rationale")
    require(errors, has_value(review, "Candidate moments and rejected opportunities"), "review missing candidate and rejected opportunity record")
    require(errors, has_value(review, "Intervention fit"), "review missing intervention fit")

    if expected in {"leave simple", "craft only"}:
        require(errors, has_value(review, "Craft sufficiency evidence"), f"review missing craft evidence for {expected}")
    if expected == "add moment":
        authored = (field_value(review, "Authored move") or "").strip().lower()
        require(errors, authored not in {"", "none", "not applicable", "n/a", "tbd"}, "review missing authored move for add moment")
        require(errors, has_value(review, "Authored move evidence and fallback"), "review missing authored move evidence and fallback")
        tool = (field_value(review, "Motion trigger and implementation tool") or "").strip().lower()
        require(errors, tool not in {"", "none", "not applicable", "n/a", "tbd"}, "review missing motion trigger and implementation tool for add moment")
        library_decision = (field_value(review, "Library or material decision") or "").strip().lower()
        require(errors, library_decision not in {"", "none", "not applicable", "n/a", "tbd"}, "review missing library or material decision for add moment")
    return errors


def eval_leave_simple_justified(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    return validate_intervention_record(review, "leave simple")


def eval_craft_only_justified(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    return validate_intervention_record(review, "craft only")


def eval_add_moment_proof(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    return validate_intervention_record(review, "add moment")


def eval_explicit_motion_request_honored(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    errors = validate_intervention_record(review, "add moment")
    user_intent = (field_value(review, "User motion intent") or "").strip().lower()
    if user_intent != "requested":
        errors.append("explicit-motion-request-honored requires User motion intent: requested")
    return errors


def eval_missing_exploration(root: Path) -> list[str]:
    errors: list[str] = []
    brief = read(root, ".noootwo/brief.md")
    require(errors, bool(brief), "missing .noootwo/brief.md")
    require(errors, not has_unresolved(brief), ".noootwo/brief.md unresolved")
    require(errors, "classification" in brief.lower(), "brief classification missing")
    require(errors, has_value(brief, "What needs to be made or changed"), "brief objective missing")
    require(errors, has_value(brief, "Product, brand, stack, runtime, or content constraints found during exploration"), "brief discovered constraints missing")
    require(errors, has_value(brief, "High-impact unknowns that can materially change the result"), "brief unresolved uncertainty missing")
    return errors


def eval_missing_user_decision(root: Path) -> list[str]:
    errors: list[str] = []
    directions = read(root, ".noootwo/directions.md")
    require(errors, bool(directions), "missing .noootwo/directions.md")
    require(errors, not has_unresolved(directions), ".noootwo/directions.md unresolved")
    require(errors, directions.lower().count("compared direction") >= 3, "directions compare fewer than 3 paths")
    require(errors, has_value(directions, "Why multiple reasonable directions exist"), "directions do not justify why comparison was needed")
    decision_recorded = (
        has_value(directions, "User selected direction")
        or has_value(directions, "User selected option")
        or USER_DELEGATED_RE.search(directions) is not None
    )
    require(errors, decision_recorded, "directions missing user decision or delegated choice")
    return errors


def eval_artifact_not_reviewable(root: Path) -> list[str]:
    errors: list[str] = []
    review = read(root, ".noootwo/review.md")
    require(errors, bool(review), "missing .noootwo/review.md")
    require(errors, not has_unresolved(review), ".noootwo/review.md unresolved")
    require(errors, has_value(review, "Artifact reviewed"), "review missing artifact reviewed line")
    require(errors, has_value(review, "URL, screenshot path, preview, simulator, recording, or accepted limitation"), "review missing artifact evidence")
    require(errors, has_value(review, "Viewports/devices reviewed"), "review missing viewport/device evidence")
    return errors


def eval_generic_drift(root: Path) -> list[str]:
    errors: list[str] = []
    review = read(root, ".noootwo/review.md")
    require(errors, bool(review), "missing .noootwo/review.md")
    require(errors, "generic drift checks" in review.lower(), "review generic drift checks missing")
    require(errors, has_value(review, "Generic fallback signs found"), "review missing generic fallback diagnosis")
    require(errors, has_value(review, "Style preserved only at the surface, not in the mechanism"), "review missing mechanism-drift diagnosis")
    return errors


def eval_layout_defects(root: Path) -> list[str]:
    errors: list[str] = []
    review = read(root, ".noootwo/review.md")
    require(errors, bool(review), "missing .noootwo/review.md")
    require(errors, has_value(review, "Layout defects found"), "review missing layout defect record")
    require(errors, has_value(review, "Return to exploration, directions, approved spec, implementation plan, artifact, responsive pass, typography pass, stack pass, or handoff"), "review missing return action")
    return errors


def eval_implementation_closure(root: Path) -> list[str]:
    errors: list[str] = []
    spec = read(root, ".noootwo/specs/active-design.md")
    plan = read(root, ".noootwo/plans/active-implementation.md")
    require(errors, bool(spec), "missing approved design spec")
    require(errors, bool(plan), "missing implementation plan")
    require(errors, not has_unresolved(spec), "approved design spec unresolved")
    require(errors, not has_unresolved(plan), "implementation plan unresolved")
    require(errors, APPROVED_RE.search(spec) is not None, "approved design spec not approved")
    require(errors, PLAN_APPROVED_RE.search(plan) is not None, "implementation plan not approved or delegated")
    require(errors, has_value(plan, "How the artifact will be produced"), "implementation plan missing artifact production path")
    require(errors, has_value(plan, "Generic fallback risks"), "implementation plan missing drift risk record")
    return errors


def eval_style_prose_without_visual_evidence(root: Path) -> list[str]:
    errors: list[str] = []
    style = read(root, ".noootwo/style-discovery.md")
    directions = read(root, ".noootwo/directions.md")
    review = read(root, ".noootwo/review.md")
    require(errors, bool(style) or bool(directions), "missing style discovery or directions")
    if style:
        require(errors, "style evidence check" in style.lower(), "style discovery missing Style Evidence Check")
        require(errors, has_value(style, "Visual evidence"), "style discovery missing visual evidence")
        require(errors, has_value(style, "Anti-example"), "style discovery missing anti-example")
        require(errors, has_value(style, "Implementation translation"), "style discovery missing implementation translation")
        require(errors, has_value(style, "Confidence"), "style discovery missing confidence")
        if (field_value(style, "Visual evidence") or "").lower() == "missing":
            require(errors, (field_value(style, "Confidence") or "").lower() == "low", "style discovery missing evidence must be low confidence")
            require(errors, has_value(style, "Artifact/spike required"), "style discovery missing spike requirement")
    if directions:
        require(errors, "style evidence check" in directions.lower(), "directions missing Style Evidence Check")
        require(errors, has_value(directions, "Artifact/spike required"), "directions missing spike requirement")
        if (field_value(directions, "Visual evidence") or "").lower() == "missing":
            require(errors, (field_value(directions, "Confidence") or "").lower() == "low", "directions missing evidence must be low confidence")
    if review:
        require(errors, has_value(review, "Style understanding fit"), "review missing style understanding fit")
    return errors


def eval_visual_direction_implemented_as_default_ui(root: Path) -> list[str]:
    errors: list[str] = []
    review = read(root, ".noootwo/review.md")
    require(errors, bool(review), "missing .noootwo/review.md")
    require(errors, has_value(review, "Style understanding fit"), "review missing style understanding fit")
    require(errors, has_value(review, "Generic fallback signs found"), "review missing generic fallback diagnosis")
    require(
        errors,
        "default-override" in review.lower() or "default override" in review.lower(),
        "review missing default override review",
    )
    require(errors, has_value(review, "Return action"), "review missing return action")
    return errors


def eval_direction_samples_not_prose(root: Path) -> list[str]:
    directions = read(root, ".noootwo/directions.md")
    if not directions:
        return ["missing .noootwo/directions.md"]
    return validate_direction_sample_records(root, directions)


def eval_weak_runtime_fallback(root: Path) -> list[str]:
    directions = read(root, ".noootwo/directions.md")
    style = read(root, ".noootwo/style-discovery.md")
    errors = validate_direction_sample_records(root, directions) if directions else ["missing .noootwo/directions.md"]
    fallback = (field_value(style, "Weak-runtime fallback used") or "").strip().lower()
    require(
        errors,
        fallback.startswith("one full sample plus two lightweight variants"),
        "style discovery does not record one full sample plus two lightweight variants",
    )
    return errors


def eval_same_medium_mechanism(root: Path) -> list[str]:
    board = read(root, ".noootwo/reference-board.md")
    if not board:
        return ["missing .noootwo/reference-board.md"]
    return validate_source_records(root, board)


def eval_broken_capture_rejected(root: Path) -> list[str]:
    board = read(root, ".noootwo/reference-board.md")
    if not board:
        return ["missing .noootwo/reference-board.md"]
    return validate_source_records(root, board)


def eval_intentional_aesthetic_flags_pass(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    errors = validate_aesthetic_review(review)
    decision = (field_value(review, "Decision") or "").strip().lower()
    require(errors, decision.startswith("ready"), "intentional aesthetic flags must be able to pass with a ready decision")
    return errors


def eval_aesthetic_harm_blocks_ready(root: Path) -> list[str]:
    review = read(root, ".noootwo/review.md")
    if not review:
        return ["missing .noootwo/review.md"]
    return validate_aesthetic_review(review)


SCENARIOS = {
    "missing-exploration-before-build": eval_missing_exploration,
    "missing-user-decision-under-ambiguity": eval_missing_user_decision,
    "artifact-built-but-not-reviewable": eval_artifact_not_reviewable,
    "directionally-right-but-generic-drift": eval_generic_drift,
    "layout-defects-after-fast-delivery": eval_layout_defects,
    "implementation-closure": eval_implementation_closure,
    "style-prose-without-visual-evidence": eval_style_prose_without_visual_evidence,
    "visual-direction-implemented-as-default-ui": eval_visual_direction_implemented_as_default_ui,
    "leave-simple-justified": eval_leave_simple_justified,
    "craft-only-justified": eval_craft_only_justified,
    "add-moment-proof": eval_add_moment_proof,
    "explicit-motion-request-honored": eval_explicit_motion_request_honored,
    "direction-samples-not-prose": eval_direction_samples_not_prose,
    "weak-runtime-fallback": eval_weak_runtime_fallback,
    "same-medium-mechanism": eval_same_medium_mechanism,
    "broken-capture-rejected": eval_broken_capture_rejected,
    "intentional-aesthetic-flags-pass": eval_intentional_aesthetic_flags_pass,
    "aesthetic-harm-blocks-ready": eval_aesthetic_harm_blocks_ready,
}

DEFAULT_SCENARIOS = [
    "missing-exploration-before-build",
    "missing-user-decision-under-ambiguity",
    "artifact-built-but-not-reviewable",
    "directionally-right-but-generic-drift",
    "layout-defects-after-fast-delivery",
    "implementation-closure",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Noootwo artifact structure for workflow pressure tests.")
    parser.add_argument("target", nargs="?", default=".", help="Target project directory.")
    parser.add_argument(
        "--scenario",
        choices=sorted(SCENARIOS) + ["all"],
        default="all",
        help="Scenario to evaluate. Defaults to all.",
    )
    args = parser.parse_args()

    root = Path(args.target).resolve()
    scenario_names = DEFAULT_SCENARIOS if args.scenario == "all" else [args.scenario]
    all_errors: list[str] = []

    for name in scenario_names:
        errors = SCENARIOS[name](root)
        if errors:
            all_errors.extend([f"{name}: {error}" for error in errors])

    if all_errors:
        print("Noootwo artifact eval failed:")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print("Noootwo artifact eval passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
