The heavy weapons Fed fights with a chaingun or a sniper rifle and can also throw hand grenades. The kill feed shows
it as "Fed".

## Attributes

- **Squad Name** (`netname`) - Sets the squad the Fed belongs to. Feds with the same squad name form one squad, and
  the Fed with **SquadLeader** set gathers and leads it
    - If you leave this key empty, the Fed forms a squad with the unnamed monsters on its side that it can see within
      1024 units
- **Weapons** (`weapons`) - Picks the gun the Fed carries, and the choices with HG also throw hand grenades
    - Chaingun (1) - A chaingun
    - Chaingun + HG (3) - A chaingun and hand grenades
    - Sniper (8) - A sniper rifle
    - Sniper + HG (10) - A sniper rifle and hand grenades
    - If you leave this key empty or set 0, the Fed carries a chaingun and hand grenades
- **Ignore Friendly Damage** (`Ff`) - Sets whether monsters and players on the Fed's side can hurt it
    - No (0) - All damage hurts it
    - Yes (1) - Damage from monsters and players on its side doesn't hurt it

## Flags

- **SquadLeader** (32) - With a **Squad Name**, this Fed gathers the other Feds with that name into its squad and
  leads it. A named squad without a leader never forms

## In combat

The Fed has 100 health and kicks for 10 damage in close combat. Its aim gets better with more players in the Co-op
round and with the server's Fed aim setting, and its guns hit like this:

- The **chaingun** fires a burst with each shot, and each bullet deals 12 to 25 damage. At the normal Fed aim, a
  burst has 2 bullets with 1 or 2 players in the Co-op round, 3 bullets with 3 or 4 players, and 4 bullets with 5
  or more players and in the other game modes
- The **sniper rifle** fires one round with each shot, which deals 38 to 60 damage. With more than 8 players in the
  Co-op round, and in the other game modes, the round explodes where it hits and deals 88 to 172 damage

The server setting for the Fed aim is [`mp_junioracmar`](../../server/settings.md#monsters) (set in `server.cfg` or
the server console). Players earn XP for hurting and killing the Fed. See [Co-op](../../game-modes/coop.md#xp) for
more details.

## See also

- [`monster_human_grunt`](monster_human_grunt.md) - the Fed
- [`monstermaker`](monstermaker.md) - spawns monsters while the map runs
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength

## Changes since 1.38

- **Ignore Friendly Damage** works wherever the key is in the entity. In SBO 1.38, any key after it set it back to
  "No"
