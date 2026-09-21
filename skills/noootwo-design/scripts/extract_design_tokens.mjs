#!/usr/bin/env node
// Capture real design values from a live page: colour, type, spacing, shape,
// motion, and breakpoints. Zero npm dependencies; drives the Chrome already on
// this machine over the DevTools Protocol using Node's built-in WebSocket.
//
//   node extract_design_tokens.mjs https://example.com --out .noootwo/design-tokens.md
//   node extract_design_tokens.mjs https://example.com --dtcg tokens.json --json raw.json
//
// Requires Node 22+ and a local Chrome. When either is missing the command exits
// non-zero with an explanation, so the caller records a degraded capture instead
// of inventing values.

import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:net';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import process from 'node:process';

const CHROME_CANDIDATES = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome',
  '/usr/bin/google-chrome-stable',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  '/snap/bin/chromium',
].filter(Boolean);

const USAGE = `Usage: node extract_design_tokens.mjs <url> [options]

  --out <file>        write a markdown summary
  --json <file>       write the raw observation JSON
  --dtcg <file>       write W3C DTCG design tokens
  --compare <file>    compare against a baseline written by --json; exits 2 on drift
  --viewport <WxH>    viewport size, default 1440x900
  --wait <ms>         settle time after load, default 4000
  --chrome <path>     explicit Chrome binary
  --timeout <ms>      overall budget, default 45000
  --probe-motion <selector>  sample a moving element and report stillness ratio
  --screenshot <file> write a viewport PNG screenshot
  --quiet             suppress the markdown summary on stdout
`;

function parseArgs(argv) {
  const options = {
    url: null,
    out: null,
    json: null,
    dtcg: null,
    compare: null,
    screenshot: null,
    chrome: null,
    probeMotion: null,
    viewport: { width: 1440, height: 900 },
    wait: 4000,
    timeout: 45000,
    quiet: false,
  };
  const takesValue = new Set(['--out', '--json', '--dtcg', '--compare', '--viewport', '--wait', '--chrome', '--timeout', '--probe-motion', '--screenshot']);

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--help' || arg === '-h') {
      process.stdout.write(USAGE);
      process.exit(0);
    }
    if (arg === '--quiet') {
      options.quiet = true;
      continue;
    }
    if (takesValue.has(arg)) {
      const value = argv[i + 1];
      if (!value) throw new Error(`${arg} needs a value`);
      i += 1;
      if (arg === '--viewport') {
        const [width, height] = value.toLowerCase().split('x').map(Number);
        if (!width || !height) throw new Error('--viewport must look like 1440x900');
        options.viewport = { width, height };
      } else if (arg === '--wait') {
        options.wait = Number(value);
      } else if (arg === '--timeout') {
        options.timeout = Number(value);
      } else if (arg === '--probe-motion') {
        options.probeMotion = value;
      } else {
        options[arg.slice(2)] = value;
      }
      continue;
    }
    if (!options.url) {
      options.url = arg;
      continue;
    }
    throw new Error(`unexpected argument: ${arg}`);
  }

  if (!options.url) throw new Error('a url is required');
  if (!/^[a-z]+:\/\//i.test(options.url)) {
    options.url = `https://${options.url}`;
  }
  return options;
}

function findChrome(explicit) {
  if (explicit) {
    if (!existsSync(explicit)) throw new Error(`Chrome not found at ${explicit}`);
    return explicit;
  }
  return CHROME_CANDIDATES.find((candidate) => existsSync(candidate)) ?? null;
}

function assertRuntime() {
  const major = Number(process.versions.node.split('.')[0]);
  if (major < 22) {
    throw new Error(`Node 22+ is required for the built-in WebSocket; found ${process.versions.node}`);
  }
}

function pickPort() {
  return new Promise((resolve, reject) => {
    const server = createServer();
    server.unref();
    server.on('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });
}

async function waitForDevtools(port, timeoutMs) {
  const deadline = Date.now() + timeoutMs;
  let lastError = null;
  while (Date.now() < deadline) {
    try {
      const response = await fetch(`http://127.0.0.1:${port}/json/version`);
      if (response.ok) return await response.json();
    } catch (error) {
      lastError = error;
    }
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
  throw new Error(`Chrome did not expose DevTools on port ${port}: ${lastError?.message ?? 'timeout'}`);
}

async function openTab(port, url) {
  const response = await fetch(`http://127.0.0.1:${port}/json/new?${encodeURIComponent(url)}`, { method: 'PUT' });
  if (!response.ok) {
    throw new Error(`could not open a tab: ${response.status} ${await response.text()}`);
  }
  return response.json();
}

// Runs inside the page. A real function so it can be stringified without
// escaping a nested template literal.
function collectInPage() {
  const tally = (values) => {
    const counts = new Map();
    for (const value of values) {
      if (!value) continue;
      counts.set(value, (counts.get(value) ?? 0) + 1);
    }
    return [...counts.entries()].sort((a, b) => b[1] - a[1]).map(([value, count]) => ({ value, count }));
  };
  const top = (values, limit) => tally(values).slice(0, limit);

  const isVisible = (el) => {
    const rect = el.getBoundingClientRect();
    if (rect.width < 2 || rect.height < 2) return false;
    const style = getComputedStyle(el);
    return style.visibility !== 'hidden' && style.display !== 'none' && Number(style.opacity) > 0.05;
  };

  const backgroundColors = [];
  const textColors = [];
  const borderColors = [];
  const fontFamilies = [];
  const fontSizes = [];
  const fontWeights = [];
  const lineHeights = [];
  const letterSpacings = [];
  const radii = [];
  const shadows = [];
  const paddings = [];
  const gaps = [];
  const transitions = [];
  const animationNames = [];

  const elements = document.querySelectorAll('*');
  for (const el of elements) {
    let style;
    try {
      style = getComputedStyle(el);
    } catch {
      continue;
    }

    const background = style.backgroundColor;
    if (background && background !== 'rgba(0, 0, 0, 0)' && background !== 'transparent') {
      backgroundColors.push(background);
    }
    const border = style.borderTopWidth !== '0px' ? style.borderTopColor : null;
    if (border && border !== 'rgba(0, 0, 0, 0)') borderColors.push(border);

    const hasText = Array.from(el.childNodes).some((node) => node.nodeType === 3 && node.textContent.trim());
    if (hasText) {
      textColors.push(style.color);
      fontFamilies.push(style.fontFamily);
      fontSizes.push(style.fontSize);
      fontWeights.push(style.fontWeight);
      lineHeights.push(style.lineHeight);
      if (style.letterSpacing && style.letterSpacing !== 'normal') letterSpacings.push(style.letterSpacing);
    }

    if (style.borderTopLeftRadius && style.borderTopLeftRadius !== '0px') radii.push(style.borderTopLeftRadius);
    if (style.boxShadow && style.boxShadow !== 'none') shadows.push(style.boxShadow.split(/,(?![^(]*\))/)[0].trim());
    if (style.padding && style.padding !== '0px') paddings.push(style.padding);
    if (style.gap && style.gap !== 'normal' && style.gap !== '0px') gaps.push(style.gap);

    if (style.transitionDuration && style.transitionDuration !== '0s') {
      const durations = style.transitionDuration.split(',').map((part) => part.trim());
      const timings = style.transitionTimingFunction.split(',').map((part) => part.trim());
      for (let index = 0; index < Math.max(durations.length, timings.length); index += 1) {
        const duration = durations[index % durations.length];
        const timing = timings[index % timings.length];
        if (duration && duration !== '0s') transitions.push(`${duration} ${timing}`);
      }
    }
    if (style.animationName && style.animationName !== 'none') {
      animationNames.push(`${style.animationName} ${style.animationDuration} ${style.animationIterationCount}`);
    }
  }

  const interactiveSelector = 'button, [role="button"], a[href], input, select, textarea, summary';
  const interactive = [];
  for (const el of document.querySelectorAll(interactiveSelector)) {
    if (interactive.length >= 3) break;
    if (!isVisible(el)) continue;
    const index = interactive.length;
    el.setAttribute('data-noootwo-probe', String(index));
    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    interactive.push({
      index,
      tag: el.tagName.toLowerCase(),
      label: (el.getAttribute('aria-label') || el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      center: { x: Math.round(rect.left + rect.width / 2), y: Math.round(rect.top + rect.height / 2) },
      rest: {
        backgroundColor: style.backgroundColor,
        color: style.color,
        transform: style.transform,
        boxShadow: style.boxShadow,
        transitionDuration: style.transitionDuration,
        transitionTimingFunction: style.transitionTimingFunction,
        transitionProperty: style.transitionProperty,
      },
    });
  }

  const breakpoints = new Set();
  for (const sheet of document.styleSheets) {
    let rules;
    try {
      rules = sheet.cssRules;
    } catch {
      continue;
    }
    for (const rule of rules ?? []) {
      if (!rule.media) continue;
      for (const query of rule.media) {
        const match = /(\d+(?:\.\d+)?)px/.exec(query);
        if (match) breakpoints.add(Number(match[1]));
      }
    }
  }

  return {
    url: location.href,
    title: document.title,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    elementCount: elements.length,
    backgroundColors: top(backgroundColors, 10),
    textColors: top(textColors, 8),
    borderColors: top(borderColors, 6),
    fontFamilies: top(fontFamilies, 5),
    fontSizes: top(fontSizes, 12),
    fontWeights: top(fontWeights, 6),
    lineHeights: top(lineHeights, 8),
    letterSpacings: top(letterSpacings, 6),
    radii: top(radii, 8),
    shadows: top(shadows, 5),
    paddings: top(paddings, 10),
    gaps: top(gaps, 6),
    transitions: top(transitions, 8),
    animationNames: top(animationNames, 6),
    breakpoints: [...breakpoints].sort((a, b) => a - b),
    interactive,
  };
}

function probeInPage(index) {
  const el = document.querySelector(`[data-noootwo-probe="${index}"]`);
  if (!el) return null;
  const style = getComputedStyle(el);
  return {
    backgroundColor: style.backgroundColor,
    color: style.color,
    transform: style.transform,
    boxShadow: style.boxShadow,
  };
}

async function probeMotionInPage(selector, durationMs, intervalMs) {
  const el = document.querySelector(selector);
  if (!el) return { found: false, selector };
  const samples = [];
  const startedAt = performance.now();
  const read = () => {
    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    samples.push({
      at: Math.round(performance.now() - startedAt),
      opacity: Number(style.opacity),
      transform: style.transform,
      x: Math.round(rect.left),
      y: Math.round(rect.top),
    });
  };
  read();
  await new Promise((resolve) => {
    const timer = setInterval(() => {
      read();
      if (performance.now() - startedAt >= durationMs) {
        clearInterval(timer);
        resolve();
      }
    }, intervalMs);
  });
  return { found: true, selector, samples };
}

function connectCdp(wsUrl) {
  const socket = new WebSocket(wsUrl);
  const pending = new Map();
  let nextId = 0;

  socket.addEventListener('message', (event) => {
    let payload;
    try {
      payload = JSON.parse(event.data);
    } catch {
      return;
    }
    const resolve = pending.get(payload.id);
    if (!resolve) return;
    pending.delete(payload.id);
    resolve(payload);
  });

  const ready = new Promise((resolve, reject) => {
    socket.addEventListener('open', () => resolve());
    socket.addEventListener('error', () => reject(new Error('DevTools socket failed')));
  });

  const send = (method, params = {}) =>
    new Promise((resolve, reject) => {
      const id = (nextId += 1);
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error(`${method} timed out`));
      }, 20000);
      pending.set(id, (payload) => {
        clearTimeout(timer);
        resolve(payload);
      });
      socket.send(JSON.stringify({ id, method, params }));
    });

  return { ready, send, close: () => socket.close() };
}

function toHex(value) {
  const match = /rgba?\(([^)]+)\)/i.exec(value ?? '');
  if (!match) return value;
  const parts = match[1].split(/[\s,/]+/).filter(Boolean).map(Number);
  const [r, g, b] = parts;
  const alpha = parts.length > 3 ? parts[3] : 1;
  if ([r, g, b].some((part) => Number.isNaN(part))) return value;
  const hex = `#${[r, g, b].map((part) => Math.round(part).toString(16).padStart(2, '0')).join('')}`;
  return alpha >= 1 ? hex : `${hex}${Math.round(alpha * 255).toString(16).padStart(2, '0')}`;
}

function msFromDuration(value) {
  const match = /([\d.]+)\s*(ms|s)\b/.exec(value ?? '');
  if (!match) return null;
  return match[2] === 's' ? Math.round(Number(match[1]) * 1000) : Math.round(Number(match[1]));
}

function buildDtcg(observation) {
  const tokens = {
    $description: `Observed values captured from ${observation.url} on ${observation.captured}.`,
    color: {},
    fontFamily: {},
    fontWeight: {},
    dimension: {},
    duration: {},
    cubicBezier: {},
  };

  observation.backgroundColors.slice(0, 6).forEach((entry, index) => {
    tokens.color[`canvas-${index + 1}`] = { $type: 'color', $value: toHex(entry.value), $extensions: { count: entry.count } };
  });
  observation.textColors.slice(0, 5).forEach((entry, index) => {
    tokens.color[`text-${index + 1}`] = { $type: 'color', $value: toHex(entry.value), $extensions: { count: entry.count } };
  });
  observation.fontFamilies.forEach((entry, index) => {
    tokens.fontFamily[index === 0 ? 'body' : `family-${index + 1}`] = { $type: 'fontFamily', $value: entry.value.split(',').map((part) => part.trim().replace(/^["']|["']$/g, '')) };
  });
  observation.fontWeights.slice(0, 5).forEach((entry) => {
    tokens.fontWeight[`w${entry.value}`] = { $type: 'fontWeight', $value: Number(entry.value) || entry.value };
  });
  observation.fontSizes.slice(0, 8).forEach((entry) => {
    tokens.dimension[`font-${entry.value}`] = { $type: 'dimension', $value: { value: Number.parseFloat(entry.value), unit: 'px' } };
  });
  observation.radii.slice(0, 6).forEach((entry, index) => {
    const numeric = Number.parseFloat(entry.value);
    tokens.dimension[`radius-${index + 1}`] = {
      $type: 'dimension',
      $value: Number.isNaN(numeric) ? entry.value : { value: numeric, unit: 'px' },
    };
  });
  observation.transitions.slice(0, 6).forEach((entry, index) => {
    const ms = msFromDuration(entry.value);
    if (ms !== null) tokens.duration[`motion-${index + 1}`] = { $type: 'duration', $value: { value: ms, unit: 'ms' } };
    const curve = /cubic-bezier\(([^)]+)\)/.exec(entry.value);
    if (curve) {
      const points = curve[1].split(',').map((part) => Number(part.trim()));
      if (points.length === 4 && points.every((point) => !Number.isNaN(point))) {
        tokens.cubicBezier[`easing-${index + 1}`] = { $type: 'cubicBezier', $value: points };
      }
    }
  });

  for (const key of Object.keys(tokens)) {
    if (key.startsWith('$')) continue;
    if (Object.keys(tokens[key]).length === 0) delete tokens[key];
  }
  return tokens;
}

function list(entries, format = (entry) => `${entry.value}  (x${entry.count})`) {
  return entries.length ? entries.map((entry) => `- ${format(entry)}`).join('\n') : '- none observed';
}

function buildMarkdown(observation) {
  const hover = observation.interactive.filter((entry) => entry.hover);
  const lines = [
    `# Extracted Design Values`,
    '',
    `Source: ${observation.url}`,
    `Captured: ${observation.captured} via ${observation.tool}`,
    `Viewport: ${observation.viewport.width}x${observation.viewport.height}; elements scanned: ${observation.elementCount}`,
    '',
    '## Color',
    '',
    'Backgrounds:',
    list(observation.backgroundColors, (entry) => `\`${toHex(entry.value)}\`  ${entry.value}  (x${entry.count})`),
    '',
    'Text:',
    list(observation.textColors, (entry) => `\`${toHex(entry.value)}\`  ${entry.value}  (x${entry.count})`),
    '',
    '## Typography',
    '',
    'Families:',
    list(observation.fontFamilies),
    '',
    'Sizes:',
    list(observation.fontSizes),
    '',
    'Weights:',
    list(observation.fontWeights),
    '',
    'Line heights:',
    list(observation.lineHeights),
    '',
    'Letter spacing:',
    list(observation.letterSpacings),
    '',
    '## Spacing And Shape',
    '',
    'Padding:',
    list(observation.paddings),
    '',
    'Gap:',
    list(observation.gaps),
    '',
    'Radius:',
    list(observation.radii),
    '',
    'Shadow:',
    list(observation.shadows),
    '',
    '## Motion',
    '',
    'Transitions:',
    list(observation.transitions),
    '',
    'Animations:',
    list(observation.animationNames),
    '',
  ];

  if (hover.length) {
    lines.push('Hover deltas:', '');
    for (const entry of hover) {
      const changed = Object.entries(entry.hover)
        .filter(([key, value]) => value && entry.rest[key] !== value)
        .map(([key, value]) => `${key}: ${entry.rest[key]} -> ${value}`);
      lines.push(`- \`${entry.tag}\` "${entry.label}": ${changed.length ? changed.join('; ') : 'no computed change'}`);
    }
    lines.push('');
  }

  lines.push('Breakpoints:', '', list(observation.breakpoints.map((value) => ({ value, count: 0 })), (entry) => `${entry.value}px`), '');
  if (observation.motionProbe) {
    const probe = observation.motionProbe;
    lines.push('## Motion Probe', '');
    if (!probe.found) {
      lines.push(`- selector not found: \`${probe.selector}\``);
    } else {
      lines.push(`- selector: \`${probe.selector}\``);
      lines.push(`- observed duration: ${probe.observedDurationMs ?? 0}ms`);
      lines.push(`- stillness ratio: ${probe.stillnessRatio ?? 1}`);
      lines.push(`- max travel delta from first sample: ${probe.maxDelta ?? 0}px`);
      lines.push('');
      lines.push('A high stillness ratio on a stretch the user expected to move is a timeline problem, not an easing problem.');
    }
    lines.push('');
  }
  lines.push('## Reading This');
  lines.push('');
  lines.push('Observed values are evidence of what a source did, not a target to copy. Map each borrowed value to a role in `.noootwo/design-tokens.md`, then confirm it against a screenshot before the artifact claims `ready`.');
  return lines.join('\n');
}

function writeTarget(path, contents) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, contents, 'utf8');
}

const DRIFT_FIELDS = [
  'backgroundColors',
  'textColors',
  'fontFamilies',
  'fontSizes',
  'fontWeights',
  'letterSpacings',
  'radii',
  'paddings',
  'gaps',
  'transitions',
];

function compareWithBaseline(observation, baselinePath) {
  let baseline;
  try {
    baseline = JSON.parse(readFileSync(baselinePath, 'utf8'));
  } catch (error) {
    throw new Error(`could not read baseline ${baselinePath}: ${error.message}`);
  }

  const changes = [];
  for (const field of DRIFT_FIELDS) {
    const before = new Set((baseline[field] ?? []).map((entry) => entry.value));
    const after = new Set((observation[field] ?? []).map((entry) => entry.value));
    for (const value of before) {
      if (!after.has(value)) changes.push({ field, change: 'removed', value });
    }
    for (const value of after) {
      if (!before.has(value)) changes.push({ field, change: 'added', value });
    }
  }

  if (changes.length === 0) {
    process.stderr.write('No drift against the baseline.\n');
    return 0;
  }

  process.stderr.write(`Design drift against ${baselinePath}:\n`);
  for (const entry of changes.slice(0, 40)) {
    process.stderr.write(`  - ${entry.field} ${entry.change}: ${entry.value}\n`);
  }
  if (changes.length > 40) {
    process.stderr.write(`  ... and ${changes.length - 40} more\n`);
  }
  process.stderr.write('Report the drift; do not repair it as a side effect of an unrelated task.\n');
  return 2;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  assertRuntime();

  const chromePath = findChrome(options.chrome);
  if (!chromePath) {
    throw new Error('No Chrome found. Pass --chrome <path>, or capture a screenshot manually and record the limitation.');
  }

  const port = await pickPort();
  const profileDir = mkdtempSync(join(tmpdir(), 'noootwo-extract-'));
  const chrome = spawn(
    chromePath,
    [
      '--headless=new',
      '--disable-gpu',
      '--hide-scrollbars',
      '--no-first-run',
      '--no-default-browser-check',
      `--remote-debugging-port=${port}`,
      `--user-data-dir=${profileDir}`,
      `--window-size=${options.viewport.width},${options.viewport.height}`,
      'about:blank',
    ],
    { stdio: 'ignore' },
  );

  let client = null;
  try {
    await waitForDevtools(port, Math.min(options.timeout, 15000));
    const tab = await openTab(port, options.url);
    client = connectCdp(tab.webSocketDebuggerUrl);
    await client.ready;
    await client.send('Runtime.enable');
    await new Promise((resolve) => setTimeout(resolve, options.wait));

    const result = await client.send('Runtime.evaluate', {
      expression: `(${collectInPage.toString()})()`,
      returnByValue: true,
      awaitPromise: true,
    });
    if (result.result?.exceptionDetails) {
      throw new Error(`page evaluation failed: ${result.result.exceptionDetails.text}`);
    }
    const observation = result.result.result.value;
    observation.captured = new Date().toISOString().slice(0, 10);
    observation.tool = `extract_design_tokens.mjs (${chromePath.split('/').pop()})`;

    const href = String(observation.url ?? '');
    if (href === 'about:blank' || href.startsWith('chrome-error:') || observation.elementCount < 5) {
      throw new Error(
        `the page did not render (${href || 'no url'}, ${observation.elementCount} elements). ` +
          'Record this source as unreachable rather than treating the capture as evidence.',
      );
    }

    if (options.screenshot) {
      const shot = await client.send('Page.captureScreenshot', { format: 'png' });
      const data = shot.result?.data;
      if (!data) {
        throw new Error('screenshot capture returned no data; record this source as unreachable');
      }
      mkdirSync(dirname(options.screenshot), { recursive: true });
      writeFileSync(options.screenshot, Buffer.from(data, 'base64'));
    }

    for (const entry of observation.interactive) {
      try {
        await client.send('Input.dispatchMouseEvent', {
          type: 'mouseMoved',
          x: entry.center.x,
          y: entry.center.y,
          buttons: 0,
        });
        await new Promise((resolve) => setTimeout(resolve, 350));
        const hover = await client.send('Runtime.evaluate', {
          expression: `(${probeInPage.toString()})(${entry.index})`,
          returnByValue: true,
        });
        entry.hover = hover.result?.result?.value ?? null;
      } catch {
        entry.hover = null;
      }
      delete entry.center;
    }

    if (options.probeMotion) {
      const probeResult = await client.send('Runtime.evaluate', {
        expression: `(${probeMotionInPage.toString()})(${JSON.stringify(options.probeMotion)}, 1200, 120)`,
        returnByValue: true,
        awaitPromise: true,
      });
      const probe = probeResult.result?.result?.value ?? { found: false, selector: options.probeMotion };
      if (probe.samples?.length) {
        const samples = probe.samples;
        let still = 0;
        for (let i = 1; i < samples.length; i += 1) {
          const a = samples[i - 1];
          const b = samples[i];
          const changed = a.x !== b.x || a.y !== b.y || a.opacity !== b.opacity || a.transform !== b.transform;
          if (!changed) still += 1;
        }
        const observedDuration = samples.length > 1 ? samples.at(-1).at - samples[0].at : 0;
        probe.stillnessRatio = samples.length > 1 ? Number((still / (samples.length - 1)).toFixed(2)) : 1;
        probe.observedDurationMs = observedDuration;
        probe.maxDelta = Math.max(0, ...samples.map((entry) => Math.abs(entry.x - samples[0].x) + Math.abs(entry.y - samples[0].y)));
      }
      observation.motionProbe = probe;
    }

    if (options.json) {
      writeTarget(options.json, `${JSON.stringify(observation, null, 2)}\n`);
    }
    if (options.dtcg) {
      writeTarget(options.dtcg, `${JSON.stringify(buildDtcg(observation), null, 2)}\n`);
    }
    const markdown = buildMarkdown(observation);
    if (options.out) {
      writeTarget(options.out, `${markdown}\n`);
    }
    if (!options.quiet) {
      process.stdout.write(`${markdown}\n`);
    }
    process.stderr.write(`Extracted ${observation.elementCount} elements from ${observation.url}\n`);
    if (options.compare) {
      return compareWithBaseline(observation, options.compare);
    }
    return 0;
  } finally {
    client?.close();
    chrome.kill('SIGKILL');
    rmSync(profileDir, { recursive: true, force: true });
  }
}

main()
  .then((code) => process.exit(code))
  .catch((error) => {
    process.stderr.write(`${error.message}\n`);
    process.exit(1);
  });
