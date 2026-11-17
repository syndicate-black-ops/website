A `func_platrot` moves up and down like a [`func_plat`](func_plat.md) and turns around its origin while it moves. You
set the origin with an origin brush.

## Attributes

- **Speed** (`speed`) - Sets how fast the platform moves up and down, in units per second, and the turn takes as
  long as the move. With 0, it is 150
- **Travel altitude** (`height`) - Sets how far the platform travels down from where you build it, in units, and a
  negative value makes it travel up. With 0, it travels its own height minus 8 units
- **Spin amount** (`rotation`) - Sets how many degrees the platform turns while it travels from the bottom to the
  top, and 0 means it doesn't turn
- **Fire On Open Start** (`fireonopening`) - Names the entities to trigger when the platform starts to move up, to its top
- **Fire On Open Start use type** (`fireonopening_triggerstate`) - Sets the [use type](../guide/trigger-modes.md)
  that the targets of **Fire On Open Start** get
- **Fire On Close Start** (`fireonclosing`) - Names the entities to trigger when the platform starts to move down, to its bottom
- **Fire On Close Start use type** (`fireonclosing_triggerstate`) - Sets the use type that the targets of **Fire On
  Close Start** get
- **Fire On Open End** (`fireonopened`) - Names the entities to trigger when the platform reaches its top
- **Fire On Open End use type** (`fireonopened_triggerstate`) - Sets the use type that the targets of **Fire On Open
  End** get
- **Fire On Close End** (`fireonclosed`) - Names the entities to trigger when the platform reaches its bottom
- **Fire On Close End use type** (`fireonclosed_triggerstate`) - Sets the use type that the targets of **Fire On
  Close End** get

## Flags

- **Toggle** (1) - The platform only moves when you trigger it: each trigger sends it to its other end, where it
  stays, and players who step on it don't start it. This flag is set by default
- **X Axis** (64) - The platform turns around the X axis instead of the vertical axis
- **Y Axis** (128) - The platform turns around the Y axis instead of the vertical axis

## See also

- [`func_plat`](func_plat.md) - the same without the turn
- [`func_rotating`](func_rotating.md) - a brush that keeps turning
- [func_platrot on TWHL](https://twhl.info/wiki/page/func_platrot) - the Half-Life entity

## Changes since 1.38

- You can use the new **Fire On** keys and their use types, **Sound radius** and the custom move and stop sounds
