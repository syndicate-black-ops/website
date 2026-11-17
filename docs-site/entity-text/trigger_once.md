A `trigger_once` is a brush trigger that fires its target the first time a player touches it, and then removes itself.
The flags let monsters and other entities fire it too, and its **Message** only shows when a player fires it.

## Attributes

- **Sound to play** (`noise`) - Sets a sound that plays at the trigger when it fires

## Flags

- **Everything else** (8) - Every other entity fires it too: anything that isn't a player, a monster, a
  [`func_pushable`](func_pushable.md) or a trigger, for example a grenade or the touch helper of a
  [`func_vehicle`](func_vehicle.md)

## See also

- [`trigger_multiple`](trigger_multiple.md) - fires again and again
- [trigger_once on TWHL](https://twhl.info/wiki/page/trigger_once) - the Half-Life entity

## Changes since 1.38

- You can use the new flag **Everything else** (8)
- Fixed `trigger_once` and `trigger_multiple` never playing their Sound to play. The game never loaded the sound. This
  was a bug in SBO 1.38
