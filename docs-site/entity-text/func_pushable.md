A `func_pushable` is a brush that players push by walking into it or by holding their use key on it. With the flag
**Breakable**, it also breaks like a [`func_breakable`](func_breakable.md), and only then do the breakable keys work.

## Attributes

- **Name** (`targetname`) - Triggering the entity breaks it if it has the flag **Breakable**, and with **Toggleable
  push**, triggering it switches it between pushable and fixed in place. See
  [Common keys](common-keys.md#targetname)
- **Friction** (`friction`) - Sets how hard it is to push, from 0 up to 399, because players can push it at up to
  400 minus this value, in units per second
    - If you leave this key empty, it is 0 and players push it at the full 400 units per second
- **Buoyancy** (`buoyancy`) - Sets how strongly it floats in water, and the value is multiplied by the size of its
  base
    - If you leave this key empty, it is 0 and it sinks
- **Toggleable push** (`toggleable_push`) - Sets whether a trigger can fix it in place
    - No (0) - Players can always push it
    - Yes (1) - Triggering it switches it between pushable and fixed in place, where it is solid like a wall, and a
      trigger then never breaks it

## Flags

- **Invert Hit Vector** (16) - With **Trigger when hit**, the entity reverses the horizontal part of the hit
  direction that it passes on, so the direction points back toward the shooter
- **Breakable** (128) - It can be broken like a `func_breakable`, with the **Strength**, the **Material type** and
  the other breakable keys

## Notes

- If a player started the chain of triggers, a trigger doesn't break the pushable, because the pushable treats the
  trigger as that player pulling it. A trigger whose [activator](../guide/entity-triggering.md#target-selectors)
  isn't a player breaks it

- A pushable can't move with a parent, because it moves on its own, but it rides along on a moving object it stands
  on. See [Moving objects](../features/moving-objects.md#standing-on-moving-objects)

## See also

- [`func_breakable`](func_breakable.md) - a brush that breaks
- [func_pushable on TWHL](https://twhl.info/wiki/page/func_pushable) - the Half-Life entity

## Changes since 1.38

- You can use the new key **Toggleable push**, the new flag **Invert Hit Vector** and the new breakable keys of
  [`func_breakable`](func_breakable.md#changes-since-138)
- With **Gibs Direction** "Relative to Attack", the gibs of a broken pushable fly away from the attacker. In SBO
  1.38, they flew toward the attacker
- New in SBO 2.1.0: **Spawn On Break** also takes a class name
