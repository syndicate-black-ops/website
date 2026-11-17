A `monster_barney_dead` is a dead Cop lying on the ground, for decoration.

## Attributes

- **Pose** (`pose`) - Sets how the dead Cop lies
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  **Pose** sets the animation

## See also

- [`monster_barney`](monster_barney.md) - the living Cop
- [monster_barney_dead on TWHL](https://twhl.info/wiki/page/monster_barney_dead) - the Half-Life entity

## Changes since 1.38

- Fixed a dead Cop, Fed or Scientist with a Pose outside the list crashing the game when the map loaded. The game did
  not check the number. This was a bug in SBO 1.38
