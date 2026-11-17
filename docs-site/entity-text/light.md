A `light` is an invisible light that the map compiler uses to light the map. A light with a **Name** can be switched
on and off while the map runs, and a [`trigger_lightstyle`](trigger_lightstyle.md) or a
[`global_light_control`](global_light_control.md) can give it another pattern.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the light on or off, and the map compiler gives a light
  with a name its own light style. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Turns the light into a spot light aimed at the named entity when the map compiler builds
  the map. The cone is 10 degrees, unless you add the key `_cone` with SmartEdit off. The game never fires it

## Flags

- **Initially dark** (1) - The light starts off and turns on when you trigger it. It only works on a light with a
  **Name**

## Notes

- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Custom
  Appearance** while the light is on, the new pattern shows at once. **Appearance** (the style number) can't change
  while the map runs, because the light would then switch the lights of another style. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`light_spot`](light_spot.md) - a light that shines in a cone
- [`light_environment`](light_environment.md) - the sun
- [Light styles](../features/light-styles.md) - how light patterns work
- [light on TWHL](https://twhl.info/wiki/page/light) - the Half-Life entity
