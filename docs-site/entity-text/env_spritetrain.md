An `env_spritetrain` moves a sprite along a path of [`path_corner`](path_corner.md) entities, the way a
[`func_train`](func_train.md) moves a brush. It isn't solid.

It uses the speed and the wait of each `path_corner`, fires their targets and obeys their teleport flag, and like a
`func_train`, it starts by itself when it has no name.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the train, and **Obey Trigger Mode** sets how.
  Without a name, the train starts by itself. See [Common keys](common-keys.md#targetname)
- **Sprite Name** (`model`) - Sets the sprite that moves along the path
- **Sprite Scale** (`scale`) - Sets the size of the sprite, so 0.5 is half and 2 is double
    - If you leave this key empty, the sprite has its normal size
- **Framerate** (`framerate`) - Sets how many frames per second the sprite plays, and 0 shows only its first frame
- **First stop target** (`target`) - Names the first `path_corner` of the path
- **Speed** (`speed`) - Sets how fast the sprite moves, in units per second, until a `path_corner` sets another
  speed, and 0 means 100
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how a trigger starts and stops the train
    - No (0) - Every trigger starts a stopped train or stops a moving one
    - Yes (1) - On starts it, Off stops it and Toggle switches it
- **Sound Volume** (`volume`) - Sets how loud the move and stop sounds are, up to 1 for full volume
    - If you leave this key empty or set 0, it is 0.85
- **Move Sound** (`noise`) - Sets the sound that loops while the train moves
- **Stop Sound** (`noise1`) - Sets the sound the train plays when it stops

## Flags

- **Initially On** (4) - The train starts moving when the map starts

## Notes

- With the render mode Normal, the sprite is drawn as Additive, so its colors are added to what is behind it
- With an **FX Amount** of 0, the sprite is drawn at full brightness, and a negative amount makes it invisible

## See also

- [`env_modeltrain`](env_modeltrain.md) - the same with a model
- [`func_train`](func_train.md) - a brush that moves along a path
- [`path_corner`](path_corner.md) - the stops of the path

## Changes since 1.38

- `env_spritetrain` is new in SBO 2.0.0
