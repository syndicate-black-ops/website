---
description: "The Cyber Minotaur is a large monster with a gun for long range and a strike for close combat, and it knows where every player is, even through walls."
---
The Cyber Minotaur is a large monster with a gun for long range and a strike for close combat, and it knows where
every player within 12000 units is, even through walls.

## In combat

The Cyber Minotaur knows where every player and monster within 12000 units is, even through walls. It fights the
enemies it can see first, and when none is in sight, it stays on the last player it saw for 5 seconds. It never
targets spectators or dead players.

Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in `server.cfg`
or in the server console). The Cyber Minotaur has 10000 health at junior (0), 27000 at normal (1), which is the
default, 50000 at hardcore (2) and 75000 at survivor (3).

It shoots at enemies up to 8192 units away when its gun has a clear line to them, and each bullet deals 12 to 29
damage. The server setting [`mp_juniorpowmonst`](../../server/settings.md#monsters) sets how many bullets each shot
has and how far they spread:

| `mp_juniorpowmonst` | Junior (0) | Normal (1) | Hardcore (2) | Very powerful (3) |
|---|---|---|---|---|
| Bullets per shot | 2 | 3 | 4 | 4 |
| Spread | 20 degrees | 15 degrees | 15 degrees | 10 degrees |

In close combat, within 200 units, it strikes for 100 damage. Explosions deal 10 times their damage to it, and players
earn XP for the damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_cyborg`](monster_cyborg.md) - another large monster that hunts players across the map
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed the Cyber Minotaur shooting from a point far away from its gun, often behind it or inside a wall. The game
  placed its gun as if the Cyber Minotaur always faced the same way. This was a bug in SBO 1.38
- Fixed the Cyber Minotaur walking off after Feds behind walls instead of fighting the players it can see. It picked
  its targets without checking that it could see them. This was a bug in SBO 1.38
- Fixed the Cyber Minotaur ejecting no shell casings. The game never set its shell casing model. This was a bug in SBO
  1.38
