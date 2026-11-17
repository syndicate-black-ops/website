A `func_trackautochange` is a piece of track that moves a [`func_tracktrain`](func_tracktrain.md) from one track to
another by itself when the train arrives on it. It has the keys of a [`func_trackchange`](func_trackchange.md).

## See also

- [`func_trackchange`](func_trackchange.md) - the same, which moves when you trigger it
- [`func_tracktrain`](func_tracktrain.md) - the train it moves
- [`path_track`](path_track.md) - the points of a track
- [func_trackautochange on TWHL](https://twhl.info/wiki/page/func_trackautochange) - the Half-Life entity

## Changes since 1.38

- You can use the new **Fire On** keys and their use types, **Sound radius** and the custom move and stop sounds
- A track change doesn't crash the server when a trigger without an activator uses it, or after its train is
  removed. In SBO 1.38, as in Half-Life, both crashed the server
