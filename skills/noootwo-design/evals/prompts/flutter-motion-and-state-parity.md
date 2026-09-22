# Eval Prompt: Flutter Motion And State Parity

Use `$noootwo-design` on a Flutter screen that currently uses a default `Scaffold + AppBar + Card + ListView`, stock transitions, icon-only controls without semantics, and no reduced-motion or text-scale check.

Expected behavior:

- Build a component state matrix for the important widgets: default, hover where supported, focus, pressed, selected, disabled, loading, empty, error, and success.
- Apply the motion ladder: built-in implicit or explicit animation and `Hero` first, the Flutter `animations` package where Material motion fits, and `flutter_animate` only as an optional micro-effect layer.
- Use `Semantics`, stable touch targets, `MediaQuery.textScaler`, and `MediaQuery.disableAnimations` where relevant.
- Keep the visual direction in Flutter-native primitives rather than translating a web card layout directly.

Failure signals:

- Keeps the default scaffold and adds a motion package to make it feel designed.
- Uses web state pseudo-classes or CSS motion vocabulary in Flutter.
- Adds animation without a reduced-motion or text-scale check.
- Leaves icon-only controls without an accessible label.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
