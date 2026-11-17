---
description: "An ambient_extraspeaker plays a sound on another entity, so the sound moves with it and never cuts off the entity's own sounds."
---
An `ambient_extraspeaker` plays a sound on another entity, so the sound moves with that entity. The sound comes from
an invisible speaker that follows the entity, so it never cuts off the entity's own sounds.

## Attributes

- **Name** (`targetname`) - Triggering the entity plays the sound, and **Not Toggled** sets whether the next
  trigger stops it. See [Common keys](common-keys.md#targetname)
- **WAV Name** (`message`) - Sets the sound it plays, which can be a `.wav` file in the `sound/` folder or a
  sentence from [`sound/sentences.txt`](https://twhl.info/wiki/page/Sentences.txt), with a `!` in front of its
  name
- **Attach to entity** (`target`) - Names the entity the sound plays on, so you can use:
    - the name of an entity - the sound plays on that entity
    - `*player` - the sound plays on the player who started the chain of triggers, if that player is alive and in
      the game, and not a spectator
    - `!activator` - the sound plays on the entity that started the chain of triggers, which can also be a monster
    - If you leave this key empty, it works like `*player`
- **Channel to use** (`channel`) - Picks the sound channel of the speaker. A new sound on the same channel of the
  same entity cuts off the sound that plays there, so sounds on different channels play together
    - Default (0) - The Static channel
    - Weapon (1)
    - Voice (2)
    - Item (3)
    - Body (4)
    - Stream (5)
    - Static (6)
- **Volume** (`health`) - Sets how loud the sound is, from 1 for very quiet up to 10 for full volume, and 0 or
  any value above 10 plays at full volume
- **Pitch** (`pitch`) - Sets the pitch of the sound: 100 is normal, 50 is one octave lower, 200 is one octave
  higher and 255 is the highest, and 0 or any value above 255 plays at normal pitch

## Flags

- **Play Everywhere** (1) - Every player hears the sound equally loud, anywhere on the map
- **Small Radius** (2) - Players hear the sound up to about 500 units away
- **Medium Radius** (4) - Players hear the sound up to about 800 units away. This flag is set by default, and the
  entity also uses this radius when no radius flag is set
- **Large Radius** (8) - Players hear the sound up to about 1250 units away
- **Start Silent** (16) - The sound doesn't start with the map, but waits for a trigger. This flag is set by
  default
- **Not Toggled** (32) - Each trigger plays the sound once, and a sound that is still playing starts again from the
  beginning. This flag is set by default. Without it, a trigger starts the sound and the next trigger stops it

## Notes

- If you clear both **Start Silent** and **Not Toggled**, the sound starts when the map starts, but only if
  **Attach to entity** names an entity. With `*player` or `!activator`, nobody has triggered anything yet, so the
  first trigger starts the sound
- Two `ambient_extraspeaker` entities that play on the same entity share its speaker, so if they also use the same
  **Channel to use**, the newer sound cuts off the older one
- If **WAV Name** is empty, the entity is removed when the map starts, and with `developer 1` set in the console, the
  console reports it
- A player who joins later doesn't hear a sound that is already playing

## See also

- [`ambient_generic`](ambient_generic.md) - plays a sound at its own position, with presets and play modes
- [`ambient_random`](ambient_random.md) - plays one of up to five sounds, picked at random
- [Music and sound](../features/music.md) - map music and sounds

## Changes since 1.38

- `ambient_extraspeaker` is new in SBO 2.0.0
