A `change_touch` shows a model, the G-Man by default, and ends a [Co-op](../../game-modes/coop.md) mission in success
when a player touches it. It works only on Co-op maps, and on other maps touching it does nothing.

The model plays its idle animations, falls to the floor and is solid, with a box 32 units wide and 72 units high
that players bump into.

## Attributes

- **Model** (`model`) - Sets the model it shows, as a path to an `.mdl` file, such as `models/gman.mdl`
    - If you leave this key empty, pick an editor model or name a file the server doesn't have, the entity is
      removed when the map starts

## Notes

- Only players end the mission by touching it, and monsters and objects that touch it do nothing
- Only the first mission result counts, so touching it after a [`game_end`](game_end.md) or a
  [`mission_failed`](mission_failed.md) has ended the mission changes nothing

## See also

- [`game_end`](game_end.md) - ends the mission in success when you trigger it
- [`mission_failed`](mission_failed.md) - ends the mission in failure when you trigger it
- [Co-op: mission end](../../game-modes/coop.md#mission-end) - what happens when a mission ends

## Changes since 1.38

- The model plays its idle animations. In SBO 1.38, it stood still on the first frame, because SBO 1.38 never set
  an animation for the model
- A missing model removes the entity. In SBO 1.38, a missing model stopped the map from loading
