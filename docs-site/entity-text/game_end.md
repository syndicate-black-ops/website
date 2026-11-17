A `game_end` ends a [Co-op](../../game-modes/coop.md) mission in success when you trigger it, and every player's
screen shows **SUCCESSFULL MISSION**. A few seconds later, the scoreboard shows and the server loads the next map.

It only works on Co-op maps, so on other maps, triggering it does nothing.

## Attributes

- **Name** (`targetname`) - Triggering the entity ends the mission. See [Common keys](common-keys.md#targetname)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing

## Notes

- Only the first mission result counts, so a `game_end`, a [`mission_failed`](mission_failed.md) or a
  [`change_touch`](change_touch.md) after it changes nothing
- The server setting [`mp_missionendtime`](../../server/settings.md#rounds-and-missions) (set in `server.cfg` or the
  server console) sets how long the end of the mission lasts

## See also

- [`mission_failed`](mission_failed.md) - ends the mission in failure
- [`change_touch`](change_touch.md) - ends the mission in success when a player touches it
- [Co-op: mission end](../../game-modes/coop.md#mission-end) - what happens when a mission ends

## Changes since 1.38

- Fixed a Co-op mission showing both FAILED MISSION and SUCCESSFULL MISSION when the map triggers both. The game showed
  every result and could count the second one. Now only the first result shows and counts. This was a bug in SBO 1.38
