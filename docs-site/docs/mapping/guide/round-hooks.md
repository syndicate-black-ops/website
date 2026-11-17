---
description: "Round hooks let your map react to its rounds: the game triggers entities with these names by itself at round starts and ends, lost rounds and the mission's end."
---

# Round hooks

Round hooks let your map react to its rounds: the game triggers entities with these names by itself at round starts
and ends, lost rounds and the mission's end. A new round respawns the players but not the map, so a door that was
opened in one round is still open in the next unless your map resets it. The hooks fire at these moments:

- the start and the end of each round
- the start of a given round number
- a lost round
- the end of the mission

If you give a [`trigger_relay`](../entities/trigger_relay.md), a [`multi_manager`](../entities/multi_manager.md) or
any other entity the name of a hook, the game triggers it at that moment. Some entities also have a key that puts
them back the way they were when the map loaded, at each round start.

## `game_round_start` and `game_round_end`

The game triggers every entity with one of these names:

| Name | When the game triggers it | Use type | Activator |
|---|---|---|---|
| `game_round_start` | At each round start, after the round's players have spawned | Toggle | The world |
| `game_round_end` | At each round end | Toggle | The world |

Several entities can have the same name, and the game triggers all of them. The activator is the world and not a
player, so use a [`trigger_entity_iterator`](../entities/trigger_entity_iterator.md) to reach each player. At the end
of a round, each [`trigger_camera`](../entities/trigger_camera.md) that holds a player's view gives it back before
the game triggers `game_round_end`.

When a round starts and ends depends on the game mode:

| Game mode | When a round starts | When a round ends |
|---|---|---|
| Co-op | When the round's players spawn and the screen shows **ROUND START** | When the round is lost or won, when the players leave or when the mission ends |
| Battle Royale | When the round's players spawn | When the round has a winner or nobody is left |
| Bounty Killer | When a player with a loadout spawns and the game picks the Hunted | When the Hunted leaves or becomes a spectator, but not when a player kills the Hunted, because the killer then becomes the Hunted and the round goes on |

## Round numbers, lost rounds and the mission's result

The game fires four more names the same way, with the use type Toggle and the world as the activator:

| Name | When the game triggers it | Game modes |
|---|---|---|
| `game_round_<N>`, such as `game_round_1` or `game_round_2` | Right after the `game_round_start` of round N | Co-op, where N is the round on the scoreboard, and Battle Royale, but not Bounty Killer, which counts no rounds |
| `game_round_failed` | When a round is lost and the screen shows **FAILED ROUND**, after its `game_round_end` and before the pause and the next round | Co-op, where losing the last round fires `game_mission_failed` instead |
| `game_mission_success` | When the mission succeeds through a [`game_end`](../entities/game_end.md) or a [`change_touch`](../entities/change_touch.md), after the round's `game_round_end` | Co-op, once per map |
| `game_mission_failed` | When the mission fails through a [`mission_failed`](../entities/mission_failed.md) or because the team lost its last round, after the round's `game_round_end` | Co-op, once per map |

Battle Royale and Bounty Killer have no lost rounds and no mission, so the last three names never fire there. The
mission's result is already fixed when its hook fires, so if the hook triggers a `game_end` or a `mission_failed`,
nothing changes.

![One Co-op round: the Reset at round start entities go back, the players spawn, game_round_start and game_round_1, game_round_2 and so on fire, and the team plays. A lost round fires game_round_end, then game_round_failed and a 5 second pause before the next round, or game_mission_failed after the last round. A game_end or change_touch fires game_round_end, then game_mission_success | 480](../../assets/img/diagram-round-hooks.webp)

*The entities that fire during one Co-op round*

## Reset at round start

The key **Reset at round start** (`round_reset`) puts an entity back the way it was when the map loaded, at each
round start before the players spawn. The reset fires nothing, and works in Co-op, Battle Royale and Bounty Killer.

These entities have the key:

- [`trigger_condition`](../entities/trigger_condition.md), [`trigger_random`](../entities/trigger_random.md),
  [`trigger_random_unique`](../entities/trigger_random_unique.md), [`trigger_timer`](../entities/trigger_timer.md),
  [`trigger_entity_iterator`](../entities/trigger_entity_iterator.md)
- [`game_number`](../entities/game_number.md), [`locus_variable`](../entities/locus_variable.md)
- [`env_state`](../entities/env_state.md), [`env_model`](../entities/env_model.md)
- [`trigger_lightstyle`](../entities/trigger_lightstyle.md) and
  [`global_light_control`](../entities/global_light_control.md), where the key is called **Reset light styles at
  round start** and puts every light style of the map back to the pattern it had when the map started
- [`item_pickup`](../entities/item_pickup.md) and [`player_inventory`](../entities/player_inventory.md), where the
  key does a different reset for inventory items (see their pages for more details)

A [`trigger_objective`](../entities/trigger_objective.md) has the flag **Reset on new round** (2) for the same job.

Other entities, such as doors and counters, don't have this key, so they keep their state into the next round. To
reset them, trigger them from an entity named `game_round_start`, for example by sending an Off to a door that has
[Obey Trigger Mode](trigger-modes.md#obey-trigger-mode) set.

## Player hooks

The game also triggers entities with these names when something happens to a player, with that player or the killer
as the activator:

| Name | When the game triggers it | Activator |
|---|---|---|
| `game_playerjoin` | When a player joins the server | The player |
| `game_playerspawn` | When a player spawns, and when a player joins | The player |
| `game_playerdie` | When a player dies | The player who died |
| `game_playerkill` | When a player kills another player | The killer |
| `game_playerleave` | When a player leaves the server | The player |

## Alive players

Logic entities that count or look for players only see alive players. A player counts from the moment they spawn
until they die, so spectators, the Game Master and players waiting for the next round never count. This applies, for
example, to
[`trigger_entity_iterator`](../entities/trigger_entity_iterator.md),
[`trigger_sensor`](../entities/trigger_sensor.md), [`trigger_inout`](../entities/trigger_inout.md), and the messages
of [`env_tutor`](../entities/env_tutor.md) and [`game_messagebox`](../entities/game_messagebox.md).

## Changes since 1.38

- `game_round_start`, `game_round_end` and the **Reset at round start** key are new
- The game now triggers entities named `game_round_<N>` when round N starts, `game_round_failed` when a round is
  lost, and `game_mission_success` or `game_mission_failed` when the mission ends

## See also

- [Co-op](../../game-modes/coop.md) - how Co-op rounds and missions work
- [Trigger modes](trigger-modes.md) - the use types On, Off, Toggle and Set
- [Masters and states](masters-and-states.md) - states that you can reset at each round
- [Map names and spawns](../basics/map-names-and-spawns.md) - spawn points and spawn zones
