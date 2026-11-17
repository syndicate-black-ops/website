---
description: "A trigger_changealias points an info_alias at a new name or entity when you trigger it."
---
A `trigger_changealias` points an [`info_alias`](info_alias.md) at a new name or entity when you trigger it, and from
then on, every `*alias` in the map means the new name or entity.

## Attributes

- **Name** (`targetname`) - Triggering the entity by this name changes the alias. See
  [Common keys](common-keys.md#targetname)
- **Alias to affect** (`target`) - Names the alias, by its plain name without a `*`. If several aliases have the
  name, it changes all of them
- **String to Set** (`netname`) - Sets what the alias points to after the change
    - A name, a [wildcard](../guide/entity-triggering.md#wildcards) such as `room1_*`, a member of an
      [`info_group`](info_group.md) such as `grp.door`, or another alias such as `*other` - The alias keeps this
      text. With `*other`, it follows `other` each time `other` changes later
    - [`!activator` or `*locus`](../guide/locus.md#entity-names-in-a-locus-key) - The entity that started the chain
      of triggers, such as the player who pressed a button, even if that entity has no name
    - [`!caller`](../guide/entity-triggering.md#target-selectors) - The entity that fired the `trigger_changealias`

## Flags

- **Resolve references** (1) - The entity looks up **String to Set** at once, and the alias keeps the first entity
  it finds. Later changes to another alias named in it don't change this one. If the entity finds nothing, the alias
  points nowhere
- **Debug Mode** (2) - With `developer 1` set in the console, the console shows each change it makes

## Notes

- If you trigger it while the game fires the targets of another trigger, the change starts when that firing is done
- If no `info_alias` has the name in **Alias to affect**, nothing changes. With `developer 1` set in the console, the
  console shows a message about it
- It can't change a [`multi_alias`](multi_alias.md)

## See also

- [What * means in a name](../guide/entity-triggering.md#what-star-means) - wildcards, aliases and the built-in names
- [`info_alias`](info_alias.md) - the alias it changes
- [`info_group`](info_group.md) - points an alias at a group when you trigger it
- [Entity triggering](../guide/entity-triggering.md#aliases) - how `*name` works

## Changes since 1.38

- `trigger_changealias` is new in SBO 2.1.0
