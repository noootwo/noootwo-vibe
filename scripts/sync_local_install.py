#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


IGNORE_NAMES = shutil.ignore_patterns(
    ".git",
    "__pycache__",
    ".DS_Store",
)

DEFAULT_AGENT_SKILLS_ROOT = Path.home() / ".agents" / "skills"
DEFAULT_CODEX_SKILLS_ROOT = Path.home() / ".codex" / "skills"
KNOWN_AGENT_SKILL_ROOTS = (
    DEFAULT_AGENT_SKILLS_ROOT,
    DEFAULT_CODEX_SKILLS_ROOT,
    Path.home() / ".claude" / "skills",
    Path.home() / ".cursor" / "skills",
    Path.home() / ".gemini" / "skills",
    Path.home() / ".windsurf" / "skills",
    Path.home() / ".codeium" / "skills",
)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.is_symlink() or dst.is_file():
        dst.unlink()
    elif dst.exists():
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


def inspect_install(
    source: Path,
    target_root: Path,
    skill_names: list[str],
    all_skill_names: list[str],
) -> tuple[dict, list[str]]:
    errors: list[str] = []
    skills: list[dict] = []
    for skill_name in skill_names:
        source_version = load_version(source / "skills" / skill_name)
        target_skill = target_root / skill_name
        target_version = load_version(target_skill)
        has_skill_md = (target_skill / "SKILL.md").is_file()
        skill_errors: list[str] = []
        if target_version is None:
            skill_errors.append(f"{target_skill}: missing VERSION")
        elif source_version != target_version:
            skill_errors.append(
                f"{target_skill}: expected {source_version or 'unknown'}, found {target_version}"
            )
        if not has_skill_md:
            skill_errors.append(f"{target_skill}: missing SKILL.md")
        errors.extend(skill_errors)
        skills.append(
            {
                "name": skill_name,
                "expected": source_version,
                "installed": target_version,
                "skill_md": has_skill_md,
                "ok": not skill_errors,
            }
        )

    stale = stale_noootwo_skills(target_root, all_skill_names)
    for path in stale:
        errors.append(
            f"{path}: stale Noootwo skill not in skills.json; rerun with --prune"
        )

    report = {
        "root": str(target_root),
        "ok": not errors,
        "skills": skills,
        "stale": [str(path) for path in stale],
    }
    return report, errors


def inspect_roots(
    source: Path,
    roots: list[Path],
    skill_names: list[str],
    all_skill_names: list[str],
) -> tuple[list[dict], list[str]]:
    reports: list[dict] = []
    errors: list[str] = []
    for root in roots:
        report, root_errors = inspect_install(source, root, skill_names, all_skill_names)
        reports.append(report)
        errors.extend(root_errors)
    return reports, errors


def print_install_result(reports: list[dict], errors: list[str]) -> None:
    if errors:
        print("Install check failed:")
        for error in errors:
            print(f"  - {error}")
        return
    for report in reports:
        print(f"Verified {len(report['skills'])} skills in {report['root']}")


def stale_noootwo_skills(target_root: Path, skill_names: list[str]) -> list[Path]:
    if not target_root.is_dir():
        return []
    names = set(skill_names)
    return sorted(
        path
        for path in target_root.iterdir()
        if (path.is_dir() or path.is_symlink())
        and path.name.startswith("noootwo-")
        and path.name not in names
    )


def root_label(target_root: Path) -> str:
    label = target_root.parent.name.lstrip(".") or "root"
    return "".join(character if character.isalnum() or character in "-_" else "-" for character in label)


def prune_stale(
    target_root: Path,
    skill_names: list[str],
    backup_root: Path,
    stamp: str,
    quiet: bool,
) -> None:
    stale = stale_noootwo_skills(target_root, skill_names)
    if not stale:
        return
    for path in stale:
        destination = backup_root / stamp / root_label(target_root) / path.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(destination))
        if not quiet:
            print(f"Pruned stale skill {path.name}: {destination}")


def unique_roots(roots: list[Path]) -> list[Path]:
    unique: list[Path] = []
    for root in roots:
        resolved = root.expanduser().resolve()
        if resolved not in unique:
            unique.append(resolved)
    return unique


def existing_known_roots(target_root: Path, codex_target_root: Path) -> list[Path]:
    return unique_roots(
        [
            root
            for root in KNOWN_AGENT_SKILL_ROOTS
            if root.is_dir()
        ]
        + [root for root in (target_root, codex_target_root) if root.is_dir()]
    )


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
    parser.add_argument("--prune", action="store_true", help="Move stale noootwo-* skills that are not in skills.json into the backup root.")
    parser.add_argument("--backup-root", default=str(Path.home() / ".codex" / "skill-backups"), help="Where --prune moves stale skills.")
    parser.add_argument("--skill", action="append", help="Skill name to sync. Repeat for multiple. Defaults to every skill in skills.json.")
    parser.add_argument("--check", action="store_true", help="Do not copy. Verify installed VERSION and SKILL.md files in the target roots.")
    parser.add_argument("--all-known", action="store_true", help="Use every existing known agent skill root instead of only the target roots.")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable install report.")
    args = parser.parse_args()

    if args.check and args.prune:
        parser.error("--check and --prune cannot be combined")
    if args.all_known and args.skill:
        parser.error("--all-known requires the complete skills.json set; do not combine it with --skill")

    source = Path(args.source).resolve()
    target_root = Path(args.target_root).resolve()
    codex_target_root = Path(args.codex_target_root).resolve()
    all_skill_names = load_skill_names(source)
    skill_names = args.skill or all_skill_names

    if args.check:
        if args.all_known:
            roots = existing_known_roots(target_root, codex_target_root)
        else:
            roots = unique_roots(
                [root for root in (target_root, codex_target_root) if root.is_dir()]
            )
        if not roots:
            raise SystemExit("No installed skill roots found to check.")
        reports, errors = inspect_roots(source, roots, skill_names, all_skill_names)
        if args.json:
            print(json.dumps({"ok": not errors, "roots": reports, "errors": errors}, indent=2))
        else:
            print_install_result(reports, errors)
        return 0 if not errors else 1

    if args.all_known:
        roots = existing_known_roots(target_root, codex_target_root)
        if not roots:
            raise SystemExit("No installed skill roots found to sync.")
    else:
        roots = [target_root]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = Path(args.backup_root).expanduser().resolve()
    for root in roots:
        root.mkdir(parents=True, exist_ok=True)
        for skill_name in skill_names:
            skill_dir = source / "skills" / skill_name
            if not skill_dir.is_dir():
                raise SystemExit(f"Skill not found: {skill_name}")
            copy_tree(skill_dir, root / skill_name)
            if not args.json:
                print(f"Synced {skill_name}: {root / skill_name}")

        if args.prune:
            prune_stale(root, all_skill_names, backup_root, stamp, args.json)

    reports, errors = inspect_roots(source, roots, skill_names, all_skill_names)
    if args.json:
        print(json.dumps({"ok": not errors, "roots": reports, "errors": errors}, indent=2))
    else:
        print_install_result(reports, errors)
    if errors:
        return 1

    should_dedupe = (
        not args.all_known
        and (target_root == DEFAULT_AGENT_SKILLS_ROOT.resolve() or args.dedupe_codex)
    )
    if not args.no_dedupe_codex and should_dedupe:
        remove_codex_duplicates(skill_names, target_root, codex_target_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
