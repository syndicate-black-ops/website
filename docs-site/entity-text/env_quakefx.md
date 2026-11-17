---
description: "An env_quakefx plays a particle effect from Quake each time you trigger it, such as a tar explosion, a lava splash or a teleport splash."
---
An `env_quakefx` plays a particle effect from Quake each time you trigger it: a tar explosion, a lava splash, a
teleport splash, an explosion, an implosion or a burst of particles. The entity is removed after one use unless it is
**Repeatable**.

## Attributes

- **Name** (`targetname`) - Triggering the entity plays the effect. See [Common keys](common-keys.md#targetname)
- **Position** (`message`) - Sets where the effect plays. It takes a [locus position](../guide/locus.md), so you can
  use a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain of
  triggers
    - If you leave this key empty, the effect plays at the `env_quakefx` itself
- **Effect type** (`impulse`) - Picks the effect. Only Implosion and Particle Burst read the radius and duration
  keys, and only Particle Burst reads the color
    - Tar Explosion (4)
    - Lava Splash (10)
    - Teleport Splash (11)
    - Explosion (12)
    - Implosion (14) - Lines of particles that rush in toward the center
    - Particle Burst (122) - Particles in one color that fly out of the position
- **Particle Burst: color number** (`frags`) - With Particle Burst, sets the color, as a number of the game's color
  palette
- **Implosion/Particle Burst: radius** (`armortype`) - With Implosion or Particle Burst, sets the radius of the
  effect in units, and for Implosion, up to 255
- **Implosion/Particle Burst: duration** (`health`) - With Implosion or Particle Burst, sets how many seconds the
  effect lasts, up to 25.5
- **Implosion tracer count** (`armorvalue`) - With Implosion, sets how many lines of particles rush in, up to 255

## Flags

- **Repeatable** (1) - The entity stays after it plays, so you can trigger it again. Without this flag, it removes
  itself after one use

## Notes

- If the entity can't find the position that **Position** names, nothing plays for that trigger
- Players who join later don't see an effect that has already played

## See also

- [`env_particle`](env_particle.md) - particle effects from Aurora scripts
- [`env_funnel`](env_funnel.md) - a large funnel of particles
- [`env_explosion`](env_explosion.md) - an explosion with a fireball and damage

## Changes since 1.38

- `env_quakefx` is new in SBO 2.0.0
