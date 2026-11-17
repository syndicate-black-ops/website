A `target_cdaudio` plays a track of the Half-Life CD for every player in the game when a player comes within its
radius, or when you trigger it. It can also stop the track, and it works once and then removes itself.

## Attributes

- **Track #** (`health`) - Sets the track every player hears
    - Stop (-1, default) - It stops the track that is playing
    - If you leave this key empty, it is 0 and no track plays
- **Player Radius** (`radius`) - With a value above 0, the track also plays when any player comes within this many
  units. With 0, only a trigger plays it

## See also

- [`trigger_cdaudio`](trigger_cdaudio.md) - the brush version
- [`ambient_music`](ambient_music.md) - plays an MP3 file for every player
- [target_cdaudio on TWHL](https://twhl.info/wiki/page/target_cdaudio) - the Half-Life entity

## Changes since 1.38

- Fixed `trigger_cdaudio` and `target_cdaudio` playing their music only for the player in the first server slot. The
  game sent the music only to that slot. This was a bug in SBO 1.38
- Fixed only the player in the first server slot starting the track by coming within the **Player Radius**. Any player
  starts it now
