A `path_track` marks a stop on the path of a [`func_tracktrain`](func_tracktrain.md), and these paths can branch.

## Attributes

- **Next stop target** (`target`) - Names the next `path_track` on the path
- **Fire On Pass** (`message`) - The `path_track` fires this target when a train passes it
- **Branch Path** (`altpath`) - Names another `path_track` that the path can branch to, and triggering this
  `path_track` switches between **Next stop target** and the branch
- **Fire on dead end** (`netname`) - The `path_track` fires this target when a train stops here because the path
  ends here or the next `path_track` is disabled
- **New Train Speed** (`speed`) - Sets the speed, in units per second, that a train takes when it reaches this point.
  A `func_tracktrain` takes this speed only if players can't drive it (the **No User Control** flag), but a
  [`func_train`](func_train.md) always takes it
    - If you leave this key empty or set 0, the speed doesn't change

## Flags

- **Disabled** (1) - The path is blocked here, so trains stop at this point, and triggering a `path_track` without a
  **Branch Path** switches this on and off
- **Fire once** (2) - **Fire On Pass** only fires the first time a train passes
- **Branch Reverse** (4) - A train uses the **Branch Path** when it travels backward along the path, instead of
  forward
- **Disable train controls** (8) - Once a train passes this point, players can't drive it

## See also

- [`path_corner`](path_corner.md) - the path of a `func_train`
- [`func_trackchange`](func_trackchange.md) - moves a train between two tracks
- [path_track on TWHL](https://twhl.info/wiki/page/path_track) - the Half-Life entity
