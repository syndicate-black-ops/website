---
description: "An info_player_deathmatch is a player spawn point of spawn zone 1. Every game mode spawns its players at these points."
---
An `info_player_deathmatch` is a player spawn point of spawn zone 1. Every game mode spawns its players at these
points, and in Co-op, a [`multispawn`](multispawn.md) can move the spawns to the zones 2 to 5.

## Attributes

- **Name** (`targetname`) - Puts the point in the spawn set with this name, which a [`multispawn`](multispawn.md)
  with this name as its **Spawn set** makes active. While no set is active, players don't spawn at an
  `info_player_deathmatch` with a name, because it belongs to its set only, unless every `info_player_deathmatch` on
  the map has a name
- **Target** (`target`) - Names the entities to trigger each time a player spawns there, and passes on that player as the
  [activator](../guide/entity-triggering.md#target-selectors)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  players don't spawn at this point

## How a spawn point is picked

The first spawn on a map, and the first after a change of zone or spawn set, starts at any point of the active spawn
zone or set, and each later spawn starts 1 to 9 points on from the last one used. From there, the game takes the first
point with no player within 128 units, and it skips points whose master is off. When every point of the zone or set is
taken, the player spawns at the first point tried, and the players who stand there aren't moved. When the active zone
has no point at all, players spawn at the first [`info_player_start`](info_player_start.md).

## See also

- [`info_player_go2`](info_player_go2.md) to [`info_player_go5`](info_player_go5.md) - the spawn zones 2 to 5
- [`multispawn`](multispawn.md) - moves the spawns to the next zone or to a named spawn set
- [Co-op](../../game-modes/coop.md#map-entities) - the entities of a Co-op map

## Changes since 1.38

- New in SBO 2.1.0: the key **Name** puts the point in a spawn set, which a [`multispawn`](multispawn.md) can make
  active, so you can switch between any number of spawn sets in any order, where in SBO 1.38 the spawns could only
  move on, zone by zone, up to zone 5
- The first spawn on a map can use any point of the zone, where in SBO 1.38 every spawn stepped 1 to 5 points on
  from the last one used, so the first spawn on a map always used one of the first 5 points of the zone
- Players who stand on a taken spawn point stay where they are when another player spawns there, where in SBO 1.38
  they were pushed away
