A `scripted_sentence` makes a monster or another entity speak a sentence from
[`sound/sentences.txt`](https://twhl.info/wiki/page/Sentences.txt).

## Attributes

- **Sentence Name** (`sentence`) - Sets the sentence to speak. A sentence name with a `!` in front plays that
  sentence, and a name without `!` plays a random sentence of that group
- **Speaker Type** (`entity`) - Names the speaker, as a monster's name or class name. A
  [`func_button`](func_button.md), a [`func_rot_button`](func_rot_button.md) or a [`cycler`](cycler.md) can also speak
- **Sentence Time** (`duration`) - Sets how many seconds the speaker counts as talking. The next sentence can start
  after this time plus **Delay Before Refire**
    - If you leave this key empty, it is 0
- **Search Radius** (`radius`) - When **Speaker Type** is a class name, sets how far from this entity the game looks
  for the speaker, in units. It also sets how far from the speaker the game looks for the listener, unless you set
  **Listener search radius**
    - If you leave this key empty, it is 0, so the game doesn't find a speaker given by its class name. It also
      doesn't find a listener given by its class name, unless you set **Listener search radius**
- **Delay Before Refire** (`refire`) - Sets how many seconds after the **Sentence Time** pass before the sentence can
  be spoken again
    - If you leave this key empty, it is 0
- **Listener Type** (`listener`) - Names the entity that the speaker looks at while it talks, by its name or class
  name. `player` is the nearest player
    - If you leave this key empty, the speaker looks at nobody
- **Volume** (`volume`) - Sets how loud the sentence is, from 1 for very quiet up to 10 for full volume. 0 or less, or
  a value that isn't a number, gives full volume
- **Sound Radius** (`attenuation`) - Sets how far away players hear the sentence
- **Follow action** (`follow_action`) - Sets what the speaker does when it starts the sentence. A monster that was
  attacked never follows
    - Start following (1) - It follows the nearest player, but a Cop only does this as a player ally with a
      **Followage policy** set
- **Fire after speaking** (`fire_after`) - Fires this target **Sentence Time** seconds after the sentence starts,
  plus **Delay before fire after**
- **Delay before fire after** (`fire_after_delay`) - Sets how many seconds after the sentence pass before **Fire after
  speaking** fires
- **Listener search radius** (`listener_radius`) - Sets how far the listener is looked for
    - If you leave this key empty or set 0, it is the **Search Radius**
- **Allow use** (`allow_use`) - With Yes, players can still press the use key on the speaker while it says this
  sentence
- **Search origin** (`search_origin`) - Sets where the game looks for the speaker when **Speaker Type** is a class
  name, as a [locus position](../guide/locus.md)
    - If you leave this key empty, it is this entity

## Flags

- **Fire Once** (1) - The entity removes itself after the sentence is spoken once
- **Followers Only** (2) - Only a monster that follows a player speaks it
- **Interrupt Speech** (4) - The speaker says it also when it is busy, if it is alive
- **Others stop talking** (8) - Other monsters around the speaker stop talking when the sentence starts. Without this
  flag, they keep talking

## See also

- [`scripted_sequence`](scripted_sequence.md) - plays an animation on a monster
- [`speaker`](speaker.md) - plays announcements at random times
- [scripted_sentence on TWHL](https://twhl.info/wiki/page/scripted_sentence) - the Half-Life entity

## Changes since 1.38

- A `func_button`, a `func_rot_button` or a `cycler` can be the speaker, but in SBO 1.38 only monsters could speak
- A **Volume** that isn't a number gives the default volume. In SBO 1.38 such a value could stop or hang the server
- You can use the new keys **Follow action**, **Fire after speaking**, **Delay before fire after**, **Listener search
  radius**, **Allow use** and **Search origin**
