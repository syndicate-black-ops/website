An `env_fade` fades the screen of players to a color, or back from a color, each time you trigger it.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts the fade. See [Common keys](common-keys.md#targetname)
- **Duration** (`duration`) - Sets how many seconds the fade takes
    - If you leave this key empty, it is 0 and the screen changes at once
- **Hold Fade** (`holdtime`) - Sets how many seconds the screen stays fully faded after the fade, before it clears
- **Fade Alpha** (`renderamt`) - Sets how strong the fade is at its peak, from 0 for no fade up to 255, which covers
  the screen completely
    - If you leave this key empty, it is 0 and you can't see the fade
- **Fade Color** (`rendercolor`) - Sets the color the screen fades to, as red, green and blue from 0 up to 255

## Flags

- **Fade From** (1) - The screen starts at the fade color and fades back to normal. Without this flag, it fades from
  normal to the color
- **Modulate** (2) - The color tints the screen, because it multiplies the colors of the picture. Without this flag,
  the color is painted over the picture
- **Activator Only** (4) - Only the player who triggered the entity sees the fade. Without this flag, every player
  sees it
- **Directional blind** (8) - The strength of the fade for each player depends on how directly they look at the
  `env_fade`. It is at full strength when they look within about 30 degrees of it, weaker the further they look
  away, and nothing when it is beside or behind them

## See also

- [`env_shake`](env_shake.md) - shakes the view of players
- [`color_correction`](color_correction.md) - changes the colors of the 3D view for as long as it is on
- [`env_overlay`](env_overlay.md) - shows a picture over the screen

## Changes since 1.38

- You can use the new flag **Directional blind**
