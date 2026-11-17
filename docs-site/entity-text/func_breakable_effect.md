A `func_breakable_effect` plays the break of a [`func_breakable`](func_breakable.md) each time you trigger it: the
sound and the flying gibs of its material. Nothing breaks, because the brush is invisible and not solid.

## Attributes

- **Name** (`targetname`) - Triggering the entity plays the break. See [Common keys](common-keys.md#targetname)
- **Material type** (`material`) - Picks the material whose break sound plays and whose gibs fly, as on a
  `func_breakable`, and Unbreakable Glass breaks like Glass
    - Glass (0)
    - Wood (1)
    - Metal (2)
    - Flesh (3)
    - Cinder Block (4)
    - Ceiling Tile (5)
    - Computer (6)
    - Unbreakable Glass (7)
    - Rocks (8)
- **Gib Model** (`gibmodel`) - Sets a model for the gibs, which the entity uses instead of the gibs of the material
- **Custom number of gibs** (`m_iGibs`) - Sets how many gibs fly, up to 255. With 0, the game decides, and with -1,
  no gibs fly
- **At position** (`position`) - Sets where the gibs come out, and the sound always plays at the brush. It takes a
  [locus position](../guide/locus.md), so it can be a point such as `0 0 64`, the name of an entity, or `!activator`
  for the entity that started the chain of triggers
    - If you leave this key empty, the gibs come out of the middle of the brush

## Flags

- **Repeatable** (1) - The entity stays after it is used, so you can trigger it again. Without this flag, it removes
  itself after one use
- **Smoke trails on gibs** (8192) - The gibs trail smoke as they fly
- **Transparent gibs** (16384) - The gibs are drawn see-through

## Notes

- If **At position** can't be worked out, nothing plays that time
- Players who join later don't see gibs that have already flown

## See also

- [`func_breakable`](func_breakable.md) - a brush that breaks
- [`env_shooter`](env_shooter.md) - shoots a model or a sprite of your choice

## Changes since 1.38

- `func_breakable_effect` is new in SBO 2.0.0
