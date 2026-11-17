An `env_funnel` shows a large funnel of particles each time you trigger it, like the one in the resonance cascade of
Half-Life. The particles flow from all around into the center, and the entity is removed after one use unless it is
**Repeatable**.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows the funnel. See [Common keys](common-keys.md#targetname)
- **Position** (`message`) - Sets where the funnel shows. It takes a [locus position](../guide/locus.md), so you
  can use a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain
  of triggers
    - If you leave this key empty, the funnel is at the `env_funnel` itself
- **Particle sprite** (`netname`) - Sets the sprite the particles are drawn with
    - If you leave this key empty, it is `sprites/flare6.spr`

## Flags

- **Reverse** (1) - The particles flow out of the center instead of into it
- **Repeatable** (2) - The entity stays after it plays, so you can trigger it again. Without this flag, it removes
  itself after one use

## Notes

- If the entity can't find the position that **Position** names, nothing shows for that trigger

## See also

- [`env_warpball`](env_warpball.md) - the flash and the lightning that Xen monsters appear in
- [`env_quakefx`](env_quakefx.md) - particle effects from Quake
- [`env_particle`](env_particle.md) - particle effects from Aurora scripts

## Changes since 1.38

- You can use the new keys **Position** and **Particle sprite** and the new flag **Repeatable**
