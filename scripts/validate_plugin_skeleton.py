#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_plugin_manifest(root: Path, errors: list[str]) -> None:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        error(errors, "missing .codex-plugin/plugin.json")
        return

    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive
        error(errors, f"invalid plugin.json: {exc}")
        return

    if not isinstance(payload, dict):
        error(errors, "plugin.json must contain an object")
        return

    for field in ("name", "version", "description", "skills", "interface"):
        if field not in payload:
            error(errors, f"plugin.json missing `{field}`")

    interface = payload.get("interface")
    if isinstance(interface, dict):
        for field in (
            "displayName",
            "shortDescription",
            "longDescription",
            "developerName",
            "category",
            "capabilities",
            "defaultPrompt",
        ):
            if field not in interface:
                error(errors, f"plugin.json interface missing `{field}`")
    else:
        error(errors, "plugin.json `interface` must be an object")

    skills_path = payload.get("skills")
    if skills_path != "./skills/":
        error(errors, "plugin.json `skills` should point to `./skills/` for this repository layout")


def validate_shared_core(root: Path, errors: list[str]) -> None:
    required_paths = (
        "SKILL.md",
        "README.md",
        "references",
        "scripts",
        "evals/prompts",
        "assets/noootwo-harness-template",
    )
    for relative_path in required_paths:
        path = root / relative_path
        if not path.exists():
            error(errors, f"missing shared core path: {relative_path}")

    root_skill = root / "SKILL.md"
    if root_skill.is_file():
        frontmatter = parse_skill_frontmatter(root_skill, errors)
        if frontmatter:
            for field in ("name", "description"):
                value = frontmatter.get(field)
                if not isinstance(value, str) or not value.strip():
                    error(errors, f"root SKILL.md missing non-empty `{field}`")
    else:
        error(errors, "missing root SKILL.md compatibility entrypoint")


FRONTMATTER_FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$")
AGENT_DISPLAY_RE = re.compile(r'^\s{2}display_name:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_SHORT_RE = re.compile(r'^\s{2}short_description:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_PROMPT_RE = re.compile(r'^\s{2}default_prompt:\s*"?(.*?)"?\s*$', re.MULTILINE)


def parse_skill_frontmatter(skill_md: Path, errors: list[str]) -> dict | None:
    try:
        raw = skill_md.read_text(encoding="utf-8")
    except OSError:
        error(errors, f"unable to read {skill_md}")
        return None

    if not raw.startswith("---\n"):
        error(errors, f"{skill_md} must start with YAML frontmatter")
        return None

    end = raw.find("\n---", 4)
    if end == -1:
        error(errors, f"{skill_md} frontmatter is not closed")
        return None

    frontmatter: dict[str, str] = {}
    for line in raw[4:end].splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = FRONTMATTER_FIELD_RE.match(line)
        if not match:
            error(errors, f"{skill_md} frontmatter contains unsupported line: {line}")
            return None
        key, value = match.groups()
        frontmatter[key] = value.strip().strip('"').strip("'")

    unsupported = sorted(set(frontmatter) - {"name", "description"})
    if unsupported:
        error(
            errors,
            f"{skill_md} frontmatter only supports `name` and `description`; found unsupported fields: {', '.join(unsupported)}",
        )
        return None
    return frontmatter


def validate_skill_dir(skill_dir: Path, errors: list[str]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        error(errors, f"skill `{skill_dir.name}` is missing SKILL.md")
        return

    frontmatter = parse_skill_frontmatter(skill_md, errors)
    if not frontmatter:
        return

    for field in ("name", "description"):
        value = frontmatter.get(field)
        if not isinstance(value, str) or not value.strip():
            error(errors, f"skill `{skill_dir.name}` frontmatter missing non-empty `{field}`")

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if agent_yaml.is_file():
        try:
            raw = agent_yaml.read_text(encoding="utf-8")
        except Exception as exc:  # pragma: no cover - defensive
            error(errors, f"skill `{skill_dir.name}` agent yaml invalid: {exc}")
            return
        if "interface:" not in raw:
            error(errors, f"skill `{skill_dir.name}` agent yaml missing interface block")
            return
        matches = {
            "display_name": AGENT_DISPLAY_RE.search(raw),
            "short_description": AGENT_SHORT_RE.search(raw),
            "default_prompt": AGENT_PROMPT_RE.search(raw),
        }
        for field, match in matches.items():
            if match is None or not match.group(1).strip():
                error(errors, f"skill `{skill_dir.name}` agent yaml missing non-empty interface.{field}")


def validate_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        error(errors, "missing skills/ directory")
        return

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not skill_dirs:
        error(errors, "skills/ directory has no child skills")
        return

    if not (skills_root / "noootwo-design" / "SKILL.md").is_file():
        error(errors, "skills/ must include the `noootwo-design` front-door child skill")
        return

    for skill_dir in skill_dirs:
        validate_skill_dir(skill_dir, errors)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Noootwo plugin skeleton.")
    parser.add_argument("target", nargs="?", default=".", help="Repository root to validate.")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    errors: list[str] = []
    validate_plugin_manifest(root, errors)
    validate_shared_core(root, errors)
    validate_skills(root, errors)

    if errors:
        print("Plugin skeleton validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"Plugin skeleton validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
