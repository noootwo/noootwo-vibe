#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


AGENTS_SECTION_HEADING = "## UI/Design Workflow"
AGENTS_SECTION_RE = re.compile(r"^(#{1,6})\s+UI/Design Workflow\s*$")

PROFILE_FILES = {
    "minimal": {
        "system.md",
        "design-tokens.md",
        "adoption.md",
        "brief.md",
        "directions.md",
        "review.md",
    },
    "deep": {
        "system.md",
        "design-tokens.md",
        "adoption.md",
        "brief.md",
        "directions.md",
        "review.md",
        "style-discovery.md",
        "reference-board.md",
        "style-calibration.md",
    },
    "production": {
        "system.md",
        "design-tokens.md",
        "adoption.md",
        "brief.md",
        "directions.md",
        "review.md",
        "specs/active-design.md",
        "plans/active-implementation.md",
        "handoff/implementation.md",
        "handoff/acceptance.md",
        "handoff/assets.md",
    },
}
PROFILE_FILES["full"] = {
    "system.md",
    "design-tokens.md",
    "adoption.md",
    "product-facts.md",
    "brief.md",
    "style-calibration.md",
    "style-discovery.md",
    "reference-board.md",
    "directions.md",
    "review.md",
    "specs/active-design.md",
    "plans/active-implementation.md",
    "handoff/implementation.md",
    "handoff/acceptance.md",
    "handoff/assets.md",
}


def merge_agents_section(agents_path: Path, section_text: str) -> str:
    section_text = section_text.strip() + "\n"

    if not agents_path.exists():
        agents_path.write_text(section_text, encoding="utf-8")
        return "created"

    existing = agents_path.read_text(encoding="utf-8")
    lines = existing.splitlines()
    start_index = None

    section_level = 2
    for index, line in enumerate(lines):
        match = AGENTS_SECTION_RE.match(line.strip())
        if match:
            start_index = index
            section_level = len(match.group(1))
            break

    if start_index is None:
        prefix = existing.rstrip()
        merged = f"{prefix}\n\n{section_text}" if prefix else section_text
        agents_path.write_text(merged, encoding="utf-8")
        return "appended"

    end_index = len(lines)
    for index in range(start_index + 1, len(lines)):
        line = lines[index]
        heading_match = re.match(r"^(#{1,6})\s+", line)
        if heading_match and len(heading_match.group(1)) <= section_level:
            end_index = index
            break

    replacement = section_text.rstrip().splitlines()
    merged_lines = lines[:start_index] + replacement + lines[end_index:]
    merged = "\n".join(merged_lines).rstrip() + "\n"
    agents_path.write_text(merged, encoding="utf-8")
    return "updated"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap the .noootwo harness into a target project."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files inside the destination .noootwo directory.",
    )
    parser.add_argument(
        "--skip-agents",
        action="store_true",
        help="Do not create or merge the target project's AGENTS.md UI/Design Workflow section.",
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILE_FILES),
        default="minimal",
        help="Harness profile to copy. Defaults to minimal to reduce pending/TBD noise.",
    )
    args = parser.parse_args()

    package_root = Path(__file__).resolve().parent.parent
    source_root = package_root / "assets" / "noootwo-harness-template"
    agents_template = package_root / "assets" / "AGENTS.md"
    target_root = Path(args.target).resolve()
    destination_root = target_root / ".noootwo"

    if not source_root.exists():
        raise SystemExit(f"Template source not found: {source_root}")
    if not args.skip_agents and not agents_template.exists():
        raise SystemExit(f"AGENTS template not found: {agents_template}")

    copied: list[Path] = []
    skipped: list[Path] = []

    selected_files = PROFILE_FILES[args.profile]

    for source_path in sorted(source_root.rglob("*")):
        relative_path = source_path.relative_to(source_root)
        relative_key = relative_path.as_posix()
        destination_path = destination_root / relative_path

        if source_path.is_dir():
            if any(path.startswith(f"{relative_key}/") for path in selected_files):
                destination_path.mkdir(parents=True, exist_ok=True)
            continue

        if relative_key not in selected_files:
            continue

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        if destination_path.exists() and not args.force:
            skipped.append(destination_path)
            continue

        shutil.copy2(source_path, destination_path)
        copied.append(destination_path)

    print(f"Bootstrapped {destination_root} using profile: {args.profile}")
    if copied:
        print("Copied:")
        for path in copied:
            print(f"  - {path}")
    if skipped:
        print("Skipped existing files:")
        for path in skipped:
            print(f"  - {path}")
    if skipped and not args.force:
        print("Re-run with --force to overwrite existing files.")

    if args.skip_agents:
        print("Skipped AGENTS.md integration.")
    else:
        agents_status = merge_agents_section(
            target_root / "AGENTS.md",
            agents_template.read_text(encoding="utf-8"),
        )
        print(f"AGENTS.md integration: {agents_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
