A `monster_tripmine` is an armed trip mine fixed to a wall. A beam goes out from it the way it faces, and the mine
explodes for 280 damage when something crosses the beam, so you place it on a wall facing away from the wall.

## Attributes

- **Classification** (`classify`) - Sets the side that a [`trigger_sensor`](trigger_sensor.md) with a relationship
  filter sees the mine on, and whose friendly fire rule the blast follows, so Feds and turrets that ignore friendly
  damage aren't hurt by a mine on their side. The classes are on the [Monster classes](../guide/monster-classes.md) page
    - If you leave this key empty or set 0, the mine is on no side

## Flags

- **Quick power-up** (1) - The mine arms 1 second after the map loads, instead of 2.5 seconds

## Notes

- An armed mine that a door runs into explodes at once
- A mine that a **KillTarget** removes takes its beam with it

## See also

- [`monster_satchel`](monster_satchel.md) - a live satchel charge
- [monster_tripmine on TWHL](https://twhl.info/wiki/page/monster_tripmine) - the Half-Life entity

## Changes since 1.38

- Fixed a satchel charge or a trip mine under a door jamming the door. The door now sets it off. This was a bug in SBO
  1.38
- Fixed a trip mine that a Kill target removes leaving its beam behind. The game removed the mine but not its beam.
  This was a bug in SBO 1.38
- You can use the new keys **Classification** and **Unkillable**
