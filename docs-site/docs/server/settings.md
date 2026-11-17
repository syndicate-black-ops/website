# Server settings

These are the game's server cvars (console variables) with their defaults. You set them in `server.cfg` on a dedicated
server or in `listenserver.cfg` on a listen server, which the server runs at every map start, and you can also change
them in the server console. The tables also list a few engine settings that the shipped config files set. Their
default is a dash, because the engine gives them their value, not the game.

## Rounds and missions

| Cvar | Default | Effect |
|---|---|---|
| `mp_hardcore` | 100 | In Co-op, the percentage of the players alive at the round start who must die for the round to be lost, from 0 to 100. With 100, the round is lost when every player is dead |
| `mp_easymode` | 1 | In Co-op, gives a map with a [`max_round`](../mapping/entities/max_round.md) 1.5 times the number of rounds it sets, and a map without one 10 rounds instead of 7. Setting it to 0 turns this off |
| `mp_loadouttime` | 45 | In Co-op and Battle Royale, how many seconds a player without a loadout can hold up the round start, counted from when they joined or last used the briefing or loadout menus. After that, the round starts without them. Setting it to 0 waits for every player |
| `mp_missionendtime` | 5 | In Co-op, how many seconds pass from the mission result to the scoreboard and the map change, from 1 to 600. If you set more than 5, the players who are still alive become observers 5 seconds after the result |
| `mp_timelimit` | 20 | How many minutes a map lasts. Setting it to 0 turns the limit off. Has no effect on Co-op maps |
| `mp_fraglimit` | 0 | How many frags end the map. Setting it to 0 turns the limit off. Has no effect on Co-op maps |
| `mp_chattime` | 10 | How many seconds the scoreboard stays up at the end of a map before the next map loads |

See [Co-op](../game-modes/coop.md) for more details on the rules these settings change.

## Players

| Cvar | Default | Effect |
|---|---|---|
| `mp_friendlyfire` | 1 | In Co-op, lets players hurt each other. Setting it to 0 turns this off |
| `mp_ban` | 0 | In Co-op, makes a player who killed 5 or more teammates on the map spawn with 3 health and no weapons, not even fists, when set to 1. That player's model is automatically switched to the Hunted's model from Bounty Killer, and they see "you are a teamKiller". Suicides don't count, and the count starts again when the player rejoins or the map changes |
| `mp_junior` | 0 | Makes hits on players do less damage when set to 1: a head hit does 2 times the damage instead of 10 times, and chest and stomach hits do normal damage instead of 2 and 3 times |
| `mp_flashlight` | 1 | Lets players use the flashlight. Setting it to 0 turns this off |
| `mp_footsteps` | - | An engine setting. Players' footsteps make sounds when they move faster than walking or climb a ladder. Setting it to 0 turns footstep sounds off. The shipped `server.cfg` sets 1, and **Create server** offers it |
| `sv_clienttrace` | - | An engine setting that sets the size of the players' bounding boxes for collisions, but not for movement. The shipped `server.cfg` and `listenserver.cfg` set 3.5 |
| `mp_forcerespawn` | 1 | In Bounty Killer, respawns dead players by themselves after 5 seconds, or sooner if they press a key. Setting it to 0 makes them respawn only when they press a key. Players in Co-op and Battle Royale don't respawn this way |
| `mp_autocrosshair` | 0 | Shows the autoaim crosshair when autoaim (`sv_aim`) has a target, when set to 1. The shipped config files turn autoaim off |
| `decalfrequency` | 30 | How many seconds a player must wait between two sprays |
| `sv_infinite_ammo` | 0 | Makes weapons use no ammo and never reload when set to 1 |
| `sv_allowbunnyhopping` | 0 | Removes the speed limit of bunny hopping when set to 1 |

## Idle players

| Cvar | Default | Effect |
|---|---|---|
| `mp_afk_time` | 60 | How many seconds an alive player can go without input before an AFK sign shows above them. Setting it to 0 turns the sign off |
| `mp_afk_spectate_time` | 0 | How many seconds an alive player can go without input before the game moves them to spectator mode. 0 turns this off |

Only alive players can be idle, and bots never are. Dying or a new round doesn't reset the idle time, but any input
or command does. A player that `mp_afk_spectate_time` moves to spectator mode stays there until they leave it. See
[Spectating](../playing/spectating.md) for more details.

## Semiclip

Semiclip lets players walk through each other for a while after a round starts, so they don't block each other at
the spawn.

| Cvar | Default | Effect |
|---|---|---|
| `mp_semiclip` | 1 | Lets players walk through each other for `mp_semiclip_time` seconds. Setting it to 0 turns semiclip off |
| `mp_semiclip_time` | 15 | How many seconds semiclip lasts after a round starts in Co-op and Battle Royale, or after the map starts in Bounty Killer, from 0 to 180. With 0, semiclip never ends |
| `mp_semiclip_effects` | 1 | Makes players you can walk through fade more the nearer they are. Setting it to 0 gives them a fixed transparency, and only within 200 units |

During semiclip, bullets, blades, explosions, monsters and triggers hit players as usual. When it ends, players who
stand inside each other can still pass through each other until they move apart.

## Monsters

| Cvar | Default | Effect |
|---|---|---|
| `mp_juniorpowmonst` | 1 | How much damage monsters do: 0 is junior, 1 normal, 2 hardcore and 3 very powerful |
| `mp_junioracmar` | 1 | How well the Feds and the Cops aim: 0 is junior, 1 normal, 2 veteran and 3 elite |
| `mp_juniorpvmonst` | 1 | How much health monsters have: 0 is junior, 1 normal, 2 hardcore and 3 survivor |
| `mp_makermon` | 1 | How many monsters a [`monstermaker`](../mapping/entities/monstermaker.md) makes in all and keeps alive at once: 0 is half, 1 normal, 2 double and 3 triple. A change applies from the next map on |
| `mp_speedmon` | 1 | How fast the map's [`monstermaker`](../mapping/entities/monstermaker.md) entities make monsters: 0 is half, 1 normal, 2 double and 3 triple speed, and any other value counts as 1. With -1, the map's monster makers make nothing while the Game Master can still place monsters, so nobody can finish a map that needs the monsters from its makers |

## Game Master

| Cvar | Default | Effect |
|---|---|---|
| `mp_gmmode` | 0 | In Co-op, lets one player at a time become the Game Master with the Game Master key (Default: <kbd>K</kbd>) when set to 1. You can change it during a map |

The server console command `gm_toggle <name or #userid>` turns a player's Game Master mode on or off on any Co-op
map, even when `mp_gmmode` is 0. See [Co-op](../game-modes/coop.md#game-master) for more details on the Game Master.

## Kill feed

| Cvar | Default | Effect |
|---|---|---|
| `mp_killfeed_npc` | 1 | Which monster kills show in the kill feed: 0 shows none, 1 shows monsters killing players and players killing monsters, and 2 shows only monsters killing players |

## Maps

| Cvar | Default | Effect |
|---|---|---|
| `mp_map_compat` | 1 | Applies `maps/map_compat.txt` to the maps it names. Setting it to 0 loads every map as it is. The game reads it when a map starts loading. See [Server files](files.md#map-compatibility) for more details |
| `sv_pushable_fixed_tick_fudge` | 15 | How fast a player pulls a [`func_pushable`](../mapping/entities/func_pushable.md) with the use key, per second. Below 0, the speed is per frame instead |

## Read-only

The game sets these cvars itself, and server browsers read them.

| Cvar | Default | Effect |
|---|---|---|
| `game_version` | The game's version | The SBO version of the server's game library |
| `mp_round` | 0 | In Co-op and Battle Royale, the current round or the last round played. It is 0 before the first round |
| `mp_roundlimit` | 0 | In Co-op, the map's number of rounds. It is 0 in the other modes |
| `mp_timeleft` | 0 | How many seconds are left on the map while a time limit counts down |
| `mp_fragsleft` | 0 | How many frags are left before the frag limit |

## Changes since 1.38

- The game's settings have SBO's defaults in the game itself, and `game.cfg` no longer overrides `server.cfg` on every
  map
- Fixed the shipped `game.cfg` resetting the **Create server** choices of a listen server on every map. It forced its
  own values on every map load
- The default for `mp_hardcore` is now 100 instead of 80
- On a listen server, the default time limit is now 20 minutes instead of 15, and Game Master mode is now off by default. A dedicated
  server already got these values from `server.cfg`
- The default for `mp_autocrosshair` is now 0 instead of 1
- The next map loads `mp_chattime` seconds after the end-of-map scoreboard shows. In SBO 1.38 it also waited up to 2
  minutes for a key press, and a click on the scoreboard did not count as one
- New settings: `mp_loadouttime`, `mp_missionendtime`, `mp_semiclip`, `mp_semiclip_time`, `mp_semiclip_effects`,
  `mp_afk_time`, `mp_afk_spectate_time`, `mp_killfeed_npc`, `sv_infinite_ammo`, `sv_allowbunnyhopping`,
  `sv_pushable_fixed_tick_fudge` and `mp_map_compat`
- The read-only settings `mp_round`, `mp_roundlimit` and `game_version` show the round, the round limit and the game
  version
- `mp_speedmon -1` turns off the map's monster makers
- The server command `gm_toggle <name or #userid>` turns a player's Game Master mode on or off
- `mp_allowmonsters` is removed. In SBO 1.38 the setting worked the wrong way round: 1 removed every monster
- `mp_XP` has been removed. XP and levels are always on, and Create server no longer shows the option
- `mp_falldamage` has been removed. It did nothing, fall damage always depends on the speed of the fall

## See also

- [Server files](files.md) - the files a server reads and writes
- [Co-op](../game-modes/coop.md) - the rules of Co-op maps, which most of these settings change
- [Spectating](../playing/spectating.md) - spectator mode, where idle players go
