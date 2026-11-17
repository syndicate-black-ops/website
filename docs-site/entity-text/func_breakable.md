A `func_breakable` breaks into pieces when it takes enough damage or when you trigger it, with the sound and the gibs
of its material. It can drop an object, explode, and fire its **Target** when it breaks.

## Flags

- **Only Trigger** (1) - Only a trigger breaks it, and no damage lowers its health, not even a monster's melee
  attack
- **Touch** (2) - A player who runs into it breaks it when their speed divided by 100 is at least its **Strength**,
  and the player takes a quarter of that as damage
- **Pressure** (4) - It breaks when a player stands on it, after its **Delay before fire**
- **Invert Hit Vector** (16) - With **Trigger when hit**, the entity reverses the horizontal part of the hit
  direction that it passes on, so the direction points back toward the shooter
- **Instant Crowbar** (256) - A player's melee hit breaks it at once, even when its **Strength** is high. This
  flag is set by default
- **Explosives Only** (512) - Only explosions hurt it, so bullets and melee hits do nothing
- **Not solid** (4096) - Players, monsters and shots pass through it, but a trigger can still break it
- **Smoke trails on gibs** (8192) - The gibs trail smoke as they fly
- **Transparent gibs** (16384) - The gibs are drawn see-through

## Notes

- If **Gibs Direction** is "Relative to Attack", the gibs fly away from the attacker when damage breaks it. With
  "Random", they fly in random directions
- Unbreakable Glass never breaks, not even when you trigger it

## See also

- [`func_breakable_effect`](func_breakable_effect.md) - plays the break of a breakable, with nothing to break
- [`func_pushable`](func_pushable.md) - a brush players can push, which can also be breakable
- [func_breakable on TWHL](https://twhl.info/wiki/page/func_breakable) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Custom number of gibs**, **Custom gib scale**, **Trigger when hit**, **Target's
  Activator**, **Spark When Hit** and **Switch Texture When Damaged**, and the new flags **Invert Hit Vector**,
  **Explosives Only**, **Not solid**, **Smoke trails on gibs** and **Transparent gibs**
- A breakable with **Only Trigger** keeps its health when a monster hits it in melee. In SBO 1.38, these hits
  lowered its health and could break it
- With **Gibs Direction** "Relative to Attack", the gibs fly away from the attacker. In SBO 1.38, they flew toward
  the attacker
- New in SBO 2.1.0: **Spawn On Break** also takes a class name
