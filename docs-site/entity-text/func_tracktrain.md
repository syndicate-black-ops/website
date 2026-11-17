---
description: "A func_tracktrain is a train that players can drive along a track of path_track entities, or that moves by itself."
---
A `func_tracktrain` is a train that players drive along a track of [`path_track`](path_track.md) entities from a
[`func_traincontrols`](func_traincontrols.md) on it, or that moves by itself at its **Initial speed**. It turns and
tilts with the track.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the train. See
  [Common keys](common-keys.md#targetname)
- **First stop target** (`target`) - Names the first `path_track`, where the train starts
- **Sound** (`sounds`) - Picks the rail sound the train loops while it moves, which goes up in pitch as the train goes
  faster, and **Custom move sound** replaces it. With None and no custom move sound, the train plays no move, start
  or brake sound
    - None (0)
    - Rail 1 (1)
    - Rail 2 (2)
    - Rail 3 (3)
    - Rail 4 (4)
    - Rail 6 (5)
    - Rail 7 (6)
- **Distance between the wheels** (`wheels`) - Sets the distance between the front and the back wheels of the train,
  in units, and the train looks this far ahead on the track to turn and tilt along it
    - If you leave this key empty or set 0, a moving train looks 100 units ahead, but where it starts, it isn't
      turned along the track
- **Height above track** (`height`) - Sets how high the origin of the train rides above the `path_track` points, in
  units
    - If you leave this key empty, it is 0 and the origin rides on the path
- **Initial speed** (`startspeed`) - Sets the speed the train has when the map starts, in units per second, and 0
  means it stands still
- **Speed** (`speed`) - Sets the top speed of the train, in units per second, and 0 means 100
- **Damage on crush** (`dmg`) - Sets the damage dealt each frame to anything that blocks the train, and the speed the
  blocker is pushed away at. Riders aren't hurt, and 0 deals no damage
- **Volume** (`volume`) - Sets how loud the sounds of the train are, from 1 for quiet up to 10 for full volume, and 0
  means 10. For no sound, set **Sound** to None
- **Bank angle on turns** (`bank`) - Sets how far the train leans into turns, in degrees
- **Sound radius** (`soundradius`) - Sets how far the move, start and brake sounds carry
    - Small (-2) - Up to about 500 units away
    - Medium (-1) - Up to about 800 units away
    - Default (0) - Up to about 1250 units away
    - Huge (1) - Up to about 2000 units away
    - Enormous (2) - Up to about 4000 units away
    - Play Everywhere (3) - Anywhere on the map, and the sounds are as loud far away as close by
- **Custom move sound** (`custommovesnd`) - Sets a sound file played instead of the **Sound** choice, with the pitch
  set by the speed
- **Custom brake sound** (`customstopsnd`) - Sets the sound file of the brake
    - If you leave this key empty, it is `plats/ttrain_brake1.wav`

## Flags

- **No Pitch** (1) - The train doesn't tilt up and down with the track, so it stays level
- **No User Control** (2) - Players can't drive the train
- **Forwards Only** (4) - Players can only drive the train forward, not in reverse
- **Passable** (8) - Players and objects pass through the train

## Notes

- Neither [`trigger_changevalue`](trigger_changevalue.md) nor [`trigger_copyvalue`](trigger_copyvalue.md) can change
  how fast a train moves, because the train keeps its top speed from when the map loads, and
  [`train_setspeed`](train_setspeed.md) is the entity that sets a train's speed. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`path_track`](path_track.md) - the points of a track
- [`func_traincontrols`](func_traincontrols.md) - the place where a player drives the train
- [`func_trackchange`](func_trackchange.md) - moves the train to another track
- [`func_train`](func_train.md) - a brush that moves along a path of `path_corner` entities
- [func_tracktrain on TWHL](https://twhl.info/wiki/page/func_tracktrain) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Sound radius**, **Custom move sound** and **Custom brake sound**
