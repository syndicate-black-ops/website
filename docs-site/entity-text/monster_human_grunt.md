The Fed is a soldier who fights in a squad, with a rifle or a shotgun and hand grenades or a grenade launcher. Its
hunter version, [`monster_grunt_hunter`](monster_grunt_hunter.md), seeks out players across the map.

## Attributes

- **Stand Ground Range** (`standgroundrange`) - In a fight, the Fed holds its spot and shoots, reloads and waits until
  an enemy it can shoot comes this close, in units
    - If you leave this key empty or set 0, it moves around as usual
- **Squad Name** (`netname`) - Gives the Fed a squad name, so Feds with the same name form one squad, which only forms
  around the one with **SquadLeader** set
    - If you leave this key empty, the Fed forms a squad with others of its kind that it can see within 1024 units
- **Weapons** (`weapons`) - Sets the gun and grenades the Fed carries, where **HG** adds hand grenades and **GL** a
  grenade launcher
    - If you leave this key empty or set 0, the Fed carries the Federal and hand grenades
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Fed's AI picks its animations
- **Ignore Friendly Damage** (`Ff`) - Sets whether damage from monsters on its side hurts it
    - No (0, default) - All damage hurts it
    - Yes (1) - Damage from monsters on its side doesn't hurt it

## Flags

- **SquadLeader** (32) - With a **Squad Name**, this Fed gathers the others with that name into its squad and leads
  it, and a named squad without a leader never forms

## In combat

A Fed has 100 health, and its Federal rifle fires one bullet per shot for 12 to 29 damage. With the default value 1 of
the server setting [`mp_junioracmar`](../../server/settings.md#monsters), its Saan Auto-Shotgun fires 4 pellets per
shot, or 6 when the Co-op round has 7 or more players and outside Co-op, and each pellet deals 30 to 45 damage. Other
values of `mp_junioracmar` change the number of pellets. You set `mp_junioracmar` in `server.cfg` or in the server
console. A Fed aims more tightly when the Co-op round has more players and when `mp_junioracmar` is higher, and
outside Co-op it aims as it does for 7 or more players. Up close, it kicks for 10 damage. Players earn XP for the
damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_grunt_repel`](monster_grunt_repel.md) - a Fed that slides down a rope
- [`monster_grunt_hunter`](monster_grunt_hunter.md) - the hunter version
- [`dark_grunt`](dark_grunt.md) - the Fed with heavy weapons
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [monster_human_grunt on TWHL](https://twhl.info/wiki/page/monster_human_grunt) - the Half-Life entity

## Changes since 1.38

- Fixed Ignore Friendly Damage turning off on Feds, Heavy Weapons Feds, Fed Hunters, Assassins and Sentry Guns when
  the map gave another key after it. Every later key set it back to off. This was a bug in SBO 1.38
- You can use the new key **Stand Ground Range**
