# Data UI Rubric

Use this for dashboards, analytics, monitoring, finance, ops workbenches, admin panels, and any UI where charts or metrics carry product meaning.

## Core Rule

Charts and metrics cannot be decorative. They must help the user decide, diagnose, compare, prioritize, or act.

## Required Checks

- Axes, units, scale, range, and time window are clear or intentionally omitted with a stated reason.
- Data state is visible: live, stale, simulated, empty, loading, partial, error, or degraded.
- Priority is clear: the user can tell which exception, metric, or segment matters first.
- Action path is visible: inspect, filter, acknowledge, drill down, compare, export, resolve, or hand off.
- Anomaly and threshold logic is named when shown.
- Color carries meaning beyond decoration and does not rely on hue alone.
- Dense layouts still preserve scanning rhythm and focus order.

## Failure Flags

- Bars, lines, maps, or gauges with no labels, units, or decision role.
- Hero marketing headline dominating an operational surface.
- Metrics that look precise but lack source, state, or time window.
- Empty dashboard chrome replacing a real workflow.
- Decorative data shapes used to make the UI feel advanced.

## Review Decision

- If the interface is visually strong but the data is decorative, mark `refine`.
- If the surface claims to be a workbench but lacks a credible action path, mark `pivot`.
- If no artifact proves data hierarchy and interaction states, mark `needs artifact`.
