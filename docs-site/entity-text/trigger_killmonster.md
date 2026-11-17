---
description: "A trigger_killmonster kills monsters when you trigger it, as a weapon does, and their monstermaker counts them as dead."
---
A `trigger_killmonster` kills monsters when you trigger it, as a weapon does, so the monsters play their death or turn
into gibs, and their [`monstermaker`](monstermaker.md) counts them as dead. A **KillTarget** only makes an entity
disappear.

## Attributes

- **Monster's name** (`target`) - Kills living monsters with this name
- **Monster's class name** (`message`) - Kills living monsters of this class, such as `monster_zombie`
- **Monster's squad name** (`netname`) - Kills living monsters with this squad name

## Flags

- **Remove on fire** (1) - It works once and then removes itself
- **Always gib** (16) - The monsters turn into gibs instead of dying with a body

## Notes

- With two or three filters set, a monster has to match all of them
- It skips monsters that are dying and dead bodies
- The class name `player` kills every alive player
- The kill always works, because the random weak hits of the damage rules don't apply to it

## See also

- [`trigger_hurt_remote`](trigger_hurt_remote.md) - hurts entities by name or class
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs

## Changes since 1.38

- `trigger_killmonster` is new
