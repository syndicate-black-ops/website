---
description: "SBO has three game modes: Co-op, Battle Royale and Bounty Killer."
---

# Game modes

SBO has three game modes: Co-op, Battle Royale and Bounty Killer. The start of a map's name sets which mode it plays,
and a map whose name has none of these prefixes, such as a Half-Life deathmatch map, plays Bounty Killer.

| Prefix | Mode | What happens |
|---|---|---|
| `co_` | [Co-op](coop.md) | Players on one team complete missions and fight against monsters in rounds |
| `br_` | [Battle Royale](battle-royale.md) | Every player fights every other player in rounds, and the last player alive wins the round |
| `bk_` | [Bounty Killer](bounty-killer.md) | One player is the Hunted while every other player hunts them, and whoever kills the Hunted becomes the next Hunted |

## The modes side by side

| | Co-op | Battle Royale | Bounty Killer |
|---|---|---|---|
| Rounds | Yes | Yes | No |
| After you die | You respawn at the next round | You respawn at the next round | You respawn after a few seconds |
| Loadout | You choose it | No loadout. You spawn as a random agent with one random weapon, item or bonus | You choose it |
| Monsters | Yes, and many get stronger the more players are in the round | Only those the map places | Only those the map places |
| The map ends | When the mission succeeds or fails | At the time or frag limit | At the time or frag limit |
| Friendly fire | A server setting, on by default | Always on | Always on |

## Spectators

In every mode you can enter persistent spectator mode by typing `spectate` in the console or `/spec` in the chat.
Spectators never count toward rounds, scores or how strong the monsters are, and you stay in spectator mode after you
reconnect or the map changes. See [Spectating](../playing/spectating.md) for more details.
