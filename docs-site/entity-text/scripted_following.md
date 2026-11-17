A `scripted_following` makes a Scientist, or another monster that follows players, start or stop following the player
who triggered it. A Cop only starts following if it is a player ally with a **Followage policy** set.

## Attributes

- **Affected monster name** (`entity`) - Names the talking monster. Only the first living monster with this name
  changes
- **Fire on start following** (`on_start_following`) - Fires this target when the monster starts following, if it
  wasn't following before. The player is the activator
- **Fire on stop following** (`on_stop_following`) - Fires this target when the monster stops following, if it was
  following before. The player is the activator
- **Use type** (`use_type`) - Sets whether a trigger makes the monster start or stop following
    - Make stop following (-1) - Every trigger makes it stop
    - Forward input (0, default) - On makes it start, Off makes it stop and Toggle switches it
    - Make start following (1) - Every trigger makes it start

## Flags

- **Remove on fire** (1) - The entity removes itself after it is used

## Notes

- Only monsters that follow players when used react to it
- Only an alive player counts as the activator, and for anyone else nothing happens
- If the trigger is On, or **Use type** is "Make start following", and the monster is in a script, the entity tries
  again every 0.1 seconds until the monster is free

## See also

- [`monster_scientist`](monster_scientist.md) - the Scientist, who follows players
- [`scripted_schedule`](scripted_schedule.md) - tells monsters what to do about a spot

## Changes since 1.38

- `scripted_following` is new
