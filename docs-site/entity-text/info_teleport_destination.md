An `info_teleport_destination` marks the place where a [`trigger_teleport`](trigger_teleport.md) sends what touches
it. Its angles set the direction the teleported entity faces when it arrives.

## Attributes

- **Name** (`targetname`) - The name you put in the **Target** key of a `trigger_teleport`. See
  [Common keys](common-keys.md#targetname)
- **Target** (`target`) - With **Trigger on arrival**, the point fires this each time something arrives, and passes
  on what arrived as the [activator](../guide/entity-triggering.md#target-selectors)

## Flags

- **Trigger on arrival** (32) - Each arrival fires **Target**

## See also

- [`trigger_teleport`](trigger_teleport.md) - moves what touches it to this point
- [Teleports and jump pads](../features/teleports-and-jump-pads.md) - teleports and their keys
- [info_teleport_destination on TWHL](https://twhl.info/wiki/page/info_teleport_destination) - the Half-Life entity

## Changes since 1.38

- You can use the new key **Target** and the new flag **Trigger on arrival**
