A `monster_sitting_scientist` is a Scientist sitting on a chair, who turns its head and talks to nearby players. It
can't be hurt, used or made to follow, and it doesn't fight, walk or react.

## Attributes

- **Classification** (`classify`) - Sets the side that a [`trigger_sensor`](trigger_sensor.md) with a relationship
  filter sees it on, while no monster ever sees it
    - If you leave this key empty or set 0, it is "Human military"
- **Is player ally** (`is_player_ally`) - With Yes, a `trigger_sensor` with a relationship filter sees it as a player
  ally, unless you set **Classification**
- **Voice pitch** (`voicepitch`) - Sets the pitch of its voice, where 100 is the normal pitch
    - If you leave this key empty or set 0, it keeps its own voice pitch
- **Speech Prefix** (`SpeakAs`) - Makes it speak the lines of another voice, such as `BA` for a Cop or `SC` for a
  Scientist, and the lines that voice doesn't have stay silent
- **Body** (`body`) - Sets the Scientist's head, and Luther also has darker hands
    - Random (-1, default) - It picks one of the four heads when the map starts
    - If you leave this key empty, it has the head Glasses
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Scientist plays its own sitting animations

## Flags

- **Gag** (2) - It doesn't start talking by itself, and it only says a scripted sentence with **Interrupt Speech**,
  but it still answers a question that another talker asks it

## See also

- [`monster_scientist`](monster_scientist.md) - the Scientist that walks and follows players
- [`scripted_sentence`](scripted_sentence.md) - makes a monster say a sentence
- [monster_sitting_scientist on TWHL](https://twhl.info/wiki/page/monster_sitting_scientist) - the Half-Life entity
