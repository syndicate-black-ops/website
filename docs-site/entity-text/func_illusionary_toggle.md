---
description: "A func_illusionary_toggle is drawn like a wall but isn't solid, and it appears and disappears when you trigger it."
---
A `func_illusionary_toggle` is drawn like a wall but isn't solid, like a [`func_illusionary`](func_illusionary.md),
and it appears and disappears when you trigger it, like a [`func_wall_toggle`](func_wall_toggle.md) that players walk
through.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows or hides the brush: the
  [use type](../guide/trigger-modes.md) On shows it, Off hides it and Toggle switches it. See
  [Common keys](common-keys.md#targetname)

## Flags

- **Starts Invisible** (1) - The brush is hidden until you trigger it

## See also

- [`func_illusionary`](func_illusionary.md) - the same, always shown
- [`func_wall_toggle`](func_wall_toggle.md) - a solid wall that you can show and hide

## Changes since 1.38

- `func_illusionary_toggle` is new in SBO 2.0.0
