A `mission_failed` ends a Co-op mission with a failure when you trigger it, and every player's screen shows **FAILED
MISSION**.

## Attributes

- **Master** (`master`) - Names a [master](../guide/masters-and-states.md), and while the master is off, triggering
  the entity does nothing

## Notes

- Only the first mission result counts
- A few seconds after the result, the scoreboard shows and the server loads the next map. The server setting
  [`mp_missionendtime`](../../server/settings.md#rounds-and-missions) (set in `server.cfg` or in the server console) sets how
  long this takes
- The entity only works on Co-op maps, and on other maps triggering it does nothing

## See also

- [`game_end`](game_end.md) - ends the mission with a success
- [Co-op: mission end](../../game-modes/coop.md#mission-end) - what happens when a mission ends

## Changes since 1.38

- Fixed a Co-op mission showing both FAILED MISSION and SUCCESSFULL MISSION when the map triggers both. The game showed
  every result and could count the second one. Now only the first result shows and counts. This was a bug in SBO 1.38
