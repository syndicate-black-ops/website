A `monster_generic` is a model that acts as a monster in scripts. It has no AI of its own, so
[`scripted_sequence`](scripted_sequence.md) entities make it walk and play animations.

It still has a class, which sets how other monsters treat it. By default it is a player ally, so monsters that fight
players, such as the Apache, attack it. Its **Classification** key changes who attacks it, not what it does. See
[Monster classes](../guide/monster-classes.md) for more details.

## Attributes

- **Model** (`model`) - Sets the model the monster uses. The default is a placeholder that only the editor has, so if
  you keep it, the game removes the entity when the map starts
- **Body** (`body`) - Sets which submodel of each body group of the model shows, where 0 shows the first of each

## Flags

- **Not solid, can't be hurt** (4) - Players and monsters walk through the monster, and nothing can hurt it

## Notes

- If the entity has no model, a model under `models/editor/` or a model file the server doesn't have, the game removes
  it when the map loads, and with `developer 1` set in the console, the console names it

## See also

- [`monster_furniture`](monster_furniture.md) - a model that scripts animate but that never walks
- [`scripted_sequence`](scripted_sequence.md) - plays an animation on a monster
- [monster_generic on TWHL](https://twhl.info/wiki/page/monster_generic) - the Half-Life entity

## Changes since 1.38

- A `cycler`, `monster_generic`, `monster_furniture`, `change_touch` or `env_glow` with a missing model or sprite is
  removed when the map loads. In SBO 1.38 the map did not load
