# Ponytail Source

This directory records the external source used to inform Noootwo Review's lean-code-review reference.

## Source

- Project: Ponytail
- Repository: `https://github.com/DietrichGebert/ponytail`
- License: MIT
- Checked: 2026-07-06
- Commit checked: `40e50d9e03242aa5dd53ac771950f9127362b25f`
- Local user-provided PDF: `/Users/notwo/Downloads/为什么你的AI代码越来越冗余？答案在这套七层流程里.pdf`

## Adopted

- Seven-rung minimal-code review ladder: current need, existing project code, standard library, native platform capability, installed dependency, shrink fragmented code, minimum new code.
- Lean review tags inspired by Ponytail review/audit commands.
- Safety boundary: do not remove validation, error handling, security, accessibility, explicitly requested behavior, or the smallest useful check.
- Honesty boundary: benchmark savings are external measurements, not automatic current-repo savings.

## Not Vendored

The full Ponytail repository is intentionally not copied into this skill. Excluded material includes benchmarks, runtime hooks, plugin adapters, assets, MCP package, cross-editor configuration, scripts, and command implementations.

Reason: Noootwo Vibe keeps skill bodies and references lean. Vendoring the full repository would increase context and maintenance cost without improving the Noootwo Review trigger path.

## Notes

Noootwo Review is not a Ponytail clone. It remains a code-health, maintainability, and project-health review skill with an added lean-review lens.
