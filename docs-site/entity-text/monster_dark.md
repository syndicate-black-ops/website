The Sectum is a monster that attacks from a distance with two lightning beams, and it only fights up close when it has
to.

## Attributes

- **Squad Name** (`netname`) - Gives the Sectum a group name. When it spots an enemy and calls out, every monster with
  the same **Squad Name** within 512 units learns about the enemy and attacks it
    - If you leave this key empty, it calls no one
- **Body** (`body`) - Sets the Sectum's head
    - Random (-1, default) - Each Sectum picks one of the four heads when it spawns
    - If you leave this key empty, it has the head Butcher

## Flags

- **Wait until provoked** (64) - The Sectum ignores players until it is hurt, or until another monster with the same
  **Squad Name** within 512 units calls it about an enemy

## In combat

Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in `server.cfg`
or in the server console). The Sectum has 100 health at junior (0), 210 at normal (1), which is the default, 450 at
hardcore (2) and 700 at survivor (3).

It attacks from a distance with two lightning beams, one from each arm, which reach 1024 units, and after a beam
attack it waits 0.5 to 4 seconds before the next one. Each beam deals more damage when the Co-op round has more
players, and outside Co-op it uses the value for 7 or more players:

| Players in the round | 1 or 2 | 3 or 4 | 5 or 6 | 7 or more |
|---|---|---|---|---|
| Beam damage | 20 | 25 | 30 | 50 |

These are the damage values at normal monster damage, and the server setting
[`mp_juniorpowmonst`](../../server/settings.md#monsters) picks other values. Up close, it swipes with its claws for 30
damage each, with a reach of 70 units. Explosions deal 10 times their damage to it, and electric hits don't hurt it at
all. Players earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_alien_slave`](monster_alien_slave.md) - the Demon Slave, which only fights up close
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed Wait until provoked doing nothing on Sectum, Demon Slaves, Demon Slave Hunters, Werewolves and Werewolf
  Hunters. They attacked as soon as they saw a player. This was a bug in SBO 1.38
