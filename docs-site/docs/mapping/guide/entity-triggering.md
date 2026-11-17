---
description: "When an entity fires, it triggers the entities named in its Target and removes the entities named in its KillTarget, and besides a plain name, these keys accept wildcards, target selectors and aliases."
---

# Entity triggering [[ported:hlunified]]

When an entity fires, it triggers the entities named in its **Target** and removes the entities named in its
**KillTarget**, and besides a plain name, these keys accept wildcards, target selectors and aliases. With them, one
button can trigger a whole group of entities, the player who pressed it, or a different door each time:

- a wildcard matches every name that starts the same way
- a target selector stands for an entity in the chain of triggers that is firing
- an alias stands for the entity the alias points to at that moment

These forms work in the keys every entity already has, so you don't need any new keys for them.

## Wildcards

If a target ends in `*`, it matches every entity whose name starts with the part before the `*`, so a **Target** of
`room1_*` triggers both an entity named `room1_door1` and one named `room1_sprite1`, and a **KillTarget** of
`room1_*` removes both of them.

The `*` only works at the end, so `room1_*` matches, but `room*_door` doesn't. You give the entities ordinary
names, and only the target ends in `*`. The wildcard works in every key the game uses to find an entity by its name:
in **Target** and **KillTarget**, in the targets of a [`multi_manager`](../entities/multi_manager.md), in the "Fire
On" keys, in path corners, in the destinations of a [`trigger_changevalue`](../entities/trigger_changevalue.md), in
[locus](locus.md) keys and in all the others. Some keys take a class name as well as a name, such as the **Target
Monster** of a [`scripted_sequence`](../entities/scripted_sequence.md), and these keys match class names the same
way, as in `monster_*`.

A wildcard never matches the entity that is firing, even when its own name starts the same way. A
[`trigger_relay`](../entities/trigger_relay.md) named `room1_relay` with the target `room1_*` triggers the other
`room1_` entities once and skips itself, and its **KillTarget** of `room1_*` doesn't remove the relay itself. With
`developer 2` set in the console, the console shows each entity it skips.

## Target selectors

Instead of a name, you can write a target selector in **Target** and **KillTarget**:

| Selector | The entity it stands for |
|---|---|
| `!activator` | The entity that started the chain of triggers, which is usually the player who pressed the button or touched the trigger |
| `!caller` | The entity that fired this one. In an entity's own **Target** and **KillTarget**, that is the entity itself |

These rules apply to the selectors:

- A **KillTarget** never removes a player, so a **KillTarget** of `!activator` removes nothing when a player started
  the chain, but it removes a monster that did
- A **KillTarget** of `!caller` removes the entity itself
- If a selector in an entity's own **Target** stands for that same entity, the entity doesn't trigger, because it
  would trigger itself without end. This happens with `!caller`, and with `!activator` on a `trigger_relay` that
  passes itself on as the activator
- A `trigger_relay` passes itself on as the activator, as it does in Half-Life, but with the flag **Forward
  activator** it passes on the activator it got, such as the player, and with **Pass caller as activator** it passes
  on the entity that fired it
- If the entity has a **Delay**, the delayed trigger keeps the activator, and `!caller` is then the delayed trigger
  itself, not the entity
- Any other name that starts with `!` finds nothing, and with `developer 2` set in the console, the console shows a
  message
- Entities that find their target with the [locus](locus.md) rules, such as
  [`env_explosion`](../entities/env_explosion.md), [`trigger_hurt_remote`](../entities/trigger_hurt_remote.md) and
  [`locus_beam`](../entities/locus_beam.md), accept `!activator`, `*locus` and `*player`, but not `!caller`
- The logic entities and `trigger_changevalue` accept `!activator` and `!caller`, where `!caller` is the entity that
  fired them

## Aliases [[ported:spirit]]

An alias is a stand-in name you can point at different entities while the map runs. For example, make an
[`info_alias`](../entities/info_alias.md) named `exit`, and write `*exit` (the alias name with a `*` in front) in a
**Target**, and the target is then the entity `exit` points to at that moment. A
[`trigger_changealias`](../entities/trigger_changealias.md) points the alias at a different entity, so one button
can open one door first and another door later without any change to the button. Like wildcards, aliases work in
every key that names an entity, such as **Target**, **KillTarget**, **Master** and the targets of a
[`multi_manager`](../entities/multi_manager.md).

| You write | It stands for |
|---|---|
| `*exit` | The entity, or entities, that the alias named `exit` points to at that moment |
| `exit` | The `info_alias` itself, for example to switch it |
| `grp.door` | The member `door` of the [`info_group`](../entities/info_group.md) named `grp` |
| `*exit.door` | The member `door` of the group the alias `exit` points to |

These rules apply to aliases:

- An alias can point to a wildcard such as `room1_*`, to another alias such as `*other`, or to a group member such
  as `grp.door`
- A name with a dot is a group reference only if an `info_group` has the name before the dot, so all other names
  with dots stay plain names
- If a target changes an alias while an entity fires its targets, the change waits until all of those targets have
  fired, so every target of one firing gets the same entity
- An alias never makes an entity trigger or remove itself, the same as a wildcard
- If aliases point to each other in a loop, the search stops after 16 steps and finds nothing, and with
  `developer 1` set in the console, the console shows a message

A [`multi_alias`](../entities/multi_alias.md) is an alias for several entities at once, or for a random choice among
them.

### One button for a different door each time

This button opens `door_a`, then `door_b`, then `door_c`, and then starts again with `door_a`:

1. Make a [`func_button`](../entities/func_button.md) with **Target** set to `press`
2. Make a [`multi_manager`](../entities/multi_manager.md) named `press`
3. Turn SmartEdit off and give the `multi_manager` the key `*next_door` with the value `0`, which opens the door
   the alias points to
4. Give the `multi_manager` the key `next_door` with the value `0.1`, which moves the alias to the next door
5. Make an [`info_alias`](../entities/info_alias.md) named `next_door` with **Use Mode** set to "List"
6. Turn SmartEdit off and give the `info_alias` the keys `door_a` = `1`, `door_b` = `2` and `door_c` = `3`

### One pair of buttons for two wings

Two wings each have an inner and an outer door, and one pair of buttons opens the doors of the wing whose group you
triggered last:

1. Make two [`info_group`](../entities/info_group.md) entities named `wing_a` and `wing_b`
2. Turn SmartEdit off and give each group the keys `inner` and `outer`, with the names of the inner and outer door of
   its wing as the values
3. Set **Alias to change when fired** to `wing` on both groups
4. Make an [`info_alias`](../entities/info_alias.md) named `wing`
5. Make a button with **Target** set to `*wing.inner`, and a second button with **Target** set to `*wing.outer`
6. Trigger `wing_a` or `wing_b`, for example from a [`trigger_multiple`](../entities/trigger_multiple.md) at the
   entrance of each wing, to point the alias `wing` at that group

## What * means in a name {#what-star-means}

A `*` means something different depending on where it is in the name, and you only write it where you use a name,
never in the name you give an entity:

| You write | It means |
|---|---|
| `room1_*` | A `*` at the end is a wildcard: every entity whose name starts with `room1_` |
| `*exit` | A `*` at the start is an alias: the entity the [`info_alias`](../entities/info_alias.md) named `exit` points to |
| `*locus`, `*player` | Built-in names that some keys accept: the entity that started the chain of triggers, and that entity if it is a player ([Locus system](locus.md)) |
| `*` | A `*` on its own is a wildcard for every named entity, so the entity triggers everything in the map that has a name, except itself |
| `*room*` | Not allowed: it finds nothing, and with `developer 1` set in the console, the console says so. To use a wildcard through an alias, point the alias at `room*` and write `*alias` |

Because `*locus` and `*player` are built-in names, the game refuses an alias named `locus` or `player`, and also an
alias or a group whose own name starts with `*`. A refused entity is removed when the map starts, and with
`developer 1` set in the console, the console reports each one.

## Notes

- No stock or custom map has a name or a target that ends in `*`, or a target that starts with `!` other than the
  two selectors, so wildcards and selectors change nothing in existing maps
- No stock or custom map has a name or a target that starts with `*` other than `*locus` and `*player`, and no
  `info_group` matches the one name with dots (`E.Y.E`), so aliases change nothing in existing maps

## Changes since 1.38

- A target that ends in `*` is a wildcard that triggers or removes every entity whose name starts the same way
- Target and Kill target accept `!activator`, the entity that started the chain (usually the player). Kill target
  `!caller` makes an entity remove itself
- `info_alias`, `multi_alias`, `trigger_changealias` and `info_group`: aliases, which are stand-in names that point to
  other entities and can be repointed while the map runs. Write `*name` in a Target, Kill target or Master to use
  whatever the alias `name` points to at that moment. For example, one button can open a different door after a
  `trigger_changealias` repoints its alias

## See also

- [Common keys](../entities/common-keys.md) - **Target**, **Delay** and **KillTarget**
- [Entity keyvalues](entity-keyvalues.md) - how keys and values work
- [Locus system](locus.md) - keys that ask another entity for a value
- [Trigger modes](trigger-modes.md) - the use types On, Off, Toggle and Set
- [`info_alias`](../entities/info_alias.md), [`trigger_changealias`](../entities/trigger_changealias.md),
  [`multi_alias`](../entities/multi_alias.md), [`info_group`](../entities/info_group.md) - the alias entities
