---
description: "An env_modeltrain moves a model along a path of path_corner entities, the way a func_train moves a brush."
---
An `env_modeltrain` moves a model along a path of [`path_corner`](path_corner.md) entities, the way a
[`func_train`](func_train.md) moves a brush, and plays one animation while it stands still and another while it moves.

It uses the speed and the wait of each `path_corner`, fires their targets and obeys their teleport flag, and like a
`func_train`, it starts by itself when it has no name. The middle of the model goes to each `path_corner`.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the train, and **Obey Trigger Mode** sets how.
  Without a name, the train starts by itself. See [Common keys](common-keys.md#targetname)
- **Model** (`model`) - Sets the model that moves along the path, as a path to an `.mdl` file
- **Model Scale** (`scale`) - Draws the model this many times its size, so 0.5 is half and 2 is double
    - If you leave this key empty, the model has its normal size
- **First stop target** (`target`) - Names the first `path_corner` of the path
- **Speed** (`speed`) - Sets how fast the train moves, in units per second, until a `path_corner` sets another
  speed, and 0 means 100
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how a trigger starts and stops the train
    - No (0) - Every trigger starts a stopped train or stops a moving one
    - Yes (1) - On starts it, Off stops it and Toggle switches it
- **Sound Volume** (`volume`) - Sets how loud the move and stop sounds are, up to 1 for full volume
    - If you leave this key empty or set 0, it is 0.85
- **Move Sound** (`noise`) - Sets the sound that loops while the train moves
- **Stop Sound** (`noise1`) - Sets the sound the train plays when it stops
- **Idle sequence** (`idle_sequence`) - Sets the name of the animation the model plays while the train stands still
    - If you leave this key empty, it is the first animation of the model
- **Custom idle framerate** (`idle_framerate`) - Sets how fast the idle animation plays: 1 is its own speed and 2 is
  twice as fast
    - If you leave this key empty or set 0, it is 1
- **Move sequence** (`move_sequence`) - Sets the name of the animation the model plays while the train moves
- **Custom move framerate** (`move_framerate`) - Sets how fast the move animation plays: 1 is its own speed and 2 is
  twice as fast
    - If you leave this key empty or set 0, it is 1
- **Turn Policy** (`turn_policy`) - Sets how the model turns when it leaves a `path_corner`
    - Instant (0) - It turns at once to face the next `path_corner`
    - Instant, only YAW (1) - It turns at once, but only left or right, toward the next `path_corner`
    - No turn (2) - It keeps its angles

## Flags

- **Initially On** (4) - The train starts moving when the map starts

## Notes

- The train is solid, and it deals 2 crush damage to anything that blocks it, at most twice a second
- Every animation loops

## See also

- [`env_spritetrain`](env_spritetrain.md) - the same with a sprite
- [`func_train`](func_train.md) - a brush that moves along a path
- [`path_corner`](path_corner.md) - the stops of the path
- [`env_model`](env_model.md) - an animated model that stays in place

## Changes since 1.38

- `env_modeltrain` is new in SBO 2.0.0
