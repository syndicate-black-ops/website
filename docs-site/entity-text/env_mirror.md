---
description: "An env_mirror makes a mirror for models: every monster, item and other model near it is drawn a second time, flipped across the mirror."
---
An `env_mirror` makes a mirror for models: every monster, item and other model within its radius is drawn a second
time, flipped across the mirror, and players too if you set **Draw Player**. The mirror doesn't reflect the world, so
to show the room in it, you build a mirrored copy of the room behind the mirror brush and make the brush see-through.

The brush is solid. While the mirror is off, the brush is drawn opaque and no model is reflected. Players who join
later get the mirror as it is at that moment.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the mirror on or off. See
  [Common keys](common-keys.md#targetname)
- **Radius** (`radius`) - Sets how far from the middle of the brush, in units, models are reflected
    - If you leave this key empty or set 0, it is 330
- **Mirror axis** (`frags`) - Picks the axis the mirror reflects across, which matches the way the mirror faces
    - X or automatic (0) - The axis of the thinnest side of the brush, and X for a wall that faces east or west
    - Y (1) - A wall that faces north or south
    - Z (2) - A shiny floor or ceiling
- **Reflecting side** (`side`) - Picks which side of the mirror the reflection is for
    - Both (0) - The side the player looks from, with the mirror plane in the middle of the brush. A floor mirror on
      the Z axis only reflects on its top face
    - Positive only (1) - Only the east, north or top face
    - Negative only (2) - Only the west, south or bottom face
- **Render Mode** (`rendermode`) - Sets how the mirror brush is drawn while the mirror is on, with **FX Amount** as
  its opacity. While the mirror is off, the brush is drawn opaque
    - Normal (0) - Opaque, which hides the mirrored room
    - Color (1) - Drawn in the **FX Color**
    - Texture (2) - The texture, as see-through as **FX Amount** says
    - Additive (5) - The texture, added to what is behind it
- **FX Amount** (`renderamt`) - Sets how opaque the mirror brush is with the render modes Texture and Additive, from
  1 for nearly invisible up to 255 for opaque, and between 60 and 150 the mirrored room behind it shows through
- **FX Color** (`rendercolor`) - Sets the color the mirror brush is drawn in with the render mode Color, as red,
  green and blue from 0 up to 255

## Flags

- **Draw Player** (1) - The mirror also reflects players, so each player sees the other players and their own model
  in it. Without this flag, the mirror reflects no player
- **Start Off** (2) - The mirror is off until you trigger it

## Notes

- A map can have at most 32 mirrors that are on at the same time

## See also

- [Mirrors](../features/mirrors.md) - how to build the mirrored room
- [`env_render`](env_render.md) - changes the render settings of other entities

## Changes since 1.38

- `env_mirror` is new in SBO 2.0.0
