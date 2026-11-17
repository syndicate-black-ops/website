A `trigger_entity_iterator` fires its target once for each entity that passes its filters, with that entity as
`!activator`. For example, it can fire once for every player, or once for every monster named `wave2`.

## Attributes

- **Filter entities by name** (`name_filter`) - Only counts entities with this name
    - If you leave this key empty, any name counts
- **Filter entities by class name** (`classname_filter`) - Only counts entities of this class
    - If you leave this key empty, any class counts
- **Filter entities by status** (`status_filter`) - Only counts living or only dead entities. Players never count as
  dead, because the iterator skips players who aren't alive
- **Target for each entity** (`target`) - Fires this target once for each entity. `!activator` and `!caller` in this
  key are the iterator's own activator and caller
- **Trigger state for each entity** (`triggerstate`) - Sets the [use type](../guide/trigger-modes.md) the target gets
- **Run mode** (`run_mode`) - Sets how a trigger runs the passes over the entities
    - Run once (0, default) - Each trigger makes one pass
    - Run once, multiple runs at once (1) - Each trigger starts its own pass, even while another is running
    - Toggle on/off (2) - A trigger starts passes that repeat until you trigger it again
- **Maximum runs** (`maximum_runs`) - With "Toggle on/off", sets how many passes it makes, and 0 means no limit
- **Delay between entities** (`delay_between_triggers`) - Sets how many seconds pass between two entities of one pass.
  With 0, it does the whole pass at once
- **Delay between runs** (`delay_between_runs`) - With "Toggle on/off", sets how many seconds pass between two passes
- **Trigger after each run** (`trigger_after_run`) - Fires this target at the end of each pass. If the activator is
  gone by then, the iterator itself is the activator
- **Reset at round start** (`round_reset`) - With Yes, the entity goes back to the way it was when the map loaded, at
  each round start before the players spawn. See
  [Round hooks](../guide/round-hooks.md) for more details

## Notes

- Players only count while they are alive. The iterator also skips entities that the game is removing
- A target that triggers the iterator while it runs doesn't start a new run, but Off or Toggle stops the run
- The class name, key names and values are the same as in Sven Co-op, but SBO only goes through alive players

## See also

- [`trigger_sensor`](trigger_sensor.md) - fires for each entity within a radius
- [Round hooks](../guide/round-hooks.md) - the names the game fires at round starts, with the world as activator

## Changes since 1.38

- `trigger_entity_iterator` is new
