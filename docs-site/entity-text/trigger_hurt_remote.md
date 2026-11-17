A `trigger_hurt_remote` damages or heals entities by name or by class when you trigger it, without a brush. It works
once for each trigger, or every few seconds while it is on.

## Attributes

- **Target** (`target`) - Names the entities it hurts, and `!activator` is whoever triggered it
- **Target class name** (`targetclass`) - Hurts every entity of this class too, and `player` means every alive
  player. An entity that matches both **Target** and **Target class name** is hurt twice
- **Damage** (`dmg`) - Sets the damage for each trigger, or for each **Delay** with **Constant**. A negative value
  heals, up to the entity's maximum health
- **Damage type** (`damagetype`) - Sets the kind of damage it deals, which picks the HUD damage icon. Armor doesn't
  stop "FALL" or "DROWN", and kinds such as "POISON" or "RADIATION" keep hurting a player for a while
- **Gibbing policy** (`gib_policy`) - Sets whether a kill turns the body into gibs
- **Delay** (`delay`) - With **Constant**, sets how many seconds pass between two hurts while it is on
    - If you leave this key empty or set 0, it is 0.1
- **Minimum health** (`min_health`) - Damage never takes health below this. With a minimum, poison, nerve gas,
  radiation and the other lasting damage types only hurt once, and the damage after the hit doesn't happen
    - If you leave this key empty or set 0, there is no minimum
- **Armor damage** (`armordmg`) - With **Do armor damage**, sets how much armor each hurt takes from a player, down to
  0. A negative value gives armor, up to 100

## Flags

- **Instant kill** (1) - It kills, and monsters turn to gibs unless **Gibbing policy** is "Never gib". With a negative
  damage, it heals to full health instead
- **Constant** (2) - A trigger switches it on or off, and it obeys On and Off. While it is on, it hurts every
  **Delay** seconds
- **Start on** (4) - With **Constant**, it hurts from the start of the map. Without this flag, it waits for a
  trigger
- **Do armor damage** (8) - Each hurt also takes **Armor damage** from a player's armor
- **Do damage to dead** (16) - It hurts dead bodies too, and a crush, fall, blast, sonic or club hit turns a body into
  gibs
- **Ignore armor** (256) - Armor takes nothing and protects nothing. Armor from a player's armor class only protects
  against hits on its body parts, so it never takes this entity's damage. So the flag only matters for battery armor
  on a player without an armor class
- **No camera punch** (512) - A hurt player's view doesn't kick

## Notes

- It only hurts or heals alive players
- A hit doesn't push the player. The normal damage rules apply as to any hit, so there are random strong and weak
  hits, and armor only protects some parts of the body
- The attacker is the activator of the trigger, or with **Constant**, the activator of the trigger that turned it on.
  So the player who pressed the button gets the kill of a monster. Without an activator, the entity itself is the
  attacker
- When a player's trigger hurts another player, the entity itself is the attacker. So the server setting
  [`mp_friendlyfire`](../../server/settings.md#players) (set in `server.cfg` or in the server console),
  doesn't stop the damage, and the kill feed names `trigger_hurt_remote`

## See also

- [`trigger_hurt`](trigger_hurt.md) - a brush that hurts what touches it
- [`trigger_killmonster`](trigger_killmonster.md) - kills monsters by name or class

## Changes since 1.38

- `trigger_hurt_remote` is new
