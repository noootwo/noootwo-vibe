#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_FILES = [
    Path(".noootwo/directions.md"),
    Path(".noootwo/review.md"),
    Path(".noootwo/design-tokens.md"),
]

DEEP_REQUIRED_FILES = [
    Path(".noootwo/style-discovery.md"),
    Path(".noootwo/reference-board.md"),
]

IMPLEMENTATION_REQUIRED_FILES = [
    Path(".noootwo/specs/active-design.md"),
    Path(".noootwo/plans/active-implementation.md"),
]

STATUS_PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
READY_DECISION_RE = re.compile(r"^\s*-\s*ready,\s*refine,\s*pivot,\s*or\s*needs artifact\s*:\s*ready\s*$", re.IGNORECASE | re.MULTILINE)
DECISION_LINE_RE = re.compile(r"^\s*-\s*ready,\s*refine,\s*pivot,\s*or\s*needs artifact\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
RETURN_ACTION_RE = re.compile(r"^\s*-\s*return to .+?:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
APPROVED_BY_USER_RE = re.compile(r"approved by user\s*:\s*(?:yes|true|approved)", re.IGNORECASE)
PLAN_APPROVED_RE = re.compile(r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)", re.IGNORECASE)
USER_DELEGATED_RE = re.compile(r"user delegated choice to agent\s*:\s*(?:yes|true|delegated)", re.IGNORECASE)
ARTIFACT_FAMILY_LINE_RE = re.compile(
    r"^\s*-\s*Artifact family\s*:\s*(ui surface|fixed-canvas graphic|slide deck|live artifact)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def read_if_exists(target_root: Path, relative_path: Path) -> str:
    path = target_root / relative_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def validate_file(target_root: Path, relative_path: Path) -> list[str]:
    path = target_root / relative_path
    errors: list[str] = []

    if not path.exists():
        return [f"{relative_path} is missing"]

    content = path.read_text(encoding="utf-8")
    if STATUS_PENDING_RE.search(content):
        errors.append(f"{relative_path} is still Status: pending")
    if TBD_RE.search(content):
        errors.append(f"{relative_path} contains unresolved TBD placeholders")
    if not content.strip():
        errors.append(f"{relative_path} is empty")

    return errors


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def has_meaningful_value(content: str, label: str) -> bool:
    pattern = re.compile(
        rf"^\s*-\s*{re.escape(label)}\s*:\s*(?!\s*(?:TBD|pending|none|no|not selected yet|not reviewed|blocked)\s*$).+\S",
        re.IGNORECASE | re.MULTILINE,
    )
    return bool(pattern.search(content))


def missing_sections(content: str, sections: list[str], path_label: str) -> list[str]:
    lower_content = content.lower()
    return [
        f"{path_label} is missing {section}"
        for section in sections
        if section not in lower_content
    ]


def extract_artifact_family(brief_content: str, spec_content: str) -> str | None:
    for content in (brief_content, spec_content):
        if not content:
            continue
        match = ARTIFACT_FAMILY_LINE_RE.search(content)
        if match:
            return match.group(1).strip().lower()
    return None


def validate_brief(target_root: Path, strict_workflow: bool) -> list[str]:
    if not strict_workflow:
        return []

    relative = Path(".noootwo/brief.md")
    errors = validate_file(target_root, relative)
    content = read_if_exists(target_root, relative)
    if not content:
        return errors

    errors.extend(
        missing_sections(
            content,
            [
                "classification",
                "objective",
                "audience and context",
                "success criteria",
                "discovered constraints",
                "unresolved uncertainty",
                "user decisions or delegated defaults",
                "artifact plan",
            ],
            ".noootwo/brief.md",
        )
    )
    require(errors, ARTIFACT_FAMILY_LINE_RE.search(content) is not None, ".noootwo/brief.md missing explicit artifact family")
    require(errors, has_meaningful_value(content, "What needs to be made or changed"), ".noootwo/brief.md missing concrete objective")
    require(errors, has_meaningful_value(content, "Primary success signal"), ".noootwo/brief.md missing success criteria")
    return errors


def validate_directions(target_root: Path, deep_mode: bool, strict_workflow: bool) -> list[str]:
    relative = Path(".noootwo/directions.md")
    content = read_if_exists(target_root, relative)
    if not content:
        return []

    errors: list[str] = []
    sections = [
        "direction requirement",
        "user decision",
        "preservation contract",
    ]
    if strict_workflow or deep_mode:
        sections.extend(
            [
                "compared direction 1",
                "compared direction 2",
                "compared direction 3",
            ]
        )
    errors.extend(missing_sections(content, sections, ".noootwo/directions.md"))

    compared_count = len(re.findall(r"^##\s+Compared Direction \d", content, re.MULTILINE))
    if strict_workflow or deep_mode:
        require(errors, compared_count >= 3, ".noootwo/directions.md must compare 3 directions for direction-sensitive work")

    if "why multiple reasonable directions exist" in content.lower():
        direction_required = has_meaningful_value(content, "Why multiple reasonable directions exist")
        if direction_required:
            selection_recorded = (
                has_meaningful_value(content, "User selected direction")
                or has_meaningful_value(content, "User selected option")
                or USER_DELEGATED_RE.search(content) is not None
            )
            require(
                errors,
                selection_recorded,
                ".noootwo/directions.md compares viable directions but does not record user choice or delegation",
            )

    return errors


def validate_review(target_root: Path, allow_non_ready: bool, deep_mode: bool, strict_workflow: bool) -> list[str]:
    relative = Path(".noootwo/review.md")
    content = read_if_exists(target_root, relative)
    if not content:
        return []

    brief_content = read_if_exists(target_root, Path(".noootwo/brief.md"))
    spec_content = read_if_exists(target_root, Path(".noootwo/specs/active-design.md"))
    artifact_family = extract_artifact_family(brief_content, spec_content)

    errors: list[str] = []
    errors.extend(
        missing_sections(
            content,
            [
                "artifact evidence",
                "findings",
                "generic drift checks",
                "layout, readability, and responsive checks",
                "artifact delivery checks",
                "decision",
                "return action",
                "open issues",
            ],
            ".noootwo/review.md",
        )
    )

    require(errors, has_meaningful_value(content, "Artifact reviewed"), ".noootwo/review.md missing artifact reviewed record")
    require(errors, has_meaningful_value(content, "URL, screenshot path, preview, simulator, recording, or accepted limitation"), ".noootwo/review.md missing artifact evidence path or accepted limitation")
    require(errors, has_meaningful_value(content, "Preview surface used"), ".noootwo/review.md missing preview surface record")
    require(errors, DECISION_LINE_RE.search(content) is not None, ".noootwo/review.md does not record a review decision")
    require(errors, RETURN_ACTION_RE.search(content) is not None, ".noootwo/review.md does not record a return action")

    if strict_workflow:
        require(errors, has_meaningful_value(content, "Strongest authored move"), ".noootwo/review.md missing strongest authored move")
        require(errors, has_meaningful_value(content, "Mismatch between intent and rendered result"), ".noootwo/review.md missing intent-vs-rendered mismatch record")

    if artifact_family == "fixed-canvas graphic":
        require(errors, has_meaningful_value(content, "Export target checked"), ".noootwo/review.md missing export target check for fixed-canvas graphic")
        require(errors, has_meaningful_value(content, "Artifact-family-specific evidence captured"), ".noootwo/review.md missing artifact-specific evidence for fixed-canvas graphic")
    elif artifact_family == "slide deck":
        require(errors, has_meaningful_value(content, "Export target checked"), ".noootwo/review.md missing export target check for slide deck")
        require(errors, has_meaningful_value(content, "Fixed-canvas, deck-flow, or live-state defects found"), ".noootwo/review.md missing deck-flow check")
    elif artifact_family == "live artifact":
        require(errors, has_meaningful_value(content, "Artifact-family-specific evidence captured"), ".noootwo/review.md missing live-state evidence")
        require(errors, has_meaningful_value(content, "Fixed-canvas, deck-flow, or live-state defects found"), ".noootwo/review.md missing live-state delivery check")

    if not allow_non_ready and not READY_DECISION_RE.search(content):
        errors.append(".noootwo/review.md decision is not ready")

    if READY_DECISION_RE.search(content):
        open_issue_block = re.search(r"## Open Issues\s+(.+)$", content, re.IGNORECASE | re.DOTALL)
        if open_issue_block:
            block_text = open_issue_block.group(1)
            if re.search(r"\b(block|blocking|unresolved|yes)\b", block_text, re.IGNORECASE):
                errors.append(".noootwo/review.md marks ready while open issues still read as blocking or unresolved")

    return errors


def validate_tokens(target_root: Path) -> list[str]:
    relative = Path(".noootwo/design-tokens.md")
    content = read_if_exists(target_root, relative)
    if not content:
        return []
    return missing_sections(content, ["preservation contract"], ".noootwo/design-tokens.md")


def validate_deep_mode(target_root: Path) -> list[str]:
    errors: list[str] = []

    for relative_path in DEEP_REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    style_content = read_if_exists(target_root, Path(".noootwo/style-discovery.md"))
    if style_content:
        errors.extend(
            missing_sections(
                style_content,
                [
                    "source accessibility",
                    "source evidence",
                    "evidence levels",
                    "rejected surfaces",
                    "preservation contract",
                ],
                ".noootwo/style-discovery.md",
            )
        )

    reference_content = read_if_exists(target_root, Path(".noootwo/reference-board.md"))
    if reference_content:
        errors.extend(
            missing_sections(
                reference_content,
                [
                    "source url or artifact",
                    "borrowed mechanism",
                    "selected mechanisms",
                    "preservation contract",
                ],
                ".noootwo/reference-board.md",
            )
        )

    return errors


def validate_implementation_gate(target_root: Path, strict_workflow: bool) -> list[str]:
    errors: list[str] = []

    for relative_path in IMPLEMENTATION_REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    spec_content = read_if_exists(target_root, Path(".noootwo/specs/active-design.md"))
    if spec_content:
        errors.extend(
            missing_sections(
                spec_content,
                [
                    "approval",
                    "design contract",
                    "preservation contract",
                    "design system contract",
                    "surface inventory",
                    "implementation contract",
                    "artifact and review contract",
                ],
                ".noootwo/specs/active-design.md",
            )
        )
        require(errors, APPROVED_BY_USER_RE.search(spec_content) is not None, ".noootwo/specs/active-design.md is not approved by user")
        require(errors, ARTIFACT_FAMILY_LINE_RE.search(spec_content) is not None, ".noootwo/specs/active-design.md missing explicit artifact family")
        if strict_workflow:
            require(errors, has_meaningful_value(spec_content, "Layout grammar"), ".noootwo/specs/active-design.md missing layout grammar")
            require(errors, has_meaningful_value(spec_content, "Typography system"), ".noootwo/specs/active-design.md missing typography system")
            require(errors, has_meaningful_value(spec_content, "Color role system"), ".noootwo/specs/active-design.md missing color role system")
            require(errors, has_meaningful_value(spec_content, "Artifact grammar"), ".noootwo/specs/active-design.md missing artifact grammar")
            require(errors, has_meaningful_value(spec_content, "Preview surface required before ready"), ".noootwo/specs/active-design.md missing preview surface contract")
            require(errors, has_meaningful_value(spec_content, "Export target or delivery format"), ".noootwo/specs/active-design.md missing export target contract")

    plan_content = read_if_exists(target_root, Path(".noootwo/plans/active-implementation.md"))
    if plan_content:
        errors.extend(
            missing_sections(
                plan_content,
                [
                    "preconditions",
                    "implementation scope",
                    "component and system mapping",
                    "verification plan",
                    "known drift risks",
                    "implementation steps",
                    "completion criteria",
                ],
                ".noootwo/plans/active-implementation.md",
            )
        )
        require(errors, PLAN_APPROVED_RE.search(plan_content) is not None, ".noootwo/plans/active-implementation.md is not approved or delegated")
        if strict_workflow:
            require(errors, has_meaningful_value(plan_content, "Artifact family confirmed"), ".noootwo/plans/active-implementation.md missing artifact family confirmation")
            require(errors, has_meaningful_value(plan_content, "How the artifact will be produced"), ".noootwo/plans/active-implementation.md missing artifact production plan")
            require(errors, has_meaningful_value(plan_content, "How screenshots/previews will be reviewed"), ".noootwo/plans/active-implementation.md missing screenshot/preview review plan")
            require(errors, has_meaningful_value(plan_content, "How export or delivery output will be checked"), ".noootwo/plans/active-implementation.md missing export/delivery verification plan")
            require(errors, has_meaningful_value(plan_content, "Generic fallback risks"), ".noootwo/plans/active-implementation.md missing generic fallback risk record")
            require(errors, has_meaningful_value(plan_content, "Artifact-family-specific delivery risks"), ".noootwo/plans/active-implementation.md missing artifact-specific delivery risk record")

    return errors


def validate_detail_translation_gate(target_root: Path) -> list[str]:
    errors: list[str] = []

    tokens = read_if_exists(target_root, Path(".noootwo/design-tokens.md"))
    if tokens:
        errors.extend(missing_sections(tokens, ["detail rules"], ".noootwo/design-tokens.md"))

    spec = read_if_exists(target_root, Path(".noootwo/specs/active-design.md"))
    if spec:
        errors.extend(missing_sections(spec, ["surface inventory", "detail translation constraints"], ".noootwo/specs/active-design.md"))

    plan = read_if_exists(target_root, Path(".noootwo/plans/active-implementation.md"))
    if plan:
        errors.extend(
            missing_sections(
                plan,
                [
                    "component and system mapping",
                    "known drift risks",
                ],
                ".noootwo/plans/active-implementation.md",
            )
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that Noootwo design deliverables are ready for handoff."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--allow-non-ready",
        action="store_true",
        help="Only validate that required Noootwo files are complete; do not require the review decision to be ready.",
    )
    parser.add_argument(
        "--deep-mode",
        action="store_true",
        help="Also validate deep-mode style discovery, reference board, and evidence coverage.",
    )
    parser.add_argument(
        "--implementation-gate",
        action="store_true",
        help="Also require an approved design spec and approved/delegated implementation plan.",
    )
    parser.add_argument(
        "--detail-translation-gate",
        action="store_true",
        help="Also require implementation-stage detail-translation coverage.",
    )
    parser.add_argument(
        "--strict-workflow",
        action="store_true",
        help="Require the full generic workflow closure: brief, direction decision, implementation verification, and evidence-backed review.",
    )
    args = parser.parse_args()

    target_root = Path(args.target).resolve()
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    errors.extend(validate_brief(target_root, args.strict_workflow))
    errors.extend(validate_tokens(target_root))
    errors.extend(validate_directions(target_root, args.deep_mode, args.strict_workflow))
    errors.extend(validate_review(target_root, args.allow_non_ready, args.deep_mode, args.strict_workflow))
    if args.deep_mode:
        errors.extend(validate_deep_mode(target_root))
    if args.implementation_gate:
        errors.extend(validate_implementation_gate(target_root, args.strict_workflow))
    if args.detail_translation_gate:
        errors.extend(validate_implementation_gate(target_root, args.strict_workflow))
        errors.extend(validate_detail_translation_gate(target_root))

    if errors:
        print("Noootwo readiness validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Noootwo readiness validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
