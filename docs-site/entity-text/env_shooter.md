---
description: "An env_shooter shoots a model or a sprite of your choice each time you trigger it, as gibs that bounce or stick, or as shots that fly."
---
An `env_shooter` shoots a model or a sprite of your choice each time you trigger it, as gibs that bounce or stick, or
as shots that fly and can fire targets when they hit something.

## Attributes

- **Name** (`targetname`) - Triggering the entity shoots its gibs. See [Common keys](common-keys.md#targetname)
- **Model or Sprite name** (`shootmodel`) - Sets the model (`.mdl`) or the sprite (`.spr`) it shoots. A model with
  several submodels gives each gib one of them at random
    - If you leave this key empty, or use an editor model or a file the server doesn't have, the entity is removed
      when the map starts
- **Material Sound** (`shootsounds`) - Picks the material the gibs are made of, so they play its sounds when they
  hit something
    - None (-1) - The gibs make no sound
    - Glass (0)
    - Wood (1)
    - Metal (2)
    - Flesh (3)
    - Concrete (4)
- **Gib Scale** (`scale`) - Sets the size of each gib or shot, where 1 is the size of the model or the sprite, 2 is
  double and 0.5 is half
    - If you leave this key empty, the gibs have their normal size
- **Gib Skin** (`skin`) - Sets the skin of each gib, for a model with several skins, where 0 is the first
- **Gib Blood Color** (`bloodcolor`) - Sets the blood the gibs leave on the surfaces they hit
    - Default (0) - The gibs don't bleed
    - Human (247) - Red blood
    - Alien (195) - Yellow blood
- **Start gib body** (`start_gib_body`) - Sets the first submodel a gib can take, so the gibs skip the submodels
  before it and take one from this one on, at random
- **Gib/Shot physics** (`m_iPhysics`) - Sets how each piece moves. A gib is a piece of debris, and a shot is a
  sprite or model that flies and fires the collision targets when it hits something
    - Bouncy gib (0) - A gib that bounces until it comes to rest
    - Sticky gib (1) - A gib that sticks to the first surface it hits
    - Noclip shot (2) - A shot that flies through walls and everything else, so it never fires the collision targets
    - Fly shot (3) - A shot that flies straight, without gravity
    - Fly & bounce shot (4) - A shot that flies straight and bounces off surfaces
    - Arc shot (5) - A shot that falls in an arc
    - Arc & bounce shot (6) - A shot that falls in an arc and bounces off surfaces
- **Start frame** (`frame`) - Sets the frame the sprite of a shot starts on, where 0 is the first. Gibs ignore it
- **Framerate** (`framerate`) - Sets how many frames per second the sprite of a shot plays. Gibs ignore it
    - If you leave this key empty or set 0, the shot shows one frame
- **Bounce friction** (`m_fFriction`) - Sets how much speed a bounce shot loses when it bounces, from 0 for none,
  so it bounces back at full speed, up to 1, where it doesn't bounce and slides along the surface
- **Fire on collision (shot)** (`m_iszTouch`) - Names the entities a shot triggers each time it touches something,
  at most every 0.1 seconds, with the shot as the [activator](../guide/entity-triggering.md#target-selectors)
- **Fire on collision (what it hit)** (`m_iszTouchOther`) - Names the entities a shot triggers each time it touches
  something, at most every 0.1 seconds, with what it hit as the activator. When it hits a wall or the floor of the
  map, the shot at the point of the hit is the activator
- **Shot size** (`m_vecSize`) - Sets the size of the box of a shot, as X Y Z in units
    - If you leave this key empty, the shot is a point

## Flags

- **Repeatable** (1) - The entity stays after it has shot all its gibs, so you can trigger it again. Without this
  flag, it is removed after the last gib
- **Don't wait till land** (4) - Each gib fades out when its **Gib Life** ends, even while it still flies. Without
  this flag, it waits until it lands
- **Start instantly** (8) - The first gib flies at the moment you trigger the entity. Without this flag, it flies a
  moment later

## Notes

- The entity reads **Gib Velocity**, **Position** and **Direction and speed** again for each gib, for the entity that
  started the chain of triggers
- If the entity can't find the value of one of those keys, it skips that gib, but the gib still counts toward
  **Number of Gibs**
- Once the map runs, [`trigger_changevalue`](trigger_changevalue.md) and [`trigger_copyvalue`](trigger_copyvalue.md)
  can't change **Model or Sprite name**, so the entity keeps shooting its model, and with `developer 1` set in the
  console, the console says why

## See also

- [`gibshooter`](gibshooter.md) - shoots body gibs
- [`env_explosion`](env_explosion.md) - an explosion with a fireball and damage
- [env_shooter on TWHL](https://twhl.info/wiki/page/env_shooter) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Position**, **Direction and speed**, **Fire on spawn**, **Gib Blood Color**, **Start gib
  body**, **Gib/Shot physics**, **Start frame**, **Framerate**, **Bounce friction**, both **Fire on collision** keys
  and **Shot size**, and the new flags **Don't wait till land** and **Start instantly**
- **Gib Velocity** also takes a range or the name of a `calc_` entity
