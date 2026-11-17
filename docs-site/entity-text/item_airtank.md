An `item_airtank` is an oxygen tank that gives a player who touches it 12 more seconds of air under water.

## Attributes

- **Name** (`targetname`) - Gives the tank a name that other entities can use to find it. See
  [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger when a player takes air from it, and again when it is full again. See
  [Common keys](common-keys.md#target)

## Notes

- After a player takes air, the tank gives none for 30 seconds, and then it is full again
- The tank has 20 health, and when it is destroyed, it explodes for 50 damage

## See also

- [`func_water`](func_water.md) - water that can rise and fall
- [item_airtank on TWHL](https://twhl.info/wiki/page/item_airtank) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Object Hint Template** and **Hint Distance**
