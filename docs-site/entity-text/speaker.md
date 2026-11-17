A `speaker` plays random sentences of a sentence group at random times, like the announcements in Half-Life.

## Attributes

- **Announcement Presets** (`preset`) - Sets a Half-Life announcer sentence group that the speaker picks a random
  sentence from
    - None (0, default) - The speaker uses **Sentence Group Name** instead
- **Sentence Group Name** (`message`) - Names a sentence group from
  [`sound/sentences.txt`](https://twhl.info/wiki/page/Sentences.txt), such as `C1A0_`. The speaker plays a random
  sentence of the group, and then another one after a random time from 15 seconds to 2.25 minutes. A single sentence
  written as `!NAME` plays once. If you pick a preset, the speaker ignores this key
- **Volume** (`health`) - Sets how loud the speaker is, from 0 for silent up to 10 for full volume
    - If you leave this key empty, it is 0 and the speaker is silent

## Flags

- **Start Silent** (1) - The speaker is silent when the map loads, until a trigger turns it on. Without this flag, the
  first announcement comes 5 to 15 seconds after the map loads

## Notes

- A trigger turns the announcements on or off, as the [use type](../guide/trigger-modes.md) says
- A speaker with the preset None and no **Sentence Group Name** removes itself when the map starts

## See also

- [`scripted_sentence`](scripted_sentence.md) - makes a monster speak one sentence
- [`ambient_generic`](ambient_generic.md) - plays a sound
- [speaker on TWHL](https://twhl.info/wiki/page/speaker) - the Half-Life entity
