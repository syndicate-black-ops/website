An `info_alias` is a stand-in name for another entity, and you can point it somewhere else while the game runs. If you
write `*` and the alias's name in a **Target**, **KillTarget**, **Master** or any other key that names an entity, the
game uses the entity the alias points to at that moment. See the [Entity
triggering](../guide/entity-triggering.md#aliases) guide for more details.

Triggering the alias by its plain name switches it: in On/Off mode it changes between its two references, and in List
mode it steps through a list of names. A [`trigger_changealias`](trigger_changealias.md) can point it at any other
name or entity.

## Attributes

- **Name** (`targetname`) - Sets the alias's name. Write it with a `*` in front, such as `*exit`, where you mean the
  entity it points to, and without the `*` to trigger the alias itself. See [Common keys](common-keys.md#targetname)
- **Reference while On** (`target`) - Names what the alias points to while it is on. This can be a name, a
  [wildcard](../guide/entity-triggering.md#wildcards) such as `room1_*` for every entity whose name starts with
  `room1_`, another alias such as `*other`, or a member of an [`info_group`](info_group.md) such as `grp.door`
- **Reference while Off** (`netname`) - Names what the alias points to while it is off, in the same way
- **Use Mode** (`mode`) - Picks what a trigger does to the alias
    - On/Off (0) - A trigger with the [use type](../guide/trigger-modes.md) Toggle or Set switches the alias between
      on and off, On turns it on and Off turns it off
    - List (1) - The alias points to the names in a list, starting with the first. On, Toggle and Set step to the
      next name, Off steps back to the one before, and the list wraps around at both ends. If a
      [`trigger_changealias`](trigger_changealias.md) pointed the alias at one of the list's names, the next step
      starts from that name. You make the list with SmartEdit off: one key per name, the name as the key and its
      place in the list, from 1 to 16, as the value

## Flags

- **Start Off** (1) - In On/Off mode, the alias starts off, so it points to **Reference while Off**
- **Debug Mode** (2) - With `developer 1` set in the console, the console shows each change of what the alias points
  to

## Notes

- If an alias changes while the targets of one trigger are being fired, the change takes effect once that firing is
  done, so all the targets see the same entity
- An alias can point to an entity that has no name, such as a player, when a
  [`trigger_changealias`](trigger_changealias.md) sets it to [`!activator`](../guide/locus.md#entity-names-in-a-locus-key)
- If several aliases have the same name, `*name` stands for every entity any of them points to
- If aliases point to each other in a loop, `*name` finds nothing, and with `developer 1` set in the console, the
  console reports it
- The game removes an alias named `locus` or `player`, because [`*locus` and
  `*player`](../guide/locus.md#entity-names-in-a-locus-key) are built-in names, and it also removes an alias whose
  name starts with `*`. With `developer 1` set in the console, the console reports each one when the map starts
- `*name*`, with a `*` at both ends, isn't allowed and finds nothing, but an alias can point to a
  [wildcard](../guide/entity-triggering.md#wildcards) such as `name*`

## See also

- [What * means in a name](../guide/entity-triggering.md#what-star-means) - wildcards, aliases and the built-in names
- [Entity triggering](../guide/entity-triggering.md#aliases) - how `*name` mixes with wildcards and selectors, with
  small setups
- [`trigger_changealias`](trigger_changealias.md) - points an alias at a new name or entity
- [`multi_alias`](multi_alias.md) - an alias for several entities at once
- [`info_group`](info_group.md) - a set of names that you reach with `group.member`
- [`trigger_changetarget`](trigger_changetarget.md) - changes the **Target** of one entity instead

## Changes since 1.38

- `info_alias` is new in SBO 2.1.0
