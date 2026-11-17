A `cycler` shows a model and plays its animations in a loop (Half-Life used it to look at the animations of a model).
It is solid, and it never dies, because damage only changes the animation it plays.

## Attributes

- **Name** (`targetname`) - Each trigger stops or starts the animation, like a player's use key does. See
  [Common keys](common-keys.md#targetname)
- **Model** (`model`) - Sets the model it shows, as a path to an `.mdl` file
    - If you leave this key empty, or use an editor model or a file the server doesn't have, the entity is removed
      when the map starts
- **Animation sequence** (`sequence`) - Sets the animation it starts with, as its number in the model. With 0, the
  model plays its first animation in a loop, and with any other number, the model stands still on the first frame of
  that animation

## Notes

- Each hit on a playing model starts its next animation, and each hit on a model that stands still moves it one frame
  on. With `developer 1` set in the console, the console shows the animation number and the frame after each hit
- Players can stop and start the animation with their use key
- A [`scripted_sentence`](scripted_sentence.md) can name it as its speaker

## See also

- [`env_model`](env_model.md) - an animated model for a map
- [`env_static`](env_static.md) - a model that stands still
- [`monster_generic`](monster_generic.md) - a model that acts like a simple monster

## Changes since 1.38

- If the model is an editor model or a file the server doesn't have, the entity is removed when the map starts. In SBO
  1.38, the game tried to load the model, and a missing file stopped the map from loading
- A [`scripted_sentence`](scripted_sentence.md) can make it speak
