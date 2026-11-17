# Server logs

When you turn logging on with `log on` in the server console or `server.cfg`, the server writes the game's events to
its log files in `syndicate/logs/` and to the console. Each line starts with the date and time, such as
`L 11/02/2026 - 20:15:03: `, and a player appears as `"<name><<user id>><<Steam ID>><<user id>>"`, for example
`"Fed<12><STEAM_0:1:23456><12>"`.

## Players

| Line | When |
|---|---|
| `"<player>" entered the game` | A player joins the game |
| `"<player>" disconnected` | A player leaves |
| `"<name>" (<address>) refused: game version <version>, the server needs <minimum> or newer` | The server turns away a player whose game is too old. `<version>` is `none` when the player's game sent no version. |
| `"<player>" client "<version>" "<system>" "<engine>" "<renderer>"` | Once per connection, a moment after the player joins. See [Client info](#client-info) for more details |
| `"<player>" changed name to "<new name>"` | A player changes their name |
| `"<player>" say "<text>"` | A player sends a chat message |

Entering or leaving spectator mode writes no log line, and neither does an idle player's AFK sign or their move to
spectator mode.

### Client info

Once per connection, the server writes which game the player plays with, which helps with bug reports and
statistics. The SBO version comes from the information the player's game sends when it connects. A moment after the
player joins, the server also asks the player's game for a few console settings, and from the answers it tells the
operating system, the engine and the renderer. It writes the line as soon as all the answers are back, or 30 seconds
later with the answers it has by then. A bot gets its line as soon as it joins, and a reconnect writes a new line, but
a map change doesn't. The answers only go to the server, so nothing is added to the player's info and other players
receive nothing.

```text
L 11/08/2026 - 20:28:00: "Player<2><STEAM_0:1:1234><2>" client "SBO 2.1.0" "Linux" "HL25" "OpenGL"
```

| Value | What it can be |
|---|---|
| Version | `SBO 2.1.0`, which has a build part on a development build, such as `SBO 2.1.0+1a2b3c4d`. It is `none` when the game sent no version, which happens for an HLTV proxy or the host of a listen server on an old build, and `bot` for bots |
| System | `Windows` or `Linux`. It is `unknown` for an older game or one that didn't answer, and `none` for bots |
| Engine | `HL25` is Steam Half-Life since its 25th anniversary update, and `legacy` is its `steam_legacy` beta. It can also be `Xash3D`, `bot` or `unknown` |
| Renderer | `OpenGL` or `software`. It is `unknown` when the game didn't answer, and `none` for bots |

## Kills

| Line | When |
|---|---|
| `"<killer>" killed "<victim>" with "<weapon>"` | A player kills another player |
| `"<player>" committed suicide with "<weapon>"` | A player kills themselves |
| `"<player>" was killed by "<monster>"` | A monster kills a player. The monster has the name it has in the kill feed, for example `"Fed"`, `"Cop"` or `"Auto Turret"`, and every kind of Fed is `"Fed"`. A monster that a Game Master placed is `"<Game Master>'s <monster>"`, for example `"Sadako's Fed"` |
| `"<player>" committed suicide with "<cause>" (world)` | A player dies from the world, for example from a fall, a trigger, water or a gun turret with nobody at its controls |

The weapon is its short name, such as `rc28`, `k444` or `sword`. A grenade from the Vindico grenade launcher is
`glauncher` and a hand grenade is `grenade`. When one of the map's gun turrets kills someone, the kill line or the
world line names the turret as the weapon, whether or not a player is at its controls:

| Turret | Weapon |
|---|---|
| [`func_tank`](../mapping/entities/func_tank.md) | `tank` |
| [`func_tanklaser`](../mapping/entities/func_tanklaser.md) | `tanklaser` |
| [`func_tankrocket`](../mapping/entities/func_tankrocket.md) | `tankrocket` |
| [`func_tankmortar`](../mapping/entities/func_tankmortar.md) | `tankmortar` |

A player at a turret's controls gets the turret's kills, so the line reads `"<player>" killed "<victim>" with "tank"`.

In SBO 1.38, a `func_tankrocket` rocket was `rpg_rocket`, a `func_tankmortar` blast was `env_explosion`, and the beam
of a `func_tanklaser` with nobody at its controls was `env_laser`. SBO 1.38 also wrote `grenade` for a Vindico grenade
launcher kill, the same as a hand grenade.

SBO 2.0.0 used other monster names in the kill lines:

| SBO 2.1.0 and newer | SBO 2.0.0 |
|---|---|
| `"Cop"` | `"Barney"` |
| `"Sectum"` | `"Sectum Streuoum"` |
| `"Scientist"` | `"Sectum"` |
| `"Cyber Minotaur"` | `"Big Streum"` |
| `"Cyborg"` | `"Big Cyborg"` |
| `"Demon Slave"`, for every Demon Slave | `"Alien Slave"` for a `monster_hunter` |
| `"Fed"`, for every Fed | `"Grunt"` for a rappelling Fed |

## Rounds and missions

The game writes round and mission events as `World triggered` lines. Bounty Killer writes none.

| Line | Mode | When |
|---|---|---|
| `World triggered "Round_Start" (round "<n>" of "<rounds>")` | Co-op | A round starts, and `<rounds>` is the map's number of rounds |
| `World triggered "Round_End" (round "<n>" of "<rounds>")` | Co-op | A round ends |
| `World triggered "Successful_Mission"` | Co-op | The mission succeeds |
| `World triggered "Failed_Mission"` | Co-op | The mission fails |
| `World triggered "Round_Start" (round "<n>" of "infinite")` | Battle Royale | A round starts |
| `World triggered "Round_End" (round "<n>" of "infinite")` | Battle Royale | A round ends |
| `World triggered "BR_Round_Winner" (round "<n>", winner "<name>", authid "<Steam ID>", wins "<w>")` | Battle Royale | One player is left at the end of a round, and `<w>` counts that player's round wins on the map |
| `World triggered "BR_Round_Winner" (round "<n>", winner "none")` | Battle Royale | Nobody is left at the end of a round, or more than one player is |
| `World triggered "BR_Map_Winner" (winner "<name>", authid "<Steam ID>", wins "<w>", rounds "<r>")` | Battle Royale | The map ends, and this names the player with the most round wins |
| `World triggered "BR_Map_Winner" (winner "draw", wins "<w>", rounds "<r>")` | Battle Royale | The map ends and several players share the most wins |
| `World triggered "BR_Map_Winner" (winner "none", rounds "<r>")` | Battle Royale | The map ends and no round had a winner |

## Changes since 1.38

- The server log has round and mission lines
- The server log writes a player killed by a monster as killed by that monster. In SBO 1.38 it wrote that death as a
  suicide
- The server log names each gun turret in its kill lines
- A Vindico grenade launcher kill is `glauncher` instead of `grenade`, so the kill feed shows the grenade launcher icon
  instead of the hand grenade icon
- The server log has a line for each player with their game version, system, engine and renderer, and a line for each
  player it turns away for an old game version

## See also

- [Server settings](settings.md) - every setting, with its default
- [Co-op](../game-modes/coop.md) - how Co-op rounds and missions work
- [Battle Royale](../game-modes/battle-royale.md) - how Battle Royale rounds and winners work
