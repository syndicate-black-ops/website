The Osprey is a transport aircraft that flies along a path and drops Feds on ropes to replace the map's dead Feds.

## Attributes

- **Target** (`target`) - Names the [`path_corner`](path_corner.md) the Osprey flies to first, and from there it
  follows the path
- **Number of Feds per deploy** (`num`) - Sets how many Feds the Osprey drops at each stop, from 1 to 4, and it only
  drops Feds to replace dead ones
    - If you leave this key empty or set 0, it is 4
- **Trigger on deploy (Osprey)** (`trigger_on_deploy`) - Fires each time the Osprey starts dropping Feds, with the
  Osprey as the activator
- **Trigger on deploy (Fed)** (`trigger_on_deploy_grunt`) - Fires once for each Fed the Osprey drops, with that Fed as
  the activator

## Flags

- **Start Inactive** (64) - The Osprey waits until you trigger it before it starts flying its path, while without this
  flag, it starts one second after the map starts

## In combat

The Osprey has 400 health, and when it crashes, its explosion deals 300 blast damage around it, while smoke comes from
the engine that takes the hit. Its **Trigger Condition** works, including "Take Damage", "50% Health Remaining" and
"Death".

## Its Feds' side

The Feds the Osprey drops take its **Classification** and **Is player ally** keys, so an Osprey with **Is player
ally** set to Yes drops Feds that are player allies too. Without these keys, the Feds keep their own side and fight
the players.

## See also

- [`monster_human_grunt`](monster_human_grunt.md) - the Feds it drops
- [`monster_apache`](monster_apache.md) - the attack helicopter
- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [monster_osprey on TWHL](https://twhl.info/wiki/page/monster_osprey) - the Half-Life entity

## Changes since 1.38

- Fixed Feds dropped by an Osprey ignoring the Osprey's Classification and Is player ally, so an allied Osprey drops
  allied Feds
- You can use the new keys **Trigger on deploy (Osprey)** and **Trigger on deploy (Fed)**
- Fixed a shot-down Apache or Osprey keeping its place in its monster maker. The maker never heard that it died. This
  was a bug in SBO 1.38
- Fixed turrets, Sentry Guns, the Apache and the Osprey never firing their Trigger Condition. In SBO 1.38, their own AI
  code never checked it
- Fixed an Osprey on a closed path with no fast corner hanging the server. It searched the path for a fast corner
  without end. This was a bug in SBO 1.38
- Fixed a hit Osprey smoking from its other engine. A hit on one engine made the other one smoke. This was a bug in
  SBO 1.38
