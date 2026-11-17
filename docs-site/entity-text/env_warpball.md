---
description: "An env_warpball plays the effect Xen monsters appear in each time you trigger it: a glowing sprite, green lightning, sounds and a shake."
---
An `env_warpball` plays the effect that Xen monsters appear in each time you trigger it: a glowing sprite, green
lightning to the walls around it, two sounds, a shake of the view and, with a flag, a flash of light.

A [`monstermaker`](monstermaker.md) that names it in its **Warpball** key plays it where each monster appears.

## Attributes

- **Name** (`targetname`) - Triggering the entity plays the effect. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger each time the entity plays the effect, but not when a `monstermaker` plays
  it. See [Common keys](common-keys.md#target)
- **Sprite Name** (`model`) - Sets the sprite of the effect
- **Shake Amplitude** (`amplitude`) - Sets how hard the view shakes, from 0 up to 16
    - If you leave this key empty or set 0, it is 6
- **Shake Duration** (`duration`) - Sets how many seconds the view shakes
    - If you leave this key empty or set 0, it is 1
- **Shake Frequency** (`frequency`) - Sets how fast the view shakes, from 0.1 for a single jolt up to 255 for a fast
  rumble
    - If you leave this key empty or set 0, it is 160
- **Shake and Beam Radius** (`radius`) - Sets how far, in units, the lightning reaches and the shake is felt
- **Sprite Scale** (`scale`) - Sets the size of the sprite, where 1 is its own size, and it also sets the size of the
  flash of light
- **Sprite Framerate** (`framerate`) - Sets how many frames per second the sprite plays
    - If you leave this key empty or set 0, it is 12
- **Warp position** (`warp_target`) - Sets where the effect plays. It takes a [locus position](../guide/locus.md), so
  you can use a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain
  of triggers
    - If you leave this key empty, the effect plays at the `env_warpball` itself
- **Damage delay** (`damage_delay`) - With **Kill center**, sets how many seconds pass between the effect and the
  damage
- **Beam color** (`beamcolor`) - Sets the color of the lightning, as red, green and blue from 0 up to 255
    - If you leave this key empty or set `0 0 0`, it is green, `20 243 20`
- **Max beam count** (`beamcount`) - Sets the most bolts of lightning, up to 64, and each time, the effect draws
  between half of them and all of them
- **Custom sound 1** (`noise1`) - Sets the first sound
    - If you leave this key empty, it is `debris/beamstart2.wav`
- **Custom sound 2** (`noise2`) - Sets the second sound
    - If you leave this key empty, it is `debris/beamstart7.wav`, but only when **Custom sound 1** is empty too
- **Sound volume** (`volume`) - Sets how loud the sounds are, from above 0 up to 1 for full volume
    - If you leave this key empty or set 0, it is 1
- **AI Sound type** (`aisound`) - Picks a sound that only monsters within the radius hear
    - No sound (0) - Monsters hear nothing
    - Combat (1) - Draws monsters in
    - Danger (32) - Makes monsters run
- **AI Sound duration** (`aisound_duration`) - Sets how many seconds monsters can hear the AI sound
    - If you leave this key empty or set 0, it is 0.3
- **Sprite 2 Name** (`model2`) - Sets a second sprite played with the first, such as `sprites/xflare1.spr`
- **Sprite 2 color** (`rendercolor2`) - Sets the color of the second sprite
    - If you leave this key empty, it has the color of the first sprite
- **Sprite 2 brightness** (`renderamt2`) - Sets the brightness of the second sprite, from 0 up to 255
    - If you leave this key empty or set 0, it has the brightness of the first sprite
- **Sprite 2 scale** (`scale2`) - Sets the size of the second sprite, where 1 is its own size
    - If you leave this key empty or set 0, it has the size of the first sprite
- **Sprite 2 framerate** (`framerate2`) - Sets how many frames per second the second sprite plays
    - If you leave this key empty or set 0, it plays at the speed of the first sprite

## Flags

- **Remove on fire** (1) - The entity is removed after it plays once
- **Kill center** (2) - The effect deals 300 shock damage to everything within 48 units of its center
- **No screen shake** (4) - The effect doesn't shake the view
- **Dynamic light** (8) - The effect makes a short flash of light in the color of the sprite
- **No sounds** (16) - The effect plays no sound

## Notes

- The lightning goes from the center to the walls within the radius, and in open space, a few bolts go out to half
  the radius instead
- With the render mode Normal, the sprite is drawn as Glow, with the render FX Normal it is drawn as No dissipation,
  and the FX color `0 0 0` gives the green `77 210 130`
- The damage of **Kill center** comes from the `env_warpball` itself, so nobody gets the kill
- Players who join later don't see an effect that has already played
- Once the map runs, [`trigger_changevalue`](trigger_changevalue.md) and [`trigger_copyvalue`](trigger_copyvalue.md)
  can't change **Sprite 2 Name**, so the effect keeps its sprite, and with `developer 1` set in the console, the
  console says why

## See also

- [`monstermaker`](monstermaker.md) - its **Warpball** key plays an `env_warpball` where each monster appears
- [`env_shockwave`](env_shockwave.md) - a ring that grows outward
- [`env_beam`](env_beam.md) - a beam between two entities or points

## Changes since 1.38

- `env_warpball` is new in SBO 2.0.0
