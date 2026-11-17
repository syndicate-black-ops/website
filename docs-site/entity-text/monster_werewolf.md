The Werewolf is a monster that only attacks up close and heals itself while it is hurt. Its hunter version is
[`monster_werewolf_hunter`](monster_werewolf_hunter.md).

## Attributes

- **Squad Name** (`netname`) - Gives the Werewolf a group name. When it spots an enemy, every monster with the same
  **Squad Name** within 512 units is provoked and goes after that enemy too
    - If you leave this key empty, it calls no one

## Flags

- **Wait until provoked** (64) - The Werewolf ignores players until it is hurt, or until another monster with the same
  **Squad Name** within 512 units calls it about an enemy

## In combat

With a **Target**, it starts idle and walks its path like other monsters, and without one, it starts alert.

Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in `server.cfg`
or in the server console). The Werewolf has 500 health at junior (0), 900 at normal (1), which is the default, 1500 at
hardcore (2) and 2500 at survivor (3). Once it has 200 health or less, each hit it takes has a 2 in 10 chance to heal
it, by 150, 300, 350 or 550 health at these same settings.

It attacks with two claw swipes, each of which reaches 100 units. A swipe deals more damage when the Co-op round has
more players, and outside Co-op it uses the value for 7 or more players:

| Players in the round | 1 or 2 | 3 or 4 | 5 or 6 | 7 or more |
|---|---|---|---|---|
| Swipe damage | 20 | 25 | 30 | 40 |

These are the damage values at normal monster damage, and the server setting
[`mp_juniorpowmonst`](../../server/settings.md#monsters) picks other values. Claw hits from other monsters on its side
don't hurt it. Players earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more
details.

## See also

- [`monster_werewolf_hunter`](monster_werewolf_hunter.md) - the hunter version
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed Wait until provoked doing nothing on Sectum, Demon Slaves, Demon Slave Hunters, Werewolves and Werewolf
  Hunters. They attacked as soon as they saw a player. This was a bug in SBO 1.38
- Fixed Demon Slaves and Werewolves losing the flags that the map gives them, such as Fade Corpse, as soon as they
  wake up. The game cleared their flags the first time they moved. This was a bug in SBO 1.38
- Fixed a Werewolf with a Target walking its path only after it calmed down. It started alert instead of idle. This
  was a bug in SBO 1.38
- Fixed Werewolves being unable to move about 50% of the time. Their model has a second walk animation with no ground
  movement, and the game picked it at random
