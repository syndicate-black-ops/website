---
description: "A nuclear_explosion makes a huge explosion each time you trigger it, with a fireball, a mushroom cloud, a shock wave and blast damage."
---
A `nuclear_explosion` makes a huge explosion each time you trigger it, with a fireball, a mushroom cloud, a shock wave
ring, a glow and then an afterglow, as well as blast damage around it, a screen shake and the sound
`weapons/mortarhit.wav`.

## Attributes

- **Master** (`master`) - Names a [master](../guide/masters-and-states.md), and while the master is off, triggering
  the entity does nothing
- **Explosion size** (`v1`) - Sets the size of the main fireball in tenths of its normal size, from 0 up to 255, so 60
  draws it 6 times as large
- **Explosion opacity** (`v2`) - Sets how opaque the main fireball is, from 0 for invisible up to 255 for opaque
- **Smoke size** (`v3`) - Sets the size of the mushroom cloud in tenths, from 0 up to 255
- **Disc lifetime** (`v4`) - Sets how long the shock wave disc lasts in tenths of a second, from 0 up to 255, which
  also sets how fast it grows
- **Disc width** (`v5`) - Sets the width of the shock wave disc in tenths, from 0 up to 255
- **Disc brightness** (`v6`) - Sets how bright the shock wave disc is, from 0 up to 255
- **Disc texture scroll** (`v7`) - Sets how fast the disc's texture scrolls, from 0 up to 255, which makes no visible
  difference with the normal white sprite
- **Glow lifetime** (`v8`) - Sets how long the glow of the fireball lasts in tenths of a second, from 0 up to 255
- **Glow size** (`v9`) - Sets the size of the glow in tenths, from 0 up to 255
- **Glow brightness** (`v10`) - Sets how bright the glow is, from 0 up to 255
- **Explosion damage** (`v11`) - Sets the blast damage at the center, which falls off with distance
- **Explosion radius** (`v12`) - Sets how far the blast damage reaches, in units
- **Shake radius** (`v13`) - Sets how far away players feel the screen shake, in units
- **Afterglow lifetime** (`v14`) - Sets how long the afterglow lasts in tenths of a second, from 0 up to 255, and the
  afterglow follows when the glow ends
- **Afterglow size** (`v15`) - Sets the size of the afterglow in tenths, from 0 up to 255
- **Afterglow brightness** (`v16`) - Sets how bright the afterglow is, from 0 up to 255

## See also

- [`env_explosion`](env_explosion.md) - a normal explosion
- [`env_shake`](env_shake.md) - shakes the view of players

## Changes since 1.38

- Fixed nuclear explosions never showing their afterglow. The game set up the afterglow but never gave it a time to
  start. This was a bug in SBO 1.38
