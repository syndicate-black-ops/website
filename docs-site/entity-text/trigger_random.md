A `trigger_random` fires one of up to 16 targets at random, either once for each trigger or, with **Timed**, again and
again after random delays.

## Attributes

- **Number of targets** (`target_count`) - Sets how many target slots it picks from, where 0 means up to the last
  slot you filled
- **Minimum delay** (`min_delay`) - With **Timed**, sets the shortest delay between two fires, in seconds
- **Maximum delay** (`max_delay`) - With **Timed**, sets the longest delay between two fires, in seconds
- **Trigger number limit** (`trigger_number`) - With **Timed**, sets how many times it fires before it turns off,
  where 0 means no limit
- **Trigger on limit** (`trigger_on_limit`) - Fires when it reaches the **Trigger number limit**
- **Trigger when all fired** (`trigger_on_exhaust`) - With **Unique**, fires when every target has fired once
- **First target to fire** (`first_target`) - Sets the slot from 1 to 16 that fires first, where 0 picks one at random
- **Reset at round start** (`round_reset`) - With Yes, the entity goes back to its state at map load at each round
  start, before the players spawn. See
  [Round hooks](../guide/round-hooks.md) for more details

## Flags

- **Start on** (1) - With **Timed**, it starts firing when the map starts
- **Trigger once** (2) - With **Timed**, it fires once each time it is started, and then stops
- **Reusable** (4) - With **Unique**, once every target has fired, all of them can be picked again
- **Timed** (8) - Every trigger starts or stops it, and the [use type](../guide/trigger-modes.md) makes no
  difference. While it runs, it fires a random target after each random delay between **Minimum delay** and
  **Maximum delay**
- **Unique** (16) - Each target only fires once until all of them have fired
- **Not repetitive** (32) - The same target never fires twice in a row, if there are two or more
- **Scheduled order** (64) - The random picks follow a sequence that is fixed when the map starts
- **Scheduled delays** (128) - With **Timed**, the random delays follow a sequence that is fixed when the map starts

## Notes

- Without **Timed**, the target gets the activator of the trigger. With **Timed**, the `trigger_random` is the
  activator
- An empty slot between filled slots can be picked, and then nothing fires
- A target that triggers the same `trigger_random` while it fires is ignored
- Maps from Sven Co-op may call this entity `trigger_random_time`, and SBO accepts that name too. It is a
  `trigger_random` with **Timed** set. [`trigger_random_unique`](trigger_random_unique.md) is a `trigger_random` with
  **Unique** set

## See also

- [`trigger_timer`](trigger_timer.md) - fires one target after random delays
- [`trigger_random_unique`](trigger_random_unique.md) - picks each target once

## Changes since 1.38

- `trigger_random` is new
