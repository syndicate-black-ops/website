---
description: "A multispawn moves the Co-op spawns when you trigger it, to a named spawn set or to the next spawn zone."
---
A `multispawn` moves the Co-op spawns when you trigger it, either to a named [spawn
set](../basics/map-names-and-spawns.md#spawn-sets) or to the next spawn zone: from zone 1, which is the
[`info_player_deathmatch`](info_player_deathmatch.md) entities, to [`info_player_go2`](info_player_go2.md), and so on
up to [`info_player_go5`](info_player_go5.md).

## Attributes

- **Master** (`master`) - Names a [master](../guide/masters-and-states.md), and while the master is off, triggering
  the entity does nothing
- **Spawn set** (`spawnset`) - The name of a spawn set, which is every spawn point
  ([`info_player_deathmatch`](info_player_deathmatch.md) and [`info_player_go2`](info_player_go2.md) to
  [`info_player_go5`](info_player_go5.md)) whose **Name** is this name. When you trigger the entity, that set becomes
  the active one and players spawn only at its points, until another `multispawn` changes the spawns. If you leave
  this key empty, the entity moves the spawns to the next zone instead and ends the active spawn set

## Notes

- Each trigger of a `multispawn` without a **Spawn set** moves the spawns one zone on, and after zone 5 they stay at
  zone 5
- A `multispawn` with a **Spawn set** doesn't move the zone, so a `multispawn` without one later goes on from the zone
  the spawns were in before
- A spawn set's points can be of any of the five spawn point classes, and the game picks a point of the set the same
  way it picks one of a zone
- If no spawn point has the name in **Spawn set**, players spawn in the active zone as if no set were active, and with
  `developer 1` set in the console, a message says so
- [`trigger_changevalue`](trigger_changevalue.md) can change **Spawn set** while the map runs, and the new name is
  used the next time you trigger the `multispawn`
- Every map starts at zone 1 with no spawn set active, and players spawn in the new zone or set from the next round
  on. A new round doesn't reset the map, so it keeps the zone and the set
- The entity only works on Co-op maps, and on other maps triggering it does nothing

## See also

- [Map names and spawns](../basics/map-names-and-spawns.md) - spawn points and spawn zones
- [Spawn sets](../basics/map-names-and-spawns.md#spawn-sets) - how named spawn sets and zones work together
- [Co-op: map entities](../../game-modes/coop.md#map-entities) - the entities that control Co-op

## Changes since 1.38

- Spawn points can be grouped into spawn sets by giving them a name, and the new Spawn set key of `multispawn`
  switches to any set, in any order
