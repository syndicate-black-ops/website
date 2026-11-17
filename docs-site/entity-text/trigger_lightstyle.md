A `trigger_lightstyle` gives named lights another appearance when you trigger it. An appearance is a pattern of
brightness, such as a flicker, a slow fade to dark or a strobe, and the change can fade in, last for a time or stay.
See [Light styles](../features/light-styles.md) for how light styles work.

## Attributes

- **Light(s) to affect** (`target`) - Names the lights to change: a [`light`](light.md), a
  [`light_spot`](light_spot.md) or a [`light_environment`](light_environment.md) with a name, or `!activator`. It
  doesn't change other entities
- **New appearance** (`appearance`) - Sets the new appearance. 0 to 12 are Half-Life's light styles, 13 is off, 14 to
  16 fade the light in and 17 to 19 fade it out
- **Custom appearance** (`pattern`) - Sets your own appearance as letters from `a` for dark to `z` for bright, and `m`
  is normal. The pattern plays at 10 letters a second, and if you set one, the entity ignores **New appearance**
    - The entity drops other characters, reads capitals as small letters and keeps only the first 63 letters
- **Fade time** (`m_iFade`) - Sets how many seconds the light takes to reach the new appearance, and 0 changes it at
  once
- **Hold time** (`m_iWait`) - Sets how many seconds the new appearance lasts before the light goes back to its own.
  Decimals such as 0.6 work
    - If you leave this key empty or set -1, the new appearance stays
- **Reset light styles at round start** (`round_reset`) - With Yes, every light style of the map goes back to the way
  it was when the map started. This happens at each round start, before the players spawn

## Notes

- A fade goes from the first letter of the light's current pattern to the first letter of the new one, one step every
  0.1 seconds. Then the new pattern starts
- Lights that share a style change together
- Triggering a light by its name ends a fade or a hold on it, and the light switches on or off with its own
  appearance
- Players who join later see the lighting as it is at that time
- With **Reset light styles at round start**, the game sets these again: the world's styles, every named light's own
  appearance (on or off as the light is at that moment) and every
  [`global_light_control`](global_light_control.md) without a name
- The key is `appearance` and not Spirit of Half-Life's `style`. The compile tools give a named entity with a `style`
  key other than 0 the switchable style of its name. See
  [Compiler notes](../basics/compiler-notes.md) for more details

## See also

- [`global_light_control`](global_light_control.md) - sets a pattern on many lights at once
- [Light styles](../features/light-styles.md) - how light styles and patterns work

## Changes since 1.38

- `trigger_lightstyle` is new
