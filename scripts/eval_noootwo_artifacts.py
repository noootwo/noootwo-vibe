#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
USER_DELEGATED_RE = re.compile(r"user delegated choice to agent\s*:\s*(?:yes|true|delegated)", re.IGNORECASE)
APPROVED_RE = re.compile(r"approved by user\s*:\s*(?:yes|true|approved)", re.IGNORECASE)
PLAN_APPROVED_RE = re.compile(r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)", re.IGNORECASE)


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


SCENARIOS = {
    "missing-exploration-before-build": eval_missing_exploration,
    "missing-user-decision-under-ambiguity": eval_missing_user_decision,
    "artifact-built-but-not-reviewable": eval_artifact_not_reviewable,
    "directionally-right-but-generic-drift": eval_generic_drift,
    "layout-defects-after-fast-delivery": eval_layout_defects,
    "implementation-closure": eval_implementation_closure,
}

DEFAULT_SCENARIOS = list(SCENARIOS.keys())


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
