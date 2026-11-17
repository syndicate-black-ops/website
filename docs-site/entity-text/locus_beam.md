A `locus_beam` makes a beam each time you trigger it, between two entities, between two positions, or from a position
in a direction. Each beam is an entity of its own that can hurt what it touches, and it stays until its **Duration**
is over or a **KillTarget** removes it.

## Attributes

- **Name** (`targetname`) - Triggering the entity makes a beam. See [Common keys](common-keys.md#targetname)
- **Start at** (`m_iszStart`) - Sets where the beam starts, as an entity name or a
  [locus position](../guide/locus.md), as **Start & End are** says. With `!activator`, it is the entity that started
  the chain of triggers
    - If you leave this key empty, no beam is made
- **End at** (`m_iszEnd`) - Sets where the beam ends, as an entity name, a locus position, or with "Position &
  Direction", a [locus vector](../guide/locus.md) added to the start. With `*locus`, it is the entity that started
  the chain of triggers
    - If you leave this key empty, it works like `*locus`
- **Start & End are** (`impulse`) - Picks what **Start at** and **End at** name, and an end that is an entity follows
  that entity while it moves
    - Entity & Entity (0) - Two entities
    - Position & Entity (1) - A position and an entity
    - Position & Position (2) - Two positions
    - Position & Direction (3) - A position and a vector, so the end is the start plus the vector
- **Sprite name** (`m_iszSprite`) - Sets the sprite of the beam. It is loaded with the map, so changing it while the
  map runs does nothing
- **Brightness** (`renderamt`) - Sets how bright the beam is, from 1 up to 255, and with 0 you can't see it
- **Color** (`rendercolor`) - Sets the color of the beam, as red, green and blue from 0 up to 255, and with `0 0 0` you
  can't see it, or with **Draw solid** it is black
- **Width** (`m_iWidth`) - Sets how wide the beam is, and with 0 you can't see it
- **Distortion** (`m_iDistortion`) - Sets how much the beam wobbles, where 0 is straight, and with **Draw sine**, the
  height of the wave
- **Start frame** (`m_fFrame`) - Sets the frame of the sprite each beam starts on
- **Scroll rate** (`m_iScrollRate`) - Sets how fast the texture moves along the beam
- **Duration** (`m_fDuration`) - Sets how many seconds pass before the beam is removed, and with 0, it stays until a
  **KillTarget** with its name removes it
- **Damage per second** (`m_fDamage`) - Sets the damage dealt per second to the first thing the beam touches. The
  entity that triggered the `locus_beam` gets the kill, except when a player's beam hurts another player, where the
  beam itself is the attacker
- **Damage type** (`m_iDamageType`) - Picks the kind of damage the beam deals
    - Generic (0)
    - Crush (1)
    - Bullet (2)
    - Slash (4)
    - Burn (8)
    - Freeze (16)
    - Blast (64)
    - Club (128)
    - Shock (256)
    - Sonic (512)
    - Energy beam (1024)
    - Drown (16384)
    - Nerve gas (65536)
    - Poison (131072)
    - Radiation (262144)
    - Chemical (1048576)
- **Name of the beams** (`m_iszTargetName`) - Sets the name each beam gets, so a **KillTarget** of that name removes
  the beams
- **Fire on spawn** (`target`) - The entity fires this each time it makes a beam, and passes on the beam as the
  [activator](../guide/entity-triggering.md#target-selectors)
- **Start attachment** (`m_iStartAttachment`) - For a start that is an entity, starts the beam at this attachment
  point of its model, from 1 up to 4
- **End attachment** (`m_iEndAttachment`) - For an end that is an entity, ends the beam at this attachment point of
  its model, from 1 up to 4

## Flags

- **Start sparks** (16) - Sparks fly at the start of the beam every 0.1 seconds
- **End sparks** (32) - Sparks fly at the end of the beam every 0.1 seconds
- **Decal end** (64) - The beam leaves scorch marks where it hits a wall
- **Fade start** (128) - The beam fades in from its start, so it is see-through at the start and solid toward the end
- **Fade end** (256) - The beam fades out toward its end, so it is solid at the start and see-through at the end
- **Draw solid** (512) - The beam is drawn solid, where normally its colors are added to what is behind it
- **Draw sine** (1024) - The beam is drawn as a wave, whose height **Distortion** sets

## Notes

- An entity without a model, such as an [`info_target`](info_target.md) or a [`path_corner`](path_corner.md), counts
  as its position
- The damage, the sparks and the scorch marks work as on an [`env_laser`](env_laser.md), because every 0.1 seconds
  the beam is traced from its start to its end
- Only alive players are hurt. When a player's beam hurts another player, the beam is the attacker, so the server
  setting [`mp_friendlyfire`](../../server/settings.md#players) (set in `server.cfg` or the server console) doesn't
  stop it
- No beam is made when the map is close to the limit of entities
- In **Start attachment** and **End attachment**, 1 is the first attachment point of the model, which
  [`calc_position`](calc_position.md) calls Attachment point 0

## See also

- [Locus guide](../../guides/locus.md) - a beam that follows the player, step by step
- [`env_beam`](env_beam.md) - a beam between two entities or points
- [`env_laser`](env_laser.md) - a beam that ends where it hits a wall
- [Locus system](../guide/locus.md) - the positions and vectors these keys take

## Changes since 1.38

- `locus_beam` is new in SBO 2.0.0
