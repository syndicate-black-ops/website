---
description: "Battle Royale maps (br_*) put every player against every other player in rounds, and the last player alive wins the round."
---

# Battle Royale

Battle Royale maps (`br_*`) put every player against every other player in rounds, and the last player alive wins the
round. Players do not choose a loadout in Battle Royale, each round you spawn as a random agent with one random
weapon, item or bonus. Every kill awards you a point, the last kill of a round awards 5 instead, and the player who
wins the round gets 3 additional points.

## Joining

When you join a Battle Royale server, a small menu with one choice, **1.go**, opens. Once you choose it, you are
ready and you spectate until the next round starts. See [Equipment](#equipment) for more details on the random
items.

## Rounds

![How Battle Royale rounds run: the game checks every 10 seconds whether a round can start, and a player still choosing can hold it up to 45 seconds. With only 1 player ready, that player spawns and waits for players. With 2 or more ready, the round starts, and with mp_semiclip on (the default) players walk through each other for 15 seconds. When only 1 player or nobody is alive, the round is over, the player still alive scores 3 and the next round comes 5 seconds later. If the others leave or go to spectator mode, the round ends with no winner and the game checks again 10 seconds later | 480](../assets/img/diagram-br-rounds.webp)

*How a Battle Royale round starts and ends*

### Round start

A round needs at least two players who chose **go**. A player who hasn't selected **go** yet can hold up the round start
for up to 45 seconds by default, counted from when they joined or last used the menus. The game checks every 10
seconds whether a round can start, and again right away when a player chooses **go** or leaves.

While only one player is ready, that player spawns once and can move around the map while a message shows **Waiting
for players...**, and the round starts as soon as a second player is ready.

At the start of a round, every ready player spawns with a new random item and **ROUND START** shows on every player's
screen. Players can walk through each other for 15 seconds by default.

### End of a round

A player who dies spectates until the next round. The round ends when only one player or nobody is still alive, and
then **ROUND OVER** shows and the next round starts 5 seconds later.

If the other players leave the server or enter persistent spectator mode and only one of the round's players is left
in the game, the round ends without a winner, and the game waits 10 seconds before it checks again.

## Score

| Event | Score |
|---|---|
| The last kill of the round (instead of +1) | +5 |
| Winning the round (being the last player alive) | +3 |
| Any other kill during a round | +1 |

Deaths from the world, such as falls and drowning, and deaths from monsters cost no score.

## End of the map

The map ends when its time is up, after 20 minutes by default, or when a player reaches the server's frag limit,
which is off by default. The scoreboard then shows, and the server loads the next map from the map cycle.

## Equipment

Every player spawns with their fists and one random item, as a male or a female agent at random. If the map has a
[`game_player_equip`](../mapping/entities/game_player_equip.md) without the **Use Only** flag, players also get its
items at every spawn.

Each spawn draws one of 40 chances, and each item below has the number of chances in its row:

| Chance | Item |
|---|---|
| 3 in 40 each | Croon RC 28, Canon of terror, Croon PM 66 and Saan auto-shotgun |
| 2 in 40 each | Fusion warhammer, Chainsaw sword, Energy sword, .444k Bear killer, Croon FA 18, Vindico plasma sniper, Croon NM 33 sniper, Vindico Federal, Benelli and Pitbull |
| 1 in 40 each | Grenades, mines, satchels, Vindico grenade launcher, Vindico Avenger minigun, nuclear rocket launcher and medikit |
| 1 in 40 | No item, but 150 armor and a speed of 500 until your next weapon switch |

See [Weapons and items](../playing/weapons-and-items.md) for more details on each item.

## Map entities

| Entity | Effect |
|---|---|
| [`info_player_deathmatch`](../mapping/entities/info_player_deathmatch.md) | A spawn point |
| [`game_player_equip`](../mapping/entities/game_player_equip.md) | Players get its items at every spawn on top of their fists and their random item, unless its **Use Only** flag is set |

The game triggers the entities named `game_round_start` at the start of every round, `game_round_<N>` right after it
(for example `game_round_2`), and `game_round_end` at its end. See [Round hooks](../mapping/guide/round-hooks.md) for
more details.

## Settings

These server settings affect every game mode, including Battle Royale. You set them in `server.cfg` or in the server console. See
[Server settings](../server/settings.md) for more details.

| Cvar | Default | Effect |
|---|---|---|
| [`mp_loadouttime`](../server/settings.md#rounds-and-missions) | 45 | How many seconds a player who hasn't chosen **go** can hold up the round start. Setting it to 0 makes the round wait for every player |
| [`mp_semiclip`](../server/settings.md#semiclip) | 1 | Lets players walk through each other after a round starts. Setting it to 0 turns this off |
| [`mp_semiclip_time`](../server/settings.md#semiclip) | 15 | How many seconds players can walk through each other after a round starts |
| [`mp_timelimit`](../server/settings.md#rounds-and-missions) | 20 | How many minutes a map lasts. Setting it to 0 turns the limit off |
| [`mp_fraglimit`](../server/settings.md#rounds-and-missions) | 0 | How many frags end the map. Setting it to 0 turns the limit off |
| [`mp_chattime`](../server/settings.md#rounds-and-missions) | 10 | How many seconds the scoreboard stays up before the next map loads |

## Changes since 1.38

- Suicides no longer cost points in Battle Royale and Bounty Killer. In SBO 1.38 a suicide cost 5 points in Battle
  Royale and 10 in Bounty Killer, which only made matches last longer
- Fixed a single player in Battle Royale losing their weapons and respawning with "ROUND START" every 10 seconds. The
  game now waits for a second player
- A player who has not chosen a loadout, or **go** in Battle Royale, holds up the round start for at most 45 seconds. In
  SBO 1.38 the round waited for that player with no time limit

## See also

- [Game modes](index.md) - the three modes side by side
- [Co-op](coop.md) - all players against the monsters
- [Bounty Killer](bounty-killer.md) - everyone hunts one player
