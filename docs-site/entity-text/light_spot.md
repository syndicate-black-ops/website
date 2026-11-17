A `light_spot` lights the map in a cone when you compile the map. With a **Name**, you can switch it on and off while
the map runs, and a [`trigger_lightstyle`](trigger_lightstyle.md) or a
[`global_light_control`](global_light_control.md) can give it another pattern.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the light on or off, and the map compiler gives a light
  with a name its own light style. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Only for the map compiler, which aims the spot light at the target, such as an
  [`info_null`](info_null.md)

## Flags

- **Initially dark** (1) - The light starts off, and triggering it switches it on and off. It needs a **Name** to be
  switched

## Notes

- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Custom
  Appearance** while the light is on, the new pattern shows at once. **Appearance** (the style number) can't change
  while the map runs, because the light would then switch the lights of another style. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`light`](light.md) - a light that shines in every direction
- [`light_environment`](light_environment.md) - the sun
- [Light styles](../features/light-styles.md) - how light patterns work
- [light_spot on TWHL](https://twhl.info/wiki/page/light_spot) - the Half-Life entity
