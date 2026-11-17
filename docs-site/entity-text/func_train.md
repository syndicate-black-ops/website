A `func_train` moves along a path of [`path_corner`](path_corner.md) entities, from one to the next, and waits at each
one as long as its **Wait here** says. The middle of the brush goes to each `path_corner`, and without a **Name**, the
train starts by itself.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the train, and **Obey Trigger Mode** sets how. See
  [Common keys](common-keys.md#targetname)
- **Fire On Start** (`fireonstart`) - Names the entities to trigger each time the train sets off toward the next `path_corner`, at
  every corner
- **Fire On Stop** (`fireonstop`) - Names the entities to trigger each time the train stops: at a corner with a wait, at the end of
  the path, or when you stop it
- **First stop target** (`target`) - Names the first `path_corner`, where the train starts when the map starts and
  moves on along the path from there
- **Speed** (`speed`) - Sets how fast the train moves, in units per second, and 0 means 100. A `path_corner` with a
  **New Train Speed** changes it
- **Angular Velocity** (`avelocity`) - Makes the train turn all the time, as three speeds in degrees per second for
  the turns around the Y, the Z (vertical) and the X axes
- **Damage on crush** (`dmg`) - Sets the damage dealt to anything that blocks the train, at most every half second
    - If you leave this key empty or set 0, it is 2, unless the train has **No default damage**
- **Contents** (`skin`) - With **Not solid**, sets what the brush is filled with: -3 is water, -4 is slime, -5 is
  lava and 0 is a normal brush
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how a trigger starts and stops the train
    - No (0) - Every trigger starts or stops it, as in Half-Life
    - Yes (1) - On starts it, Off stops it and Toggle switches it, so On while it moves and Off while it stands still
      do nothing
- **Move sound pitch** (`soundpitch`) - Sets the pitch of the move sound, where 100 is normal
    - If you leave this key empty or set 0, the pitch is normal

## Flags

- **Initially On** (4) - A train with a **Name** starts moving when the map starts. A train without a name always
  does
- **Not solid** (8) - Players, monsters and shots pass through the train
- **No default damage** (64) - A **Damage on crush** of 0 deals no damage, instead of the default 2

## Notes

- When a trigger stops the train, its move sound stops and its stop sound plays
- From a `path_corner` with **New Train rot. Speed**, the train turns around its vertical axis while it moves

## See also

- [`path_corner`](path_corner.md) - the stops of the path
- [`func_tracktrain`](func_tracktrain.md) - a train that players drive along a track
- [`env_modeltrain`](env_modeltrain.md) - a model that moves along a path
- [func_train on TWHL](https://twhl.info/wiki/page/func_train) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Obey Trigger Mode**, **Fire On Start**, **Fire On Stop**, **Move sound pitch**, **Sound
  radius** and the custom move and stop sounds, and the new flags **Initially On** and **No default damage**
- A train that a trigger stops also stops its move sound. In SBO 1.38, the sound kept looping until the train moved
  again
- Fixed the New Train rot. Speed key of `path_corner` being ignored. The game never read the key
