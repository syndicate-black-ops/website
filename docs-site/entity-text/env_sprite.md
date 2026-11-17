An `env_sprite` shows a sprite, or a studio model, at its position. You can switch it on and off, and it can ride on
another entity.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows or hides the sprite, as the
  [use type](../guide/trigger-modes.md) says. Without a name, the sprite is always shown. See
  [Common keys](common-keys.md#targetname)
- **Framerate** (`framerate`) - For a sprite, sets how many frames per second it plays. For a studio model, sets how
  fast its animation plays: 1 is the animation's own speed, 0.5 is half and 0 holds the first frame
    - If you leave this key empty, it is 0, so a sprite doesn't animate and a model holds its first frame
- **Sequence** (`sequence`) - For a studio model only, sets the number of the animation it plays, where 0 is the first
- **Sprite or model** (`model`) - Sets the sprite (`.spr`) or the studio model (`.mdl`) it shows
    - If you leave this key empty, or use an editor model or a file the server doesn't have, the entity is removed
      when the map starts
- **Scale** (`scale`) - Sets the size, so 0.5 is half and 2 is double. For a studio model, only the look changes
    - If you leave this key empty or set 1, it has its normal size
- **Attached to entity...** (`message`) - Names an entity the sprite rides on, so it moves with that entity
- **...at attachment point** (`frags`) - Picks where on the model of that entity the sprite sits
    - 0 (0) - At the entity's own position
    - 1 (1) - At the first attachment point of the model, a point the model maker placed
    - 2 (2) - At the second attachment point
    - 3 (3) - At the third attachment point
    - 4 (4) - At the fourth attachment point
- **Start frame** (`impulse`) - Sets the frame of a sprite it starts on each time it is shown, where 0 is the first,
  and a negative number picks a random frame

## Flags

- **Start on** (1) - A sprite with a **Name** is shown when the map starts. A sprite without a name is always shown
- **Play Once** (2) - The sprite plays its frames once and then hides, until you show it again. A studio model hides
  when its animation is done
- **Don't mess Yaw** (8) - The entity uses its angles as the map gives them. Without this flag, a yaw set in the
  editor turns the sprite around the axis it faces along

## Notes

- A studio model keeps playing its animation on each player's game without the server

## See also

- [`env_glow`](env_glow.md) - a sprite that is always shown
- [`env_static`](env_static.md) - a model that stands still
- [`env_model`](env_model.md) - an animated model with an on and an off animation
- [Model scale](../features/model-scale.md) - how scale works on models
- [env_sprite on TWHL](https://twhl.info/wiki/page/env_sprite) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Attached to entity...**, **...at attachment point** and **Start frame** and the new flag
  **Don't mess Yaw**
- A studio model plays its animation at the speed that **Framerate** sets. In SBO 1.38, it played the animation
  **Framerate** times too fast
- The `scale` key draws models at that scale. SBO 1.38 always drew them at their normal size
