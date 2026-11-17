A `global_light_control` sets a light pattern on all lights without a style, on all lights with a style, or on the
style of named lights. Without a name, it sets its pattern when the map starts, and with a name, it sets it each time
you trigger it.

Players who join later see the lighting as it is at that moment.

## Attributes

- **Name** (`targetname`) - Triggering the entity sets its pattern. See [Common keys](common-keys.md#targetname)
- **Pattern** (`pattern`) - Sets the pattern, as letters from `a` for dark up to `z` for bright, where `m` is normal,
  played at 10 letters a second. The entity ignores other characters, capital letters count as small letters, and at most
  63 letters are kept
- **Only these named lights** (`target_entity`) - Names the lights to change, and the entity then ignores its flags.
  Lights that share a style change together
    - If you leave this key empty, the flags choose the lights
- **Reset light styles at round start** (`round_reset`) - Sets whether every light style of the map goes back to its
  state of the map start at each new round, before the players spawn, as on a
  [`trigger_lightstyle`](trigger_lightstyle.md)
    - No (0) - The lights keep their pattern from round to round
    - Yes (1) - The lights go back to their state of the map start

## Flags

- **Also styles 1-63** (65536) - The pattern is also set on every other light style, from 1 up to 63, which covers
  the lights with a style and the named lights
- **Not the default style** (131072) - The pattern isn't set on the lights without a style

## See also

- [`trigger_lightstyle`](trigger_lightstyle.md) - changes named lights, with a fade and a hold time
- [Light styles](../features/light-styles.md) - how light patterns work

## Changes since 1.38

- `global_light_control` is new in SBO 2.0.0
