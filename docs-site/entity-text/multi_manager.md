A `multi_manager` fires a list of targets, each after its own delay, and passes the activator of the trigger on to
them. Each key name you add is the name of a target, and its value is the delay in seconds.

## Flags

- **multithreaded** (1) - Each trigger starts its own run of the targets, even while an earlier run is still going,
  while without this flag, the entity ignores triggers until it has fired all its targets
- **Once only** (8) - The entity removes itself once it has fired all its targets, but with **multithreaded**, it
  stays and fires on every trigger
- **Instant** (1024) - Targets with a delay of 0 fire at once, in the same server frame as the trigger, while without
  this flag, they fire in the next frame

## Notes

- A `multi_manager` fires up to 64 targets and leaves out every target key after the 64th. With `developer 1` set in
  the console, the console names each key it leaves out when the map loads
- You add the target keys with SmartEdit turned off. A key name can only appear once, so to fire the same target
  twice, you write `name#1` and `name#2`, and the game ignores everything from the `#` on
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes the delay
  of a target, that target fires once, at the new time. For a target listed more than once, the key `name` changes its
  first entry and `name#1` its second entry, and so on, even if you wrote other numbers in the entity. See
  [Changing keys](../guide/changing-keys.md)

## See also

- [`trigger_relay`](trigger_relay.md) - passes one trigger on
- [Entity triggering](../guide/entity-triggering.md) - target names and wildcards
- [multi_manager on TWHL](https://twhl.info/wiki/page/multi_manager) - the Half-Life entity

## Changes since 1.38

- You can use the new flags **Once only** and **Instant**
- `multi_manager` can now fire up to 64 targets instead of 16 as in the original
