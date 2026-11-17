A `monster_hevsuit_dead` is a dead person in an HEV suit lying on the ground, for decoration.

## Attributes

- **Pose** (`pose`) - Sets how the body lies
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  **Pose** sets the animation

## See also

- [`monster_hgrunt_dead`](monster_hgrunt_dead.md) - a dead Fed
- [monster_hevsuit_dead on TWHL](https://twhl.info/wiki/page/monster_hevsuit_dead) - the Half-Life entity

## Changes since 1.38

- Fixed a **Pose** outside the list crashing the game when the map loaded. Such a value now gives the last pose of the
  list, or the first pose for a value below 0
