An `info_group` holds a set of named members, each standing for an entity name. If you write the group's name, a dot
and a member's name in a **Target**, such as `guards.leader`, the game uses the entity that member stands for. See the
[Entity triggering](../guide/entity-triggering.md#aliases) guide for more details.

You list the members with SmartEdit off, one key per member: the member's name as the key and the entity name it
stands for as the value. When you trigger a group, it points the [`info_alias`](info_alias.md) named in **Alias to
change when fired** at itself, and `*alias.member` then means that member of whichever group the alias points to.

## Attributes

- **Name** (`targetname`) - Sets the group's name, which goes before the dot. See
  [Common keys](common-keys.md#targetname)
- **Alias to change when fired** (`target`) - Names an [`info_alias`](info_alias.md), and triggering the group
  points that alias at the group
- **Default member prefix** (`defaultmember`) - Sets the name the game uses for a member the group doesn't have:
  this prefix with the member's name added. If a group named `bobs` has the prefix `bob_` and no member
  `house`, `bobs.house` means the entity `bob_house`

## Flags

- **Debug Mode** (2) - With `developer 1` set in the console, the console shows when the group changes its alias, and
  each member it doesn't have when it has no **Default member prefix**

## Notes

- A name with a dot only counts as a group member when a group with the part before the dot exists, so other names
  with dots work as before
- A member can name another group, so `grp.a.b` means the member `b` of the group that the member `a` of `grp`
  names

## See also

- [What * means in a name](../guide/entity-triggering.md#what-star-means) - wildcards, aliases and the built-in names
- [`info_alias`](info_alias.md) - the alias a group points at itself
- [Entity triggering](../guide/entity-triggering.md#aliases) - group references and aliases, with small setups

## Changes since 1.38

- `info_group` is new in SBO 2.1.0
