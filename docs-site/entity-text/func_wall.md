---
description: "A func_wall stands still like a part of the world, but you can give it render settings and switch it to its alternate textures."
---
A `func_wall` stands still like a part of the world, but you can give it render settings, such as see-through glass,
and switch between its normal and alternate textures by triggering it.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches its textures between the normal frame and the alternate
  `+a` frame. See [Common keys](common-keys.md#targetname)

## Flags

- **Use Angles** (2) - The wall keeps the angles set in the map. Without this flag, the angles are set to `0 0 0`

## See also

- [`func_wall_toggle`](func_wall_toggle.md) - a wall that you can show and hide
- [`func_illusionary`](func_illusionary.md) - a brush that isn't solid
- [func_wall on TWHL](https://twhl.info/wiki/page/func_wall) - the Half-Life entity

## Changes since 1.38

- You can use the new flag **Use Angles**
