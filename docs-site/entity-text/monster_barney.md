The Cop is a guard with a pistol who fights on the side of the Feds, so Cops are enemies of the players.

## Attributes

- **Gun State** (`bodystate`) - Sets whether the Cop starts with its gun in the holster or in its hand
    - Random (-1) - Each Cop picks one of the two at random
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Cop's AI picks its animations

## In combat

The Cop has 100 health, and each pistol shot deals 8 to 22 damage. It aims more tightly when the Co-op round has more
players and when the server setting [`mp_junioracmar`](../../server/settings.md#monsters) (set in `server.cfg` or in
the server console) is higher. Outside Co-op, it aims as it does for 7 or more players. Players earn XP for
the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## Notes

- A Cop only follows a player who presses the use key on it if it is a player ally, through **Is player ally** or the
  **Classification** "Player ally", and its **Followage policy** is Regular. See [Common keys](common-keys.md#talkmonster)
  for more details

## See also

- [`monster_barney_dead`](monster_barney_dead.md) - a dead Cop for decoration
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength
- [monster_barney on TWHL](https://twhl.info/wiki/page/monster_barney) - the Half-Life entity

## Changes since 1.38

- Fixed every Cop following a player who pressed the use key on it, even though Cops fight on the side of the Feds. A
  Cop now only follows if it is a player ally with the **Followage policy** Regular
