A `monstermaker` makes monsters while the map runs, one every **Frequency** seconds while it is on, until it has made
its **Number of Monsters**. It can pass names, paths, weapons, flags and any other key on to the monsters it makes.

## Attributes

- **Target On Release** (`target`) - Fires each time the maker makes a monster, before the monster appears, or after
  it if you set **Target's Activator**
- **Children's Name** (`netname`) - Gives every monster the maker makes this name
- **Children's squad name** (`squadname`) - Gives every monster the maker makes this squad name
- **Children's weapons** (`weapons`) - Gives every Fed the maker makes these weapons, and for a Fed with heavy weapons,
  1 gives the chaingun and 8 the sniper rifle
    - The monster's own (0, default) - Each Fed keeps its own weapons
- **Children's Ignore Friendly Damage** (`Ff`) - Sets whether every Fed, Assassin and turret the maker makes ignores
  damage from its allies
    - If you leave this key empty, it is No
- **Children's Target (path)** (`childtarget`) - Names the [`path_corner`](path_corner.md) or
  [`path_track`](path_track.md) that every monster the maker makes walks or flies along
    - If you leave this key empty, the monsters get no path
- **Children's TriggerTarget** (`childtriggertarget`) - Gives every monster the maker makes this **TriggerTarget**,
  which the monster fires when its **Children's Trigger Condition** happens
- **Children's Trigger Condition** (`childtriggercondition`) - Gives every monster the maker makes this **Trigger
  Condition**, which works like a monster's own
- **Children's spawnflags** (`childspawnflags`) - Gives every monster the maker makes these flags on top of its own,
  as the sum of the monster's flag values, so for example 32 gives a [`monster_apache`](monster_apache.md) **Fire
  Rockets**. An Apache that the maker makes only waits for a trigger with 64 (**Start Inactive**), and not with 4,
  because bit 4 is this maker's **MonsterClip** for its monsters
- **Monster Type** (`monstertype`) - Sets the kind of monster the maker makes. "Rappelling Fed" and "Rappelling Fed
  Hunter" make a rope spot instead, so you fire the **Children's Name** to send a Fed down. Each spot counts as a live
  monster for good, and the children keys don't reach the Fed
    - If you leave this key empty, the game removes the maker when the map starts and writes a line in the server
      console
- **Number of Monsters** (`monstercount`) - Sets how many monsters the maker makes in all, where -1 means no limit.
  The server setting [`mp_makermon`](../../server/settings.md#monsters) changes this number and **Max live
  children**, and [`mp_speedmon`](../../server/settings.md#monsters) changes the **Frequency**. You set both in
  `server.cfg` or in the server console
    - If you leave this key empty, there is no limit
- **Children's body** (`body`) - Gives every monster the maker makes this body, such as the head of a Scientist or
  the look of a Sectum. Feds and Zombie Grunts keep their own body, because their body also sets their gun
    - If you leave this key empty or set 0, each monster keeps its own body
- **Children's scale** (`scale`) - Gives every monster the maker makes this [model scale](../features/model-scale.md)
    - If you leave this key empty, each monster keeps its own size
- **Frequency** (`delay`) - Sets how many seconds pass between two monsters. To make a new monster only when the last
  one dies, set **Max live children** to 1
    - If you leave this key empty or set 0, the maker doesn't wait and makes monsters as fast as it can
- **Max live children** (`m_imaxlivechildren`) - The maker makes no new monster while this many of its monsters are
  alive, and 0 or less counts as 1
    - If you leave this key empty, there is no limit
- **Spawn position** (`spawnorigin`) - Sets where each monster appears, as a [locus position](../guide/locus.md) that
  the maker works out again for each monster, so it can be `x y z`, an entity name or `!activator`
    - If you leave this key empty, monsters appear at the maker
- **Face position** (`face_position`) - Sets the point each monster faces when it appears, as a locus position, where
  `*player` is the nearest alive player
    - If you leave this key empty, monsters face the way the maker faces
- **Warpball** (`warpball`) - Names an [`env_warpball`](env_warpball.md) that plays where each monster appears
- **Warp at monster's...** (`impulse`) - Sets where on the new monster the warpball plays
- **Delay before spawn** (`spawndelay`) - Sets how many seconds pass between the warpball and the monster appearing
    - If you leave this key empty or set 0, the monster appears at once
- **Delay after blocked** (`delay_after_blocked`) - Sets how many seconds the maker waits before it tries again when
  something stood on the spot
    - If you leave this key empty, it waits the **Frequency**
- **Target's Activator** (`target_activator`) - Sets the activator that **Target On Release** gets
    - Don't pass activator (-1) - The targets get no activator
    - Default (Monstermaker, before the monster spawns) (0) - The maker, and the targets fire before the monster
      appears
    - Monstermaker (after the monster spawns) (1) - The maker, and the targets fire after the monster appears
    - Spawned monster (2) - The new monster
    - Forward my activator (3) - The entity that triggered the maker
- **Max yaw deviation** (`yawdeviation`) - Turns each monster by a random amount, up to this many degrees to the left
  or the right
- **Trigger on death notice** (`trigger_on_death_notice`) - Fires each time one of the maker's monsters dies
- **Children's classification** (`classify`) - Sets the class every monster the maker makes fights in, from the
  classes on the [Monster classes](../guide/monster-classes.md) page
    - If you leave this key empty or set 0, each monster keeps its own side
- **Reverse Relationship** (`respawn_as_playerally`) - With Yes, every monster the maker makes changes sides, as with
  **Is player ally**
- **Make blocker move away** (`make_blocker_move_away`) - Sets whether the maker asks a monster that stands on the
  spot to move away, and whether that monster walks or runs
- **Gag** (`gag`) - With Yes, every monster the maker makes gets **Gag**, so it makes no idle sounds
- **Override Render Mode** (`change_rendermode`) - With Yes, every monster the maker makes gets this maker's render
  settings

## Flags

- **Start ON** (1) - A named maker starts making monsters when the map loads, the first one after **Frequency**
  seconds, and a maker without a name always runs
- **Cyclic** (4) - Each trigger makes one monster, instead of turning the maker on and off
- **MonsterClip** (8) - [`func_monsterclip`](func_monsterclip.md) brushes block the monsters the maker makes
- **Prisoner** (16) - The monsters get **Prisoner**, so they see nobody and no monster sees them
- **Auto size BBox** (32) - The check for a free spot before a monster appears uses the monster's own size, instead of
  a box of 68 by 68 units below the maker
- **Cyclic backlog** (64) - With **Cyclic**, a trigger that finds the spot blocked is kept, and the maker makes the
  monster once the spot is free
- **Pre-Disaster** (256) - The monsters get **Pre-Disaster**
- **Monster Flag 64** (8192) - The monsters get the monster flag 64, which is **Start Inactive** for Apaches and
  turrets and **Wait until provoked** for the Sectum, the Demon Slave and its hunter, and the Werewolf and its hunter
- **Non-solid corpse** (65536) - The monsters' corpses aren't solid
- **Ignore move away requests** (524288) - Players who push a monster the maker made don't make it step aside
- **Act out of PVS** (1048576) - The monsters look, listen and act even when no player is near them

## Keys for the monsters [[ported:hlunified]]

A key whose name starts with `#` goes to every monster the maker makes, under its name without the `#`, so a key
`#unkillable` with the value `1` makes every monster unkillable. The monster gets these keys before it spawns, the
way a monster placed in the map gets its keys, and the maker's own children keys, such as **Children's Target
(path)**, apply after them. The maker loads what these keys name, such as a sound file, when the map loads, and you
add these keys in the editor with SmartEdit turned off.

A maker accepts up to 64 such keys, and with `developer 1` set in the console, the console notes each key past that.
The keys `#model`, `#new_model`, `#health`, `#max_health`, `#displayname` and `#classname` aren't passed on, and with
`developer 2` set in the console, the console notes each one. You can't add or change a `#` key while the map runs,
because a new value could need a file that the map hasn't loaded.

## Notes

- A maker with a name and **Start ON** makes its first monster **Frequency** seconds after the map starts, and its
  first trigger turns it off
- A monster that dies frees its place among **Max live children**, and so does a shot-down Apache or Osprey or a
  destroyed turret
- A [`monster_turret`](monster_turret.md) that the maker makes only comes out by itself with **Children's spawnflags**
  32, which is the turret's **Autostart**
- The corpses of the maker's monsters fade out, except when **Number of Monsters** is 1
- The server can make **Number of Monsters** and **Max live children** half as large, but never below 1, twice or
  three times as large, and it can make the **Frequency** delay twice as long, half or a third as long, or turn every
  maker off. A maker that is turned off this way makes nothing, and it starts again when the setting changes back
- Once the map runs, [`trigger_changevalue`](trigger_changevalue.md) and [`trigger_copyvalue`](trigger_copyvalue.md)
  can only set **Monster Type** to a class that the map already loads, which is a class the map places, one that
  another maker makes, or a morph monster, and on a maker with `#` keys they can't change it at all. A refused change
  leaves the maker's class as it was, and with `developer 1` set in the console, the console says why
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) gives a maker that
  made its last monster a new **Number of Monsters**, it starts again, so a maker that was on makes its next monster
  after **Frequency** seconds and a cyclic one takes triggers again. The server's `mp_makermon` scales the new count
  as it scales the map's, and reading the key back gives the monsters still to make before that scaling. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`env_warpball`](env_warpball.md) - the teleport effect a maker can play
- [`monster_apache`](monster_apache.md) - a monster with its own rules for makers
- [Co-op: monsters](../../game-modes/coop.md#monsters) - the server settings for monster strength
- [monstermaker on TWHL](https://twhl.info/wiki/page/monstermaker) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Children's Target (path)**, **Children's TriggerTarget**, **Children's Trigger
  Condition**, **Children's spawnflags**, **Children's weapons**, **Children's squad name**, **Children's Ignore
  Friendly Damage**, **Children's body**, **Children's scale**, **Children's classification**, **Spawn position**,
  **Face position**, **Warpball**, **Warp at monster's...**, **Delay before spawn**, **Delay after blocked**,
  **Target's Activator**, **Max yaw deviation**, **Trigger on death notice**, **Reverse Relationship**, **Make blocker
  move away**, **Gag** and **Override Render Mode**
- Fixed a monster maker of 1 monster making monsters without end when the server halves monster counts. Half of 1 is
  0, which the maker read as no limit. This was a bug in SBO 1.38
- Fixed a named monster maker with Start ON not starting with the map (its first trigger turned it off)
- Fixed a shot-down Apache or Osprey keeping its place in its monster maker. The maker never heard that it died. This
  was a bug in SBO 1.38
- Fixed a destroyed turret or Sentry Gun keeping its place in its monster maker. The maker never heard that it died.
  This was a bug in SBO 1.38
- Fixed an Apache from a monster maker with MonsterClip waiting for a trigger forever. The MonsterClip flag has the same
  value as the Apache's Wait for trigger flag. This was a bug in SBO 1.38
- Fixed a monster maker without a monster type stopping the server when the map loaded. It tried to load a monster
  with an empty name
- `mp_speedmon -1` turns off the map's monster makers
- A key written as `#name` on a monster maker is passed on as `name` to every monster it makes
- Fixed a bug in monster maker set to unlimited monsters (-1) stopping after about 4.29 billion monsters had been
  spawned. If anyone wants to confirm, run the any map for 138 years and let me know if it's fixed
