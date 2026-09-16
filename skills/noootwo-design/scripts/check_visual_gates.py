#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_VIEWPORTS = [
    ("phone", 390, 844),
    ("narrow", 768, 1024),
    ("desktop", 1440, 900),
]


CHECK_JS = """
() => {
  const doc = document.documentElement;
  const body = document.body;
  const overflowX =
    Math.ceil(doc.scrollWidth) > Math.ceil(window.innerWidth) + 1 ||
    Math.ceil(body.scrollWidth) > Math.ceil(window.innerWidth) + 1;

  const describe = (el) => {
    const text = (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 120);
    const rect = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      text,
      left: Math.round(rect.left),
      right: Math.round(rect.right),
      width: Math.round(rect.width),
      scrollWidth: el.scrollWidth,
      clientWidth: el.clientWidth
    };
  };

  const criticalSelector = [
    'h1',
    'h2',
    'h3',
    'nav',
    'button',
    '[role="button"]',
    '[data-noootwo-critical-text]'
  ].join(',');

  const offscreenCritical = Array.from(document.querySelectorAll(criticalSelector))
    .filter((el) => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && (rect.left < -1 || rect.right > window.innerWidth + 1);
    })
    .slice(0, 12)
    .map(describe);

  // Motion findings are advisory evidence, not gate failures. Confirm each one
  // against a screenshot or DOM inspection before it changes a review decision.
  const motion = { linearSpatial: [], slowInteraction: [], noReducedMotion: [], opacityOnlyState: [], endlessLoops: [] };

  const reducedMotionHandled = Array.from(document.styleSheets).some((sheet) => {
    let rules;
    try {
      rules = sheet.cssRules;
    } catch {
      return false;
    }
    return Array.from(rules ?? []).some((rule) => (rule.conditionText || '').includes('prefers-reduced-motion'));
  });

  const interactiveSelector = 'button, [role="button"], a[href], input, select, textarea, summary, [data-state]';
  const spatialProperties = ['transform', 'translate', 'top', 'left', 'right', 'bottom', 'margin', 'width', 'height', 'inset'];

  let animationSeen = false;
  for (const el of document.querySelectorAll('body *')) {
    const rect = el.getBoundingClientRect();
    if (rect.width < 2 || rect.height < 2) continue;
    let style;
    try {
      style = window.getComputedStyle(el);
    } catch {
      continue;
    }

    const properties = (style.transitionProperty || '').split(',').map((part) => part.trim());
    const timings = (style.transitionTimingFunction || '').split(',').map((part) => part.trim());
    const durations = (style.transitionDuration || '').split(',').map((part) => part.trim());
    const hasTransition = durations.some((value) => value && value !== '0s');
    if (hasTransition) animationSeen = true;
    if (style.animationName && style.animationName !== 'none') animationSeen = true;

    const movesSpace = properties.some((property) => spatialProperties.some((token) => property.includes(token)));
    if (movesSpace && timings.includes('linear')) {
      motion.linearSpatial.push(describe(el));
    }

    const isInteractive = el.matches(interactiveSelector);
    if (isInteractive && hasTransition) {
      const longest = durations.reduce((max, value) => {
        const seconds = value.endsWith('ms') ? parseFloat(value) / 1000 : parseFloat(value);
        return Number.isFinite(seconds) ? Math.max(max, seconds) : max;
      }, 0);
      if (longest > 0.5) motion.slowInteraction.push(describe(el));
    }

    const meaningfulStateChange = isInteractive || el.hasAttribute('data-state') || el.getAttribute('aria-expanded') !== null;
    if (meaningfulStateChange && hasTransition && properties.length > 0 && properties.every((property) => property === 'opacity')) {
      motion.opacityOnlyState.push(describe(el));
    }

    if (style.animationIterationCount === 'infinite') {
      const insideControl = el.closest('button, [role="button"], a[href], input, select, label');
      const isAmbient = el.getAttribute('aria-hidden') === 'true' || el.closest('[aria-hidden="true"]');
      if (insideControl && !isAmbient) motion.endlessLoops.push(describe(el));
    }
  }

  for (const key of Object.keys(motion)) {
    motion[key] = motion[key].slice(0, 8);
  }
  if (animationSeen && !reducedMotionHandled) {
    motion.noReducedMotion.push({ tag: 'document', text: 'animation present with no prefers-reduced-motion rule', left: 0, right: 0, width: 0, scrollWidth: 0, clientWidth: 0 });
  }

  const clippedText = Array.from(document.querySelectorAll('body *'))
    .filter((el) => {
      const text = (el.textContent || '').replace(/\\s+/g, ' ').trim();
      if (text.length < 16) return false;
      const style = window.getComputedStyle(el);
      const hidesOverflow = style.overflow === 'hidden' || style.textOverflow === 'ellipsis';
      return hidesOverflow && el.scrollWidth > el.clientWidth + 1;
    })
    .slice(0, 12)
    .map(describe);

  return {
    url: window.location.href,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    scrollWidth: doc.scrollWidth,
    bodyScrollWidth: body.scrollWidth,
    overflowX,
    offscreenCritical,
    clippedText,
    motion
  };
}
"""


def normalize_target(target: str) -> str:
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https", "file"}:
        return target

    path = Path(target).resolve()
    if not path.exists():
        raise SystemExit(f"Target is not a URL or existing file: {target}")
    return path.as_uri()


def parse_viewport(value: str) -> tuple[str, int, int]:
    label, _, size = value.partition(":")
    if not size:
        size = label
        label = size
    width_text, _, height_text = size.lower().partition("x")
    if not width_text or not height_text:
        raise argparse.ArgumentTypeError("Viewport must be WIDTHxHEIGHT or label:WIDTHxHEIGHT")
    return label, int(width_text), int(height_text)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Noootwo responsive visual gates for a local URL or static HTML file."
    )
    parser.add_argument("target", help="Local URL or HTML file path to inspect.")
    parser.add_argument(
        "--viewport",
        action="append",
        type=parse_viewport,
        help="Viewport as WIDTHxHEIGHT or label:WIDTHxHEIGHT. Can be passed multiple times.",
    )
    parser.add_argument(
        "--screenshot-dir",
        help="Optional directory for viewport screenshots.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # pragma: no cover - depends on optional local tooling
        print(
            "Playwright for Python is required for automated visual gates. "
            "Install it or record manual screenshot evidence in .noootwo/review.md."
        )
        print(f"Import error: {exc}")
        return 2

    target_url = normalize_target(args.target)
    viewports = args.viewport or DEFAULT_VIEWPORTS
    screenshot_dir = Path(args.screenshot_dir).resolve() if args.screenshot_dir else None
    if screenshot_dir:
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    results = []
    failures = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        for label, width, height in viewports:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(target_url, wait_until="networkidle")
            result = page.evaluate(CHECK_JS)
            result["label"] = label
            results.append(result)

            if screenshot_dir:
                page.screenshot(path=str(screenshot_dir / f"{label}-{width}x{height}.png"), full_page=True)

            if result["overflowX"]:
                failures.append(f"{label}: horizontal overflow ({result['scrollWidth']} > {width})")
            if result["offscreenCritical"]:
                failures.append(f"{label}: critical elements offscreen")
            if result["clippedText"]:
                failures.append(f"{label}: clipped text detected")

        browser.close()

    motion_labels = {
        "linearSpatial": "spatial movement on a linear curve",
        "slowInteraction": "interactive control with a transition longer than 500ms",
        "noReducedMotion": "animation present with no prefers-reduced-motion rule",
        "opacityOnlyState": "state change carried by opacity alone",
        "endlessLoops": "endless animation inside a control",
    }
    motion_findings: dict[str, list[dict]] = {}
    for result in results:
        for key, label in motion_labels.items():
            entries = (result.get("motion") or {}).get(key) or []
            if not entries:
                continue
            bucket = motion_findings.setdefault(label, [])
            if not any(item["viewport"] == result["label"] for item in bucket):
                bucket.append({"viewport": result["label"], "examples": entries[:3], "count": len(entries)})

    if args.json:
        print(json.dumps({"results": results, "failures": failures, "motionFindings": motion_findings}, indent=2))
    else:
        for result in results:
            print(
                f"{result['label']}: viewport={result['viewport']['width']}x{result['viewport']['height']} "
                f"scrollWidth={result['scrollWidth']} overflowX={result['overflowX']} "
                f"offscreenCritical={len(result['offscreenCritical'])} clippedText={len(result['clippedText'])}"
            )
        if motion_findings:
            print("Motion findings (advisory; confirm against a screenshot or DOM before changing a decision):")
            for label, entries in motion_findings.items():
                viewports = ", ".join(entry["viewport"] for entry in entries)
                examples = entries[0]["examples"]
                sample = examples[0]["tag"] if examples else "-"
                print(f"  - {label} [{viewports}] first seen on <{sample}>")
        else:
            print("Motion findings: none.")
        if failures:
            print("Visual gate failed:")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print("Visual gate passed.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
