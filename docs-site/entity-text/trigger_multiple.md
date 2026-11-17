A `trigger_multiple` is a brush trigger that fires its target each time a player touches it, and then waits before it
can fire again. The flags let monsters and other entities fire it too, and its **Message** only shows when a player
fires it.

## Attributes

- **Delay before reset** (`wait`) - Sets how many seconds pass after it fires before it can fire again. A negative
  value makes it fire once and then remove itself
    - If you leave this key empty or set 0, it is 0.2
- **Sound to play** (`noise`) - Sets a sound that plays at the trigger each time it fires

## Flags

- **Everything else** (8) - Every other entity fires it too: anything that isn't a player, a monster, a
  [`func_pushable`](func_pushable.md) or a trigger, for example a grenade or the touch helper of a
  [`func_vehicle`](func_vehicle.md)

## See also

- [`trigger_once`](trigger_once.md) - fires once and removes itself
- [`trigger_inout`](trigger_inout.md) - fires when something enters and when it leaves
- [trigger_multiple on TWHL](https://twhl.info/wiki/page/trigger_multiple) - the Half-Life entity

## Changes since 1.38

- You can use the new flag **Everything else** (8)
- Fixed `trigger_once` and `trigger_multiple` never playing their Sound to play. The game never loaded the sound. This
  was a bug in SBO 1.38
