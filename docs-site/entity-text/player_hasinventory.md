---
description: "A player_hasinventory checks whether the player who triggers it carries an inventory item, and fires Pass Target or Fail Target."
---
A `player_hasinventory` checks whether the player who triggers it carries an inventory item, and fires **Pass Target**
if they have it and **Fail Target** if they don't. As the **Master** of a door, a button or a trigger, it makes that
entity work only for a player who carries the item. Items come from [`item_pickup`](item_pickup.md) and
[`player_inventory`](player_inventory.md).

![Room 1 of the inventory test map: the door locked while the red keycard is on its stand, the card in the HUD's inventory row after the pickup, and the door open for the player who carries it](../../assets/img/screens/keycard-door.webp)

*A door that opens only for the player who carries the red keycard*

## Attributes

- **Item name** (`item_name`) - Names the item to check for, by its **Item name**
- **Pass Target** (`pass_target`) - Fires this target if the player has the item. With **Shared**, it fires this
  target if the team's shared items hold the item
- **Fail Target** (`fail_target`) - Fires this target if the player doesn't have the item, or with **Shared**, if the
  shared items don't hold it

## Flags

- **Shared** (4) - It checks the team's shared items instead, and it answers any activator, the world too. Without
  this flag, it only answers an alive player

## See also

- [`item_pickup`](item_pickup.md) - an item that players pick up, with a keycard door example
- [`player_hasweapon`](player_hasweapon.md) - the same check for a weapon
- [Masters and states](../guide/masters-and-states.md) - entities that lock others

## Changes since 1.38

- `player_hasinventory` is new in SBO 2.1.0
