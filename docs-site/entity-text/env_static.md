An `env_static` shows a model that each player's game draws by itself, so the server doesn't send it. It isn't solid,
so players and monsters walk through it.

The model takes no model precache slot, and players download it with the map, together with its texture file and its
sequence groups. An `env_static` without a name also takes no entity slot.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows or hides the model for every player, as the
  [use type](../guide/trigger-modes.md) says. A **KillTarget** hides it for good. See
  [Common keys](common-keys.md#targetname)
- **Model** (`model`) - Sets the model it shows, as a path to an `.mdl` file. A new entity starts with
  `models/editor/env_static.mdl`, an editor model that only the editor has, a box 32 by 32 by 72 units labeled
  ENV STATIC whose arrow shows the yaw
    - If you leave this key empty, keep the editor model, or name a file the server doesn't have, the entity is
      removed when the map starts
- **Body** (`body`) - Sets the body group value of the model, where 0 is the first
- **Skin** (`skin`) - Sets the skin of the model, where 0 is the first
- **Animation sequence** (`sequence`) - Sets the number of the animation the model plays, where 0 is the first
- **Animation speed** (`framerate`) - Sets how fast the animation plays: 1 is its own speed, 2 is twice as fast and
  0 holds it still
- **Scale** (`scale`) - Sets the size of the model, so 0.5 is half and 2 is double, and 0 or 1 is the normal size

## Flags

- **Start invisible** (2) - The model is hidden until you trigger the entity
- **In the 3D sky** (4) - The model is in the sky room of an [`env_sky`](env_sky.md), and it shows in the 3D sky.
  Without this flag, a model in the sky room never shows

## Notes

- The model is fixed when the map starts. Only its name (show, hide) and a **KillTarget** change it, so
  [`trigger_changevalue`](trigger_changevalue.md) and a parent do nothing
- Players who join later see every model as it is at that moment
- A map shows at most 1024 `env_static` models, and the game leaves out the others
- In the 3D sky, an `env_static` costs no network traffic, unlike an [`env_model`](env_model.md) there. Keep it
  to about a hundred models, because every one is drawn each frame while the 3D sky is on

## See also

- [`env_model`](env_model.md) - an animated model with an on and an off state, which can be solid
- [`env_sprite`](env_sprite.md) - a sprite or a model that you can switch on and off
- [Props, models and fades](../features/props-and-fades.md) - models in a map

## Changes since 1.38

- `env_static` is new in SBO 2.0.0
- `env_static` has a new In the 3D sky flag, which shows the model in the sky room of an `env_sky` without any network
  cost
- A Kill target on an `env_static` now hides its model. Before, the model stayed on screen
