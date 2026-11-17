An `ambient_random` plays one of up to five sounds at its position, picked at random each time you turn it on. It
never picks the sound it played last, so the same sound doesn't play twice in a row.

It works like [`ambient_generic`](ambient_generic.md), but it has no play modes and can't play MP3 files.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts a sound, and if the sound loops, the next trigger stops
  it. See [Common keys](common-keys.md#targetname)
- **WAV Name** (`message`) - Sets the first sound, which is the one that plays when the map starts. It can be a
  `.wav` file in the `sound/` folder or a sentence from
  [`sound/sentences.txt`](https://twhl.info/wiki/page/Sentences.txt), with a `!` in front of its name
    - If you leave this key empty, the first of the other sounds that is set takes its place
- **WAV Name 2** (`noise`) - Sets the second sound to pick from, a `.wav` file or a sentence like **WAV Name**
- **WAV Name 3** (`noise1`) - Sets the third sound to pick from
- **WAV Name 4** (`noise2`) - Sets the fourth sound to pick from
- **WAV Name 5** (`noise3`) - Sets the fifth sound to pick from
- **Volume** (`health`) - Sets how loud the sound is, from 0 for silent up to 10 for full volume. Default 10
- **Dynamic Presets** (`preset`) - Picks a ready-made effect that changes the sound while it plays. If you pick a
  preset, the entity ignores **Volume**, **Start Volume**, the fade, pitch and spin keys, the LFO keys and
  **Incremental spinup count**, because the preset sets all of these itself. Every preset fades the sound in when
  it starts. In the list, "spins up" means the pitch rises as the sound starts, and "spins down" means it falls
  when you turn the sound off
    - None (0, default) - No preset, so the entity uses its own keys
    - Huge Machine (1) - Spins up very slowly from a low pitch to the highest pitch, then spins down and fades out
      very slowly
    - Big Machine (2) - Like "Huge Machine", but a little faster
    - Machine (3) - Spins up at medium speed from normal pitch to the highest pitch, and spins down slowly
    - Slow Fade in (4) - Normal pitch, fading in and out very slowly
    - Fade in (5) - Normal pitch, fading in and out slowly
    - Quick Fade in (6) - Normal pitch, fading in at medium speed and out slowly
    - Slow Pulse (7) - Half volume, with the volume jumping a little up and down, slowly
    - Pulse (8) - Like "Slow Pulse", but faster
    - Quick pulse (9) - Like "Slow Pulse", but fast
    - Slow Oscillator (10) - A little above normal pitch, with the pitch rising and falling smoothly and slowly
    - Oscillator (11) - Like "Slow Oscillator", but faster
    - Quick Oscillator (12) - Like "Slow Oscillator", but fast
    - Grunge pitch (13) - Half the normal pitch
    - Very low pitch (14) - 70% of the normal pitch
    - Low pitch (15) - 90% of the normal pitch
    - High pitch (16) - 120% of the normal pitch
    - Very high pitch (17) - 180% of the normal pitch
    - Screaming pitch (18) - The highest pitch, 255% of normal
    - Oscillate spinup/down (19) - Spins up very slowly from a low pitch to double pitch, then the pitch rises and
      falls smoothly, and it spins down very slowly
    - Pulse spinup/down (20) - Spins up very slowly from a low pitch to the highest pitch, then the pitch jumps up
      and down, and it spins down very slowly
    - Random pitch (21) - Normal pitch that changes slowly at random
    - Random pitch fast (22) - A high pitch that changes fast at random
    - Incremental Spinup (23) - Each trigger raises the pitch one step until it reaches the highest pitch after 5
      steps, and a trigger can't turn the sound off
    - Alien (24) - Spins up very slowly from a very low pitch to double pitch, with the pitch changing at random
    - Bizzare (25) - Spins up from normal pitch to a high pitch, while the pitch and the volume swing strongly up
      and down
    - Planet X (26) - A low pitch, with the pitch and the volume changing at random
    - Haunted (27) - Spins up fast from a little below normal pitch to a little above it, while the pitch and the
      volume jump a little up and down, slowly
- **Start Volume** (`volstart`) - Sets the volume a fade in starts from and a fade out ends at, from 0 for silent
  up to 10 for full volume. Default 0
- **Fade in time** (`fadein`) - Fades the sound in from **Start Volume** when it starts, from 1 for the fastest
  fade up to 100 for the slowest, and 0 means no fade in. Default 0
- **Fade out time** (`fadeout`) - Fades the sound out to **Start Volume** when you turn it off, from 1 for the
  fastest fade up to 100 for the slowest, and 0 means the sound stops at once. Default 0
- **Pitch** (`pitch`) - Sets the pitch of the sound: 100 is normal, 50 is one octave lower, 200 is one octave
  higher and 255 is the highest. Default 100
- **Start Pitch** (`pitchstart`) - Sets the pitch a spin up starts from and a spin down ends at. Default 100
- **Spin up time** (`spinup`) - Raises the pitch from **Start Pitch** to **Pitch** when the sound starts, from 1
  for the fastest spin up to 100 for the slowest, and 0 means no spin up. Default 0
- **Spin down time** (`spindown`) - Lowers the pitch to **Start Pitch** when you turn the sound off, from 1 for the
  fastest spin down to 100 for the slowest, and 0 means no spin down. Default 0
- **LFO type** (`lfotype`) - Makes the pitch or the volume swing up and down while the sound plays (LFO means "low
  frequency oscillator"). Default 0
    - Off (0, default) - No swing
    - Square (1) - Jumps between high and low
    - Triangle (2) - Rises and falls smoothly
    - Random (3) - Jumps to random values
- **LFO rate** (`lforate`) - Sets how fast the swing goes, from 0 up to 1000, and a higher value is faster.
  Default 0
- **LFO mod pitch** (`lfomodpitch`) - Sets how far the swing moves the pitch, in percent from 0 up to 100, and 0
  means the pitch doesn't swing. Default 0
- **LFO mod vol** (`lfomodvol`) - Sets how far the swing moves the volume, in percent from 0 up to 100, and 0 means
  the volume doesn't swing. Default 0
- **Incremental spinup count** (`cspinup`) - Makes each trigger raise the pitch one step instead of turning the
  sound off. The steps go from **Start Pitch** up to the highest pitch, and this key sets how many there are, up
  to 100, with 0 turning it off. Default 0

## Flags

- **Play Everywhere** (1) - Every player hears the sound at full volume, anywhere on the map
- **Small Radius** (2) - Players hear the sound up to about 500 units away
- **Medium Radius** (4) - Players hear the sound up to about 800 units away. This flag is set by default, and the
  entity also uses this radius when no radius flag is set
- **Large Radius** (8) - Players hear the sound up to about 1250 units away
- **Start Silent** (16) - A looping sound doesn't start with the map, but waits for a trigger
- **Not Toggled** (32) - The sound plays once per trigger, and triggering it while it plays starts it again from
  the beginning, so a trigger can't turn it off

## Notes

- Each time you turn the entity on, it picks one of the other sounds that are set, so with only one sound set it
  plays that sound every time
- If one of the sounds is an `.mp3` file, the entity leaves that sound out, and with `developer 1` set in the console,
  the server console reports it
- Without **Not Toggled**, the entity treats every sound as a loop, so the first trigger starts a sound and the
  next one stops it, and only the trigger that starts a sound picks a new one
- If you pick a preset, the entity ignores **Volume** because the preset sets the volume itself: most presets play
  at full volume, and the three pulse presets, "Slow Pulse", "Pulse" and "Quick pulse", play at half volume
- If you set more than one radius flag, the entity uses the smallest radius, and **Play Everywhere** wins over all
  of them
- If no sound is set at all, the entity is removed when the map starts, and with `developer 1` set in the console, the
  console reports it

## See also

- [`ambient_generic`](ambient_generic.md) - plays one sound, with play modes and MP3 files
- [`ambient_extraspeaker`](ambient_extraspeaker.md) - plays a sound or a sentence on another entity, which it
  follows
- [`speaker`](speaker.md) - plays random sentences of a sentence group, at random times
- [Music and sound](../features/music.md) - map music and sounds

## Changes since 1.38

- `ambient_random` is new in SBO 2.0.0
