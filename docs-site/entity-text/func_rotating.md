A `func_rotating` keeps turning around its origin, set with an origin brush, such as a fan, a wheel or a gear. It can
play a sound while it turns and hurt what touches it.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops it, and **Obey Trigger Mode** sets how. See
  [Common keys](common-keys.md#targetname)
- **Rotation Speed** (`speed`) - Sets how fast it turns, in degrees per second, and 0 means it doesn't turn
- **Volume** (`volume`) - Sets how loud its sound is, from 0 for silent up to 10 for full volume
- **Friction** (`fanfriction`) - With **Spin up with acceleration**, sets how fast it speeds up and slows down:
  every 0.1 seconds, it gains or loses this percent of its **Rotation Speed**, so 100 is at once and low values
  take longer. With 0, it is 100
- **Fan Sounds** (`sounds`) - Picks the sound it loops while it turns, and the pitch goes up and down as it speeds up
  and slows down. A sound file in **WAV Name** replaces it
    - No Sound (0)
    - Fast Whine (1)
    - Slow Rush (2)
    - Medium Rickety (3)
    - Fast Beating (4)
    - Slow Smooth (5)
- **WAV Name** (`message`) - Sets a sound file that loops while it turns, instead of **Fan Sounds**. With a spin up,
  its pitch and volume rise and fall with the speed
- **X Y Z - Move here after lighting** (`spawnorigin`) - Sets a position, as X Y Z, that the entity moves to when the
  map starts, after the map compiler has lit it where you built it, and `0 0 0` leaves it where it is
- **Damage inflicted when blocked** (`dmg`) - Sets the damage to anything that blocks it, each time it pushes against
  it, and 0 deals no damage
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how a trigger starts and stops it
    - No (0) - Every trigger starts or stops it, as in Half-Life
    - Yes (1) - On starts it, Off stops it and Toggle switches it, so On while it turns and Off while it stands still
      do nothing

## Flags

- **Start ON** (1) - It starts to turn about 1.5 seconds after the map starts. Without this flag, it waits for a
  trigger
- **Reverse Direction** (2) - It turns the other way
- **X Axis** (4) - It turns around the X axis instead of the vertical axis
- **Y Axis** (8) - It turns around the Y axis instead of the vertical axis
- **Spin up with acceleration** (16) - It speeds up and slows down step by step when it starts or stops, at the rate
  that **Friction** sets, instead of starting and stopping at once
- **Fan Pain** (32) - Touching it hurts, with damage of its turning speed divided by 10, and pushes the toucher away
- **Not Solid** (64) - Players, monsters and shots pass through it
- **Small Radius** (128) - Players hear its sound up to about 500 units away
- **Medium Radius** (256) - Players hear its sound up to about 800 units away
- **Large Radius** (512) - Players hear its sound up to about 1250 units away. This flag is set by default, and the
  entity also uses this radius when no radius flag is set

## Notes

- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Rotation
  Speed** while it spins, it spins at the new speed at once, and a speed of 0 stops it and its sound. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`func_door_rotating`](func_door_rotating.md) - a door that turns
- [`func_pendulum`](func_pendulum.md) - a brush that swings back and forth
- [func_rotating on TWHL](https://twhl.info/wiki/page/func_rotating) - the Half-Life entity

## Changes since 1.38

- You can use the new key **Obey Trigger Mode**
- **Volume** works, where in SBO 1.38 every `func_rotating` played at full volume. The game read the key only as
  `Volume` with a capital V, but the editor writes `volume`, so the value was never used
