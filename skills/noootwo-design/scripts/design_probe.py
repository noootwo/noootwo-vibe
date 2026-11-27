#!/usr/bin/env python3
"""Deterministic rendered evidence for noootwo-design.

The probe captures the required viewport/state matrix, measures mechanical
defects, and writes one JSON file plus screenshots. It does not judge hierarchy,
composition, or taste; the design assessment owns those.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse


DEFAULT_VIEWPORTS = [
    ("320x800", 320, 800),
    ("390x844", 390, 844),
    ("768x1024", 768, 1024),
    ("1440x900", 1440, 900),
]

DEFAULT_STATES = [
    ("default", ""),
    ("error", "?state=error"),
    ("loading", "?state=loading"),
    ("focus", "?state=focus"),
    ("long", "?state=long"),
]

PROBE_JS = r"""
(payload) => {
  const viewport = { width: window.innerWidth, height: window.innerHeight };
  const doc = document.documentElement;
  const body = document.body;
  const all = Array.from(document.querySelectorAll('body *'));

  const rect = (el) => {
    const r = el.getBoundingClientRect();
    return {
      left: Math.round(r.left), top: Math.round(r.top),
      right: Math.round(r.right), bottom: Math.round(r.bottom),
      width: Math.round(r.width), height: Math.round(r.height)
    };
  };

  const visible = (el) => {
    const c = getComputedStyle(el);
    if (c.display === 'none' || c.visibility === 'hidden' || Number(c.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };

  const text = (el) => (el.textContent || '').replace(/\s+/g, ' ').trim();

  const label = (el) => {
    const cls = el.className && typeof el.className === 'string'
      ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.')
      : '';
    return el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + cls;
  };

  const overflowX =
    Math.ceil(doc.scrollWidth) > viewport.width + 1 ||
    Math.ceil(body.scrollWidth) > viewport.width + 1;

  const criticalSelector = 'h1,h2,h3,nav,button,[role="button"],a[href]';
  const offscreenCritical = Array.from(document.querySelectorAll(criticalSelector))
    .filter(visible)
    .map((el) => ({ node: label(el), text: text(el).slice(0, 80), rect: rect(el) }))
    .filter((item) => item.rect.right > viewport.width + 1 || item.rect.left < -1)
    .slice(0, 20);

  const clippedText = all
    .filter((el) => {
      const c = getComputedStyle(el);
      if (!['hidden', 'clip'].includes(c.overflowX)) return false;
      return text(el).length > 0 && el.scrollWidth > el.clientWidth + 1;
    })
    .map((el) => ({ node: label(el), text: text(el).slice(0, 80), scrollWidth: el.scrollWidth, clientWidth: el.clientWidth }))
    .slice(0, 20);

  const offscreenText = all
    .filter((el) => {
      if (!visible(el)) return false;
      if (el.children.length > 0) return false;
      return text(el).length > 0;
    })
    .map((el) => ({ node: label(el), text: text(el).slice(0, 80), rect: rect(el) }))
    .filter((item) => item.rect.right > viewport.width + 1 || item.rect.left < -1)
    .slice(0, 20);

  const active = document.activeElement;
  const focus = { active: active && active !== document.body ? label(active) : null, obscured: false, overlapArea: 0, overlaps: [] };
  if (active && active !== document.body) {
    const ar = active.getBoundingClientRect();
    Array.from(document.querySelectorAll('body *')).forEach((el) => {
      const c = getComputedStyle(el);
      if (!['fixed', 'sticky'].includes(c.position)) return;
      if (!visible(el)) return;
      const br = el.getBoundingClientRect();
      const ox = Math.max(0, Math.min(ar.right, br.right) - Math.max(ar.left, br.left));
      const oy = Math.max(0, Math.min(ar.bottom, br.bottom) - Math.max(ar.top, br.top));
      const area = Math.round(ox * oy);
      if (area > 0) {
        focus.obscured = true;
        focus.overlapArea += area;
        focus.overlaps.push({ node: label(el), area });
      }
    });
  }

  const barOverlaps = [];
  const bars = all.filter((el) => {
    const c = getComputedStyle(el);
    return ['fixed', 'sticky'].includes(c.position) && visible(el) && el.getBoundingClientRect().height > 0;
  });
  bars.forEach((bar) => {
    const br = bar.getBoundingClientRect();
    all.forEach((el) => {
      if (bar === el || bar.contains(el)) return;
      if (!visible(el)) return;
      const isControl = ['INPUT', 'SELECT', 'TEXTAREA', 'BUTTON'].includes(el.tagName);
      const isText = el.children.length === 0 && text(el).length > 0;
      if (!isControl && !isText) return;
      const er = el.getBoundingClientRect();
      const ox = Math.max(0, Math.min(er.right, br.right) - Math.max(er.left, br.left));
      const oy = Math.max(0, Math.min(er.bottom, br.bottom) - Math.max(er.top, br.top));
      const area = Math.round(ox * oy);
      if (area > 8) {
        barOverlaps.push({ bar: label(bar), node: label(el), text: text(el).slice(0, 60), area });
      }
    });
  });

  const parseColor = (value) => {
    const m = String(value).match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const parts = m[1].split(',').map((v) => parseFloat(v.trim()));
    return { r: parts[0], g: parts[1], b: parts[2], a: parts.length > 3 ? parts[3] : 1 };
  };

  const lum = (c) => {
    const f = (x) => {
      const v = x / 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };

  const contrast = (a, b) => {
    const l1 = lum(a), l2 = lum(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  };

  const backgroundOf = (el) => {
    let node = el;
    while (node && node !== document.documentElement) {
      const c = getComputedStyle(node);
      const bg = parseColor(c.backgroundColor);
      if (bg && bg.a > 0.95) return { color: bg, gradient: c.backgroundImage.includes('gradient') };
      if (c.backgroundImage && c.backgroundImage.includes('gradient')) return { color: null, gradient: true };
      node = node.parentElement;
    }
    return { color: parseColor(getComputedStyle(document.body).backgroundColor), gradient: false };
  };

  const contrastFindings = [];
  const seenContrast = new Set();
  all.forEach((el) => {
    if (!visible(el) || el.children.length > 0) return;
    const value = text(el);
    if (!value) return;
    const c = getComputedStyle(el);
    const size = parseFloat(c.fontSize);
    if (!Number.isFinite(size) || size < 10) return;
    const fg = parseColor(c.color);
    if (!fg) return;
    const bg = backgroundOf(el);
    if (!bg.color || bg.gradient) {
      if (bg.gradient && !seenContrast.has('gradient:' + label(el))) {
        seenContrast.add('gradient:' + label(el));
        contrastFindings.push({ node: label(el), text: value.slice(0, 60), ratio: null, required: null, confidence: 'unresolved-gradient' });
      }
      return;
    }
    const weight = parseInt(c.fontWeight, 10) || 400;
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const required = large ? 3.0 : 4.5;
    const ratio = Math.round(contrast(fg, bg.color) * 100) / 100;
    const key = label(el) + ':' + c.color + ':' + ratio;
    if (ratio + 0.05 < required && !seenContrast.has(key)) {
      seenContrast.add(key);
      contrastFindings.push({ node: label(el), text: value.slice(0, 60), ratio, required, confidence: 'measured' });
    }
  });

  const controlFindings = [];
  const controlAdvisories = [];
  Array.from(document.querySelectorAll('input,select,textarea,button,[role="button"]')).forEach((el) => {
    if (!visible(el)) return;
    const c = getComputedStyle(el);
    const bg = parseColor(c.backgroundColor);
    const border = parseColor(c.borderTopColor);
    const width = parseFloat(c.borderTopWidth) || 0;
    const parentBg = backgroundOf(el.parentElement || el);
    if (!parentBg.color) return;
    const filled = bg && bg.a > 0.9 && contrast(bg, parentBg.color) >= 3;
    if (filled) return;
    if (!border || width <= 0 || border.a < 0.5) return;
    const ratio = Math.round(contrast(border, parentBg.color) * 100) / 100;
    if (ratio + 0.05 < 3) {
      const isButton = el.tagName === 'BUTTON' || el.getAttribute('role') === 'button';
      const value = text(el);
      let textPasses = false;
      if (isButton && value) {
        const fg = parseColor(c.color);
        const surface = backgroundOf(el);
        if (fg && surface.color && !surface.gradient) {
          const size = parseFloat(c.fontSize);
          const weight = parseInt(c.fontWeight, 10) || 400;
          const large = size >= 24 || (size >= 18.66 && weight >= 700);
          textPasses = contrast(fg, surface.color) + 0.05 >= (large ? 3.0 : 4.5);
        }
      }
      if (isButton && textPasses) {
        controlAdvisories.push({ node: label(el), ratio, required: 3, reason: 'boundary-secondary-text-passes' });
      } else {
        controlFindings.push({ node: label(el), ratio, required: 3 });
      }
    }
  });

  const tapFindings = [];
  Array.from(document.querySelectorAll('button,[role="button"],a[href],input,select,textarea,summary')).forEach((el) => {
    if (!visible(el)) return;
    const r = el.getBoundingClientRect();
    if (r.width < 24 || r.height < 24) {
      tapFindings.push({ node: label(el), width: Math.round(r.width), height: Math.round(r.height) });
    }
  });

  const unlabeled = [];
  Array.from(document.querySelectorAll('input,select,textarea')).forEach((el) => {
    if (!visible(el)) return;
    const id = el.id;
    const labelled = (id && document.querySelector(`label[for="${CSS.escape(id)}"]`)) ||
      el.closest('label') ||
      el.getAttribute('aria-label') ||
      el.getAttribute('aria-labelledby') ||
      el.getAttribute('title');
    if (!labelled) unlabeled.push(label(el));
  });

  const missingAlt = Array.from(document.querySelectorAll('img')).filter((img) => visible(img) && !img.hasAttribute('alt')).map(label);
  const loadingBusy = document.querySelector('[aria-busy="true"]') !== null;

  return {
    viewport,
    scrollWidth: Math.ceil(doc.scrollWidth),
    bodyScrollWidth: Math.ceil(body.scrollWidth),
    overflowX,
    offscreenCritical,
    clippedText,
    offscreenText,
    focus,
    barOverlaps,
    contrastFindings,
    controlFindings,
    controlAdvisories,
    tapFindings,
    unlabeled,
    missingAlt,
    loadingBusy,
    documentLanguage: document.documentElement.lang || ''
  };
}
"""

RESET_SCROLL_JS = r"""
() => {
  window.scrollTo(0, 0);
  Array.from(document.querySelectorAll('*')).forEach((el) => {
    const c = getComputedStyle(el);
    if (/(auto|scroll)/.test(c.overflowY) && el.scrollHeight > el.clientHeight + 1) {
      el.scrollTop = 0;
    }
  });
}
"""

SCROLL_BOTTOM_JS = r"""
() => {
  window.scrollTo(0, document.documentElement.scrollHeight);
  Array.from(document.querySelectorAll('*')).forEach((el) => {
    const c = getComputedStyle(el);
    if (/(auto|scroll)/.test(c.overflowY) && el.scrollHeight > el.clientHeight + 1) {
      el.scrollTop = el.scrollHeight;
    }
  });
}
"""


def normalize_target(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme in ("http", "https", "file"):
        return value
    path = Path(value).expanduser().resolve()
    if path.is_dir():
        path = path / "index.html"
    return path.as_uri()


def with_query(url: str, query: str) -> str:
    if not query:
        return url
    joiner = "&" if "?" in url else "?"
    return url + joiner + query.lstrip("?")


def parse_state(value: str) -> tuple[str, str]:
    if "=" not in value:
        return value, ""
    name, query = value.split("=", 1)
    return name, query


def png_ok(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "missing"
    if path.stat().st_size < 1024:
        return False, "too small"
    with path.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            return False, "not a PNG"
    return True, "ok"


def capture_ok(path: Path) -> tuple[bool, str]:
    ok, reason = png_ok(path)
    if not ok:
        return ok, reason
    try:
        from validate_noootwo_readiness import validate_capture_file

        defect = validate_capture_file(path)
        if defect:
            return False, defect
    except Exception:
        pass
    return True, "ok"


def blocker(kind: str, viewport: str, state: str, detail: str) -> dict:
    return {"kind": kind, "viewport": viewport, "state": state, "detail": detail}


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture and measure a rendered UI artifact.")
    parser.add_argument("target", help="Local HTML file, directory with index.html, or http(s) URL.")
    parser.add_argument("--out", default=".noootwo/design", help="Output directory. Defaults to .noootwo/design.")
    parser.add_argument("--viewport", action="append", default=None, help="WIDTHxHEIGHT or label:WIDTHxHEIGHT. Repeatable.")
    parser.add_argument("--state", action="append", default=None, help="NAME or NAME=?query. Repeatable.")
    parser.add_argument("--browser-channel", default=None, help="Playwright browser channel, such as chrome.")
    parser.add_argument("--allow-blockers", action="store_true", help="Write findings but exit 0.")
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print("Playwright for Python is required for design_probe.py.")
        print(f"Import error: {exc}")
        return 2

    screenshots = Path(args.out).expanduser().resolve() / "shots"
    if screenshots.exists():
        shutil.rmtree(screenshots)
    screenshots.mkdir(parents=True, exist_ok=True)

    if args.viewport:
        viewports = []
        for item in args.viewport:
            if ":" in item and not item.split(":")[0].isdigit():
                label, size = item.split(":", 1)
            else:
                size = item
                label = item
            width, height = size.lower().split("x", 1)
            viewports.append((label, int(width), int(height)))
    else:
        viewports = DEFAULT_VIEWPORTS

    states = [parse_state(item) for item in args.state] if args.state else DEFAULT_STATES
    target = normalize_target(args.target)
    results = []
    captures = []
    blockers = []
    advisories = []

    try:
        with sync_playwright() as playwright:
            launch = {"channel": args.browser_channel} if args.browser_channel else {}
            try:
                browser = playwright.chromium.launch(**launch)
            except Exception:
                browser = playwright.chromium.launch(channel="chrome")

            for label, width, height in viewports:
                for state, query in states:
                    page = browser.new_page(viewport={"width": width, "height": height})
                    page.goto(with_query(target, query), wait_until="networkidle")
                    page.wait_for_timeout(250)

                    if state == "focus":
                        page.evaluate(
                            """() => {
                              const candidates = Array.from(document.querySelectorAll('input,select,textarea,button,a[href]'))
                                .filter((el) => {
                                  const c = getComputedStyle(el);
                                  const r = el.getBoundingClientRect();
                                  return c.display !== 'none' && c.visibility !== 'hidden' && r.width > 0 && r.height > 0
                                    && !el.closest('.save-bar,[role="dialog"]');
                                });
                              const target = candidates[candidates.length - 1];
                              if (target) { target.scrollIntoView({ block: 'end' }); target.focus(); }
                            }"""
                        )

                    if state != "focus":
                        page.evaluate(RESET_SCROLL_JS)
                    page.wait_for_timeout(100)

                    shot = screenshots / f"{label}-{state}.png"
                    page.screenshot(path=str(shot), full_page=True)
                    ok, reason = capture_ok(shot)
                    captures.append(
                        {
                            "viewport": label,
                            "state": state,
                            "region": "primary",
                            "path": str(shot),
                            "valid": ok,
                            "reason": reason,
                        }
                    )
                    if not ok:
                        blockers.append(blocker("invalid-capture", label, state, f"{shot} {reason}"))

                    page.evaluate(SCROLL_BOTTOM_JS)
                    page.wait_for_timeout(150)
                    data = page.evaluate(PROBE_JS, {})

                    if data["barOverlaps"] or data["focus"]["obscured"]:
                        bottom = screenshots / f"{label}-{state}-bottom.png"
                        page.screenshot(path=str(bottom), full_page=False)
                        bottom_ok, bottom_reason = capture_ok(bottom)
                        captures.append(
                            {
                                "viewport": label,
                                "state": state,
                                "region": "bottom",
                                "path": str(bottom),
                                "valid": bottom_ok,
                                "reason": bottom_reason,
                            }
                        )
                        if not bottom_ok:
                            blockers.append(blocker("invalid-capture", label, state, f"{bottom} {bottom_reason}"))

                    if data["overflowX"]:
                        blockers.append(blocker("horizontal-overflow", label, state, f"scrollWidth={data['scrollWidth']} viewport={width}"))
                    if data["offscreenCritical"]:
                        names = ", ".join(item["node"] for item in data["offscreenCritical"][:5])
                        blockers.append(blocker("offscreen-critical", label, state, names))
                    if data["clippedText"]:
                        names = ", ".join(item["node"] for item in data["clippedText"][:5])
                        blockers.append(blocker("clipped-text", label, state, names))
                    if data["barOverlaps"]:
                        names = ", ".join(f"{item['bar']} covers {item['node']}" for item in data["barOverlaps"][:5])
                        blockers.append(blocker("fixed-bar-overlap", label, state, names))
                    if data["focus"]["obscured"]:
                        nodes = ", ".join(item["node"] for item in data["focus"]["overlaps"][:3])
                        blockers.append(blocker("focus-obscured", label, state, f"{data['focus']['active']} under {nodes}"))
                    measured = [item for item in data["contrastFindings"] if item["confidence"] == "measured"]
                    if measured:
                        names = ", ".join(f"{item['node']}={item['ratio']}" for item in measured[:5])
                        blockers.append(blocker("text-contrast", label, state, names))
                    if data["controlFindings"]:
                        names = ", ".join(f"{item['node']}={item['ratio']}" for item in data["controlFindings"][:5])
                        blockers.append(blocker("control-contrast", label, state, names))
                    if data["controlAdvisories"]:
                        names = ", ".join(f"{item['node']}={item['ratio']}" for item in data["controlAdvisories"][:5])
                        advisories.append({"kind": "control-boundary-low", "viewport": label, "state": state, "detail": names})
                    if data["unlabeled"]:
                        blockers.append(blocker("unlabeled-control", label, state, ", ".join(data["unlabeled"][:5])))
                    if data["missingAlt"]:
                        advisories.append({"kind": "missing-alt", "viewport": label, "state": state, "detail": ", ".join(data["missingAlt"][:5])})
                    if data["tapFindings"]:
                        names = ", ".join(f"{item['node']}={item['width']}x{item['height']}" for item in data["tapFindings"][:5])
                        advisories.append({"kind": "small-target", "viewport": label, "state": state, "detail": names})
                    if state == "loading" and not data["loadingBusy"]:
                        advisories.append({"kind": "loading-not-announced", "viewport": label, "state": state, "detail": "no aria-busy=true"})
                    unresolved = [item for item in data["contrastFindings"] if item["confidence"] == "unresolved-gradient"]
                    if unresolved:
                        advisories.append({"kind": "gradient-contrast-unresolved", "viewport": label, "state": state, "detail": ", ".join(item["node"] for item in unresolved[:5])})

                    results.append(
                        {
                            "viewport": label,
                            "state": state,
                            "viewport_size": data["viewport"],
                            **{key: value for key, value in data.items() if key != "viewport"},
                        }
                    )
                    page.close()

            browser.close()
    except Exception as exc:
        print(f"design_probe failed: {exc}")
        return 2

    payload = {
        "target": target,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "viewports": [label for label, _, _ in viewports],
        "states": [name for name, _ in states],
        "captures": captures,
        "results": results,
        "blockers": blockers,
        "advisories": advisories,
    }
    out_dir = Path(args.out).expanduser().resolve()
    (out_dir / "probe.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = ["# Design Probe", "", f"- Target: `{target}`", f"- Viewports: {', '.join(payload['viewports'])}", f"- States: {', '.join(payload['states'])}", ""]
    lines.append("| Viewport / state | Overflow | Offscreen | Clipped | Focus | Contrast | Controls |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for result in results:
        lines.append(
            "| {viewport} / {state} | {overflow} | {offscreen} | {clipped} | {focus} | {contrast} | {controls} |".format(
                viewport=result["viewport"],
                state=result["state"],
                overflow="yes" if result["overflowX"] else "no",
                offscreen=len(result["offscreenCritical"]),
                clipped=len(result["clippedText"]),
                focus="hidden" if result["focus"]["obscured"] else ("n/a" if not result["focus"]["active"] else "ok"),
                contrast=len([item for item in result["contrastFindings"] if item["confidence"] == "measured"]),
                controls=len(result["controlFindings"]),
            )
        )
    lines.extend(["", "## Blockers", ""])
    lines.extend(f"- `{item['kind']}` — {item['viewport']} / {item['state']}: {item['detail']}" for item in blockers)
    if not blockers:
        lines.append("- None.")
    lines.extend(["", "## Advisories", ""])
    lines.extend(f"- `{item['kind']}` — {item['viewport']} / {item['state']}: {item['detail']}" for item in advisories)
    if not advisories:
        lines.append("- None.")
    (out_dir / "probe.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {out_dir / 'probe.json'}")
    print(f"Blockers: {len(blockers)}; advisories: {len(advisories)}")
    for item in blockers[:12]:
        print(f"- {item['kind']} {item['viewport']}/{item['state']}: {item['detail']}")
    if blockers and not args.allow_blockers:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
