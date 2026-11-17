---
description: "The Cyborg is a large robot that fires plasma bolts from a distance and strikes up close, and it knows where every player is, even through walls."
---
The Cyborg is a large robot that fires plasma bolts from a distance and strikes up close, and it knows where every
player within 12000 units is, even through walls. It doesn't bleed.

## In combat

The Cyborg knows where every player and monster within 12000 units is, even through walls, and goes after its enemies
across the map. Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set
in `server.cfg` or in the server console). The Cyborg has 5000 health at junior (0), 10000 at normal (1), which is the
default, 30000 at hardcore (2) and 55000 at survivor (3).

It fires plasma bolts at enemies up to 8192 units away when its gun has a clear line to them, and each bolt flies at
1800 units per second and deals 30 to 50 damage. In close combat, within 200 units, it strikes for 100 damage, and it
never shoots at a monster that is that close but strikes it instead. Explosions deal 10 times their damage to it.

Players earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_cyberminotor`](monster_cyberminotor.md) - another large monster that hunts players across the map
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed Cyborgs being unable to move about 50% of the time. Their model has a second walk animation with no ground
  movement, and the game picked it at random. This was a bug in SBO 1.38
