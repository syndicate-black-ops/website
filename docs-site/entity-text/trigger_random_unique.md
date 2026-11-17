---
description: "A trigger_random_unique works like a trigger_random where each target fires only once."
---
A `trigger_random_unique` works like a [`trigger_random`](trigger_random.md) where each target fires only once: each
trigger fires one of the targets that haven't fired yet, with the activator of the trigger. Maps from Sven Co-op use
the same name.

## Attributes

- **Number of targets** (`target_count`) - Sets how many target slots it picks from, where 0 means up to the last
  slot you filled
- **First target to fire** (`first_target`) - Sets the slot from 1 to 16 that fires first, where 0 picks one at random
- **Trigger when all fired** (`trigger_on_exhaust`) - Fires when every target has fired once, with the
  `trigger_random_unique` as the activator
- **Reset at round start** (`round_reset`) - With Yes, the entity goes back to its state at map load at each round
  start, before the players spawn. See
  [Round hooks](../guide/round-hooks.md) for more details

## Flags

- **Reusable** (1) - When every target has fired, the targets can fire again. Without this flag, the entity then
  does nothing
- **Not repetitive** (32) - The same target never fires twice in a row, if there are two or more left
- **Scheduled order** (64) - The random picks follow a sequence that is fixed when the map starts

## Notes

- An empty slot between filled slots can be picked, and then nothing fires
- A target that triggers the same `trigger_random_unique` while it fires is ignored

## See also

- [`trigger_random`](trigger_random.md) - picks a random target, also with timers

## Changes since 1.38

- `trigger_random_unique` is new
