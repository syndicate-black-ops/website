An `env_model` shows an animated model with one animation while it is on and another while it is off. Each animation
can loop, stop on its last frame, or switch the entity to its other state when it ends.

Triggering the entity switches it on or off, as the [use type](../guide/trigger-modes.md) says, and the model plays
the animation of its new state.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches it on or off. See
  [Common keys](common-keys.md#targetname)
- **Model name** (`model`) - Sets the model it shows, as a path to an `.mdl` file. A new entity starts with
  `models/editor/env_model.mdl`, an editor model that only the editor has, a box 32 by 32 by 72 units labeled
  ENV MODEL whose arrow shows the yaw
    - If you leave this key empty, keep the editor model, or name a file the server doesn't have, the entity is
      removed when the map starts
- **Skin** (`skin`) - Sets the skin of the model, where 0 is the first
- **Body** (`body`) - Sets the body group value of the model, where 0 is the first
- **Scale** (`scale`) - Draws the model this many times its size, so 0.5 is half and 2 is double, and 0 or 1 is the
  normal size
- **Starting frame** (`frame`) - Sets the frame of the animation the model starts at, from 0 up to 255, and -1 picks
  a random frame
- **Sequence when on** (`m_iszSequence_On`) - Sets the name of the animation the model plays while it is on, and a
  name the model doesn't have plays its first animation
- **Behavior when on** (`m_iAction_On`) - Sets what the model does when **Sequence when on** reaches its last frame
  while the entity is on
    - Freeze when sequence ends (0) - The model stays on the last frame
    - Loop (1) - The animation starts again
    - Change state when sequence ends (2) - The entity switches off and plays **Sequence when off**
- **Framerate when on** (`m_flFramerate_On`) - Sets how fast the on animation plays: 1 is its own speed and 2 is
  twice as fast
    - If you leave this key empty or set 0, it is 1
- **Sequence when off** (`m_iszSequence_Off`) - Sets the name of the animation the model plays while it is off, and
  a name the model doesn't have plays its first animation
- **Behavior when off** (`m_iAction_Off`) - Sets what the model does when **Sequence when off** reaches its last
  frame while the entity is off
    - Freeze when sequence ends (0) - The model stays on the last frame
    - Loop (1) - The animation starts again
    - Change state when sequence ends (2) - The entity switches on and plays **Sequence when on**
- **Framerate when off** (`m_flFramerate_Off`) - Sets how fast the off animation plays: 1 is its own speed and 2 is
  twice as fast
    - If you leave this key empty or set 0, it is 1
- **Material** (`material`) - Sets the sound and the sparks, chips and puffs that bullets make when they hit the
  model. It only works with **Solid (model hitboxes)**
    - Glass (0)
    - Wood (1)
    - Metal (2)
    - Flesh (3)
    - Cinder Block (4)
    - Ceiling Tile (5)
    - Computer (6)
    - Unbreakable Glass (7)
    - Rocks (8)
- **Reset at round start** (`round_reset`) - Sets whether the entity goes back to its state of the map start at each
  new round of Co-op, Battle Royale and Bounty Killer, before the players spawn
    - No (0) - The entity keeps its state
    - Yes (1) - The entity goes back to its state of the map start

## Flags

- **Initially Off** (1) - The entity starts off and plays **Sequence when off**
- **Drop to Floor** (2) - When the map starts, the model drops onto the floor below it
- **Solid (20 unit box)** (4) - The model is solid, as a box 20 units wide
- **Solid (model hitboxes)** (8) - The model is solid in the shape of its hitboxes. The model must be compiled with `$flags 512` and
  `$hbox` lines, and a model without them is solid as the 20-unit box
- **Client-side animation** (16) - Each player's game animates the model by itself, so the server sends no frame
  updates. The server still knows when an animation ends
- **Always send to clients** (32) - The model is sent to every player, even when they can't see it, which uses more
  of the network connection

## Notes

- Bullets leave no decal on the model
- If the model has no animation with a name you set, the console reports it when `developer 1` is set in the console

## See also

- [`env_static`](env_static.md) - a model that each player's game draws by itself
- [`env_render`](env_render.md) - changes the look of a model or fades it
- [Props, models and fades](../features/props-and-fades.md) - models in a map

## Changes since 1.38

- `env_model` is new in SBO 2.0.0
