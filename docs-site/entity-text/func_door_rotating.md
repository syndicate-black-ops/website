A `func_door_rotating` opens and closes by turning around its origin, set with an origin brush. It opens when a player
touches it or uses it, or when you trigger it, and it closes again after its delay.

## Attributes

- **Distance** (`distance`) - Sets how far the door turns when it opens, in degrees
    - If you leave this key empty, it is 0 and the door doesn't turn

## Flags

- **Reverse Dir** (2) - The door turns the other way
- **One-way** (16) - The door always opens in the same direction. Without this flag, a door that turns around the
  vertical axis opens away from the player who opens it
- **X Axis** (64) - The door turns around the X axis, the east-west line of the map, instead of the vertical axis
- **Y Axis** (128) - The door turns around the Y axis, the north-south line of the map, instead of the vertical axis

## Notes

- A door with a **Name** only opens when you trigger it, not when a player touches it
- A satchel charge or an armed tripmine that blocks the door goes off, the player who placed it gets the kills, and
  the door moves on
- A door with **Starts Open** opens and closes like any other door, and it starts open
- Each player can turn the object hints off, or keep only the hint on what their use key would use, with the client
  setting [`cl_objecthint`](../../playing/options.md#player-cvars)

## See also

- [`func_door`](func_door.md) - a door that slides, with the keys both doors share
- [`func_rotating`](func_rotating.md) - a brush that keeps turning
- [func_door_rotating on TWHL](https://twhl.info/wiki/page/func_door_rotating) - the Half-Life entity

## Changes since 1.38

- You can use the same new keys as on [`func_door`](func_door.md#changes-since-138)
- A satchel charge or an armed tripmine in the way goes off and the door moves on. In SBO 1.38, the door turned
  back from it every time, so one charge could keep the door from closing for good
- A door with **Starts Open** opens and closes again and again. In SBO 1.38, it closed once and never opened again
