---
description: "A player_calc_ratio gives a number from a player, such as their health, armor, ammo or inventory items, to the keys that take a locus number."
---
A `player_calc_ratio` gives a number from a player to the keys that take a [locus number](../guide/locus.md): the
player's health, armor, ammo, inventory items or maximum speed, as the value itself or as a share of its maximum.

It does nothing when you trigger it, and it works out its value each time a key of another entity reads it. The player
is the activator of the chain of triggers that reads it, for example the player who pressed a button.

## Attributes

- **Value** (`calc_param`) - Sets what it reads from the player
    - Ammo, with the loaded clips (3) - It also adds the bullets in every weapon of that ammo type
- **Inventory item** (`item_name`) - For "Inventory item count", names the item by its **Item name**. Only the
  player's own items count, not the items the team shares
- **Number as** (`value_notion`) - Sets whether it gives the value itself or a share of its maximum
    - Absolute (0) - The value itself
    - Fraction [0..1] (1) - The value as a share of its maximum, from 0 to 1. The maximum is the player's maximum
      health for health, 100 for armor and the player's normal speed for speed
    - For ammo, the maximum is the most the player can carry. With "Ammo, with the loaded clips", the magazine sizes
      are added to it
    - For an inventory item, the fraction is 1 if the player has any and 0 if they have none
- **Ammo type** (`ammo_name`) - For "Ammo", sets which ammo it counts

## Notes

- It gives no number if the activator isn't an alive player, for example a dead player or the world. The entity
  that reads it then does nothing that time
- It also gives no number if "Ammo" has no **Ammo type**, or if "Inventory item count" has no **Inventory item**

## See also

- [`calc_ratio`](calc_ratio.md) - changes a number
- [`trigger_compare`](trigger_compare.md) - compares two numbers
- [calc_ entities guide](../../guides/calc-entities.md) - how locus numbers are worked out

## Changes since 1.38

- `player_calc_ratio` is new, and its **Value** "Inventory item count" was added in SBO 2.1.0
