A `player_inventory` gives, takes or sets an inventory item of the player who triggers it, without an
[`item_pickup`](item_pickup.md) in the world. With the flag **Shared**, it works on the team's shared items instead,
and anything can trigger it, the world too.

If it takes an item that came from an `item_pickup`, that pickup is used up and stays hidden until the next round
restart. A shared pickup with **Reset at round start** comes back at the next round start.

Items that this entity gives have no pickup in the world. A player loses a personal item when they die, lose their
weapons or leave, and when a round restarts. Shared items aren't lost this way.

## Attributes

- **Item name** (`item_name`) - Names the item, with up to 31 characters
    - If you leave this key empty and use **Remove** or **Set** with a **Count** of 0 or less, it takes every item
- **HUD icon** (`item_icon`) - Sets the icon that a new item gets on the HUD when this entity gives it
- **Operation** (`operation`) - Sets what the entity does
    - Remove (-1) - It takes the item
    - Use type (0, default) - The [use type](../guide/trigger-modes.md) decides. On and Toggle give and Off takes.
      Set makes the count the value it was triggered with, for example from a
      [`trigger_changevalue`](trigger_changevalue.md) or a `calc_` entity
    - Give (1) - It gives the item
    - Set (2) - It sets the count to **Count**
- **Count** (`count`) - Sets how many it gives, takes or sets. A Give or a Remove counts 0 or less as 1, and a Set of
  0 takes the item
- **Maximum** (`collect_limit`) - Sets the most of the item that a Give or a Set gives
    - If you leave this key empty or set 0, there is no limit, which means 32767
- **On Count Change** (`on_count_change`) - Fires this target when the count changes
- **On Item Limit** (`on_item_limit`) - Fires this target when the item is new and the player already holds 16
  different items
- **On Max Count Limit** (`on_max_count_limit`) - Fires this target when a Give or a Set finds the item at its
  **Maximum** already
- **On Count Overflow** (`on_count_overflow`) - Fires this target when the count goes over **Maximum**. The count
  stays at the maximum unless you set **Allow going over Maximum**
- **Reset at round start** (`round_reset`) - With Yes and **Remove On Fire**, the entity turns off until the next
  round and doesn't remove itself. With **Shared**, the team's count of this item goes back at each round start to
  what it holds from `item_pickup` entities

## Flags

- **Remove On Fire** (1) - The entity removes itself after it fires once
- **Allow going over Maximum** (2) - A Give or a Set may go over **Maximum**
- **Shared** (4) - It works on the team's shared items, and anything can trigger it

## Taking an item

**On Count Change** only fires when the count changes. A Remove triggered by a player who has the item fires it, but a
Remove triggered by a player without the item fires nothing. A [`player_calc_ratio`](player_calc_ratio.md) with the
**Value** "Inventory item count" gives how many of an item a player holds, and a
[`trigger_compare`](trigger_compare.md) can compare that number.

## See also

- [`item_pickup`](item_pickup.md) - an item that players pick up
- [`player_hasinventory`](player_hasinventory.md) - checks whether a player has an item

## Changes since 1.38

- `player_inventory` is new in SBO 2.1.0
