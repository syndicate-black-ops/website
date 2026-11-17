A `trigger_relay` fires its target when you trigger it, with the use type you set, so it can change a Toggle into an
On or an Off. It can also delay the trigger and pass the activator on to its targets.

## Attributes

- **Trigger State** (`triggerstate`) - Sets the [use type](../guide/trigger-modes.md#trigger-state) the targets get.
  If the key is missing, the targets get Off, as in Half-Life
    - Copy Input (-1) - The use type the relay got
    - Reverse Input (-2) - On becomes Off and Off becomes On, and other use types pass on as they came
- **Delay Before Reset** (`m_flDelayBeforeReset`) - After it fires, the relay ignores every trigger for this many
  seconds, where 0 means no wait
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md). While the master is locked for the
  activator, a trigger doesn't fire the relay's targets

## Flags

- **Remove On fire** (1) - The relay removes itself after it fires once
- **Forward activator** (64) - The targets get the activator the relay got. Without this flag, the relay itself is
  the activator
- **Pass caller as activator** (128) - The targets get the entity that triggered the relay as their activator, and
  this flag wins over **Forward activator**

## See also

- [Entity triggering](../guide/entity-triggering.md) - wildcards and the selectors `!activator` and `!caller`
- [`multi_manager`](multi_manager.md) - fires several targets with delays
- [trigger_relay on TWHL](https://twhl.info/wiki/page/trigger_relay) - the Half-Life entity

## Changes since 1.38

- You can use the new **Trigger State** choices Copy Input (-1) and Reverse Input (-2), the new key **Delay Before
  Reset** and the new flags **Forward activator** (64) and **Pass caller as activator** (128)
- `trigger_relay` has a Master
