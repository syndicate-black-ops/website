---
description: "The Zombie Hunter attacks up close, seeks out players across the map, and only head shots and explosions really hurt it."
---
The Zombie Hunter is the hunter version of the Zombie ([`monster_zombie`](monster_zombie.md)): it attacks up close,
seeks out players across the map, and only head shots and explosions really hurt it.

## In combat

It knows where every player and monster within 12000 units is, even through walls, and goes after its enemies across
the map. It has 50 health, and only head shots and explosions really hurt it. A hit on the head deals 125 times its
damage, which is the Zombie's own 25 times on top of the 5 times that every monster takes from a head shot. A hit from
an explosion deals 10 times its damage, any other hit deals only 1 point, and bullets then deal 30% of these amounts.
It attacks with its claws for 35 damage each, with a reach of 70 units, and players earn XP for the damage they deal
to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_zombie`](monster_zombie.md) - the version that stays where it is placed
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
