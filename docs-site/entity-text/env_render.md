---
description: "An env_render copies its own render settings to its targets each time you trigger it, and can also scale and fade them."
---
An `env_render` copies its own render settings (the render mode, the FX amount, the FX color and the render FX) to its
targets each time you trigger it. It can also change their scale, fade them over a time and remove them after the
fade.

## Attributes

- **Name** (`targetname`) - Triggering the entity changes its targets. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to change. You can also use `!activator` for the entity that started
  the chain of triggers, or `*player` for that entity only when it is a player. See
  [Common keys](common-keys.md#target)
- **FX Amount factor** (`message`) - Multiplies the FX amount that the targets get. It takes a
  [locus number](../guide/locus.md), so you can use a number such as `0.5`, a range such as `0.2..0.8` for a random
  number in it, or the name of a `calc_` entity
- **Scale** (`m_fScale`) - Sets the scale of the models or sprites of the targets. Their hitboxes and their solid
  box change with it, step by step during a fade, and 0 keeps the scale they have
- **Fade Time** (`frags`) - Sets how many seconds the FX amount, the color and the scale take to change smoothly to
  the new values, while the render mode and the render FX change at once. With 0, everything changes at once
- **Trigger after fading** (`netname`) - Names the entities to trigger once the change is done, or at once when it
  doesn't fade. The first target is passed on as the
  [activator](../guide/entity-triggering.md#target-selectors)

## Flags

- **No Renderfx** (1) - The targets keep their own render FX
- **No Renderamt** (2) - The targets keep their own FX amount
- **No Rendermode** (4) - The targets keep their own render mode
- **No Rendercolor** (8) - The targets keep their own FX color
- **Remove target** (32) - The targets are removed when the fade is done, but players are never removed. Without a
  **Fade Time**, nothing is removed
- **Remove self** (64) - The `env_render` removes itself after it is used

## Notes

- Each player's game draws the fade, so it is smooth on every player's screen
- A new trigger during a fade replaces the fade the entity was waiting to finish

## See also

- [Props, models and fades](../features/props-and-fades.md) - models in a map and how to fade them
- [`env_model`](env_model.md) - an animated model
- [`env_sprite`](env_sprite.md) - a sprite that you can switch on and off
- [env_render on TWHL](https://twhl.info/wiki/page/env_render) - the Half-Life entity

## Changes since 1.38

- `env_render` has the keys **FX Amount factor**, **Scale**, **Fade Time** and **Trigger after fading**, and the flags
  **Remove target** and **Remove self**. In SBO 1.38, it could only copy the render settings immediately
