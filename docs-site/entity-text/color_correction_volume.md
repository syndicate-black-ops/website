A `color_correction_volume` changes the colors of the 3D view while the player's view is inside its brush, like the
entity of the same name in Source games. The look fades in as the view enters the brush and fades out as it leaves,
and it has the same look keys as a [`color_correction`](color_correction.md).

![A test room seen from outside a toxic color correction volume and from inside it](../../assets/img/screens/cc-volume.webp)

*A color correction volume seen from outside and from inside*

The volume uses the real shape of the brush, not only the box around it. The brush is never drawn and never blocks
anything, so you can give it any texture, such as `AAATRIGGER`.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns the look on or off, as the
  [use type](../guide/trigger-modes.md) says. See [Common keys](common-keys.md#targetname)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  the look is off too
- **Fade Time** (`fadeDuration`) - Sets how many seconds the look takes to fade in when the view enters the brush,
  and to fade out when it leaves. The same time is used when you turn the look on or off

## Notes

- The volume's look mixes with other color corrections. See
  [How the looks mix](color_correction.md#how-the-looks-mix) for more details
- Players can turn color correction off by typing `mat_colorcorrection 0` in the console. See
  [Settings](../../playing/options.md#player-cvars) for more details

## See also

- [`color_correction`](color_correction.md) - a look around a point, or over the whole map
- [Color correction](../features/color-correction.md) - lookup table files and how looks mix
- [`env_fogzone`](env_fogzone.md) - fog inside a brush

## Changes since 1.38

- `color_correction_volume` is new in SBO 2.1.0
