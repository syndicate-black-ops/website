---
description: "An env_blood sprays blood each time you trigger it, as a splash or as a stream of drops, and can leave a blood stain."
---
An `env_blood` sprays blood each time you trigger it, either as a splash or as a stream of drops, and it can leave a
blood stain on the surface the blood flies toward.

## Attributes

- **Name** (`targetname`) - Triggering the entity sprays the blood. See [Common keys](common-keys.md#targetname)
- **Blood Color** (`color`) - Picks the color of the blood drops and stains. You can also type any color number of
  the game's palette from 2 up to 255, and any other number gives red
    - Red (Human) (0) - Red blood
    - Yellow (Alien) (1) - Yellow blood
    - Darker Red (70)
    - Bright Yellow (192)
    - Green (244)
    - White (12)
    - Grey (5)
    - Brown (25)
    - Olive (59)
    - Grey green (178)
    - Orange (92)
    - Goldish (106)
    - Peach (124)
    - Magenta (145)
    - Tan (161)
    - Blue (210)
    - Darker Blue (214)
    - Bluish (43)
    - If you leave this key empty, the blood is black, and its decals are the yellow alien kind
- **Initial position** (`target`) - Sets where the blood appears. It takes a [locus position](../guide/locus.md), so
  you can use a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain
  of triggers. The entity ignores it with **On Player**
    - If you leave this key empty, the blood appears at the `env_blood` itself
- **Direction** (`netname`) - Sets the direction the blood flies in. It takes a [locus vector](../guide/locus.md), so
  you can use three numbers such as `0 0 1` for up, or the name of an entity, which gives the direction that entity
  moves in.
  The entity ignores it with **Random Direction**
    - If you leave this key empty, the blood flies in the direction of the entity's **Pitch Yaw Roll**
- **Amount of blood** (`amount`) - Sets how much blood it sprays, as the damage it stands for, so a bigger number
  makes a bigger splash or a stronger stream, up to 255
    - If you leave this key empty, it is 0, so no drops appear and no decal is made, but with **Blood Stream** a
      stream still comes out, with no force

## Flags

- **Random Direction** (1) - The blood flies in a random direction each time
- **Blood Stream** (2) - Sprays a stream of blood drops instead of a single splash
- **On Player** (4) - The blood appears at the eyes of the player who triggered it, or at the first player when no
  player triggered it
- **Spray decals** (8) - Leaves a blood stain on the first surface in the blood's direction, up to twice
  **Amount of blood** units away

## Notes

- If the entity can't find the position or the direction that these keys name, for example because a key names an
  entity that doesn't exist, no blood appears for that trigger

## See also

- [`env_decal`](env_decal.md) - sprays a decal such as a blood stain or a scorch mark
- [Locus system](../guide/locus.md) - the positions and vectors these keys take

## Changes since 1.38

- You can use the new keys **Initial position** and **Direction**
- You can pick any palette color for the blood. In SBO 1.38, every color except red and yellow gave red
