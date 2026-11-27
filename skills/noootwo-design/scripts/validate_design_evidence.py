#!/usr/bin/env python3
"""Validate that a design review is backed by rendered evidence.

This is the active gate for noootwo-design. It checks evidence existence and
consistency, not prose shape. The legacy readiness validator remains for
historical projects and eval fixtures.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DISPOSITIONS = {"recapture", "rebuild", "fix", "ship"}
COMMANDS = {
    "shape",
    "build",
    "critique",
    "polish",
    "layout",
    "typeset",
    "harden",
    "motion",
    "system",
    "direction",
    "translate",
}
SEVERITIES = {"blocking", "advisory"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def load_json(path: Path) -> tuple[dict | None, str | None]:
    if not path.exists():
        return None, f"{path} is missing"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"{path} is not valid JSON: {exc}"


def png_ok(path: Path) -> str | None:
    if not path.exists():
        return "does not exist"
    if path.stat().st_size < 1024:
        return "is too small to be a rendered capture"
    with path.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            return "is not a PNG"
    return None


def image_ok(path: Path) -> str | None:
    if path.suffix.lower() not in IMAGE_SUFFIXES:
        return f"is not a rendered image ({path.suffix or 'no suffix'})"
    if path.suffix.lower() != ".png":
        return None if path.exists() and path.stat().st_size >= 1024 else "does not exist or is too small"
    return png_ok(path)


def resolve_evidence(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate design review evidence.")
    parser.add_argument("target", nargs="?", default=".", help="Project root.")
    parser.add_argument("--production", action="store_true", help="Require an independent reviewer.")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    review_path = root / ".noootwo" / "design" / "review.json"
    if not review_path.exists():
        review_path = root / ".noootwo" / "review.json"
    probe_path = root / ".noootwo" / "design" / "probe.json"

    errors: list[str] = []
    review, error = load_json(review_path)
    if error:
        print(f"Design evidence validation failed:\n  - {error}")
        return 1

    assert review is not None
    for field in ("target", "command", "viewports", "states", "findings", "disposition", "reviewer", "local_only", "next_action"):
        if field not in review:
            errors.append(f"{review_path} is missing `{field}`")

    disposition = str(review.get("disposition", "")).lower()
    if disposition not in DISPOSITIONS:
        errors.append(f"{review_path} disposition must be one of {sorted(DISPOSITIONS)}")

    command = str(review.get("command", "")).lower()
    if command not in COMMANDS:
        errors.append(f"{review_path} command must be one of {sorted(COMMANDS)}")

    findings = review.get("findings") or []
    if not isinstance(findings, list):
        errors.append(f"{review_path} `findings` must be a list")
        findings = []
    blocking = []
    for index, item in enumerate(findings):
        if not isinstance(item, dict):
            errors.append(f"{review_path} findings[{index}] must be an object")
            continue
        severity = str(item.get("severity", "")).lower()
        if severity not in SEVERITIES:
            errors.append(f"{review_path} findings[{index}] severity must be one of {sorted(SEVERITIES)}")
        if severity == "blocking":
            blocking.append(item)
        if not str(item.get("region", "")).strip():
            errors.append(f"{review_path} findings[{index}] needs a `region`")
        evidence = str(item.get("evidence", "")).strip()
        if not evidence:
            errors.append(f"{review_path} findings[{index}] needs rendered `evidence`")
            continue
        path = resolve_evidence(root, evidence)
        defect = image_ok(path)
        if defect:
            errors.append(f"{review_path} findings[{index}] evidence {path} {defect}")

    reviewer = str(review.get("reviewer", "")).lower()
    local_only = bool(review.get("local_only", False))
    if reviewer not in {"builder", "independent"}:
        errors.append(f"{review_path} `reviewer` must be `builder` or `independent`")
    if args.production and reviewer != "independent":
        errors.append(f"{review_path} production review requires `reviewer: independent`")
    if reviewer == "builder" and not local_only:
        errors.append(f"{review_path} builder-only review requires `local_only: true`")

    probe, error = load_json(probe_path)
    if error:
        errors.append(error)

    if disposition == "ship":
        if blocking:
            errors.append(f"{review_path} cannot ship with {len(blocking)} blocking finding(s)")
        if probe is None:
            errors.append(f"{review_path} cannot ship without {probe_path}")
        else:
            probe_blockers = probe.get("blockers") or []
            if probe_blockers:
                errors.append(f"{probe_path} still has {len(probe_blockers)} blocker(s)")
            viewports = set(review.get("viewports") or [])
            states = set(review.get("states") or [])
            if not viewports:
                errors.append(f"{review_path} ship requires at least one rendered viewport")
            if "default" not in states:
                errors.append(f"{review_path} ship requires a rendered `default` state")
            probe_viewports = set(probe.get("viewports") or [])
            probe_states = set(probe.get("states") or [])
            if viewports != probe_viewports:
                errors.append(
                    f"{review_path} viewports {sorted(viewports)} do not match {probe_path} {sorted(probe_viewports)}"
                )
            if states != probe_states:
                errors.append(
                    f"{review_path} states {sorted(states)} do not match {probe_path} {sorted(probe_states)}"
                )
            captures = probe.get("captures") or []
            results = {
                (item.get("viewport"), item.get("state")): item
                for item in (probe.get("results") or [])
                if isinstance(item, dict)
            }
            for capture in captures:
                path = resolve_evidence(root, str(capture.get("path", "")))
                defect = png_ok(path)
                if defect:
                    errors.append(f"capture {path} {defect}")
            for viewport in sorted(viewports):
                for state in sorted(states):
                    if not any(
                        c.get("viewport") == viewport
                        and c.get("state") == state
                        and c.get("region") == "primary"
                        and c.get("valid")
                        for c in captures
                    ):
                        errors.append(f"missing valid primary capture for {viewport}/{state}")
                    result = results.get((viewport, state)) or {}
                    obscured = bool(result.get("barOverlaps") or (result.get("focus") or {}).get("obscured"))
                    if obscured and not any(
                        c.get("viewport") == viewport
                        and c.get("state") == state
                        and c.get("region") == "bottom"
                        and c.get("valid")
                        for c in captures
                    ):
                        errors.append(f"missing bottom-overlap capture for {viewport}/{state}")

    if disposition in {"fix", "rebuild", "recapture"}:
        if not str(review.get("next_action", "")).strip():
            errors.append(f"{review_path} `next_action` is required for {disposition}")

    if errors:
        print("Design evidence validation failed:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print(f"Design evidence validation passed: {review_path} ({disposition}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
