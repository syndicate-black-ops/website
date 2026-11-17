A `monster_hgrunt_dead` is a dead Fed lying on the ground, for decoration.

## Attributes

- **Pose** (`pose`) - Sets how the dead Fed lies, which is the animation the game shows for the body
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  **Pose** sets the animation

## See also

- [`monster_human_grunt`](monster_human_grunt.md) - the living Fed
- [monster_hgrunt_dead on TWHL](https://twhl.info/wiki/page/monster_hgrunt_dead) - the Half-Life entity

## Changes since 1.38

- Fixed a dead Cop, Fed or Scientist with a Pose outside the list crashing the game when the map loaded. The game did
  not check the number. This was a bug in SBO 1.38
