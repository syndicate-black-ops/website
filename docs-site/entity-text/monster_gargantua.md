The Gargantua is a huge monster with flame throwers, a stomp that travels along the ground, and claw swipes.

## Attributes

- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Gargantua's AI picks its animations

## In combat

Its health depends on the server setting [`mp_juniorpvmonst`](../../server/settings.md#monsters) (set in `server.cfg`
or in the server console). The Gargantua has 5000 health at junior (0), 15000 at normal (1), which is the default,
30000 at hardcore (2) and 50000 at survivor (3). Every kind of damage hurts it, and explosions deal 10 times their
damage. Each time its flames update, they deal 30 burn damage along the flame and 20 in a small area where they hit,
and its stomp and each claw swipe deal 30 damage. Players earn XP for the damage they deal to it. See
[Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength
- [monster_gargantua on TWHL](https://twhl.info/wiki/page/monster_gargantua) - the Half-Life entity
