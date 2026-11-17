A `func_water` is water, slime or lava that moves like a [`func_door`](func_door.md) when you trigger it, so the level
of a liquid can rise or fall. It has the keys of a `func_door`.

## Attributes

- **Contents** (`skin`) - Picks what the brush is filled with, and players swim in all three, while slime and lava
  also hurt players all the time they are in it, lava more
    - Water (-3)
    - Slime (-4)
    - Lava (-5)
    - If you leave this key empty, the brush isn't a liquid, but a solid brush that moves like a door
- **Wave Height** (`WaveHeight`) - Sets how high the waves on the surface are drawn
    - If you leave this key empty, it is 0 and the surface is flat
- **Player use policy** (`directuse`) - With **Use Only**, sets how a player must look at the liquid to use it. A
  liquid isn't solid, so a look never meets it, and with "Direct only", nobody can use it
    - Default (0) - As for any object
    - Direct only (1) - The player must look straight at it
    - Not through walls (2) - The player can't use it through a wall

## Flags

- **Starts Open** (1) - The liquid starts in its moved position, and triggering it moves it back
- **Use Only** (256) - A player who touches the liquid doesn't move it, only a trigger or a player's use key does

## Notes

- A satchel charge or an armed tripmine that blocks the liquid goes off, the player who placed it gets the kills, and
  the liquid moves on

## See also

- [`func_door`](func_door.md) - a door that slides, with the keys both share
- [func_water on TWHL](https://twhl.info/wiki/page/func_water) - the Half-Life entity

## Changes since 1.38

- You can use the same new keys as on [`func_door`](func_door.md#changes-since-138)
- A satchel charge or an armed tripmine in the way goes off and the liquid moves on. In SBO 1.38, the liquid turned
  back from it every time
