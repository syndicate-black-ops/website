---
description: "A trigger_inout is a brush trigger that fires one target when an entity enters it and another when the entity leaves it."
---
A `trigger_inout` is a brush trigger that fires one target when an entity enters it and another when the entity leaves
it, with that entity as the activator.

## Attributes

- **Fire on entering** (`target`) - This target gets Toggle for each entity that enters
- **Fire on leaving** (`m_iszAltTarget`) - This target gets Toggle for each entity that leaves
- **Fire on/off** (`m_iszBothTarget`) - This target gets On for each entity that enters and Off for each entity that
  leaves
- **Triggered only by entity** (`netname`) - If you set it, only an entity with this class name or this name counts,
  and the trigger ignores its flags

## Flags

- **Monsters** (1) - Living monsters count
- **No Clients** (2) - Players don't count
- **Pushables** (4) - [`func_pushable`](func_pushable.md) entities count
- **Everything else** (8) - All other entities count, for example the touch helper of a
  [`func_vehicle`](func_vehicle.md)

## Notes

- Every 0.1 seconds, it checks against the trigger's box which entities have left
- Players only count while they are alive, so a player inside who dies, becomes a spectator or leaves the game counts
  as having left
- It checks the master for each entity, with that entity as the activator. While the master is off, entering and
  leaving fire nothing
- It keeps track of up to 64 entities inside at once, and it ignores any more

## See also

- [`trigger_multiple`](trigger_multiple.md) - fires while something touches it
- [Masters and states](../guide/masters-and-states.md) - how `trigger_inout` can drive a state

## Changes since 1.38

- `trigger_inout` is new
