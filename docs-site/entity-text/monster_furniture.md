A `monster_furniture` is a model that [`scripted_sequence`](scripted_sequence.md) entities can animate. It has no AI
of its own and never walks, and nobody attacks it unless you give it a **Classification**.

## Attributes

- **Model** (`model`) - Sets the model to show. The default is a placeholder that only the editor has, so if you keep
  it, the game removes the entity when the map starts

## Notes

- If the entity has no model, a model under `models/editor/` or a model file the server doesn't have, the game removes
  it when the map loads, and with `developer 1` set in the console, the console names it

## See also

- [`monster_generic`](monster_generic.md) - a model that scripts can also make walk
- [`scripted_sequence`](scripted_sequence.md) - plays an animation on a monster
- [monster_furniture on TWHL](https://twhl.info/wiki/page/monster_furniture) - the Half-Life entity

## Changes since 1.38

- A `cycler`, `monster_generic`, `monster_furniture`, `change_touch` or `env_glow` with a missing model or sprite is
  removed when the map loads. In SBO 1.38 the map did not load
