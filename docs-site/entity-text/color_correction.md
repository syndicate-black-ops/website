A `color_correction` changes the colors of the 3D view, like the entity of the same name in Source games. It can make
the view black and white, noir, sepia, night, a warm sunset or a toxic green, or apply any color grade you make in an
image editor and save as a lookup table file.

The look covers the whole map, or it gets stronger the nearer the player's view is to the entity. The HUD, the
crosshair, messages, screen fades, [`env_overlay`](env_overlay.md) pictures and menus keep their own colors.

![The same test room without color correction and with the seven looks of the table below: black and white, noir, sepia, night, golden hour, toxic and dream](../../assets/img/screens/cc-looks.webp)

*One room without color correction and with seven looks*

## Attributes

- **Name** (`targetname`) - Triggering the entity turns the look on or off, as the
  [use type](../guide/trigger-modes.md) says. See [Common keys](common-keys.md#targetname)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  the look is off too. It fades out when the master turns off, and fades in again when the master turns on
- **Full Strength Distance** (`minfalloff`) - Sets how far from the entity, in units, the look is at full strength.
  If one of the two distances is -1, or both are the same, the look is the same everywhere on the map
- **Fade-Out Distance** (`maxfalloff`) - Sets how far from the entity, in units, the look is gone, and between the
  two distances it fades
- **Fade In Time** (`fadeInDuration`) - Sets how many seconds the look takes to fade in when you turn it on, and 0
  turns it on at once
- **Fade Out Time** (`fadeOutDuration`) - Sets how many seconds the look takes to fade out when you turn it off, and
  0 turns it off at once

## How the looks mix

The simple keys are applied in this order: **Saturation**, **Contrast**, **Brightness**, **Gamma** and the tint. So
without a file and with every simple key at its default, the entity changes nothing.

Several color corrections mix, and the four with the most weight where the view is count. A look's weight is how
strong it is at that point, and when the weights add up to more than 1, they are scaled down to 1. An **Exclusive**
look takes its share from all the others. Each player's game works out the look from where that player's view is,
so spectators, the picture-in-picture view and demos follow their own camera.

## Looks

These are the keys of the looks in the picture above:

| Look | Keys |
|---|---|
| Black and white | **Saturation** 0 |
| Noir | **Saturation** 0, **Contrast** 1.5, **Brightness** -0.08, **Gamma** 0.9, **Tint Color** `200 215 255`, **Tint Amount** 0.35 |
| Sepia | **Saturation** 0, **Contrast** 1.1, **Brightness** 0.03, **Tint Color** `255 200 130`, **Tint Amount** 0.85 |
| Night | **Saturation** 0.5, **Contrast** 1.1, **Brightness** -0.15, **Gamma** 0.85, **Tint Color** `110 150 255`, **Tint Amount** 0.8 |
| Golden hour | **Saturation** 1.25, **Brightness** 0.04, **Gamma** 1.1, **Tint Color** `255 190 110`, **Tint Amount** 0.5 |
| Toxic | **Saturation** 0.7, **Contrast** 1.2, **Tint Color** `140 255 90`, **Tint Amount** 0.75 |
| Dream | **Saturation** 0.8, **Contrast** 0.65, **Brightness** 0.15, **Gamma** 1.15, **Tint Color** `255 210 230`, **Tint Amount** 0.4 |

## Notes

- If the game can't read the lookup table file, the entity uses only its simple keys. With `developer 1` set in
  the console, the console reports the file once
- Players can turn color correction off by typing `mat_colorcorrection 0` in the console. See
  [Settings](../../playing/options.md#player-cvars) for more details

## See also

- [Color correction](../features/color-correction.md) - lookup table files and how looks mix
- [`color_correction_volume`](color_correction_volume.md) - a look inside a brush
- [`env_fog`](env_fog.md) - fog over the whole map
- [`env_fade`](env_fade.md) - colors the screen of players for a moment

## Changes since 1.38

- `color_correction` is new in SBO 2.1.0
