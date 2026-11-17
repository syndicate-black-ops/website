A `func_guntarget` moves along a path of [`path_corner`](path_corner.md) entities, and players can shoot it down like
a target on a shooting range. When it has taken its **Damage to Take**, it stops and fires its target.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts it along its path from the next `path_corner`, with its
  full **Damage to Take** again. Once it is on its way, even while it waits at a `path_corner`, triggering it again
  or with the [use type](../guide/trigger-modes.md) Off stops it, and the use type On does nothing. See
  [Common keys](common-keys.md#targetname)
- **Speed** (`speed`) - Sets how fast the target moves from one `path_corner` to the next, in units per second, and
  0 means 100
- **First stop target** (`target`) - Names the first `path_corner`, where the target stands when the map starts
- **Fire when shot down** (`message`) - Names the entities to trigger when the `func_guntarget` has taken all its
  **Damage to Take** and stops
- **Damage to Take** (`health`) - Sets how much damage the target takes before it stops, and with 0, players can't
  shoot it down

## Flags

- **Start On** (1) - The target starts along its path 0.3 seconds after the map starts, without a trigger

## Notes

- The target can only be hurt while it is on its way, so a target that has stopped takes no more damage
- It uses the wait and the fire target of each `path_corner`, and the center of the brush moves to each one

## See also

- [`path_corner`](path_corner.md) - the stops of the path
- [`func_train`](func_train.md) - a brush that moves along a path
- [func_guntarget on TWHL](https://twhl.info/wiki/page/func_guntarget) - the Half-Life entity

## Changes since 1.38

- A trigger stops a moving gun target. In SBO 1.38, as in Half-Life, the gun target never noted that it had
  started, so a second trigger started it again from its next `path_corner`, and Off did nothing
