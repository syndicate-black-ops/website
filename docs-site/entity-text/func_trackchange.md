A `func_trackchange` is a piece of track that moves a [`func_tracktrain`](func_tracktrain.md) from one track to
another when you trigger it. The train must stand on it, and the piece moves up or down, turns, or both, and takes the
train with it.

## Notes

- The track change starts at its top position, so its first trigger moves it to the bottom, unless it has **Start
  at Bottom**
- The train only leaves the track change on the track at the position where the track change stands

## See also

- [`func_trackautochange`](func_trackautochange.md) - the same, which moves by itself when the train arrives
- [`func_tracktrain`](func_tracktrain.md) - the train it moves
- [`path_track`](path_track.md) - the points of a track
- [func_trackchange on TWHL](https://twhl.info/wiki/page/func_trackchange) - the Half-Life entity

## Changes since 1.38

- You can use the new **Fire On** keys and their use types, **Sound radius** and the custom move and stop sounds
- A track change doesn't crash the server after its train is removed. In SBO 1.38, as in Half-Life, this crashed the
  server
