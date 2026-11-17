A `game_playvideo` plays a video over the whole screen when you trigger it, for the player who started the chain of
triggers or for every player. Players download the video and its sound file with the map.

While the video plays, the player stands still and can't move, fire or change weapons, and the game goes on around
them. The video ends when it is over, when the player presses ++escape++, when they die, or at a map change.

## Attributes

- **Name** (`targetname`) - Triggering the entity plays the video, and triggering it again starts the video over. See
  [Common keys](common-keys.md#targetname)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing
- **Video file** (`video`) - Sets the video, an Ogg Theora file (`.ogv`) in the `video/` folder of the game, given
  without the folder, so `video/mymap/intro.ogv` is `mymap/intro.ogv`. The name can only use letters, digits, `/`,
  `_` and `-`, with one dot before the extension, and it can be at most 57 characters long. The video plays with its
  own Ogg Vorbis sound
- **Sound file** (`audio`) - Sets an Ogg Vorbis file (`.ogg`) in `video/`, which plays instead of the video's own
  sound
    - If you leave this key empty, the video plays its own sound

## Flags

- **All Players** (1) - The video plays for every player. Without this flag, only the player who started the chain
  of triggers sees it

## Notes

- If a file name breaks the rules above, the server console reports it when the map starts, and the entity plays
  nothing
- Players who join later don't see the video

## See also

- [Video](../features/video.md) - how to make the video files
- [`vgui_screen`](vgui_screen.md) - a video on a screen in the world

## Changes since 1.38

- `game_playvideo` is new in SBO 2.0.0
