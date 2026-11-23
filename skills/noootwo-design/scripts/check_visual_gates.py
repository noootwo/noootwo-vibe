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

DEFAULT_GEOMETRY_TOLERANCE = 1.5


CHECK_JS = """
(payload) => {
  const regions = payload?.regions ?? [];
  const tolerance = Number(payload?.tolerance ?? 1.5);
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

  // Interface findings are advisory evidence, not gate failures. Confirm each
  // one against the source, accessibility tree, or a manual keyboard pass.
  const interfaceChecks = { unlabeledControls: [], imagesMissingAlt: [], imagesMissingDimensions: [], transitionAll: [], outlineRemoved: [], smallTouchTargets: [], zoomDisabled: [] };

  const isHidden = (el) => {
    if (el.getAttribute('aria-hidden') === 'true') return true;
    const style = window.getComputedStyle(el);
    return style.display === 'none' || style.visibility === 'hidden' || Number(style.opacity) === 0;
  };

  const accessibleName = (el) => {
    const aria = (el.getAttribute('aria-label') || '').trim();
    if (aria) return aria;
    const labelledby = el.getAttribute('aria-labelledby');
    if (labelledby) {
      const joined = labelledby
        .split(/\\s+/)
        .map((id) => (document.getElementById(id)?.textContent || '').trim())
        .filter(Boolean)
        .join(' ');
      if (joined) return joined;
    }
    const title = (el.getAttribute('title') || '').trim();
    if (title) return title;
    if (el.labels && el.labels.length) {
      const label = Array.from(el.labels).map((item) => (item.textContent || '').trim()).filter(Boolean).join(' ');
      if (label) return label;
    }
    if (el.tagName.toLowerCase() === 'input' && ['submit', 'button', 'reset'].includes(el.type)) {
      const value = (el.getAttribute('value') || '').trim();
      if (value) return value;
    }
    const text = (el.textContent || '').replace(/\\s+/g, ' ').trim();
    if (text) return text;
    const imageAlt = (el.querySelector?.('img[alt]')?.getAttribute('alt') || '').trim();
    return imageAlt;
  };

  const controls = Array.from(document.querySelectorAll('button, [role="button"], a[href], input, select, textarea, summary'))
    .filter((el) => !isHidden(el));

  for (const el of controls) {
    if (el.tagName.toLowerCase() === 'input' && el.type === 'hidden') continue;
    if (!accessibleName(el)) interfaceChecks.unlabeledControls.push(describe(el));
  }

  for (const image of document.querySelectorAll('img')) {
    if (isHidden(image)) continue;
    if (!image.hasAttribute('alt')) interfaceChecks.imagesMissingAlt.push(describe(image));
    const hasAttributeSize = image.hasAttribute('width') && image.hasAttribute('height');
    const style = window.getComputedStyle(image);
    const hasAspectRatio = style.aspectRatio && style.aspectRatio !== 'auto';
    if (!hasAttributeSize && !hasAspectRatio) interfaceChecks.imagesMissingDimensions.push(describe(image));
  }

  for (const el of document.querySelectorAll('body *')) {
    const rect = el.getBoundingClientRect();
    if (rect.width < 2 || rect.height < 2 || isHidden(el)) continue;
    const style = window.getComputedStyle(el);
    const durations = (style.transitionDuration || '').split(',').map((value) => value.trim());
    const properties = (style.transitionProperty || '').split(',').map((value) => value.trim());
    const hasDuration = durations.some((value) => value && value !== '0s');
    if (hasDuration && properties.some((property) => property === 'all')) interfaceChecks.transitionAll.push(describe(el));
  }

  if (window.innerWidth <= 768) {
    for (const el of controls) {
      const style = window.getComputedStyle(el);
      if (style.display === 'inline') continue;
      const rect = el.getBoundingClientRect();
      if (rect.width < 40 || rect.height < 40) interfaceChecks.smallTouchTargets.push(describe(el));
    }
  }

  let focusReplacementSeen = false;
  let outlineRemovalSeen = false;
  for (const sheet of Array.from(document.styleSheets)) {
    let rules;
    try {
      rules = sheet.cssRules;
    } catch {
      continue;
    }
    for (const rule of Array.from(rules ?? [])) {
      const selector = rule.selectorText || '';
      const text = rule.cssText || '';
      const removesOutline = /outline\\s*:\\s*(none|0)\\b/i.test(text);
      const addsFocusVisual = /outline\\s*:\\s*(?!none|0)/i.test(text) || /box-shadow\\s*:/i.test(text);
      if ((selector.includes(':focus-visible') || selector.includes(':focus')) && addsFocusVisual) focusReplacementSeen = true;
      if (removesOutline && (selector.includes(':focus') || selector.includes('*'))) outlineRemovalSeen = true;
    }
  }
  if (outlineRemovalSeen && !focusReplacementSeen) {
    interfaceChecks.outlineRemoved.push({ tag: 'stylesheet', text: 'outline removal with no focus rule', left: 0, right: 0, width: 0, scrollWidth: 0, clientWidth: 0 });
  }

  const viewportMeta = document.querySelector('meta[name="viewport"]');
  if (viewportMeta) {
    const content = (viewportMeta.getAttribute('content') || '').toLowerCase();
    const noScale = content.includes('user-scalable=no') || content.includes('user-scalable=0');
    const maxScale = content.match(/maximum-scale\\s*=\\s*([0-9.]+)/);
    if (noScale || (maxScale && parseFloat(maxScale[1]) < 2)) interfaceChecks.zoomDisabled.push(describe(viewportMeta));
  }

  for (const key of Object.keys(interfaceChecks)) {
    interfaceChecks[key] = interfaceChecks[key].slice(0, 8);
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

  const round = (value) => Math.round(value * 10) / 10;
  const px = (value) => {
    const parsed = parseFloat(value);
    return Number.isFinite(parsed) ? parsed : 0;
  };
  const rectOf = (el) => {
    const rect = el.getBoundingClientRect();
    return {
      top: rect.top,
      right: rect.right,
      bottom: rect.bottom,
      left: rect.left,
      width: rect.width,
      height: rect.height
    };
  };
  const visibleElement = (el) => {
    if (!el || el.nodeType !== 1) return false;
    if (['script', 'style', 'template', 'noscript'].includes(el.tagName.toLowerCase())) return false;
    if (isHidden(el)) return false;
    const rect = el.getBoundingClientRect();
    return rect.width >= 2 && rect.height >= 2;
  };
  const overlapArea = (a, b) => {
    const width = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
    const height = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
    return width * height;
  };
  const itemLabel = (el) => {
    const text = (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 48);
    const id = el.id ? `#${el.id}` : '';
    return `${el.tagName.toLowerCase()}${id}${text ? `:${text}` : ''}`;
  };
  const regionConfigs = [...regions];
  for (const el of document.querySelectorAll('[data-noootwo-region]')) {
    const value = el.getAttribute('data-noootwo-region') || '';
    const selector = value
      ? `[data-noootwo-region="${value.replace(/"/g, '\\\\"')}"]`
      : '[data-noootwo-region]';
    if (!regionConfigs.some((config) => config.selector === selector)) {
      regionConfigs.push({ name: value || el.id || 'region', selector });
    }
  }

  const geometry = [];
  const seenRegions = new Set();
  for (const config of regionConfigs) {
    const record = {
      name: config.name || config.selector,
      selector: config.selector,
      status: 'ok',
      container: null,
      padding: null,
      insets: null,
      rows: 0,
      singleRow: false,
      items: 0,
      itemSource: 'children',
      innerGap: null,
      innerGaps: [],
      outerGaps: [],
      alignment: null,
      overlaps: [],
      clipped: [],
      advisories: [],
      failures: []
    };

    let region;
    try {
      region = document.querySelector(config.selector);
    } catch (error) {
      record.status = 'selector-error';
      record.failures.push(`invalid selector: ${error.message}`);
      geometry.push(record);
      continue;
    }
    if (!region) {
      record.status = 'missing';
      record.failures.push('selector matched no element');
      geometry.push(record);
      continue;
    }
    if (seenRegions.has(region)) continue;
    seenRegions.add(region);

    const container = rectOf(region);
    const style = window.getComputedStyle(region);
    record.container = {
      width: round(container.width),
      height: round(container.height),
      top: round(container.top),
      left: round(container.left)
    };
    record.padding = {
      top: round(px(style.paddingTop)),
      right: round(px(style.paddingRight)),
      bottom: round(px(style.paddingBottom)),
      left: round(px(style.paddingLeft))
    };

    let items = Array.from(region.querySelectorAll('[data-noootwo-item]')).filter(visibleElement);
    if (items.length) record.itemSource = 'data-noootwo-item';
    if (!items.length) {
      items = Array.from(region.children).filter(visibleElement);
      record.itemSource = 'children';
    }
    if (items.length === 1 && items[0] !== region) {
      const nested = Array.from(items[0].children).filter(visibleElement);
      if (nested.length) {
        items = nested;
        record.itemSource = 'nested-children';
      }
    }
    if (!items.length && region.children.length > 0) {
      record.status = 'empty';
      record.failures.push('no visible items to measure');
      geometry.push(record);
      continue;
    }
    if (!items.length && visibleElement(region)) {
      items = [region];
      record.itemSource = 'self';
    }

    const measuredItems = items.map((el) => ({ el, rect: rectOf(el), label: itemLabel(el) }));
    record.items = measuredItems.length;
    if (!measuredItems.length) {
      record.status = 'empty';
      record.failures.push('no visible items to measure');
      geometry.push(record);
      continue;
    }

    const minTop = Math.min(...measuredItems.map((item) => item.rect.top));
    const maxRight = Math.max(...measuredItems.map((item) => item.rect.right));
    const maxBottom = Math.max(...measuredItems.map((item) => item.rect.bottom));
    const minLeft = Math.min(...measuredItems.map((item) => item.rect.left));
    record.insets = {
      top: round(minTop - container.top),
      right: round(container.right - maxRight),
      bottom: round(container.bottom - maxBottom),
      left: round(minLeft - container.left)
    };

    const rows = [];
    for (const item of [...measuredItems].sort((a, b) => a.rect.top - b.rect.top || a.rect.left - b.rect.left)) {
      const center = item.rect.top + item.rect.height / 2;
      let row = rows.find((candidate) => {
        const rowCenter = candidate.top + candidate.height / 2;
        return Math.abs(center - rowCenter) <= Math.max(tolerance * 2, Math.min(item.rect.height, candidate.height) / 2);
      });
      if (!row) {
        row = { top: item.rect.top, bottom: item.rect.bottom, height: item.rect.height, items: [] };
        rows.push(row);
      }
      row.items.push(item);
      row.top = Math.min(row.top, item.rect.top);
      row.bottom = Math.max(row.bottom, item.rect.bottom);
      row.height = Math.max(row.height, item.rect.height);
    }
    record.rows = rows.length;
    record.singleRow = rows.length === 1;

    const gaps = [];
    for (const row of rows) {
      const ordered = [...row.items].sort((a, b) => a.rect.left - b.rect.left);
      for (let index = 1; index < ordered.length; index += 1) {
        const previous = ordered[index - 1];
        const current = ordered[index];
        const gap = current.rect.left - previous.rect.right;
        if (gap > tolerance * 2) {
          gaps.push({ axis: 'horizontal', from: previous.label, to: current.label, gap: round(gap) });
        }
      }
    }
    for (let index = 1; index < rows.length; index += 1) {
      const previous = rows[index - 1];
      const current = rows[index];
      const gap = current.top - previous.bottom;
      if (gap > tolerance * 2) {
        gaps.push({ axis: 'vertical', from: 'previous row', to: 'next row', gap: round(gap) });
      }
    }
    const numericGaps = gaps.map((entry) => entry.gap).sort((a, b) => a - b);
    record.innerGaps = gaps.slice(0, 12);
    record.innerGap = numericGaps.length
      ? {
          min: numericGaps[0],
          median: numericGaps[Math.floor(numericGaps.length / 2)],
          max: numericGaps[numericGaps.length - 1]
        }
      : null;

    const outerGaps = [];
    const parent = region.parentElement;
    if (parent) {
      for (const sibling of Array.from(parent.children)) {
        if (sibling === region || !visibleElement(sibling)) continue;
        const siblingRect = rectOf(sibling);
        const verticalOverlap = Math.min(container.bottom, siblingRect.bottom) - Math.max(container.top, siblingRect.top);
        const horizontalOverlap = Math.min(container.right, siblingRect.right) - Math.max(container.left, siblingRect.left);
        if (horizontalOverlap > tolerance * 2 && siblingRect.bottom <= container.top + tolerance) {
          outerGaps.push({ side: 'top', gap: round(container.top - siblingRect.bottom), sibling: itemLabel(sibling) });
        }
        if (horizontalOverlap > tolerance * 2 && siblingRect.top >= container.bottom - tolerance) {
          outerGaps.push({ side: 'bottom', gap: round(siblingRect.top - container.bottom), sibling: itemLabel(sibling) });
        }
        if (verticalOverlap > tolerance * 2 && siblingRect.right <= container.left + tolerance) {
          outerGaps.push({ side: 'left', gap: round(container.left - siblingRect.right), sibling: itemLabel(sibling) });
        }
        if (verticalOverlap > tolerance * 2 && siblingRect.left >= container.right - tolerance) {
          outerGaps.push({ side: 'right', gap: round(siblingRect.left - container.right), sibling: itemLabel(sibling) });
        }
      }
    }
    record.outerGaps = outerGaps.filter((entry) => entry.gap >= 0).slice(0, 12);

    if (record.singleRow) {
      const centers = rows[0].items.map((item) => round(item.rect.top + item.rect.height / 2));
      const topEdges = rows[0].items.map((item) => round(item.rect.top)).sort((a, b) => a - b);
      record.alignment = {
        topEdges,
        centerSpread: round(Math.max(...centers) - Math.min(...centers))
      };
    } else {
      const rowLeftEdges = rows.map((row) => round(Math.min(...row.items.map((item) => item.rect.left))));
      const clusters = [];
      for (const edge of rowLeftEdges) {
        const cluster = clusters.find((value) => Math.abs(value - edge) <= tolerance * 2);
        if (cluster === undefined) clusters.push(edge);
      }
      record.alignment = {
        rowLeftEdges,
        rowLeftAnchorCount: clusters.length,
        rowLeftSpread: round(Math.max(...rowLeftEdges) - Math.min(...rowLeftEdges))
      };
    }

    for (let left = 0; left < measuredItems.length; left += 1) {
      for (let right = left + 1; right < measuredItems.length; right += 1) {
        const area = overlapArea(measuredItems[left].rect, measuredItems[right].rect);
        if (area > 4) {
          record.overlaps.push({
            first: measuredItems[left].label,
            second: measuredItems[right].label,
            area: round(area)
          });
        }
      }
    }

    for (const item of measuredItems) {
      if (
        item.rect.top < container.top - tolerance ||
        item.rect.right > container.right + tolerance ||
        item.rect.bottom > container.bottom + tolerance ||
        item.rect.left < container.left - tolerance
      ) {
        record.clipped.push(item.label);
      }
    }

    const verticalAsymmetry = Math.abs(record.insets.top - record.insets.bottom);
    const bothVerticalEdgesFlush =
      record.insets.top <= tolerance && record.insets.bottom <= tolerance;
    const allowsAsymmetry = region.getAttribute('data-noootwo-symmetric') === 'false';
    if (record.singleRow && !allowsAsymmetry && !bothVerticalEdgesFlush && verticalAsymmetry > tolerance) {
      record.failures.push(
        `asymmetric vertical inset: top=${record.insets.top} bottom=${record.insets.bottom}`
      );
    }
    if (record.overlaps.length) record.failures.push(`sibling overlap: ${record.overlaps.length} pair(s)`);
    if (record.clipped.length) record.failures.push(`content outside container: ${record.clipped.length} item(s)`);

    const outerMinimum = record.outerGaps.length
      ? Math.min(...record.outerGaps.map((entry) => entry.gap))
      : null;
    if (outerMinimum !== null && record.innerGap && outerMinimum <= record.innerGap.median) {
      record.advisories.push(
        `outer gap ${outerMinimum}px is not greater than inner median ${record.innerGap.median}px`
      );
    }
    if (record.alignment?.centerSpread > tolerance * 2) {
      record.advisories.push(
        `single-row centers scatter by ${record.alignment.centerSpread}px`
      );
    }
    if (
      record.alignment &&
      record.alignment.rowLeftAnchorCount > 2 &&
      record.alignment.rowLeftSpread > tolerance * 2
    ) {
      record.advisories.push(
        `row left edges scatter across ${record.alignment.rowLeftAnchorCount} anchors (${record.alignment.rowLeftSpread}px spread)`
      );
    }

    geometry.push(record);
  }

  return {
    url: window.location.href,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    scrollWidth: doc.scrollWidth,
    bodyScrollWidth: body.scrollWidth,
    overflowX,
    offscreenCritical,
    clippedText,
    motion,
    interfaceChecks,
    geometry
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


def parse_region(value: str) -> dict[str, str]:
    name, separator, selector = value.partition("=")
    if not separator:
        selector = value
        name = value
    name = name.strip()
    selector = selector.strip()
    if not selector:
        raise argparse.ArgumentTypeError("Region must be SELECTOR or NAME=SELECTOR")
    return {"name": name or selector, "selector": selector}


def launch_browser(playwright, channel: str | None):
    attempts = [channel] if channel else [None, "chrome", "msedge"]
    errors = []
    for candidate in attempts:
        try:
            options = {} if candidate is None else {"channel": candidate}
            return playwright.chromium.launch(**options)
        except Exception as exc:  # pragma: no cover - depends on local browser install
            label = candidate or "bundled Chromium"
            errors.append(f"{label}: {exc}")
    raise SystemExit(
        "Could not launch a browser for visual gates. Install Playwright Chromium, "
        "pass --browser-channel chrome, or record manual screenshot evidence.\n"
        + "\n".join(errors)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Noootwo responsive visual gates, advisory interface checks, and named layout geometry for a local URL or static HTML file."
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
    parser.add_argument(
        "--region",
        action="append",
        type=parse_region,
        default=[],
        help="Layout region as NAME=SELECTOR. Can be passed multiple times; data-noootwo-region elements are included automatically.",
    )
    parser.add_argument(
        "--geometry-tolerance",
        type=float,
        default=DEFAULT_GEOMETRY_TOLERANCE,
        help="Rendered geometry tolerance in CSS pixels. Defaults to 1.5.",
    )
    parser.add_argument(
        "--require-geometry",
        action="store_true",
        help="Fail when no named or data-noootwo-region regions were measured.",
    )
    parser.add_argument(
        "--browser-channel",
        help="Optional Playwright browser channel, such as chrome or msedge. Defaults to bundled Chromium, then local Chrome/Edge.",
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
        browser = launch_browser(playwright, args.browser_channel)
        page = browser.new_page()
        for label, width, height in viewports:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(target_url, wait_until="networkidle")
            result = page.evaluate(
                CHECK_JS,
                {"regions": args.region, "tolerance": args.geometry_tolerance},
            )
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
            measured_regions = result.get("geometry") or []
            if args.require_geometry and not measured_regions:
                failures.append(
                    f"{label}: no layout regions measured; pass --region NAME=SELECTOR or mark a region with data-noootwo-region"
                )
            for region in measured_regions:
                for finding in region.get("failures") or []:
                    failures.append(f"{label}: geometry {region['name']} ({region['selector']}) {finding}")

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

    interface_labels = {
        "unlabeledControls": "interactive control without an accessible name",
        "imagesMissingAlt": "image without alt text",
        "imagesMissingDimensions": "image without stable dimensions or aspect ratio",
        "transitionAll": "transition: all on an animated element",
        "outlineRemoved": "outline removed with no focus rule",
        "smallTouchTargets": "interactive target smaller than 40px on a narrow viewport",
        "zoomDisabled": "viewport meta disables or limits zoom",
    }
    interface_findings: dict[str, list[dict]] = {}
    for result in results:
        for key, label in interface_labels.items():
            entries = (result.get("interfaceChecks") or {}).get(key) or []
            if not entries:
                continue
            bucket = interface_findings.setdefault(label, [])
            if not any(item["viewport"] == result["label"] for item in bucket):
                bucket.append({"viewport": result["label"], "examples": entries[:3], "count": len(entries)})

    geometry_findings = []
    for result in results:
        for region in result.get("geometry") or []:
            if not region.get("failures") and not region.get("advisories"):
                continue
            geometry_findings.append(
                {
                    "viewport": result["label"],
                    "region": region["name"],
                    "selector": region["selector"],
                    "status": region["status"],
                    "insets": region.get("insets"),
                    "padding": region.get("padding"),
                    "innerGap": region.get("innerGap"),
                    "outerGaps": region.get("outerGaps"),
                    "alignment": region.get("alignment"),
                    "overlaps": region.get("overlaps"),
                    "clipped": region.get("clipped"),
                    "failures": region.get("failures"),
                    "advisories": region.get("advisories"),
                }
            )

    if args.json:
        print(
            json.dumps(
                {
                    "results": results,
                    "failures": failures,
                    "motionFindings": motion_findings,
                    "interfaceFindings": interface_findings,
                    "geometryFindings": geometry_findings,
                },
                indent=2,
            )
        )
    else:
        for result in results:
            print(
                f"{result['label']}: viewport={result['viewport']['width']}x{result['viewport']['height']} "
                f"scrollWidth={result['scrollWidth']} overflowX={result['overflowX']} "
                f"offscreenCritical={len(result['offscreenCritical'])} clippedText={len(result['clippedText'])} "
                f"geometryRegions={len(result.get('geometry') or [])}"
            )
            for region in result.get("geometry") or []:
                if region.get("insets"):
                    inner = region.get("innerGap")
                    inner_text = (
                        f"{inner['min']}/{inner['median']}/{inner['max']}"
                        if inner
                        else "none"
                    )
                    verdict = "FAIL" if region.get("failures") else ("WARN" if region.get("advisories") else "PASS")
                    print(
                        f"  geometry {region['name']} [{verdict}] insets="
                        f"T{region['insets']['top']} R{region['insets']['right']} "
                        f"B{region['insets']['bottom']} L{region['insets']['left']} "
                        f"innerGap(min/median/max)={inner_text} rows={region['rows']}"
                    )
                    for finding in region.get("failures") or []:
                        print(f"    failure: {finding}")
                    for advisory in region.get("advisories") or []:
                        print(f"    advisory: {advisory}")
                else:
                    print(f"  geometry {region['name']} [{region['status']}] {region.get('failures') or 'no items'}")
        if motion_findings:
            print("Motion findings (advisory; confirm against a screenshot or DOM before changing a decision):")
            for label, entries in motion_findings.items():
                viewports = ", ".join(entry["viewport"] for entry in entries)
                examples = entries[0]["examples"]
                sample = examples[0]["tag"] if examples else "-"
                print(f"  - {label} [{viewports}] first seen on <{sample}>")
        else:
            print("Motion findings: none.")
        if interface_findings:
            print("Interface findings (advisory; confirm against source, accessibility tree, or a keyboard pass before changing a decision):")
            for label, entries in interface_findings.items():
                viewports = ", ".join(entry["viewport"] for entry in entries)
                examples = entries[0]["examples"]
                sample = examples[0]["tag"] if examples else "-"
                print(f"  - {label} [{viewports}] first seen on <{sample}>")
        else:
            print("Interface findings: none.")
        if geometry_findings:
            print("Geometry findings:")
            for finding in geometry_findings:
                print(
                    f"  - {finding['region']} [{finding['viewport']}] "
                    f"failures={len(finding['failures'])} advisories={len(finding['advisories'])}"
                )
        else:
            print("Geometry findings: none.")
        if failures:
            print("Visual gate failed:")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print("Visual gate passed.")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
