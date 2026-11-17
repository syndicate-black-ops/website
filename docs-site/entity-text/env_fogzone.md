---
description: "An env_fogzone gives a part of the map its own fog, which replaces the fog of the map's env_fog inside the zone."
---
An `env_fogzone` gives a part of the map its own fog. The zone is the box around its brushes, and inside it, the
zone's fog replaces the fog of the map's [`env_fog`](env_fog.md). Seen from outside, the zone looks like haze, and the
deeper the view goes into the zone, the more the map's fog changes into the zone's fog.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the zone on or off. Without a name, the zone is always on.
  See [Common keys](common-keys.md#targetname)
- **Fog color** (`rendercolor`) - Sets the color of the fog inside the zone, as red, green and blue from 0 up to 255
- **Density** (`density`) - Sets how thick the fog inside the zone is, so the higher the value, the closer to the
  player things fade into the fog color. You can also type any value from 0 up to 0.01, and a negative value or a
  value above 0.01 works like None
    - None (0) - No fog inside the zone, even when the map has fog
    - Misty (0.0005)
    - Thin (0.0007)
    - Hazy (0.001)
    - Moderate (0.003)
    - Dense (0.005)
    - Thick (0.01)

## Flags

- **Active** (1) - A zone with a **Name** is on when the map starts. Without this flag, a named zone starts off. This
  flag is set by default

## Notes

- Spectators in free view get the fog of the zone their camera is in
- Only the first 32 zones of a map are drawn
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Fog
  color**, **Density** or the zone's position, every player gets the new zone at once. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`env_fog`](env_fog.md) - fog over the whole map
- [`color_correction_volume`](color_correction_volume.md) - changes the colors of the view inside a brush
- [Weather and fog](../features/weather.md) - fog, rain and snow

## Changes since 1.38

- `env_fogzone` is new in SBO 2.0.0
