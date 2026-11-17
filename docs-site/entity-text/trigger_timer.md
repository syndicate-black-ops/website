A `trigger_timer` fires its target again and again while it is on, after random delays between a minimum and a
maximum.

## Attributes

- **Target** (`target`) - Fires after each delay, with the timer as the activator. With **Forward activator**, the
  activator is the entity that turned the timer on
- **Minimum delay** (`min_delay`) - Sets the shortest delay between two fires, in seconds
- **Maximum delay** (`max_delay`) - Sets the longest delay between two fires, in seconds
- **Trigger number limit** (`trigger_number`) - Sets how many times it fires before it turns off, where 0 means no
  limit
- **Trigger on limit** (`trigger_on_limit`) - Fires when it reaches the **Trigger number limit**
- **Reset at round start** (`round_reset`) - With Yes, the entity goes back to its state at map load at each round
  start, before the players spawn. See
  [Round hooks](../guide/round-hooks.md) for more details

## Flags

- **Start on** (1) - The timer is on when the map loads
- **Don't delay first fire** (32) - The first fire comes at once when the timer turns on, instead of after a random
  delay
- **Forward activator** (64) - The target gets the entity that turned the timer on as its activator. If that entity
  is gone, the timer is the activator
- **Scheduled delays** (128) - The random delays follow a sequence that is fixed when the map loads, and each delay
  is still between the minimum and the maximum
- **Don't reset trigger counter on deactivation** (256) - The timer keeps its count when it turns off, so the count
  for **Trigger number limit** continues when it turns on again. Without this flag, the count goes back to 0

## Notes

- On turns it on, Off turns it off and Toggle switches it

## See also

- [`trigger_random`](trigger_random.md) - fires a random target, also with timers

## Changes since 1.38

- `trigger_timer` is new
