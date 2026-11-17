An `env_fog` gives the whole map fog, as in Counter-Strike 1.6, and you can switch it on and off. The first `env_fog`
that is on sets the fog of the map.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the fog on or off, and the fog fades to its new state
  over about a second. Without a name, the fog is always on. See [Common keys](common-keys.md#targetname)
- **Fog color** (`rendercolor`) - Sets the color of the fog, as red, green and blue from 0 up to 255
- **Density** (`density`) - Sets how thick the fog is, so the higher the value, the closer to the player things
  fade into the fog color. You can also type any value from 0 up to 0.01, and 0, a negative value or a value above
  0.01 gives no fog
    - Misty (0.0005)
    - Thin (0.0007)
    - Hazy (0.001)
    - Moderate (0.003)
    - Dense (0.005)
    - Thick (0.01)

## Flags

- **Start active** (1) - A fog with a **Name** is on when the map starts. Without this flag, a named fog starts off

## Notes

- The fog is off while the player's view is in water, slime or lava
- Players who join later get the fog as it is at that moment
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Fog
  color** or **Density** while the fog is on, every player sees the new fog at once. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`env_fogzone`](env_fogzone.md) - fog inside a brush
- [`env_rain`](env_rain.md) - rain over the map
- [`env_snow`](env_snow.md) - snow over the map
- [Weather and fog](../features/weather.md) - fog, rain and snow

## Changes since 1.38

- `env_fog` is new in SBO 2.0.0
