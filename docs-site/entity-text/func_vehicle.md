A `func_vehicle` is a vehicle from Counter-Strike that a player steers with their move keys. A
[`func_vehiclecontrols`](func_vehiclecontrols.md) brush marks where the driver stands, and a player inside that space
takes the wheel with their use key.

After three bounces in a row against a wall, the vehicle stops instead of bouncing back again.

## Attributes

- **Name** (`targetname`) - Gives the vehicle a name that other entities can use to find it. See
  [Common keys](common-keys.md#targetname)
- **First stop target** (`target`) - Names the [`path_track`](path_track.md) the vehicle starts on. When the map
  starts, it is placed there, **Height above track** higher, facing the next `path_track`
- **Sound** (`sounds`) - Picks the engine sound the vehicle plays while it moves, which goes up in pitch with the
  speed
    - Vehicle 1 (1)
    - Vehicle 2 (2)
    - Vehicle 3 (3)
    - Vehicle 4 (4)
    - Vehicle 6 (5)
    - Vehicle 7 (6)
- **Length of the vehicle** (`length`) - Sets the length of the vehicle in units, front to back, which sets where it
  checks for walls and what it runs over
- **Width of the vehicle** (`width`) - Sets the width of the vehicle in units, which sets where it checks for walls
  and what it runs over
- **Height above track** (`height`) - Sets how many units above the first `path_track` the origin of the vehicle is
  placed. The vehicle also looks this far plus 48 units down for the ground it tilts with
- **Initial speed** (`startspeed`) - Sets the speed the vehicle has when the map starts, in units per second, and 0
  means it stands still
- **Speed** (`speed`) - Sets the top speed forward, in units per second, and 0 means 165. Backwards, it reaches 0.35
  times this, unless you set **Custom reverse speed**
- **Acceleration** (`acceleration`) - Sets how quickly the vehicle gains speed when the driver speeds up, from 1 for
  the slowest up to 10 for the fastest, and a value below 1 works like 1. Default 5
- **Push-away speed** (`dmg`) - Sets the speed, in units per second, at which something that blocks the vehicle is
  thrown away from it, plus 300 upward. It isn't damage, but something caught in front of, behind or beside the
  vehicle takes 150 crush damage
- **Volume** (`volume`) - Sets how loud the engine and brake sounds are, from 1 for quiet up to 10 for full volume,
  and 0 means 10
- **Custom reverse speed** (`reverse_speed`) - Sets the top speed backwards, in units per second
    - If you leave this key empty or set 0, it is 0.35 times **Speed**
- **Custom deceleration per 0.1 seconds** (`deceleration`) - Sets how much speed the vehicle loses every 0.1 seconds
  while nobody presses forward or back, and 0 means 20
- **Stop sound at halt** (`stop_sound_at_halt`) - Sets whether the engine goes quiet while the vehicle stands still
    - No (0) - The engine sound keeps playing
    - When stopped and no driver (1) - The engine sound stops while the vehicle stands still with nobody at the
      wheel, and starts again when the vehicle moves
- **Custom brake sound** (`brake_sound`) - Sets a sound that plays when the engine starts, for every **Sound**
    - If you leave this key empty, it is `plats/vehicle_brake1.wav`, but only for the sounds "Vehicle 1" to "Vehicle
      4"
- **Custom ignition sound** (`ignition_sound`) - Sets a sound that plays when a player takes the wheel
    - If you leave this key empty, it is `plats/vehicle_ignition.wav`
- **Touch proxy name** (`touch_proxy_name`) - Lets the vehicle set off triggers, which a vehicle doesn't touch by
  itself. With a name here, a small point entity of this name rides at the origin of the vehicle and touches
  triggers: a [`trigger_multiple`](trigger_multiple.md) or
  a [`trigger_once`](trigger_once.md) with **Everything else**, and a [`trigger_inout`](trigger_inout.md) or a
  [`trigger_jump`](trigger_jump.md) with **Everything else** or this name in its entity filter. It is one more entity
  for each vehicle, removed with its vehicle
- **Minimum light level** (`_minlight`) - Sets the lowest light level the map compiler gives the faces of the
  vehicle, from 0 up to 1, so it never turns fully dark

## Flags

- **No Pitch** (1) - The vehicle starts level, so its start direction ignores the height difference to the next
  `path_track`
- **No User Control** (2) - Players can't drive the vehicle
- **Passable** (8) - Players, monsters and shots pass through the vehicle

## Notes

- The sound keys and **Touch proxy name** are read when the map starts, so a
  [`trigger_changevalue`](trigger_changevalue.md) that changes them later has no effect

## See also

- [`func_vehiclecontrols`](func_vehiclecontrols.md) - the place where a player drives the vehicle
- [`func_tracktrain`](func_tracktrain.md) - a train that players drive along a track

## Changes since 1.38

- `func_vehicle` is new in SBO 2.0.0
