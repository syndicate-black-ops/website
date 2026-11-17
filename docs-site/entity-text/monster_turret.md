The Auto Turret is a large gun that comes out of the floor or the ceiling and fires at enemies.

## Attributes

- **Target** (`target`) - Names the entities it fires, which get On when the turret switches on and when it is
  destroyed, and Off when it switches off
- **Custom Search Time** (`maxsleep`) - Sets how many seconds the turret keeps searching after it lost its enemy,
  before it goes back in
    - If you leave this key empty or set 0, it is 15
- **Orientation** (`orientation`) - Sets whether the turret stands on the floor or hangs from the ceiling, and a
  ceiling turret is turned upside down and aims downward
- **Custom Turning Rate** (`turnrate`) - Sets how fast the turret starts turning, in degrees per second, and when it
  is far off its target, it speeds up to as much as 10 times this
    - If you leave this key empty or set 0, it is 30
- **Ignore Friendly Damage** (`Ff`) - Sets whether damage from monsters on its side hurts it
    - No (0, default) - All damage hurts it
    - Yes (1) - Damage from monsters on its side doesn't hurt it

## Flags

- **Autostart** (32) - The turret comes out by itself when it sees an enemy and goes back to watching after it
  retracts, while without this flag, it only comes out when you trigger it
- **Start Inactive** (64) - With **Autostart**, the turret doesn't watch for enemies until you trigger it once

## In combat

The turret has 200 health, but while it is retracted, damage to it is cut to a tenth, and each of its bullets
deals 21 to 56 damage. With **Fade Corpse** (512), the wreck fades out once its smoke ends,
and so does the wreck of one that a [`monstermaker`](monstermaker.md) made, unless the maker's **Number of Monsters**
is 1.

## Death trigger [[ported:hlunified]]

If **Trigger Condition** or **Trigger Alternative Condition** is "Death", the turret fires its **TriggerTarget** when it
is destroyed, once its death ends. A turret only checks its trigger conditions when it takes a new enemy, when a hit
leaves it alive and when it is destroyed, so "Got healed" fires at the first hit after the heal.

## See also

- [`monster_miniturret`](monster_miniturret.md) - the small turret
- [`monster_sentry`](monster_sentry.md) - a gun on a tripod
- [monster_turret on TWHL](https://twhl.info/wiki/page/monster_turret) - the Half-Life entity

## Changes since 1.38

- Destroyed turrets, sentry guns and ichthyosaur bodies fade away when the map sets the Fade Corpse flag. Their own
  death code never read the flag. This was a bug in SBO 1.38
- Fixed a destroyed turret or Sentry Gun keeping its place in its monster maker. The maker never heard that it died.
  This was a bug in SBO 1.38
- Fixed turrets, Sentry Guns, the Apache and the Osprey never firing their Trigger Condition. In SBO 1.38, their own AI
  code never checked it
