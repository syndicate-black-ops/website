A `trigger_startpatrol` sends a monster along a route of [`path_corner`](path_corner.md) entities.

## Attributes

- **Target monster** (`target`) - Names the monster, as a name or `!activator`. If more than one monster has that
  name, only the first one goes
- **Patrol path start** (`m_iszPath`) - Names the `path_corner` where the route starts

## Notes

- It only sends a living monster that isn't in a script and isn't fighting. A monster that follows a player stops
  following
- The monster walks the route and runs where a `path_corner` has a speed of 200 or more
- It still fights, and when it is calm again, it goes back to the route
- When a player is in the way, the monster walks around them, or it waits 2 seconds and then continues

## See also

- [`path_corner`](path_corner.md) - the points of the route
- [`scripted_schedule`](scripted_schedule.md) - tells monsters what to do about a spot

## Changes since 1.38

- `trigger_startpatrol` is new
