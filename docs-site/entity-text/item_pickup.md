An `item_pickup` is an inventory item in the world, such as a keycard, which a player picks up and carries. The map
checks for it with a [`player_hasinventory`](player_hasinventory.md) and can take it away again with a
[`player_inventory`](player_inventory.md).

Each player sees their items in a row of icons on the left of the HUD, and the items the whole team shares follow
after "TEAM".

![The inventory row: a red keycard and three fuses, then the team's blue keycard after TEAM](../../assets/img/screens/inventory-row.webp)

*The inventory row with keycards and fuses*

The `item_pickup` you place is the item itself. While a player carries it, it is hidden and remembers who holds it,
so it can always go back to where you placed it, which means it is never lost and never exists twice.

## Attributes

- **Model** (`model`) - Sets the model of the item. The model and the **Pickup sound** are loaded with the map, so a
  [`trigger_changevalue`](trigger_changevalue.md) that changes them later does nothing
    - If you leave this key empty, it is the security card of Half-Life
- **Item name** (`item_name`) - Sets the name of the item, up to 31 characters, such as `keycard_red`, and every
  check and every `player_inventory` names the item by it
    - If you leave this key empty, nobody can take the item
- **HUD icon** (`item_icon`) - Picks the icon of the item in the inventory row, as a name from `sprites/hud.txt`. You
  can also type any other name in `hud.txt`, and a name it doesn't have shows the key
    - Key (inv_key)
    - Red keycard (inv_card_red)
    - Blue keycard (inv_card_blue)
    - Yellow keycard (inv_card_yellow)
- **Count** (`count`) - Sets how many the item counts for, from 1 up to 32767
- **Collect limit** (`collect_limit`) - Sets how many of the item a player, or the team with **Shared**, can hold. A
  player can't take the item if that would make them hold more than this many, and 0 means no limit
- **Return time** (`return_timelimit`) - Sets how many seconds a dropped item lies untouched before it goes back to
  where you placed it, and with 0, it goes straight back when its holder dies
- **Keep on death** (`holder_keep_on_death`) - Sets whether the holder keeps the item when they die
    - No (0) - The item drops where the holder died
    - Yes (1) - The holder keeps the item when they die or are stripped, so in Bounty Killer and Battle Royale they
      respawn with it. It still goes back at a round restart or when they leave
- **Reset at round start** (`round_reset`) - For a shared item only, sets whether the team loses it at each round
  start. Personal items always go back
    - No (0) - The team keeps the item
    - Yes (1) - The item is taken back from the team and put on its spot at each round start
- **Pickup sound** (`noise`) - Sets the sound the player hears when they pick up the item
- **Pickup message** (`message`) - Sets a message shown to the player who takes the item

## Flags

- **Shared** (4) - The item goes into one pool for the whole team. Any alive player can use it, and so can the
  world, such as a [`trigger_relay`](trigger_relay.md) or the round hook `game_round_start`, and shared items stay
  across rounds

## What happens to a personal item

| When | What happens to the item |
|---|---|
| Its holder dies | It drops where they died, and any alive player can take it there. Untouched for **Return time**, or out of reach (in a wall, the sky, lava or slime), it goes back to where you placed it. With **Keep on death** they keep it instead. |
| Its holder is stripped (round start, `player_weaponstrip`) | It goes back to its place, unless **Keep on death** is set |
| Its holder leaves, or becomes a spectator or the Game Master | It goes back to its place at once |
| A round restarts | Every personal item goes back to its place before the players spawn |
| A `player_inventory` takes it | It is used up: hidden until the next round restart puts it back |

Deaths and players who leave don't change shared items, and with **Reset at round start**, the team loses a shared
item at each round start, and it goes back to its spot.

## Checking for an item

A [`player_hasinventory`](player_hasinventory.md) with the same **Item name** checks for the item, and as the
**Master** of a door or a button, it only lets that entity work for a player who carries the item.

![Room 1 of the inventory test map: the door locked while the red keycard is on its stand, the card in the HUD's inventory row after the pickup, and the door open for the player who carries it](../../assets/img/screens/keycard-door.webp)

*A door that opens only for the player who carries the red keycard*

Only a `player_hasinventory` that has the flag **Shared** too finds a shared item, and a
[`player_inventory`](player_inventory.md#taking-an-item) that takes the item away uses it up.

## Notes

- Only alive players pick items up
- A player holds at most 16 different items, the team pool holds 16 more, and counts go from 0 up to 32767
- When the map changes, every item is cleared, so a player who reconnects starts with nothing

## See also

- [`player_hasinventory`](player_hasinventory.md) - checks for an item
- [`player_inventory`](player_inventory.md) - gives, takes or sets an item
- [`player_calc_ratio`](player_calc_ratio.md) - **Inventory item count** gives how many of an item a player has

## Changes since 1.38

- `item_pickup` is new in SBO 2.1.0
