The Zombie Grunt is a dead Fed that still shoots, with a rifle or a shotgun and hand grenades.

## Attributes

- **Squad Name** (`netname`) - Gives the Zombie Grunt a squad name, so Zombie Grunts with the same name form one squad,
  which only forms around the one with **SquadLeader** set
    - If you leave this key empty, it forms a squad with others of its kind that it can see within 1024 units
- **Weapons** (`weapons`) - Sets the gun the Zombie Grunt fights with, an MP5 or a SPA shotgun, and the choices with
  **HG** also throw hand grenades
    - If you leave this key empty or set 0, it carries the MP5 and hand grenades

## Flags

- **SquadLeader** (32) - With a **Squad Name**, this Zombie Grunt gathers the others with that name into its squad and
  leads it, and a named squad without a leader never forms

## In combat

The Zombie Grunt has 50 health, and head shots hurt it most. With the MP5, a hit on its head deals about 125 times its
damage, and with the SPA shotgun about 6 times. A hit anywhere else deals its normal damage plus a little, and an
explosion deals about 11 times its damage. Its MP5 fires one bullet per shot for 12 to 29 damage, and its SPA shotgun
fires 4 to 6 pellets per shot, each dealing 30 to 45 damage. It aims more tightly, and the shotgun fires more pellets,
when the Co-op round has more players. Up close, it kicks for 10 damage. Players earn XP for the damage they deal to
it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_zombie`](monster_zombie.md) - the Zombie
- [`monster_human_grunt`](monster_human_grunt.md) - the living Fed
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
