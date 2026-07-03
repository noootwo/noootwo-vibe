#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


IGNORE_NAMES = shutil.ignore_patterns(
    ".git",
    "__pycache__",
    ".DS_Store",
)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, symlinks=False, ignore=IGNORE_NAMES)


def load_skill_names(root: Path) -> list[str]:
    manifest = json.loads((root / "skills.json").read_text(encoding="utf-8"))
    return [item["name"] for item in manifest["skills"]]


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Noootwo Vibe child skills into a local agent skills directory.")
    parser.add_argument("--source", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--target-root", default=str(Path.home() / ".agents" / "skills"), help="Installed skills root directory.")
    parser.add_argument("--skill", action="append", help="Skill name to sync. Repeat for multiple. Defaults to every skill in skills.json.")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    target_root = Path(args.target_root).resolve()
    skill_names = args.skill or load_skill_names(source)
    target_root.mkdir(parents=True, exist_ok=True)

    for skill_name in skill_names:
        skill_dir = source / "skills" / skill_name
        if not skill_dir.is_dir():
            raise SystemExit(f"Skill not found: {skill_name}")
        copy_tree(skill_dir, target_root / skill_name)
        print(f"Synced {skill_name}: {target_root / skill_name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
