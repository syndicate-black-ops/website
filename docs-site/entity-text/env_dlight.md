---
description: "An env_dlight makes a dynamic light, like a muzzle flash or a rocket makes, that lights the world and the models around it."
---
An `env_dlight` makes a dynamic light, the kind of light a muzzle flash or a rocket makes, which lights the world and
the models around it. You can switch it on and off with triggers or let it stay on for a set time, and it can sit on
an entity and move with it.

Players who join later see the lights that are on. Dynamic lights are not part of the light that the map compiler
bakes into the map.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the light on or off, as the
  [use type](../guide/trigger-modes.md) says. Without a name, the light is on from the start of the map. See
  [Common keys](common-keys.md#targetname)
- **Position** (`message`) - Sets where the light is. It takes a [locus position](../guide/locus.md), so you can use
  a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that switched the light on. With
  **Position is Locus Entity**, it names the entity the light sits on
    - If you leave this key empty, the light is at the `env_dlight` itself
- **Light color** (`rendercolor`) - Sets the color of the light, as red, green and blue from 0 up to 255
- **Radius** (`renderamt`) - Sets how far the light reaches, in units, from 0 up to 1023
- **Duration** (`health`) - Sets how many seconds the light stays on after it turns on, and 0 keeps it on until you
  switch it off

## Flags

- **Only once** (1) - The entity is removed when its **Duration** ends
- **Start on** (2) - The light is on from the start of the map
- **Track position updates** (4) - While the light is on, the entity finds its **Position** again every 0.1
  seconds, so with `!activator` the light follows the entity that switched it on
- **Position is Locus Entity** (8) - The light sits on the entity named in **Position**. When that entity has a
  model you can see, the light moves with it smoothly on every player's screen. On an entity without a model, such
  as an [`info_target`](info_target.md), it stays where the entity was when the light turned on, unless you also
  set **Track position updates**

## Notes

- The game has 32 dynamic lights for each player, and muzzle flashes, rockets and other effects use them too
- If the entity can't find the position that **Position** names when you switch the light on, the light stays off
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Radius**
  or **Light color** while the light is on, every player sees the change at once. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`env_elight`](env_elight.md) - a light that only lights models
- [`light`](light.md) - a light that the map compiler bakes into the map
- [`trigger_lightstyle`](trigger_lightstyle.md) - changes the pattern of named lights while the map runs
- [Light styles](../features/light-styles.md) - how lights flicker and switch
- [Lights on models](../features/model-lights.md) - how models are lit

## Changes since 1.38

- `env_dlight` is new in SBO 2.0.0
