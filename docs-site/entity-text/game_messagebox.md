---
description: "A game_messagebox opens a box with text in the middle of the screen when you trigger it, for one player or for every player."
---
A `game_messagebox` opens a box with text in the middle of the screen when you trigger it, for the player who started
the chain of triggers or for every player.

While a box is open, the player has a mouse cursor, so they can't aim, fire or change weapons, but they can still
walk. They close the box with its **Close** button, ++enter++ or their primary attack key, and a long text gets a
scroll bar, which the mouse wheel, ++page-up++ and ++page-down++ also scroll.

![A message box in game: the about box of co_sbo_showcase](../../assets/img/screens/message-box.webp)

*A message box in game*

## Attributes

- **Name** (`targetname`) - Triggering the entity opens the box. See [Common keys](common-keys.md#targetname)
- **Title** (`title`) - Sets one line in a title bar at the top of the box, and `#Token` is a text from the game's
  language files
    - If you leave this key empty, the box has no title bar
- **Text** (`message`) - Sets the text, where `\n` starts a new line and `#Token` is the text of an entry of
  `titles.txt`, and the text can be at most 1023 bytes long
    - If you leave this key empty, nothing is shown
- **Autoclose distance** (`distance`) - Sets how far from **Autoclose position** a player can be. Players farther
  away when you trigger the entity don't get the box, and the box closes when a player moves farther away. With 0,
  there is no limit
- **Autoclose position** (`position`) - Sets the point **Autoclose distance** is measured from, as the name of an
  entity or as `x y z`
    - If you leave this key empty, it is the `game_messagebox` itself

## Flags

- **All Players** (1) - The box opens for every alive player. Without this flag, only the player who started the
  chain of triggers gets it

## Notes

- Several open boxes stack, and they close newest first. A player has at most 8 open boxes, and a ninth one closes
  the oldest
- Triggering a box that is already open for a player does nothing for that player
- The box stays open through respawns and new rounds, and a map change or a disconnect closes it
- Bots get no boxes

## See also

- [Message boxes](../features/message-boxes.md) - how the boxes look and work
- [`env_tutor`](env_tutor.md) - a small message window that doesn't take the mouse
- [`game_text`](game_text.md) - a text on the HUD

## Changes since 1.38

- `game_messagebox` is new in SBO 2.0.0
