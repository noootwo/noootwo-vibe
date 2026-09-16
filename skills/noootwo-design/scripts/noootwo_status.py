#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


KEY_FILES = [
    ".noootwo/system.md",
    ".noootwo/design-tokens.md",
    ".noootwo/adoption.md",
    ".noootwo/brief.md",
    ".noootwo/style-discovery.md",
    ".noootwo/reference-board.md",
    ".noootwo/directions.md",
    ".noootwo/specs/active-design.md",
    ".noootwo/plans/active-implementation.md",
    ".noootwo/review.md",
    ".noootwo/handoff/implementation.md",
    ".noootwo/handoff/acceptance.md",
]

PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
READY_RE = re.compile(
    r"(^|\n)\s*(?:-\s*)?(?:Decision\s*:\s*)?ready\s*(?:$|\n)",
    re.IGNORECASE,
)
DECISION_RE = re.compile(r"\b(ready|refine|pivot|needs artifact|not ready)\b", re.IGNORECASE)
FULL_REDESIGN_RE = re.compile(
    r"full redesign trigger\s*:\s*(?:yes|true|triggered|full redesign)",
    re.IGNORECASE,
)
USER_SELECTED_DIRECTION_RE = re.compile(
    r"^\s*-?\s*user selected direction\s*:\s*(?!\s*(?:not selected yet|not selected|pending|none|no)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DECISION_REQUIRED_RE = re.compile(
    r"decision required before implementation\s*:\s*(?:yes|true|required)",
    re.IGNORECASE,
)
USER_SELECTED_OPTION_RE = re.compile(
    r"^\s*-?\s*user selected option\s*:\s*(?!\s*(?:TBD|not selected yet|not selected|pending|none|no|n/a|na)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DELEGATED_CHOICE_RE = re.compile(
    r"^\s*-?\s*user delegated choice to agent\s*:\s*(?:yes|true|delegated)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
APPROVED_BY_USER_RE = re.compile(
    r"approved by user\s*:\s*(?:yes|true|approved)",
    re.IGNORECASE,
)
PLAN_APPROVED_RE = re.compile(
    r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)",
    re.IGNORECASE,
)
ARTIFACT_EVIDENCE_RE = re.compile(
    r"(artifact reviewed|screenshot|preview|recording|visual proof|simulator|device|url)\s*:\s*(?!\s*(?:TBD|pending|none|no)\s*$).+",
    re.IGNORECASE,
)
MOTION_SECTION_RE = re.compile(r"^##\s+Motion\b(.*?)(?=^##\s|\Z)", re.IGNORECASE | re.MULTILINE | re.DOTALL)
MOTION_SCALE_RE = re.compile(r"duration scale\s*:\s*.*?\d+\s*ms", re.IGNORECASE | re.DOTALL)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def file_state(root: Path, relative: str) -> str:
    path = root / relative
    if not path.exists():
        return "missing"
    content = read_text(path)
    if PENDING_RE.search(content):
        return "pending"
    if TBD_RE.search(content):
        return "incomplete"
    if not content.strip():
        return "empty"
    return "complete"


def reference_state(root: Path) -> str:
    directory = root / ".noootwo" / "references"
    if not directory.is_dir():
        return "missing"
    sources = [path for path in directory.iterdir() if path.is_dir()]
    if not sources:
        return "empty"
    captures = 0
    for source in sources:
        source_note = source / "source.md"
        if not source_note.exists():
            continue
        content = read_text(source_note)
        if "unreachable" in content.lower() or any(child.suffix == ".png" for child in source.iterdir()):
            captures += 1
    return f"{captures}/{len(sources)} sources captured"


def motion_state(root: Path) -> str:
    content = read_text(root / ".noootwo/design-tokens.md")
    if not content:
        return "missing"
    match = MOTION_SECTION_RE.search(content)
    if not match:
        return "missing section"
    motion = match.group(1)
    if TBD_RE.search(motion):
        return "incomplete"
    scale = MOTION_SCALE_RE.search(motion)
    if not scale:
        return "incomplete"
    return "complete"


def infer_mode(root: Path) -> str:
    noootwo = root / ".noootwo"
    if not noootwo.exists():
        return "adopt-project"

    directions = read_text(root / ".noootwo/directions.md")
    if FULL_REDESIGN_RE.search(directions):
        return "deep"

    active_text: list[str] = []
    for relative in [".noootwo/brief.md", ".noootwo/style-discovery.md"]:
        if file_state(root, relative) == "complete":
            active_text.append(read_text(root / relative))

    combined = "\n".join(active_text).lower()
    if any(word in combined for word in ["high-end", "niche", "rare", "claude design-like", "redo all ui"]):
        return "deep"

    review_state = file_state(root, ".noootwo/review.md")
    if review_state == "complete" and DECISION_RE.search(read_text(root / ".noootwo/review.md")):
        return "review"

    if file_state(root, ".noootwo/adoption.md") != "complete":
        return "adopt-project"

    return "standard"


FIXED_CANVAS_RE = re.compile(
    r"^\s*-\s*Artifact family\s*:\s*fixed-canvas graphic\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def blockers(root: Path, inferred_mode: str) -> list[str]:
    results: list[str] = []
    directions = read_text(root / ".noootwo/directions.md")
    spec = read_text(root / ".noootwo/specs/active-design.md")
    plan = read_text(root / ".noootwo/plans/active-implementation.md")
    review = read_text(root / ".noootwo/review.md")

    if not (root / ".noootwo").exists():
        return ["missing .noootwo harness; bootstrap or run adopt-project first"]

    if FULL_REDESIGN_RE.search(directions) and not USER_SELECTED_DIRECTION_RE.search(directions):
        results.append("full redesign is triggered but no User selected direction is recorded")

    direction_selected = (
        USER_SELECTED_DIRECTION_RE.search(directions)
        or USER_SELECTED_OPTION_RE.search(directions)
        or USER_DELEGATED_CHOICE_RE.search(directions)
    )
    spec_approved = APPROVED_BY_USER_RE.search(spec)

    if not direction_selected and not spec_approved:
        if file_state(root, ".noootwo/adoption.md") != "complete":
            results.append("adoption baseline is missing, pending, or incomplete")
        if file_state(root, ".noootwo/system.md") != "complete":
            results.append("design system memory is missing, pending, or incomplete")

    if (
        USER_DECISION_REQUIRED_RE.search(directions)
        and not USER_SELECTED_OPTION_RE.search(directions)
        and not USER_DELEGATED_CHOICE_RE.search(directions)
    ):
        results.append("directions require a user decision but no selected option or delegation is recorded")

    if direction_selected and (
        file_state(root, ".noootwo/specs/active-design.md") != "complete"
        or not APPROVED_BY_USER_RE.search(spec)
    ):
        results.append("approved design spec is missing, pending, incomplete, or not approved by user")

    if spec_approved and (
        file_state(root, ".noootwo/plans/active-implementation.md") != "complete"
        or not PLAN_APPROVED_RE.search(plan)
    ):
        results.append("implementation plan is missing, pending, incomplete, or not approved/delegated")

    if file_state(root, ".noootwo/review.md") == "complete" and DECISION_RE.search(review) and not READY_RE.search(review):
        results.append("review decision is not ready")

    if file_state(root, ".noootwo/review.md") == "complete" and not ARTIFACT_EVIDENCE_RE.search(review):
        results.append("review lacks artifact/screenshot/preview evidence")

    if inferred_mode == "deep":
        if file_state(root, ".noootwo/reference-board.md") != "missing":
            reference_status = reference_state(root)
            if reference_status in {"missing", "empty"}:
                results.append("no captured reference sources under .noootwo/references/")

        fixed_canvas = bool(FIXED_CANVAS_RE.search(read_text(root / ".noootwo/brief.md")))
        if (
            not fixed_canvas
            and motion_state(root) != "complete"
            and file_state(root, ".noootwo/design-tokens.md") != "missing"
        ):
            results.append("motion contract in .noootwo/design-tokens.md is missing or incomplete")

    return results


def next_steps(root: Path, inferred_mode: str, block_list: list[str]) -> list[str]:
    if not (root / ".noootwo").exists():
        return ["run bootstrap/adopt-project and capture baseline context"]

    directions = read_text(root / ".noootwo/directions.md")
    spec = read_text(root / ".noootwo/specs/active-design.md")
    direction_selected = (
        USER_SELECTED_DIRECTION_RE.search(directions)
        or USER_SELECTED_OPTION_RE.search(directions)
        or USER_DELEGATED_CHOICE_RE.search(directions)
    )
    spec_approved = APPROVED_BY_USER_RE.search(spec)

    if not direction_selected and not spec_approved and file_state(root, ".noootwo/adoption.md") != "complete":
        return ["capture adoption baseline: current UI, tokens, components, screenshots/previews, constraints, and preserve/improve boundary"]

    if not direction_selected and not spec_approved and file_state(root, ".noootwo/system.md") != "complete":
        return ["extract or refresh .noootwo/system.md and .noootwo/design-tokens.md from real project evidence"]

    if any("User selected direction" in item or "user decision" in item for item in block_list):
        return ["ask the user to choose among the recorded options before editing UI files"]

    spec_state = file_state(root, ".noootwo/specs/active-design.md")
    if direction_selected and spec_state != "complete":
        return ["create or complete .noootwo/specs/active-design.md from the selected direction"]

    plan_state = file_state(root, ".noootwo/plans/active-implementation.md")
    if spec_approved and plan_state != "complete":
        return ["create or complete .noootwo/plans/active-implementation.md before implementation"]

    if block_list:
        return ["resolve blockers, then run validate_noootwo_readiness.py"]

    if inferred_mode in {"deep", "standard"}:
        return ["implement from the approved plan, create artifact evidence, then run review"]

    return ["continue with the selected mode and keep .noootwo evidence updated"]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize Noootwo workflow state without reading every markdown file."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    args = parser.parse_args()

    root = Path(args.target).resolve()
    inferred_mode = infer_mode(root)
    block_list = blockers(root, inferred_mode)

    print(f"Noootwo status for: {root}")
    print(f"Suggested mode: {inferred_mode}")
    print("")
    print("Files:")
    for relative in KEY_FILES:
        print(f"  - {relative}: {file_state(root, relative)}")

    print("")
    print("Evidence:")
    print(f"  - .noootwo/references/: {reference_state(root)}")
    print(f"  - motion contract: {motion_state(root)}")

    print("")
    if block_list:
        print("Blockers:")
        for item in block_list:
            print(f"  - {item}")
    else:
        print("Blockers: none detected")

    print("")
    print("Next steps:")
    for step in next_steps(root, inferred_mode, block_list):
        print(f"  - {step}")

    return 1 if block_list else 0


if __name__ == "__main__":
    raise SystemExit(main())
