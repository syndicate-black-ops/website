---
description: "A func_door slides open and closed. It opens when a player touches or uses it, or when you trigger it, and closes again after its delay."
---
A `func_door` slides open and closed. It opens in the direction of its **Pitch Yaw Roll** when a player touches it or
uses it, or when you trigger it, and it closes again after its delay.

Doors with the same **Name** open and close together, and when one of them is blocked, they all go back.

## Notes

- A door with a **Name** only opens when you trigger it, not when a player touches it
- If something blocks the door, the door deals its damage and goes back the way it came. If its **Delay before
  close** is -1, it keeps pushing instead
- A satchel charge or an armed tripmine that blocks the door goes off, the player who placed it gets the kills, and
  the door moves on
- Each player can turn the object hints off, or keep only the hint on what their use key would use, with the client
  setting [`cl_objecthint`](../../playing/options.md#player-cvars)

## See also

- [`func_door_rotating`](func_door_rotating.md) - a door that turns
- [`momentary_door`](momentary_door.md) - a door that follows a [`momentary_rot_button`](momentary_rot_button.md)
- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [func_door on TWHL](https://twhl.info/wiki/page/func_door) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Obey Trigger Mode**, **Object Hint Template** and **Hint Distance**, the **Fire On**
  keys and their use types, **Return speed**, **Player use policy**, **If locked, play locked sound on use**, the
  custom move and stop sounds, **Stop sound on the way back**, **Sound radius**, **Collision with corpses**,
  **Instantly gib corpses**, **Continue moving if blocker is crushed** and the custom locked and unlocked sounds and
  sentences
- A satchel charge or an armed tripmine in the way goes off and the door moves on. In SBO 1.38, the door turned
  back from it every time, so one charge could keep the door from closing for good
