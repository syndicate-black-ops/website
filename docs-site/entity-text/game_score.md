A `game_score` adds points to the score of the player who triggers it, or takes points away.

## Attributes

- **Name** (`targetname`) - Triggering the entity changes the score of the player who started the chain of
  triggers. Only a player can do it. See [Common keys](common-keys.md#targetname)
- **Points to add** (`points`) - Sets the points added to the score, and a negative number takes points away
    - If you leave this key empty, it is 0 and the score doesn't change
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing

## Flags

- **Allow Negative** (1) - Taking points can push a score below 0. Without this flag, a score stops at 0
- **Team Points** (2) - The points go to the teammates of the player instead of the player. The game modes have no
  teams, so nobody gets them

## See also

- [`game_player_settings`](game_player_settings.md) - changes the Co-op level and XP of a player
- [game_score on TWHL](https://twhl.info/wiki/page/game_score) - the Half-Life entity

## Changes since 1.38

- A trigger with no player at the start of the chain of triggers does nothing. In SBO 1.38, as in Half-Life, it
  crashed the server
