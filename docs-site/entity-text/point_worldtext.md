A `point_worldtext` draws text in the world at its origin, such as a label, a sign or a note, without a texture. Every
player sees it, also players who join later, spectators and demos. See [World text](../features/world-text.md) for how
to place it.

![point_worldtext labels on a wall of co_sbo_showcase](../../assets/img/screens/world-text.webp)

*World text labels on a wall*

## Attributes

- **Entity Message** (`message`) - Sets the text, and `\n` starts a new line. The text can have up to 1023 bytes of
  UTF-8 text, so accents and arrows work. A character that the font doesn't have shows as `?`
- **Text Size** (`textsize`) - Sets the height of a line, in units
- **Text Spacing X** (`textspacingX`) - Sets extra space after each letter, in 1/64 of the **Text Size** for a sans
  font or 1/128 for a mono font. Negative values pull the letters together
- **Text Spacing Y** (`textspacingY`) - Sets extra space between the lines, in 1/64 of the **Text Size** for a sans
  font or 1/128 for a mono font. Negative values pull the lines together
- **Color** (`color`) - Sets the color of the text and its opacity, as R G B A
- **Font** (`font`) - Sets the font and the outline, shadow or glow around its letters
- **Orientation** (`orientation`) - Sets how the text turns
    - Stationary (0, default) - The text lies in the plane of the entity's angles, and you read it when you look the
      way the entity points. It only has one side
    - Face player (1) - The text always faces the viewer
    - Face player, upright (2) - The text faces the viewer without tilting up or down
- **Rainbow** (`rainbow`) - With Yes, the letters cycle through the colors of the rainbow, each letter a little ahead
  of the one before it

## Flags

- **Start Off** (1) - The text stays hidden until you trigger the entity
- **Center lines** (2) - Each line is centered on the origin. Without this flag, the origin is the start of the first
  line's baseline

## Notes

- Triggering it shows or hides the text, as the [use type](../guide/trigger-modes.md) says
- A [`trigger_changevalue`](trigger_changevalue.md) or a [`trigger_copyvalue`](trigger_copyvalue.md) can change any of
  its keys while the map runs, such as `message`, `color`, `font` or `textsize`. Every player sees the change
- Text without a name takes no entity slot
- A map can have up to 1024 `point_worldtext` entities, and the game leaves out the ones after that
- Only the OpenGL renderer draws the text
- With **Move with**, the text moves and turns with its parent, and each player's game draws it there. Such text keeps its entity slot, also without a name. See
  [Moving objects](../features/moving-objects.md#cameras-world-text-and-screens)

## See also

- [World text](../features/world-text.md) - how to place text and which characters work
- [`vgui_screen`](vgui_screen.md) - a screen in the world that players click

## Changes since 1.38

- `point_worldtext` is new
