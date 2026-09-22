# Eval Prompt: Long Content And Localization

Use `$noootwo-design` on a dense list or detail surface and provide long German and Chinese labels, long identifiers, large formatted numbers, and a right-to-left locale requirement.

Expected behavior:

- Preserve hierarchy under long labels instead of shrinking text into an unreadable size.
- Use locale-aware date, number, and currency formatting rather than hardcoded English formats.
- Define truncation, wrapping, full-value access, empty, partial, and overflow behaviour for paths, identifiers, and metrics.
- Check text scale, safe areas, and RTL mirroring on the target platform, including Flutter and native.

Failure signals:

- Assumes short English strings and clips the task or primary action.
- Hides the full identifier with no copy, tooltip, detail view, or accessible value.
- Hardcodes date, currency, or number formats.
- Treats RTL as a CSS-only reversal without platform review.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
