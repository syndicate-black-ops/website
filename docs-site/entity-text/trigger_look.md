A `trigger_look` is a brush trigger that fires its target when a player standing in it keeps looking at an entity for
some time.

## Attributes

- **Look target** (`netname`) - Names the entity that the player has to look at, and the player has to look at its
  origin
- **Look time** (`look_time`) - Sets how many seconds the player has to keep looking, and looking away starts it over
- **Field of view** (`field_of_view`) - Sets how exactly the player has to look. 1.0 is dead center, 0.7 is about 45
  degrees, 0 is 90 degrees and -1 is any direction
- **Target** (`target`) - Fires this target with Toggle, with the looking player as the activator
- **Kill target** (`killtarget`) - Removes the entities with this name when the player has looked long enough
- **Delay before trigger** (`delay`) - Sets how many seconds the entity waits after the look is complete. Then it
  fires the **Target** and removes the **Kill target**

## Flags

- **Remove on fire** (1) - It fires once, and then the brush is removed. Without this flag, it fires again after each
  **Look time** while the player keeps looking

## Notes

- Each player counts their own look time, which starts again when they leave the brush or look away
- Only alive players count
- Nothing fires while the **Master** is off for that player
- The brush isn't drawn

## See also

- [`trigger_multiple`](trigger_multiple.md) - fires while a player touches it

## Changes since 1.38

- `trigger_look` is new
