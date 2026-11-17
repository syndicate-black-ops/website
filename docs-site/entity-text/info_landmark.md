---
description: "An info_landmark is a reference point: a trigger_teleport with a landmark keeps the position and speed of the toucher relative to it."
---
An `info_landmark` is a reference point for a [`trigger_teleport`](trigger_teleport.md). A teleport with a landmark
keeps the position and the speed of the toucher relative to it, so the toucher arrives at the same spot relative to
the destination.

## Attributes

- **Name** (`targetname`) - Sets the name you put in the **Landmark** key of a `trigger_teleport`. See
  [Common keys](common-keys.md#targetname)

## See also

- [`trigger_teleport`](trigger_teleport.md) - moves what touches it to a destination
- [Teleports and jump pads](../features/teleports-and-jump-pads.md) - teleports without a jump in the view
- [info_landmark on TWHL](https://twhl.info/wiki/page/info_landmark) - the Half-Life entity
