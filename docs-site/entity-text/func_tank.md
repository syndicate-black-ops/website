A `func_tank` is a mounted gun that aims at targets by itself, or that a player controls from a
[`func_tankcontrols`](func_tankcontrols.md).

The keys it shares with the other mounted guns, such as the turn rates, the barrel and the targets, are in the table
below.

## Attributes

- **Bullets** (`bullet`) - Picks the bullets the gun fires, which set the damage of each bullet when **Damage Per
  Bullet** is 0
    - None (0) - The gun fires no bullets
    - 9mm (1) - 8 to 22 damage for each hit
    - MP5 (2) - 12 to 29 damage for each hit
    - 12mm (3) - 21 to 56 damage for each hit
- **Bullet gib policy** (`bullet_gib_policy`) - Sets whether its bullets break what they kill into gibs
    - Default for func_tank (0) - With a **Damage Per Bullet** above 16 the kill breaks into gibs, at 16 or less it
      never does, and without a **Damage Per Bullet** the game decides by the damage
    - Normal (1) - The game decides by the damage
    - Never gib (2) - Kills never break into gibs
    - Always gib (3) - Kills always break into gibs
- **Damage Per Bullet** (`bullet_damage`) - Sets the damage of each bullet, and 0 uses the damage of the **Bullets**
  type
- **Bullet accuracy** (`firespread`) - Sets how far the bullets stray from where the gun points, in a cone that gets
  wider with each choice
    - Perfect Shot (0) - Every shot goes where the gun points
    - Small cone (1)
    - Medium cone (2)
    - Large cone (3)
    - Extra-large cone (4)

## Notes

- The player at the controls gets the kills of the gun: the frags, the Co-op XP and the line in the kill feed. While
  nobody is at the controls, no player gets them
- Once the map runs, [`trigger_changevalue`](trigger_changevalue.md) and [`trigger_copyvalue`](trigger_copyvalue.md)
  can't change **Smoke Sprite** or **Flash Sprite**, so the gun keeps its sprites, and with `developer 1` set in the
  console, the console says why
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) sets **Rate of
  Fire** to 0 or below, the tank fires one shot a second, and an accuracy outside the list is Perfect, as when the map
  loads. See [Changing keys](../guide/changing-keys.md)

## See also

- [`func_tankcontrols`](func_tankcontrols.md) - the place where a player takes the controls
- [`func_tanklaser`](func_tanklaser.md) - a mounted laser
- [`func_tankmortar`](func_tankmortar.md) - a mounted mortar
- [`func_tankrocket`](func_tankrocket.md) - a mounted rocket launcher
- [func_tank on TWHL](https://twhl.info/wiki/page/func_tank) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Player weapon volume**, **Fire Master**, **Bullet count**, **Behavior/Classification**,
  **Extra barrels name**, **Trigger on firing**, **Smoke sprite render mode** and **Bullet gib policy**, and the new
  flags **Laser Spot**, **Match Target** and **Smoke on empty**
