An `env_glow` shows a sprite, a glow by default, with the entity's render settings. The sprite stays on its first
frame, and triggering the entity does nothing.

## Attributes

- **Sprite Name** (`model`) - Sets the sprite it shows
    - If you leave this key empty or name a file the server doesn't have, the entity is removed when the map
      starts
- **Scale** (`scale`) - Sets the size the sprite is drawn at: 1 is its own size and 2 is double
    - If you leave this key empty or set 0, the sprite has its own size

## See also

- [`env_sprite`](env_sprite.md) - a sprite that you can switch on and off
- [Render settings](common-keys.md#renderfields) - how the sprite is drawn

## Changes since 1.38

- If the key is empty or the sprite file is missing, the entity is removed when the map starts. In SBO 1.38, this
  stopped the map from loading
