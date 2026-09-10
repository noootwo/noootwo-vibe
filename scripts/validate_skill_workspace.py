#!/usr/bin/env python3
"""Validate the Noootwo Vibe skill workspace against docs/agents/skill-authoring.md."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EXPECTED_SKILLS = [
    "noootwo-ask",
    "noootwo-workflow",
    "noootwo-product",
    "noootwo-design",
    "noootwo-review",
    "noootwo-docs",
]

# The only user-invoked skill. Everything else stays reachable by the model.
USER_INVOKED_SKILLS = {"noootwo-ask"}

# Router text is written for a human, so it may use the $name form.
ROUTER_SKILLS = {"noootwo-ask"}

MAX_DESCRIPTION_CHARS = 200
MAX_SKILL_LINES = 120
MAX_REFERENCE_FILES = 12
MIN_SHORT_DESCRIPTION = 25
MAX_SHORT_DESCRIPTION = 64

FRONTMATTER_FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$")
FRONTMATTER_ALLOWED = {"name", "description", "disable-model-invocation"}
AGENT_DISPLAY_RE = re.compile(r'^\s{2}display_name:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_SHORT_RE = re.compile(r'^\s{2}short_description:\s*"?(.*?)"?\s*$', re.MULTILINE)
AGENT_PROMPT_RE = re.compile(r'^\s{2}default_prompt:', re.MULTILINE)
AGENT_POLICY_RE = re.compile(r'^\s{2}allow_implicit_invocation:\s*(true|false)\s*$', re.MULTILINE)
BARE_SKILL_REF_RE = re.compile(r"\\?\$(noootwo-[a-z0-9-]+)")


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

    unsupported = sorted(set(frontmatter) - FRONTMATTER_ALLOWED)
    if unsupported:
        add(
            errors,
            f"{skill_md} frontmatter only supports {sorted(FRONTMATTER_ALLOWED)}; found {', '.join(unsupported)}",
        )
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
    for relative in ("docs/agents/skill-authoring.md", "docs/agents/invocation.md"):
        if not (root / relative).exists():
            add(errors, f"missing authoring standard: {relative}")


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
    name = skill_dir.name
    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.is_file():
        add(errors, f"{name} missing agents/openai.yaml")
        return
    raw = agent_yaml.read_text(encoding="utf-8")
    if "interface:" not in raw:
        add(errors, f"{name} agents/openai.yaml missing interface block")
        return

    display = AGENT_DISPLAY_RE.search(raw)
    if display is None or not display.group(1).strip():
        add(errors, f"{name} agents/openai.yaml missing non-empty display_name")

    short = AGENT_SHORT_RE.search(raw)
    if short is None or not short.group(1).strip():
        add(errors, f"{name} agents/openai.yaml missing non-empty short_description")
    else:
        length = len(short.group(1).strip())
        if not MIN_SHORT_DESCRIPTION <= length <= MAX_SHORT_DESCRIPTION:
            add(
                errors,
                f"{name} short_description must be {MIN_SHORT_DESCRIPTION}-{MAX_SHORT_DESCRIPTION} "
                f"characters; found {length}",
            )

    if AGENT_PROMPT_RE.search(raw):
        add(
            errors,
            f"{name} agents/openai.yaml must not set default_prompt; the description already carries the trigger",
        )

    policy = AGENT_POLICY_RE.search(raw)
    implicit = None if policy is None else policy.group(1) == "true"
    if name in USER_INVOKED_SKILLS:
        if implicit is not False:
            add(
                errors,
                f"{name} is user-invoked and must set policy.allow_implicit_invocation: false",
            )
    elif implicit is False:
        add(
            errors,
            f"{name} is model-invoked and must not disable implicit invocation",
        )


def validate_references(skill_dir: Path, skill_text: str, errors: list[str]) -> None:
    name = skill_dir.name
    references_root = skill_dir / "references"
    if not references_root.is_dir():
        return
    # Vendored source material under references/external/ is not skill reference;
    # only authored markdown is counted and must be reachable by a pointer.
    files = sorted(
        path
        for path in references_root.rglob("*.md")
        if "external" not in path.relative_to(references_root).parts
    )
    if len(files) > MAX_REFERENCE_FILES:
        add(
            errors,
            f"{name} has {len(files)} reference files; the standard allows {MAX_REFERENCE_FILES}",
        )
    for path in files:
        relative = path.relative_to(skill_dir).as_posix()
        if relative not in skill_text:
            add(errors, f"{name} reference {relative} is not named by a pointer in SKILL.md")

    # A pointer that names a file which does not exist is the mirror failure,
    # and it is how a merged-away reference silently disappears.
    for pointer in sorted(set(re.findall(r"references/[A-Za-z0-9_./-]+\.md", skill_text))):
        if not (skill_dir / pointer).is_file():
            add(errors, f"{name} SKILL.md points at {pointer}, which does not exist")


def validate_skill_body(skill_dir: Path, errors: list[str]) -> None:
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return
    raw = skill_md.read_text(encoding="utf-8")

    line_count = len(raw.splitlines())
    if line_count > MAX_SKILL_LINES:
        add(errors, f"{name} SKILL.md is {line_count} lines; the standard allows {MAX_SKILL_LINES}")

    description = parse_skill_frontmatter(skill_md, errors)
    if description is not None:
        value = description.get("description", "")
        if len(value) > MAX_DESCRIPTION_CHARS:
            add(
                errors,
                f"{name} description is {len(value)} characters; the standard allows {MAX_DESCRIPTION_CHARS}",
            )

    if name not in ROUTER_SKILLS:
        body = raw.split("\n---", 1)[-1]
        for match in BARE_SKILL_REF_RE.finditer(body):
            add(
                errors,
                f"{name} SKILL.md uses bare ${match.group(1)}; write a load instruction instead",
            )

    validate_references(skill_dir, raw, errors)


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
    validate_skill_body(skill_dir, errors)


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
        "assets/noootwo-harness-template/system.md",
        "scripts/bootstrap_noootwo_harness.py",
        "scripts/validate_noootwo_readiness.py",
        "scripts/check_visual_gates.py",
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
