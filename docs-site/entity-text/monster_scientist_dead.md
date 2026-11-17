A `monster_scientist_dead` is a dead Scientist lying or sitting in the map, for decoration.

## Attributes

- **Body** (`body`) - Sets the dead Scientist's head
    - Random (-1, default) - It picks one of the four heads when the map starts
    - If you leave this key empty, it has the head Glasses
- **Pose** (`pose`) - Sets how the body lies or sits
    - Hanging (3) - The Scientist model has no hanging animation, so with `developer 1` set in the console, this pose
      shows the console message "Dead scientist with bad pose"
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  **Pose** sets the animation

## See also

- [`monster_scientist`](monster_scientist.md) - the living Scientist
- [monster_scientist_dead on TWHL](https://twhl.info/wiki/page/monster_scientist_dead) - the Half-Life entity

## Changes since 1.38

- Fixed a dead Cop, Fed or Scientist with a Pose outside the list crashing the game when the map loaded. The game did
  not check the number. This was a bug in SBO 1.38
