An `env_beam` draws a beam between two entities or two points, and it can also draw the beam as a ring.

With a **Life** of 0, the beam stays on and follows its entities when they move. With a **Life** above 0, the beam
strikes again and again: each strike lasts **Life** seconds, and the next one comes **Strike again time** seconds
after it.

![Three env_beams that strike again and again: a straight beam, a lightning bolt with noise and a wider beam with Random Strike](../../assets/img/clips/env-beam-styles.webp)

*A straight beam, a lightning bolt and a wider beam with Random Strike*

## Attributes

- **Name** (`targetname`) - Triggering the entity turns the beam or its strikes on and off. Without a name, the
  beam is always on. See [Common keys](common-keys.md#targetname)
- **Brightness** (`renderamt`) - Sets how bright the beam is, from 1 for barely visible up to 255 for full
  brightness
    - If you leave this key empty, it is 0 and you can't see the beam
- **Beam Color** (`rendercolor`) - Sets the color of the beam, as red, green and blue from 0 up to 255
- **Radius** (`Radius`) - Sets how far, in units, the beam reaches for a random spot to strike when it has no
  **Ending Entity**. Without a **Start Entity** either, it strikes between two surfaces within this distance of the
  `env_beam`
    - If you leave this key empty, it is 0 and the beam finds no spot to strike
- **Life** (`life`) - Sets how many seconds each strike lasts, and 0 keeps the beam on until you turn it off
    - If you leave this key empty, it is 0 and the beam stays on
- **Width of beam** (`BoltWidth`) - Sets how thick the beam is, in tenths of a unit from 0 up to 255, so 10 is one
  unit
    - If you leave this key empty, it is 0 and you can't see the beam
- **Amount of noise** (`NoiseAmplitude`) - Sets how much the beam jitters, from 0 for a straight line up to 255 for
  a very jagged one
- **Sprite Name** (`texture`) - Sets the sprite drawn along the beam
    - If you leave this key empty, the entity is removed when the map starts
- **Texture Scroll Rate** (`TextureScroll`) - Sets how fast the sprite moves along the beam, from 0 for still up to
  100 for fast
    - If you leave this key empty, it is 0 and the sprite doesn't move
- **Frames per 10 seconds** (`framerate`) - Sets how fast the sprite animates, as the number of frames it shows in
  10 seconds, and 0 means it doesn't animate
- **Starting Frame** (`framestart`) - Sets the frame of the sprite the beam starts with
- **Strike again time** (`StrikeTime`) - With a **Life** above 0, sets how many seconds pass between the end of one
  strike and the start of the next. With **Random Strike**, it is the longest time, and each wait is random
    - If you leave this key empty, it is 0 and each strike follows the last one at once
- **Damage / second** (`damage`) - Sets how much damage the beam deals per second to what it touches. A beam with a
  **Life** above 0 deals this amount once at each strike

## Flags

- **Start On** (1) - A beam with a **Name** is on when the map starts. A beam without a name is always on
- **Toggle** (2) - With a **Life** above 0, every trigger starts or stops the strikes. Without this flag, only the
  first trigger starts or stops them, and later triggers do nothing
- **Random Strike** (4) - The time between strikes is random, from 0 up to **Strike again time**
- **Ring** (8) - The beam is drawn as a ring, and the line from the **Start Entity** to the **Ending Entity** goes
  across its middle. Both must be entities with a model, such as brush entities or monsters, or the ring isn't drawn
- **StartSparks** (16) - Sparks fly at the start of the beam each time it strikes or turns on
- **EndSparks** (32) - Sparks fly at the end of the beam each time it strikes or turns on
- **Decal End** (64) - A beam that deals damage leaves a large bullet-hole decal where it hits a wall or a brush
  entity
- **Shade Start** (128) - A beam with a **Life** of 0 fades out toward its start. If you set both shade flags, only
  this one works
- **Shade End** (256) - A beam with a **Life** of 0 fades out toward its end
- **Draw Solid** (512) - A beam with a **Life** of 0 is drawn solid, like a ribbon. Without this flag, its colors
  are added to what is behind it
- **Draw Sine** (1024) - A beam with a **Life** of 0 is drawn as a wave
- **No Camera Punch** (4096) - A player the beam hurts doesn't have their view jerk

## See also

- [`env_laser`](env_laser.md) - a beam that ends where it hits a wall
- [`locus_beam`](locus_beam.md) - a beam between positions that other entities work out
- [`env_beamtrail`](env_beamtrail.md) - a trail behind a moving entity
- [env_beam on TWHL](https://twhl.info/wiki/page/env_beam) - the Half-Life entity

## Changes since 1.38

- You can use the new flags **Draw Solid**, **Draw Sine** and **No Camera Punch**
