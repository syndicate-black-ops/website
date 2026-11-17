A `trigger_jump` is a jump pad: a brush trigger that launches what touches it on an arc to a target point. By default
it only launches players. See [Teleports and jump pads](../features/teleports-and-jump-pads.md) for how to build one.

## Attributes

- **Jump target** (`target`) - Sets where the entity lands, as the name of an entity such as an
  [`info_target`](info_target.md) or as `x y z` coordinates. It is a [locus position](../guide/locus.md), so a
  [`calc_position`](calc_position.md) or `!activator` works too. Without a target, the trigger launches nothing
- **Height** (`height`) - Sets how high the top of the arc is above the entity's origin
    - If you leave this key empty or set 0, the top of the arc is the higher of the target and the entity, plus the
      entity's height, plus 16 units
- **Trigger on jump** (`trigger_on_jump`) - Fires this target at every launch, with the launched entity as the
  activator
- **Triggered only by entity** (`netname`) - If you set it, only an entity with this class name or this name is
  launched, and the trigger ignores its flags

## Flags

- **Monsters** (1) - Living monsters are launched
- **No Clients** (2) - Players aren't launched
- **Pushables** (4) - [`func_pushable`](func_pushable.md) entities are launched
- **Everything else** (8) - All other entities are launched, for example the touch helper of a
  [`func_vehicle`](func_vehicle.md)

## Notes

- The arc follows the server's gravity, times the entity's own gravity if it has one. Without gravity, nothing is
  launched
- The trigger launches each entity by itself, and the same entity at most once every 0.2 seconds. A launch whose climb
  would last less than 0.1 seconds doesn't happen
- It only launches alive players and living monsters
- The server works out the launch, so the player's game gets the new speed with the next server update. The trigger
  plays no sound
- It has no on and off state, so triggering it by name does nothing. While its master is off, it launches nothing

## See also

- [`trigger_safe_fall`](trigger_safe_fall.md) - cancels fall damage at the landing
- [`trigger_push`](trigger_push.md) - pushes in a direction
- [Teleports and jump pads](../features/teleports-and-jump-pads.md) - how jump pads work

## Changes since 1.38

- `trigger_jump` is new
