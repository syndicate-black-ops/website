The Demon Slave is a monster that only fights up close, with two claw swipes. Its hunter version,
[`monster_hunter`](monster_hunter.md), seeks out players across the map.

## Attributes

- **Squad Name** (`netname`) - Gives the Demon Slave a group name. When it spots an enemy and cries out, every monster
  with the same **Squad Name** within 512 units is provoked and goes after that enemy too. Demon Slaves don't form
  squads, so the name only does this
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Demon Slave's AI picks its animations

## Flags

- **Wait until provoked** (64) - The Demon Slave ignores players until it is hurt, hears a fight nearby or a
  monster with the same **Squad Name** within 512 units calls it

## In combat

Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in `server.cfg`
or in the server console). The Demon Slave has 200 health at junior (0), 500 at normal (1), which is the default, 1000
at hardcore (2) and 1800 at survivor (3).

It attacks with two claw swipes, each of which reaches 100 units. A swipe deals more damage when the Co-op round has
more players, and outside Co-op it uses the value for 7 or more players:

| Players in the round | 1 or 2 | 3 or 4 | 5 or 6 | 7 or more |
|---|---|---|---|---|
| Swipe damage | 20 | 25 | 30 | 40 |

These are the damage values at normal monster damage, and the server setting
[`mp_juniorpowmonst`](../../server/settings.md#monsters) picks other values, from 10 to 30 at junior up to 55 to 100
at very powerful. Explosions deal 10 times their damage to it, and electric hits don't hurt it at all. Players earn XP
for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_hunter`](monster_hunter.md) - the hunter version
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed Wait until provoked doing nothing on Sectum, Demon Slaves, Demon Slave Hunters, Werewolves and Werewolf
  Hunters. They attacked as soon as they saw a player. This was a bug in SBO 1.38
- Fixed Demon Slaves and Werewolves losing the flags that the map gives them, such as Fade Corpse, as soon as they
  wake up. The game cleared their flags the first time they moved. This was a bug in SBO 1.38
