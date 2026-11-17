An `env_beamtrail` draws a trail behind a moving entity, made of a sprite that fades out behind it. The trail grows
only while the entity moves.

While the entity is on, each player gets the trail whenever the target comes into their view, so players who join
later and players who come back to the area see it too.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns the trail on or off, as the
  [use type](../guide/trigger-modes.md) says, and turning it off removes the trails of its targets. See
  [Common keys](common-keys.md#targetname)
- **Entity to trail** (`target`) - Names the entity that leaves the trail, and every entity with this name gets one.
  With `!activator`, it is the entity that started the chain of triggers
    - If you leave this key empty, the trail follows the `env_beamtrail` itself
- **Sprite Name** (`netname`) - Sets the sprite the trail is drawn with
    - If you leave this key empty, it is `sprites/smoke.spr`
- **Brightness** (`renderamt`) - Sets how bright the trail is, from 1 for barely visible up to 255 for full
  brightness
- **Color** (`rendercolor`) - Sets the color of the trail, as red, green and blue from 0 up to 255
- **Width** (`armorvalue`) - Sets how wide the trail is, in tenths of a unit, so 10 is one unit
- **Fade time** (`health`) - Sets how many seconds each part of the trail stays before it fades out, up to 25.5

## Flags

- **Start off** (1) - The trail doesn't start with the map, but waits for a trigger. Without this flag, it starts
  when the map starts

## See also

- [`env_beam`](env_beam.md) - a beam between two entities or points
- [`locus_beam`](locus_beam.md) - a beam between positions that other entities work out

## Changes since 1.38

- `env_beamtrail` is new in SBO 2.0.0
