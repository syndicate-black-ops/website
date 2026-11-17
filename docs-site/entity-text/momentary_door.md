A `momentary_door` is a brush door that follows a [`momentary_rot_button`](momentary_rot_button.md), so as a player
turns the wheel, the door moves along with it. The wheel sends the door its position as a number from 0 for closed up
to 1 for open.

## Flags

- **Starts Open** (1) - The door starts at its open end, so turning its wheel toward its end closes it

## Notes

- The door only reacts to the use type Set, which a `momentary_rot_button` sends with its position, and it ignores
  On, Off and Toggle
- The door moves to each new position in a tenth of a second, so it follows the wheel as fast as the wheel turns
- The **Fire On** targets get the player who turned the wheel last as their activator
- A satchel charge or an armed trip mine that blocks the door goes off, and the player who placed it gets the kills
- The move sound stops when the door reaches its position
- A [`multi_watcher`](multi_watcher.md) sees the door as on while it stands open, even a little, and as off while it
  is closed. [Entity states](../guide/masters-and-states.md#entity-states) lists the states

## See also

- [`momentary_rot_button`](momentary_rot_button.md) - the wheel that moves the door
- [`func_door`](func_door.md) - a door that opens and closes by itself
- [momentary_door on TWHL](https://twhl.info/wiki/page/momentary_door) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Custom move sound**, **Custom stop sound**, **Sound radius**, the **Fire On** targets and
  their use types, **Object Hint Template** and **Hint Distance**
- Fixed `momentary_door` never playing its Stop Sound. The game read the key but never used it. This was a bug in SBO
  1.38
- Fixed a satchel charge or a trip mine under a door jamming the door. The door now sets it off. This was a bug in SBO
  1.38
- Fixed `momentary_door` playing its move sound on after it stopped. It never stopped the sound when it arrived. This
  was a bug in SBO 1.38
