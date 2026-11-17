---
description: "A func_plat moves up and down, like a lift. A player who steps on it sends it up, or you trigger it."
---
A `func_plat` moves up and down, like a lift. Without a **Name**, it waits at the bottom, and a player who steps on it
sends it up, after which it comes back down. With a **Name**, it starts at the top, and the first trigger sends it
down, after which it works like a platform without a name.

## Attributes

- **Name** (`targetname`) - The first trigger sends the platform down, and later triggers do nothing. With the flag
  **Toggle**, each trigger sends it to its other end. See [Common keys](common-keys.md#targetname)
- **Travel altitude** (`height`) - Sets how far the platform travels down from where you build it, in units, and a
  negative value makes it travel up. With 0, it travels its own height minus 8 units
- **Speed** (`speed`) - Sets how fast the platform moves, in units per second, and 0 means 150
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
  stays, and players who step on it don't start it

## Notes

- At its top, a platform without **Toggle** goes back down 1 second after the last player steps off it, or after
  3 seconds if no player is on it
- If something blocks the platform, the platform deals 1 damage to it and goes back

## See also

- [`func_platrot`](func_platrot.md) - a platform that also turns while it moves
- [`func_train`](func_train.md) - a brush that moves along a path
- [`func_door`](func_door.md) - a door that slides
- [func_plat on TWHL](https://twhl.info/wiki/page/func_plat) - the Half-Life entity

## Changes since 1.38

- You can use the new **Fire On** keys and their use types, **Sound radius** and the custom move and stop sounds
