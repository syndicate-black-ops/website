A `func_wall_toggle` is a wall that appears and disappears when you trigger it. While it is hidden, it isn't solid.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows or hides the wall: the
  [use type](../guide/trigger-modes.md) On shows it, Off hides it and Toggle switches it. See
  [Common keys](common-keys.md#targetname)

## Flags

- **Starts Invisible** (1) - The wall starts hidden and not solid, and triggering it makes it appear
- **Use Angles** (2) - The wall keeps the angles set in the map. Without this flag, the angles are set to `0 0 0`

## See also

- [`func_wall`](func_wall.md) - a wall that is always there
- [`func_illusionary_toggle`](func_illusionary_toggle.md) - a brush that isn't solid, which you can show and hide
- [func_wall_toggle on TWHL](https://twhl.info/wiki/page/func_wall_toggle) - the Half-Life entity

## Changes since 1.38

- You can use the new flag **Use Angles**
