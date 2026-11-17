An `ambient_generic` plays a sound or a sentence at its position, either once each time you trigger it or as a loop.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts the sound, and if the sound loops, the next trigger stops
  it. See [Common keys](common-keys.md#targetname)
- **WAV Name** (`message`) - Sets the sound it plays, which can be:
    - a `.wav` file in the `sound/` folder
    - a sentence from [`sound/sentences.txt`](https://twhl.info/wiki/page/Sentences.txt), with a `!` in front of
      its name
    - an `.mp3` file in the `sound/` folder, which plays as music like [`ambient_music`](ambient_music.md) (see
      [MP3 files](#mp3-files))
- **Volume** (`health`) - Sets how loud the sound is, from 0 for silent up to 10 for full volume. Default 10
    - If you leave this key empty, it is 0 and the sound is silent, unless you pick a **Dynamic Presets** effect or
      play an `.mp3`, which ignore **Volume**
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
    - If you leave this key empty, the sound plays at normal pitch. With a spin up, the sound stops as soon as it
      starts, but with **Start Pitch** empty too, it plays at the lowest pitch instead. With a spin down, the sound
      plays at normal pitch and spins down from there when you turn it off
- **Start Pitch** (`pitchstart`) - Sets the pitch a spin up starts from and a spin down ends at. Default 100
    - If you leave this key empty, a spin up starts at normal pitch, and a spin down slides all the way to the
      lowest pitch before the sound stops
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
- **Play Mode** (`playmode`) [[ported:sevenkewp svencoop]] - Sets whether the sound loops. See
  [Play modes](#play-modes)
    - Default (0, default) - The flag **Not Toggled** and the loop points of the WAV file decide (see
      [Looping a sound](https://developer.valvesoftware.com/wiki/Looping_a_sound))
    - Play once (1) - Plays once per trigger, even a WAV file that has loop points
    - Loop (2) - Loops, even a WAV file that has no loop points
    - Play once, linear falloff (5) - Plays once, and the volume falls with distance as **Linear Min** and
      **Linear Max** set
    - Loop, linear falloff (6) - Loops, and the volume falls with distance as **Linear Min** and **Linear Max** set
- **Linear Min** (`linearmin`) [[ported:sevenkewp svencoop]] - With a linear falloff, sets how far the sound plays at
  full volume, counted in steps of 256 units, so 2 means 512 units. Default 0
- **Linear Max** (`linearmax`) [[ported:sevenkewp svencoop]] - With a linear falloff, sets the distance beyond which
  the sound is silent, counted in steps of 256 units, and between **Linear Min** and **Linear Max** the volume falls
  evenly. If you set 0, no player hears the sound. Default 0

## Flags

- **Play Everywhere** (1) - Every player hears the sound equally loud, anywhere on the map
- **Small Radius** (2) - Players hear the sound up to about 500 units away
- **Medium Radius** (4) - Players hear the sound up to about 800 units away. This flag is set by default, and the
  entity also uses this radius when no radius flag is set
- **Large Radius** (8) - Players hear the sound up to about 1250 units away
- **Start Silent** (16) - A looping sound doesn't start with the map, but waits for a trigger
- **Not Toggled** (32) - The sound plays once per trigger, and triggering it while it plays starts it again from
  the beginning, so a trigger can't turn it off

## Play modes

When the map starts, the entity reads the length and the loop points of the WAV file. If the server can't read the
file, the entity ignores the play mode and works like **Default**, and with `developer 1` set in the console, the
console names the entity.

If a player joins after a looping sound has started, they hear it one second after they enter the game.

With a linear falloff, the entity ignores the radius flags and measures each player's distance from their eyes. If
you also set **Play Everywhere**, the mode "Play once, linear falloff" works like "Play once", and the mode
"Loop, linear falloff" works like "Loop".

See also [Music and sound](../features/music.md#ambient_generic-play-modes).

## MP3 files

You can use an `.mp3` file as the sound, and every player hears it everywhere, at the MP3 volume set in their own
game options. The entity ignores **Volume**, the pitch keys, the presets and the radius flags. The MP3 only loops
if you set **Play Mode** to one of its two looping modes, "Loop" or "Loop, linear falloff", and **Start Silent**
works as usual.

The file name must follow the rules of [`ambient_music`](ambient_music.md#attributes). If it breaks them, the entity
is removed, and with `developer 1` set in the console, the server console reports it.

## Notes

- Without **Not Toggled**, the entity treats every sound as a loop, so the first trigger starts it and the next one
  stops it. A WAV file without loop points plays only once, though, so every second trigger just stops a sound that
  has already ended
- If you pick a preset, the entity ignores **Volume** because the preset sets the volume itself: most presets play
  at full volume, and the three pulse presets, "Slow Pulse", "Pulse" and "Quick pulse", play at half volume
- The spin down and the fade out only happen when you turn off a looping sound
- With **Incremental spinup count**, or the preset "Incremental Spinup", a trigger never turns the sound off, and once
  the last step is reached, more triggers do nothing
- If you set more than one radius flag, the entity uses the smallest radius, and **Play Everywhere** wins over all
  of them
- If **WAV Name** is empty, the entity is removed when the map starts, and with `developer 1` set in the console, the
  console reports it
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Volume**
  or **Pitch** while a looping sound plays, you hear the new volume or pitch at once, but with a preset the entity
  keeps the preset's values. A new sound that the map has already loaded, for example because another entity uses it,
  stops the old one and plays at once. Any other sound would have to be precached, so the entity keeps its sound and,
  with `developer 1` set in the console, prints a console line, and an MP3 can't be changed at all. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`ambient_music`](ambient_music.md) - an MP3 every player hears, everywhere
- [`ambient_random`](ambient_random.md) - plays one of up to five sounds, picked at random
- [`speaker`](speaker.md) - plays random sentences of a sentence group, at random times
- [`env_sound`](env_sound.md) - sets the echo of a room for players near it
- [Music and sound](../features/music.md) - `ambient_music` and the play modes
- [Making custom sounds](https://twhl.info/wiki/page/Tutorial:_Making_Custom_Sounds) - how to make a WAV file that
  loops, on TWHL

## Changes since 1.38

- You can use the new keys **Play Mode**, **Linear Min** and **Linear Max**
- You can use an `.mp3` file as the sound
