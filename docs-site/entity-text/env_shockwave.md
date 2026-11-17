An `env_shockwave` draws a ring that grows outward each time you trigger it, like the wave of a houndeye's attack. The
ring can be a cylinder, a torus or a flat disk, and the entity is removed after one use unless it is **Repeatable**.

## Attributes

- **Name** (`targetname`) - Triggering the entity draws the ring. See [Common keys](common-keys.md#targetname)
- **Position** (`m_iszPosition`) - Sets where the ring starts. It takes a [locus position](../guide/locus.md), so you
  can use a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain of
  triggers
    - If you leave this key empty, the ring starts at the `env_shockwave` itself
- **Sprite name** (`netname`) - Sets the sprite the ring is drawn with
    - If you leave this key empty, it is `sprites/shockwave.spr`
- **Color** (`rendercolor`) - Sets the color of the ring, as red, green and blue from 0 up to 255
- **Opacity** (`renderamt`) - Sets how opaque the ring is, from 0 for invisible up to 255 for opaque
- **Duration** (`m_iTime`) - Sets how long the ring lasts, in tenths of a second, so 10 is one second, up to 255
- **Final radius** (`m_iRadius`) - Sets the radius the ring grows to, in units
- **Wave height** (`m_iHeight`) - Sets how high the wave of the ring is, in units
- **Scroll rate** (`m_iScrollRate`) - Sets how fast the sprite moves along the ring, from 0 for still up to 255
- **Distortion** (`m_iNoise`) - Sets how much the edge of the ring jitters, from 0 for a clean ring up to 255
- **Frame rate** (`m_iFrameRate`) - Sets how fast the sprite animates, from 0 for still up to 255
- **Starting frame** (`m_iStartFrame`) - Sets the frame of the sprite the ring starts with
- **Type** (`m_cType`) - Picks the shape of the ring
    - Default (0) - A cylinder
    - Torus (19) - A ring that rolls outward
    - Disk (20) - A flat disk
    - Cylinder (21) - A ring that spreads out like a wall

## Flags

- **Centered** (1) - The ring starts at **Position**. Without this flag, it starts half the **Wave height** higher
- **Repeatable** (2) - The entity stays after it is used, so you can trigger it again. Without this flag, it removes
  itself after one use

## Notes

- If the entity can't find the position that **Position** names, nothing is drawn for that trigger
- Only players who can see the spot see the ring, and players who join later don't see a ring that has already
  played

## See also

- [`env_warpball`](env_warpball.md) - the flash and the lightning that Xen monsters appear in
- [`env_beam`](env_beam.md) - a beam between two entities or points

## Changes since 1.38

- `env_shockwave` is new in SBO 2.0.0
