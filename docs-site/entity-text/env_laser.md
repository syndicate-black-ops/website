An `env_laser` fires a laser beam from its position at a target entity. The beam stops at the first wall, player or
monster in the way, and it can hurt what it hits and show a sprite at each end.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the laser on or off, as the
  [use type](../guide/trigger-modes.md) says. Without a name, the laser is always on. See
  [Common keys](common-keys.md#targetname)
- **Target of Laser** (`LaserTarget`) - Names the entity the laser points at, and when several entities have this
  name, it picks one of them at random every 0.1 seconds
    - If you leave this key empty, the laser points at the point `0 0 0` of the map
- **Brightness** (`renderamt`) - Sets how bright the beam and its sprites are, from 1 for barely visible up to 255
  for full brightness
    - If you leave this key empty, it is 0 and you can't see the laser
- **Beam Color** (`rendercolor`) - Sets the color of the beam and its sprites, as red, green and blue from 0 up to
  255
- **Width of beam** (`width`) - Sets how wide the beam is, in tenths of a unit from 0 up to 255, so 10 is one unit
    - If you leave this key empty, it is 0 and you can't see the beam
- **Amount of noise** (`NoiseAmplitude`) - Sets how much the beam jitters, from 0 for a straight beam up to 255 for a
  very jagged one
- **Sprite Name** (`texture`) - Sets the sprite the beam is drawn with
    - If you leave this key empty, the entity is removed when the map starts
- **Start Sprite** (`StartSprite`) - Sets a sprite shown at the start of the laser while it is on
- **End Sprite** (`EndSprite`) - Sets a sprite shown where the beam ends while it is on
- **Texture Scroll Rate** (`TextureScroll`) - Sets how fast the sprite moves along the beam, from 0 for still up to
  100 for fast
    - If you leave this key empty, it is 0 and the sprite doesn't move
- **Starting Frame** (`framestart`) - Sets the frame of the sprite the beam is drawn with
- **Damage / second** (`damage`) - Sets how much damage per second the beam deals to what it hits. A player takes
  more where the beam crosses them: twice as much on the chest, three times on the stomach and ten times on the
  head
    - If you leave this key empty, it is 0 and the beam deals no damage

## Flags

- **Start On** (1) - A laser with a **Name** is on when the map starts. A laser without a name is always on
- **StartSparks** (16) - Sparks fly at the start of the beam
- **EndSparks** (32) - Sparks fly at the end of the beam
- **Decal End** (64) - The laser keeps leaving large bullet-hole decals where it hits a wall or a brush entity, ten
  times a second, even when it deals no damage
- **No Camera Punch** (4096) - A player the laser hurts doesn't have their view jerk

## Notes

- If the laser is removed, for example by a **KillTarget**, its sprites are removed with it

## See also

- [`env_beam`](env_beam.md) - a beam between two entities or points
- [`func_tanklaser`](func_tanklaser.md) - a gun that fires a laser
- [env_laser on TWHL](https://twhl.info/wiki/page/env_laser) - the Half-Life entity

## Changes since 1.38

- You can use the new key **Start Sprite** and the new flag **No Camera Punch**
- A removed laser takes its sprites with it. In SBO 1.38, the end sprite stayed behind
