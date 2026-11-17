---
description: "The Imp Hunter throws fireballs, bites and swipes with its tail, and it seeks out players across the map."
---
The Imp Hunter is the hunter version of the Imp ([`monster_imp`](monster_imp.md)): it throws fireballs from a
distance, bites and swipes with its tail up close, and seeks out players across the map.

## In combat

It knows where every player and monster within 12000 units is, even through walls, and goes after its enemies across
the map. Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in
`server.cfg` or in the server console). The Imp Hunter has 200 health at junior (0), 410 at normal (1), which is the
default, 680 at hardcore (2) and 1200 at survivor (3).

It throws fireballs at enemies between 64 and 4096 units away, but not at an enemy more than 256 units above or below
it. While it moves, it only throws at enemies up to 216 units away, and it throws one every 5 seconds, while it throws
one every 0.5 seconds when it stands still. Up close, it swipes with its tail, which knocks the target aside, and it
only bites an enemy with 35 health or less. Its attacks grow with the number of players in the Co-op round, and
outside Co-op it uses the values for 7 or more players:

| Players in the round | 1 or 2 | 3 or 4 | 5 or 6 | 7 or more |
|---|---|---|---|---|
| Fireball speed in units per second | 900 | 1100 | 1300 | 1500 |
| Fireball burn damage | 30 | 40 | 50 | 60 |
| Damage up close | 20 | 30 | 35 | 50 |

These are the damage values at normal monster damage, and the server setting
[`mp_juniorpowmonst`](../../server/settings.md#monsters) picks other values. Explosions deal 5 times their damage to
it. Players earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_imp`](monster_imp.md) - the version that stays where it is placed
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength
