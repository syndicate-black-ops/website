A `game_counter_set` sets a [`game_counter`](game_counter.md) to a new number each time you trigger it. It fires its
**Target** with the [use type](../guide/trigger-modes.md) Set and its **New Value**, so it can set any entity that
takes a number this way, such as a [`game_number`](game_number.md).

## Attributes

- **Name** (`targetname`) - Triggering the entity sets the number. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the counter to set
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing
- **New Value** (`frags`) - Sets the number the counter gets
    - If you leave this key empty, it is 0

## Flags

- **Remove On fire** (1) - The entity removes itself after it has set the counter once

## See also

- [`game_counter`](game_counter.md) - counts triggers and fires a target at a limit
- [game_counter_set on TWHL](https://twhl.info/wiki/page/game_counter_set) - the Half-Life entity
