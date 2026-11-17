A `trigger_teleport` is a brush trigger that moves what touches it to its target, which is usually an
[`info_teleport_destination`](info_teleport_destination.md). With a landmark, the teleport can be seamless: players go
from one room to its copy in a different place and don't see the change. See [Teleports and jump
pads](../features/teleports-and-jump-pads.md) for how to build one.

## Attributes

- **Target** (`target`) - Names where it sends the entities that touch it
    - If you leave this key empty, it does nothing
- **Landmark** (`message`) - Names a point entity at the trigger, such as an [`info_landmark`](info_landmark.md) or an
  [`info_target`](info_target.md), for a seamless teleport. The entity arrives at the same place relative to the
  target as it was relative to the landmark, and it keeps its speed. If the target faces a different way from the
  landmark, the entity turns by the same amount, so it keeps facing the same way relative to the target
- **Start Inactive** (`teleport_start_inactive`) - With Yes, the trigger does nothing until you turn it on, so it
  needs a **Name**. After that, Off turns it off again

## Flags

- **Monsters** (1) - Monsters are teleported too
- **No Clients** (2) - Players aren't teleported
- **Random destination** (64) - The destination is one of the entities named in **Target**, each as likely as the
  others
- **Relative** (128) - Without a landmark, the entity keeps its distance from the trigger's origin, so the trigger
  needs an origin brush
- **Keep angles** (256) - Without a landmark, the entity keeps the direction it faces
- **Keep velocity** (512) - Without a landmark, the entity keeps its speed
- **Grenades, items** (1024) - With a landmark, grenades, rockets, dropped items and gibs are teleported too

## Notes

- Without a landmark, the trigger only teleports players and monsters. With a landmark, it never teleports dead
  players or spectators
- A landmark teleport keeps a player on the ground, and the other players don't see them slide from the old place to
  the new one
- If the landmark doesn't exist, the trigger stops working, and with `developer 1` set in the console, the console
  says so
- An `info_teleport_destination` with **Trigger on arrival** fires its target at each arrival

## See also

- [`info_teleport_destination`](info_teleport_destination.md) - a destination
- [`info_landmark`](info_landmark.md) - a landmark
- [Teleports and jump pads](../features/teleports-and-jump-pads.md) - how seamless teleports work
- [trigger_teleport on TWHL](https://twhl.info/wiki/page/trigger_teleport) - the Half-Life entity

## Changes since 1.38

- Fixed a `trigger_teleport` without a Target sending players to a random spot. An empty Target matched any entity
  without a name
- `trigger_teleport` has the new key **Landmark** and the new flags **Random destination**, **Relative**, **Keep
  angles**, **Keep velocity** and **Grenades, items**
