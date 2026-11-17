A `game_zone_player` counts the players inside and outside its brush when you trigger it, and fires a target for each
of them. Spectators count neither as inside nor as outside.

## Attributes

- **Name** (`targetname`) - Triggering the entity counts the players. See [Common keys](common-keys.md#targetname)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing
- **Target for IN players** (`intarget`) - Names the entities to trigger once for each player inside the brush, and passes
  on that player as the [activator](../guide/entity-triggering.md#target-selectors)
- **Target for OUT players** (`outtarget`) - Names the entities to trigger once for each player outside the brush, and
  passes on that player as the activator
- **Counter for IN players** (`incount`) - Names the entities that get the number of players inside the brush, with
  the [use type](../guide/trigger-modes.md) Set, so a [`game_counter`](game_counter.md) or a
  [`game_number`](game_number.md) takes it as its value
- **Counter for OUT players** (`outcount`) - Names the entities that get the number of players outside the brush,
  with the use type Set

## See also

- [`trigger_inout`](trigger_inout.md) - fires targets when entities enter or leave a brush
- [game_zone_player on TWHL](https://twhl.info/wiki/page/game_zone_player) - the Half-Life entity

## Changes since 1.38

- Spectators count neither as inside nor as outside. In SBO 1.38, they counted like the other players
