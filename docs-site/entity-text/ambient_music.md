---
description: "An ambient_music plays an MP3 as map music, which every player hears everywhere on the map at their own music volume."
---
An `ambient_music` plays an MP3 as map music, which every player hears everywhere on the map at their own music volume
(**MP3 Volume** in the audio options). Players download the MP3 with the map, and spectators and dead players hear it
too.

If you trigger it with the [use type](../guide/trigger-modes.md) On, it starts the track from the beginning, and
with Off it stops the track. Any other trigger switches between the two. A track that has played to its end still
counts as playing, so the next trigger only turns the entity off, and the one after that plays the track again.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the music. See
  [Common keys](common-keys.md#targetname)
- **MP3 file** (`message`) - Sets the MP3 to play, given as a path inside the `sound/` folder, so `mymap/theme.mp3` is
  the file `sound/mymap/theme.mp3`. The game adds the file to the map's downloads. The name can only use letters,
  digits, `/`, `_`, `-` and `.`, it must end in `.mp3`, it can't contain `..`, and it can be at most 57 characters
  long. If the name breaks these rules, the entity is removed, and with `developer 1` set in the console, the server
  console reports it

## Flags

- **Start Silent** (1) - The music doesn't start with the map, but waits for a trigger
- **Loop** (2) - The music starts again each time it ends, until you stop it. Without this flag, it plays once

## Notes

- Players hear only one track at a time, so when a second `ambient_music` starts, its track replaces the first one.
  Stopping an entity only stops the music if that entity was the last one to start a track, and removing the
  entity that plays the current track stops the music too
- A player who joins later hears the current track from its beginning, and a map without music stops the music of
  the previous map
- A new round doesn't change the music

## See also

- [`ambient_generic`](ambient_generic.md) - plays a sound at its position, and can play an MP3 too
- [Music and sound](../features/music.md) - map music and the play modes of `ambient_generic`

## Changes since 1.38

- `ambient_music` is new in SBO 2.0.0
