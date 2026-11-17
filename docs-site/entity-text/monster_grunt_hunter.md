---
description: "The Fed Hunter is a Fed with a rifle or a shotgun and hand grenades who seeks out players across the map."
---
The Fed Hunter is a Fed with a rifle or a shotgun and hand grenades who seeks out players across the map instead of
waiting where you placed it. The Fed that stays where you place it is [`monster_human_grunt`](monster_human_grunt.md).

## Attributes

- **Squad Name** (`netname`) - Gives the Fed a squad name, so Feds with the same name form one squad, which only forms
  around the one with **SquadLeader** set
    - If you leave this key empty, the Fed forms a squad with others of its kind that it can see within 1024 units
- **Weapons** (`weapons`) - Sets the gun the Fed carries, and the choices with **HG** also throw hand grenades
    - If you leave this key empty or set 0, the Fed carries the Federal and hand grenades
- **Ignore Friendly Damage** (`Ff`) - Sets whether damage from monsters on its side hurts it
    - No (0, default) - All damage hurts it
    - Yes (1) - Damage from monsters on its side doesn't hurt it

## Flags

- **SquadLeader** (32) - With a **Squad Name**, this Fed gathers the others with that name into its squad and leads
  it, and a named squad without a leader never forms

## In combat

It knows where every player and monster within 12000 units is, even through walls, and goes after its enemies across
the map.

A Fed has 100 health, and its Federal rifle fires one bullet per shot for 12 to 29 damage. With the default value 1 of
the server setting [`mp_junioracmar`](../../server/settings.md#monsters), its Saan Auto-Shotgun fires 4 pellets per
shot, or 6 when the Co-op round has 7 or more players and outside Co-op, and each pellet deals 30 to 45 damage. Other
values of `mp_junioracmar` change the number of pellets. You set `mp_junioracmar` in `server.cfg` or in the server
console. A Fed aims more tightly when the Co-op round has more players and when `mp_junioracmar` is higher, and
outside Co-op it aims as it does for 7 or more players. Up close, it kicks for 10 damage. Players earn XP for the
damage they deal to it. See [Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_human_grunt`](monster_human_grunt.md) - the Fed that stays where it is placed
- [`monster_grunt_hunter_repel`](monster_grunt_hunter_repel.md) - a Fed Hunter that slides down a rope
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- Fixed Ignore Friendly Damage turning off on Feds, Heavy Weapons Feds, Fed Hunters, Assassins and Sentry Guns when
  the map gave another key after it. Every later key set it back to off. This was a bug in SBO 1.38
