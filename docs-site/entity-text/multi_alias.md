---
description: "A multi_alias is one name for several entities at once, or for a random choice among them, used as *name in a Target."
---
A `multi_alias` is one name for several entities at once, or for a random choice among them. If you write `*` and its
name in a **Target**, such as `*all_lights`, the game uses every entity it names. See [Entity
triggering](../guide/entity-triggering.md#aliases) for more details.

You list the names with SmartEdit off, one key per name, with the name as the key. The value is the name's weight or
its percent chance, depending on **Mode**, and in Normal mode the game ignores it.

## Attributes

- **Name** (`targetname`) - The name you write with a `*` in front where you mean its entities. See
  [Common keys](common-keys.md#targetname)
- **Mode** (`m_iMode`) - Picks which of the names count each time the alias is used
    - Normal (0) - Every name counts
    - Choose one (weighted) (1) - One name is chosen at random each time, and a name with a higher value is chosen
      more often, in proportion to its value
    - % chance for each (2) - Each name counts with its value as the percent chance, so none, some or all of them
      may count

## Notes

- The random choice is made once per moment of game time, so every search in that moment, such as all the targets
  of one trigger, sees the same entities
- A [`trigger_changealias`](trigger_changealias.md) can't change a `multi_alias`
- It holds up to 64 names, and it leaves out each name after that. With `developer 1` set in the console, the console
  names each name it leaves out
- Each name can be a [wildcard](../guide/entity-triggering.md#wildcards) such as `room1_*`, another alias such as
  `*other`, or a member of an [`info_group`](info_group.md) such as `grp.door`

## See also

- [What * means in a name](../guide/entity-triggering.md#what-star-means) - wildcards, aliases and the built-in names
- [`info_alias`](info_alias.md) - an alias that points to one name, and a `trigger_changealias` can repoint it
- [Entity triggering](../guide/entity-triggering.md#aliases) - how `*name` works

## Changes since 1.38

- `multi_alias` is new in SBO 2.1.0
