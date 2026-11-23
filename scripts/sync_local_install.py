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

DEFAULT_AGENT_SKILLS_ROOT = Path.home() / ".agents" / "skills"
DEFAULT_CODEX_SKILLS_ROOT = Path.home() / ".codex" / "skills"


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, symlinks=False, ignore=IGNORE_NAMES)


def load_skill_names(root: Path) -> list[str]:
    manifest = json.loads((root / "skills.json").read_text(encoding="utf-8"))
    return [item["name"] for item in manifest["skills"]]


def load_version(skill_dir: Path) -> str | None:
    version_file = skill_dir / "VERSION"
    if not version_file.is_file():
        return None
    return version_file.read_text(encoding="utf-8").strip()


def verify_install(source: Path, target_root: Path, skill_names: list[str]) -> list[str]:
    errors: list[str] = []
    for skill_name in skill_names:
        source_version = load_version(source / "skills" / skill_name)
        target_skill = target_root / skill_name
        target_version = load_version(target_skill)
        if target_version is None:
            errors.append(f"{target_skill}: missing VERSION")
            continue
        if source_version != target_version:
            errors.append(
                f"{target_skill}: expected {source_version or 'unknown'}, found {target_version}"
            )
        if not (target_skill / "SKILL.md").is_file():
            errors.append(f"{target_skill}: missing SKILL.md")

    if errors:
        print(f"Install check failed for {target_root}:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"Verified {len(skill_names)} skills in {target_root}")
    return errors


def remove_codex_duplicates(skill_names: list[str], agent_root: Path, codex_root: Path) -> None:
    if agent_root == codex_root or not codex_root.exists():
        return

    for skill_name in skill_names:
        agent_skill = agent_root / skill_name
        codex_skill = codex_root / skill_name
        if agent_skill.is_dir() and codex_skill.exists():
            shutil.rmtree(codex_skill)
            print(f"Removed duplicate Codex skill {skill_name}: {codex_skill}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Noootwo Vibe child skills into a local agent skills directory.")
    parser.add_argument("--source", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--target-root", default=str(DEFAULT_AGENT_SKILLS_ROOT), help="Installed skills root directory.")
    parser.add_argument("--codex-target-root", default=str(DEFAULT_CODEX_SKILLS_ROOT), help="Codex skills root to dedupe when syncing into the user agent skills root.")
    parser.add_argument("--dedupe-codex", action="store_true", help="Remove duplicate skills from the Codex skills root after syncing, even when --target-root is not the default agent skills root.")
    parser.add_argument("--no-dedupe-codex", action="store_true", help="Do not remove duplicate skills from the Codex skills root after syncing to the user agent root.")
    parser.add_argument("--skill", action="append", help="Skill name to sync. Repeat for multiple. Defaults to every skill in skills.json.")
    parser.add_argument("--check", action="store_true", help="Do not copy. Verify installed VERSION and SKILL.md files in the target roots.")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    target_root = Path(args.target_root).resolve()
    codex_target_root = Path(args.codex_target_root).resolve()
    skill_names = args.skill or load_skill_names(source)

    if args.check:
        roots = []
        for root in (target_root, codex_target_root):
            if root not in roots and root.is_dir():
                roots.append(root)
        if not roots:
            raise SystemExit("No installed skill roots found to check.")
        errors = []
        for root in roots:
            errors.extend(verify_install(source, root, skill_names))
        return 1 if errors else 0

    target_root.mkdir(parents=True, exist_ok=True)

    for skill_name in skill_names:
        skill_dir = source / "skills" / skill_name
        if not skill_dir.is_dir():
            raise SystemExit(f"Skill not found: {skill_name}")
        copy_tree(skill_dir, target_root / skill_name)
        print(f"Synced {skill_name}: {target_root / skill_name}")

    errors = verify_install(source, target_root, skill_names)
    if errors:
        return 1

    should_dedupe = target_root == DEFAULT_AGENT_SKILLS_ROOT.resolve() or args.dedupe_codex
    if not args.no_dedupe_codex and should_dedupe:
        remove_codex_duplicates(skill_names, target_root, codex_target_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
