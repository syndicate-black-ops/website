The Apache is an attack helicopter with a chaingun that can also fire rockets, and it flies along a path of
[`path_corner`](path_corner.md) entities.

## Attributes

- **Target** (`target`) - Names the [`path_corner`](path_corner.md) the Apache flies to first, and from there it
  follows the path
- **Rotor sound volume** (`rotorvolume`) - Sets how loud the rotor is, from 0.1 for quiet up to 1 for full volume
    - If you leave this key empty or set 0, the rotor plays at full volume
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets what triggers do to an Apache that waits for a trigger
    - No (0, default) - The first trigger starts it, and later triggers do nothing
    - Yes (1) - On starts it, and Off or Toggle stops it in the air with its rotor silent, until On starts it again

## Flags

- **Wait For Trigger** (4) - The Apache waits until you trigger it, but an Apache that a
  [`monstermaker`](monstermaker.md) makes only waits with **Start Inactive**
- **Explode sooner in the air** (8) - A shot-down Apache that is still in the air explodes 4 seconds after it dies,
  instead of 15, and with or without this flag, it explodes at once when it hits something on the way down
- **Fire Rockets** (32) - The Apache also fires rockets in pairs, 10 for each load with 10 seconds to reload, and each
  rocket deals 150 blast damage. On a path, it fires along its body while its nose points down, as in Half-Life, and
  without a path, it fires when its enemy is in sight and within 60 degrees of its nose and aims each rocket at the
  middle of the enemy's body
- **Start Inactive** (64) - The Apache waits until you trigger it
- **No Wreckage** (1024) - The Apache crashes and explodes as usual but leaves nothing behind, so no smoking wreck and
  no burst of metal debris

## In combat

The Apache has 250 health, and explosions deal 2 times their damage to it. A shot only hurts it if it hits the cockpit
or an engine or deals more than 100 damage, and bullets that hit the rotor blades never hurt it. Its chaingun fires
one bullet at a time, and each bullet deals 12 to 25 damage. Its **Trigger Condition** works, including "Take Damage"
and "50% Health Remaining", and players earn XP for the damage they deal to it. See
[Co-op](../../game-modes/coop.md#xp) for more details.

## See also

- [`monster_osprey`](monster_osprey.md) - a helicopter that drops Feds
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [monster_apache on TWHL](https://twhl.info/wiki/page/monster_apache) - the Half-Life entity

## Changes since 1.38

- You can use the new flags **Fire Rockets** and **No Wreckage** and the new keys **Rotor sound volume** and **Obey
  Trigger Mode**, while the SBO 1.38 Apache never fired rockets
- Fixed an Apache from a monster maker with MonsterClip waiting for a trigger forever. The MonsterClip flag has the same
  value as the Apache's Wait for trigger flag. This was a bug in SBO 1.38
- Fixed a shot-down Apache or Osprey keeping its place in its monster maker. The maker never heard that it died. This
  was a bug in SBO 1.38
- Fixed turrets, Sentry Guns, the Apache and the Osprey never firing their Trigger Condition. In SBO 1.38, their own AI
  code never checked it
