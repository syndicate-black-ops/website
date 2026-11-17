A `game_number` holds a number that keys that take a number can read. Unlike a [`game_counter`](game_counter.md), it
has no limit and fires nothing.

A trigger with the [use type](../guide/trigger-modes.md) On or Toggle adds 1, Off takes 1 away, and Set puts in the
number the trigger brings, such as the result a [`calc_eval_number`](calc_eval_number.md) stores.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's number key so it reads this one, and
  triggering the entity by this name changes the number. See [Common keys](common-keys.md#targetname)
- **Initial value** (`frags`) - Sets the number the entity holds when the map starts
- **Reset at round start** (`round_reset`) - Sets whether the number goes back to its value of the map start at each
  new round of Co-op, Battle Royale and Bounty Killer, before the players spawn
    - No (0) - The number keeps its value from round to round
    - Yes (1) - The number goes back to its value of the map start

## Notes

- A key that takes a position or a vector and names a `game_number` gets the position of the entity, or its
  velocity

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [`calc_eval_number`](calc_eval_number.md) - works out a number and can store it here
- [`game_counter`](game_counter.md) - counts triggers and fires a target at a limit
- [`trigger_compare`](trigger_compare.md) - compares two numbers and fires a target

## Changes since 1.38

- `game_number` is new in SBO 2.0.0
