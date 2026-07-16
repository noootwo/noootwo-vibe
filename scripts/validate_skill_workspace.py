#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EXPECTED_SKILLS = [
    "noootwo-workflow",
    "noootwo-product",
    "noootwo-design",
    "noootwo-review",
    "noootwo-docs",
]

FRONTMATTER_FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$")
AGENT_DISPLAY_RE = re.compile(r'^\s{2}display_name:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_SHORT_RE = re.compile(r'^\s{2}short_description:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_PROMPT_RE = re.compile(r'^\s{2}default_prompt:\s*"?(.*?)"?\s*$', re.MULTILINE)


def add(errors: list[str], message: str) -> None:
    errors.append(message)


def read_json(path: Path, errors: list[str]) -> dict | None:
    if not path.is_file():
        add(errors, f"missing {path}")
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        add(errors, f"invalid JSON in {path}: {exc}")
        return None
    if not isinstance(payload, dict):
        add(errors, f"{path} must contain a JSON object")
        return None
    return payload


def parse_skill_frontmatter(skill_md: Path, errors: list[str]) -> dict[str, str] | None:
    if not skill_md.is_file():
        add(errors, f"missing {skill_md}")
        return None

    raw = skill_md.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        add(errors, f"{skill_md} must start with YAML frontmatter")
        return None

    end = raw.find("\n---", 4)
    if end == -1:
        add(errors, f"{skill_md} frontmatter is not closed")
        return None

    frontmatter: dict[str, str] = {}
    for line in raw[4:end].splitlines():
        if not line.strip():
            continue
        match = FRONTMATTER_FIELD_RE.match(line)
        if not match:
            add(errors, f"{skill_md} frontmatter contains unsupported line: {line}")
            return None
        key, value = match.groups()
        frontmatter[key] = value.strip().strip('"').strip("'")

    unsupported = sorted(set(frontmatter) - {"name", "description"})
    if unsupported:
        add(errors, f"{skill_md} frontmatter only supports name and description; found {', '.join(unsupported)}")
        return None

    for field in ("name", "description"):
        if not frontmatter.get(field, "").strip():
            add(errors, f"{skill_md} missing non-empty {field}")
    return frontmatter


def validate_plugin_manifest(root: Path, errors: list[str]) -> None:
    payload = read_json(root / ".codex-plugin" / "plugin.json", errors)
    if payload is None:
        return

    expected = {
        "name": "noootwo-vibe",
        "repository": "https://github.com/noootwo/noootwo-vibe",
        "homepage": "https://github.com/noootwo/noootwo-vibe",
        "skills": "./skills/",
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            add(errors, f"plugin.json `{key}` must be {value!r}")

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        add(errors, "plugin.json interface must be an object")
        return
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
        if field not in interface:
            add(errors, f"plugin.json interface missing {field}")


def validate_root(root: Path, errors: list[str]) -> None:
    if (root / "SKILL.md").exists():
        add(errors, "root SKILL.md must not exist; it hides child skills in default discovery")
    if (root / "agents").exists():
        add(errors, "root agents/ must not exist without a root skill")
    for relative in ("README.md", "AGENTS.md", "VERSION", "skills.json", "docs/status.md"):
        if not (root / relative).exists():
            add(errors, f"missing root path: {relative}")


def validate_manifest(root: Path, errors: list[str]) -> list[dict]:
    payload = read_json(root / "skills.json", errors)
    if payload is None:
        return []
    if payload.get("repository") != "noootwo/noootwo-vibe":
        add(errors, "skills.json repository must be noootwo/noootwo-vibe")
    if payload.get("skillsRoot") != "skills":
        add(errors, "skills.json skillsRoot must be skills")
    if payload.get("releaseModel") != "independent-child-skills":
        add(errors, "skills.json releaseModel must be independent-child-skills")
    skills = payload.get("skills")
    if not isinstance(skills, list):
        add(errors, "skills.json skills must be a list")
        return []
    names = [item.get("name") for item in skills if isinstance(item, dict)]
    if names != EXPECTED_SKILLS:
        add(errors, f"skills.json must list exactly {EXPECTED_SKILLS}")
    return [item for item in skills if isinstance(item, dict)]


def validate_agent_yaml(skill_dir: Path, errors: list[str]) -> None:
    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.is_file():
        add(errors, f"{skill_dir.name} missing agents/openai.yaml")
        return
    raw = agent_yaml.read_text(encoding="utf-8")
    if "interface:" not in raw:
        add(errors, f"{skill_dir.name} agents/openai.yaml missing interface block")
        return
    for field, pattern in {
        "display_name": AGENT_DISPLAY_RE,
        "short_description": AGENT_SHORT_RE,
        "default_prompt": AGENT_PROMPT_RE,
    }.items():
        match = pattern.search(raw)
        if match is None or not match.group(1).strip():
            add(errors, f"{skill_dir.name} agents/openai.yaml missing non-empty {field}")
    if f"${skill_dir.name}" not in raw:
        add(errors, f"{skill_dir.name} default prompt should mention ${skill_dir.name}")


def validate_skill(root: Path, manifest_item: dict, errors: list[str]) -> None:
    name = manifest_item.get("name")
    path_text = manifest_item.get("path")
    version = manifest_item.get("version")
    tag_prefix = manifest_item.get("tagPrefix")
    if not isinstance(name, str) or name not in EXPECTED_SKILLS:
        add(errors, f"invalid skill name in skills.json: {name!r}")
        return
    if path_text != f"skills/{name}":
        add(errors, f"{name} path must be skills/{name}")
    if tag_prefix != f"{name}@":
        add(errors, f"{name} tagPrefix must be {name}@")

    skill_dir = root / f"skills/{name}"
    frontmatter = parse_skill_frontmatter(skill_dir / "SKILL.md", errors)
    if frontmatter and frontmatter.get("name") != name:
        add(errors, f"{name} frontmatter name mismatch")

    version_path = skill_dir / "VERSION"
    if not version_path.is_file():
        add(errors, f"{name} missing VERSION")
    else:
        actual_version = version_path.read_text(encoding="utf-8").strip()
        if actual_version != version:
            add(errors, f"{name} VERSION {actual_version!r} does not match skills.json {version!r}")

    validate_agent_yaml(skill_dir, errors)


def validate_skill_set(root: Path, manifest_items: list[dict], errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        add(errors, "missing skills directory")
        return
    if (skills_root / "noootwo-architecture").exists():
        add(errors, "noootwo-architecture must not exist; architecture belongs to noootwo-review lenses")
    actual = sorted(path.name for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    expected_sorted = sorted(EXPECTED_SKILLS)
    if actual != expected_sorted:
        add(errors, f"skills directory must contain exactly {expected_sorted}; found {actual}")
    for item in manifest_items:
        validate_skill(root, item, errors)


def validate_design_module(root: Path, errors: list[str]) -> None:
    design_root = root / "skills" / "noootwo-design"
    for relative in (
        "references/research-protocol.md",
        "references/workflow-research-notes.md",
        "assets/noootwo-harness-template/system.md",
        "evals/prompts/quick-polish.md",
        "scripts/bootstrap_noootwo_harness.py",
        "scripts/validate_noootwo_readiness.py",
    ):
        if not (design_root / relative).exists():
            add(errors, f"noootwo-design missing {relative}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Noootwo Vibe skill workspace.")
    parser.add_argument("target", nargs="?", default=".", help="Repository root to validate.")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    errors: list[str] = []
    validate_root(root, errors)
    validate_plugin_manifest(root, errors)
    manifest_items = validate_manifest(root, errors)
    validate_skill_set(root, manifest_items, errors)
    validate_design_module(root, errors)

    if errors:
        print("Skill workspace validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"Skill workspace validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
