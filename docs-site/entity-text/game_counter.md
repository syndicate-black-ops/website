A `game_counter` counts the triggers it gets, and fires its target when the count reaches its limit.

A trigger with the [use type](../guide/trigger-modes.md) On or Toggle adds 1, Off takes 1 away, and Set puts in the
number the trigger brings, such as the one a [`game_counter_set`](game_counter_set.md) sends.

## Attributes

- **Name** (`targetname`) - Triggering the entity changes the count. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger with the use type Toggle when the count reaches **Limit Value**,
  and passes on the [activator](../guide/entity-triggering.md#target-selectors) of the last trigger
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the counter does nothing
- **Initial Value** (`frags`) - Sets the count the counter starts at, and goes back to with **Reset On fire**
- **Limit Value** (`health`) - Sets the count at which the counter fires its target
    - If you leave this key empty, it is 0, so counting up never fires it, and with **Fire if over limit**, every
      count fires it

## Flags

- **Remove On fire** (1) - The counter is removed after it fires its target
- **Reset On fire** (2) - After it fires its target, the count goes back to **Initial Value**. This flag is set by
  default
- **Fire if over limit** (4) - The counter fires its target each time the count is at the limit or above it, not
  only when the count equals the limit

## Notes

- It fires its target at once, because it has no delay and no **KillTarget**
- A key that takes a number, which the editor marks with **[LR]**, can name a `game_counter` and reads its count,
  and a [`calc_eval_number`](calc_eval_number.md) can store its result in one

## See also

- [`game_counter_set`](game_counter_set.md) - sets a counter to a number
- [`game_number`](game_number.md) - holds a number without a limit
- [`trigger_counter`](trigger_counter.md) - a brush trigger that fires after a number of touches
- [game_counter on TWHL](https://twhl.info/wiki/page/game_counter) - the Half-Life entity

## Changes since 1.38

- You can use the new flag **Fire if over limit**
- Keys that take a number can read a `game_counter`
