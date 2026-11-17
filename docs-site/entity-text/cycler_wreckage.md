A `cycler_wreckage` shows a sprite, fire by default, and makes puffs of smoke for as long as the map runs. The sprite
stays on its first frame, and triggering the entity does nothing.

## Attributes

- **Sprite Name** (`model`) - Sets the sprite it shows, or a model. The smoke puffs rise from random points inside
  the size of the sprite, five times a second
    - If you leave this key empty, it shows nothing and makes only the smoke
- **Scale** (`scale`) - Sets the size the sprite is drawn at: 1 is its own size, 2 is double and 0.5 is half
    - If you leave this key empty or set 0, the sprite has its own size

## Notes

- Only players who can see the area of the entity see the smoke puffs

## See also

- [`env_smoker`](env_smoker.md) - makes smoke from the start of the map for a while, then removes itself
- [`env_sprite`](env_sprite.md) - shows a sprite that can animate

