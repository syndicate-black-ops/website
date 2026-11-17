A `trigger_auto` fires its target once, 0.1 seconds after the map loads. With a **Global State to Read**, it only
fires if that global state is On at that moment.

## Attributes

- **Global State to Read** (`globalstate`) - Names a global state that an [`env_global`](env_global.md) sets. The
  entity only fires if that state is On
    - If you leave this key empty, it always fires

## Flags

- **Remove On fire** (1) - The entity removes itself after it fires

## Notes

- Its **Trigger State** is Off by default, so its targets get the use type Off. To switch something on, set
  **Trigger State** to On or Toggle. See [Trigger modes](../guide/trigger-modes.md#trigger-state) for more details

## See also

- [`trigger_relay`](trigger_relay.md) - passes a trigger on
- [Round hooks](../guide/round-hooks.md) - the names the game fires at each round start
- [trigger_auto on TWHL](https://twhl.info/wiki/page/trigger_auto) - the Half-Life entity
