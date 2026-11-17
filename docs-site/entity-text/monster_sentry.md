The Sentry Gun is a gun on a tripod that turns to its enemies and fires. A touch or a hit wakes it up, and it doesn't
switch itself off.

## Attributes

- **Target** (`target`) - Names the entities it fires, which get On when the Sentry Gun switches on and when it is
  destroyed, and Off when it switches off
- **Custom Turning Rate** (`turnrate`) - Sets how fast the Sentry Gun starts turning, in degrees per second, and when it
  is far off its target, it speeds up to as much as 10 times this
    - If you leave this key empty or set 0, it is 30
- **Ignore Friendly Damage** (`Ff`) - Sets whether damage from monsters on its side hurts it
    - No (0, default) - All damage hurts it
    - Yes (1) - Damage from monsters on its side doesn't hurt it

## Flags

- **Autostart** (32) - The Sentry Gun switches itself on when it sees an enemy, while without this flag, it stays off
  until you trigger, touch or hit it
- **Start Inactive** (64) - With **Autostart**, the Sentry Gun doesn't look for enemies until you trigger it once

## In combat

The Sentry Gun has 100 health, and each of its bullets deals 12 to 29 damage. With **Fade Corpse** (512), the wreck
fades out once its smoke ends, and so does the wreck of one that a [`monstermaker`](monstermaker.md) made, unless the maker's **Number of Monsters**
is 1.

## Death trigger [[ported:hlunified]]

If **Trigger Condition** or **Trigger Alternative Condition** is "Death", the Sentry Gun fires its **TriggerTarget** when it
is destroyed, once its death ends. A Sentry Gun only checks its trigger conditions when it takes a new enemy, when a hit
leaves it alive and when it is destroyed, so "Got healed" fires at the first hit after the heal.

## See also

- [`monster_turret`](monster_turret.md) - the large auto turret
- [`monster_miniturret`](monster_miniturret.md) - the small turret
- [monster_sentry on TWHL](https://twhl.info/wiki/page/monster_sentry) - the Half-Life entity

## Changes since 1.38

- Destroyed turrets, sentry guns and ichthyosaur bodies fade away when the map sets the Fade Corpse flag. Their own
  death code never read the flag. This was a bug in SBO 1.38
- Fixed a destroyed turret or Sentry Gun keeping its place in its monster maker. The maker never heard that it died.
  This was a bug in SBO 1.38
- Fixed turrets, Sentry Guns, the Apache and the Osprey never firing their Trigger Condition. In SBO 1.38, their own AI
  code never checked it
- Fixed the Sentry Gun ignoring its Custom Turning Rate. It never read the key. This was a bug in SBO 1.38
- Fixed Ignore Friendly Damage turning off on Feds, Heavy Weapons Feds, Fed Hunters, Assassins and Sentry Guns when
  the map gave another key after it. Every later key set it back to off. This was a bug in SBO 1.38
