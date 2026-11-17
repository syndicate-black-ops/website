A `trigger_cdaudio` is a brush trigger that plays a track of the Half-Life CD for every player in the game when a
player touches it or when you trigger it. It works once and then removes itself.

## Attributes

- **Track #** (`health`) - Sets the track every player hears
    - Stop (-1, default) - It stops the track that is playing
    - If you leave this key empty, it is 0 and no track plays

## See also

- [`target_cdaudio`](target_cdaudio.md) - the point version with a radius
- [`ambient_music`](ambient_music.md) - plays an MP3 file for every player
- [trigger_cdaudio on TWHL](https://twhl.info/wiki/page/trigger_cdaudio) - the Half-Life entity

## Changes since 1.38

- Fixed `trigger_cdaudio` and `target_cdaudio` playing their music only for the player in the first server slot. The
  game sent the music only to that slot. This was a bug in SBO 1.38
