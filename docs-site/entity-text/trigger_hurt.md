A `trigger_hurt` is a brush trigger that hurts the players, monsters and objects inside it, or heals them if you give
it a negative damage.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns it on or off, and **Obey Trigger Mode** sets how (see
  [Trigger modes](../guide/trigger-modes.md)). Without a name, the trigger is always on
- **Target** (`target`) - The trigger fires this each time it hurts or heals something, and passes that entity
  on as the [activator](../guide/entity-triggering.md#target-selectors). See [Common keys](common-keys.md#targetx)
- **Delay before trigger** (`delay`) - Sets how many seconds the trigger waits before it fires the **Target**.
  Default 0
- **KillTarget** (`killtarget`) - Removes the entities with this name each time the trigger fires its targets, and
  it works without a **Target** too. The name can end in `*`. See
  [Entity triggering](../guide/entity-triggering.md#wildcards) for more details
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  the trigger neither hurts anything nor fires its targets
- **Damage** (`dmg`) - Sets how much damage the trigger deals per second. It deals half of the value every 0.5
  seconds, and a negative value heals. Default 10
    - If you leave this key empty, it is 0 and the trigger deals no damage
- **Untouchable entity name** (`untouchable_ent_name`) [[ported:featureful]] - The trigger never hurts an entity
  with this class name or this name, for example [`monster_scientist`](monster_scientist.md)
- **Minimum health threshold** (`min_health`) [[ported:featureful]] - The damage never takes health below this
  value, so something that already has this much health or less takes no damage. Empty or 0 means no minimum
- **Gibbing policy** (`gib_policy`) [[ported:featureful]] - Sets what happens to a body that this trigger kills
    - Default (0, default) - The body only breaks into gibs if the damage takes its health far below 0
    - Always gib (1) - The body always breaks into gibs
    - Never gib (2) - The body never breaks into gibs
- **Damage Type** (`damagetype`) - Sets the kind of damage. Some types show an icon on the player's HUD or change a
  rule, and the rest deal plain damage like GENERIC
    - GENERIC (0, default) - Plain damage
    - CRUSH (1) - Plain damage
    - BULLET (2) - Plain damage
    - SLASH (4) - Plain damage
    - BURN (8) - Shows the fire icon
    - FREEZE (16) - Shows the cold icon
    - FALL (32) - Battery armor doesn't reduce it
    - BLAST (64) - Plain damage
    - CLUB (128) - Plain damage
    - SHOCK (256) - Shows the shock icon
    - SONIC (512) - Plain damage
    - ENERGYBEAM (1024) - Plain damage
    - DROWN (16384) - Shows the drowning icon, and battery armor doesn't reduce it
    - PARALYSE (32768) - Plain damage
    - NERVEGAS (65536) - Shows the nerve gas icon
    - POISON (131072) - Shows the poison icon. After the last hit, the player keeps losing 2 health every 2 seconds
      for about 10 seconds
    - RADIATION (262144) - Shows the radiation icon, and players near the trigger hear a Geiger counter
    - DROWNRECOVER (524288) - Gives the player back the health they lost to drowning, over a few seconds
    - CHEMICAL (1048576) - Shows the chemical icon
    - SLOWBURN (2097152) - Shows the fire icon
    - SLOWFREEZE (4194304) - Shows the cold icon
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) [[ported:featureful svencoop]] - Sets how a trigger turns the
  entity on and off
    - No (0, default) - Every trigger switches it, so on becomes off and off becomes on
    - Yes (1) - On turns it on, Off turns it off and Toggle switches it

## Flags

- **Target Once** (1) - Fires the **Target** and the **KillTarget** only the first time the trigger hurts something
- **Start Off** (2) - The trigger starts off, and it needs a **Name** so you can turn it on
- **No clients** (8) - Hurts monsters and objects, but not players
- **FireClientOnly** (16) - Fires the **Target** only when the trigger hurts a player
- **TouchClientOnly** (32) - Hurts only players
- **Affect non-moving NPC's** (64) [[ported:featureful]] - Also hurts monsters that stand still inside the trigger,
  where normally it only hurts a monster while the monster moves. It doesn't work with the damage type RADIATION
- **Full dmg every 0.5 seconds** (128) [[ported:featureful]] - Deals the whole **Damage** every 0.5 seconds instead
  of half of it
- **Ignore Armor** (256) [[ported:featureful]] - Battery armor doesn't reduce the damage, and the player keeps it
  (see [Armor](#armor))
- **No Camera Punch** (512) [[ported:featureful]] - A player's view doesn't jerk when the trigger hurts them

## Armor

A player can have two kinds of armor, but only one of them works against a trigger.

- **Loadout armor** - The armor skin, the cyber torso armor and the torso + skull armor (see
  [Loadout](../../playing/loadout.md#armor)). This armor only protects against hits on body parts, and a trigger
  doesn't hit a body part. So loadout armor never reduces trigger damage, and **Ignore Armor** makes no difference
- **Battery armor** - Armor from an [`item_battery`](item_battery.md) or a [`func_recharge`](func_recharge.md), on
  a player with no loadout armor. It takes half of the damage, as in Half-Life, but not FALL or DROWN damage, and
  **Ignore Armor** turns it off for this trigger

## Notes

- The trigger hurts every player inside it every 0.5 seconds
- A healing trigger doesn't heal dead players, and it doesn't raise health above the maximum
- With **Affect non-moving NPC's**, the trigger checks the box around the brush for monsters that stand still. If the
  brush isn't a box, a monster outside the brush can get hurt
- If you set both **No clients** and **TouchClientOnly**, the trigger hurts nothing
- In a rare case, a shot hits a player on a body part that their armor doesn't cover. Right after that, trigger damage
  to another player whose loadout armor covers that part is reduced, and that player hears a ricochet sound.
  **Ignore Armor** stops this

## See also

- [`trigger_hurt_remote`](trigger_hurt_remote.md) - hurts or heals entities by name or class when you trigger it,
  without a brush
- [`game_player_hurt`](game_player_hurt.md) - hurts or heals the player who triggers it
- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [Trigger modes](../guide/trigger-modes.md) - the use types On, Off, Toggle and Set

## Changes since 1.38

- You can use the new keys **Untouchable entity name**, **Minimum health threshold**, **Gibbing policy** and
  **Obey Trigger Mode**
- You can use the new flags **Affect non-moving NPC's**, **Full dmg every 0.5 seconds**, **Ignore Armor** and
  **No Camera Punch**
- Fixed a healing `trigger_hurt` healing dead players. It did not check that the player was alive. This was a bug in
  SBO 1.38
- Fixed the Master key doing nothing on `button_target`, `trigger_hurt`, `trigger_push`, `trigger_monsterjump`,
  `momentary_rot_button` and a triggered `game_player_equip`. These entities never checked their Master, so they
  worked while locked
- Fixed a `trigger_hurt` with only a Kill target not removing that target. It fired its targets only when it also had
  a Target
