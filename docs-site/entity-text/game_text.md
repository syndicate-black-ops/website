A `game_text` shows text on the HUD when you trigger it, for the player who started the chain of triggers or for every
player. The text fades in, stays for its **Hold Time** and fades out.

![The three text effects: Fade In/Out fades the whole text, Credits fades it with letters flickering in Color2, Scan Out writes it one letter at a time](../../assets/img/clips/game-text-effects.webp)

*The three text effects*

## Attributes

- **Name** (`targetname`) - Triggering the entity shows the text. See [Common keys](common-keys.md#targetname)
- **Message Text** (`message`) - Sets the text shown on the HUD
- **X** (`x`) - Sets where the text is across the screen, from 0 for the left edge up to 1 for the right edge, and
  -1 centers it
    - If you leave this key empty, it is 0 and the text is at the left edge
- **Y** (`y`) - Sets where the text is down the screen, from 0 for the top up to 1 for the bottom, and -1 centers it
    - If you leave this key empty, it is 0 and the text is at the top
- **Text Effect** (`effect`) - Picks how the text appears and goes away
    - Fade In/Out (0) - The whole text fades in and out
    - Credits (1) - The text flashes in like the credits of Half-Life
    - Scan Out (2) - The text is written one letter at a time, and each letter flashes in **Color2** for the **Scan
      time** before it turns **Color1**
- **Color1** (`color`) - Sets the color of the text, as red, green and blue from 0 up to 255
    - If you leave this key empty, the text is black, which doesn't show
- **Color2** (`color2`) - Sets the color each letter flashes in with the effect "Scan Out"
    - If you leave this key empty, it is black, so no highlight shows
- **Fade in Time** (`fadein`) - Sets how many seconds the text takes to fade in, and with "Scan Out", how many seconds
  each letter takes
    - If you leave this key empty, it is 0 and the text appears at once
- **Fade Out Time** (`fadeout`) - Sets how many seconds the text takes to fade out after its **Hold Time**
    - If you leave this key empty, it is 0 and the text goes at once
- **Hold Time** (`holdtime`) - Sets how many seconds the text stays on the screen after it has faded in
    - If you leave this key empty, it is 0 and the text doesn't stay
- **Scan time** (`fxtime`) - With "Scan Out", sets how many seconds each letter shows in **Color2** before it turns
  **Color1**
    - If you leave this key empty, it is 0 and no highlight shows
- **Text Channel** (`channel`) - Sets the channel the text uses, so a new text on the same channel replaces the one
  shown there, while texts on different channels show at the same time
    - Channel 1 (1)
    - Channel 2 (2)
    - Channel 3 (3)
    - Channel 4 (4)
    - If you leave this key empty, it is 0, which works like Channel 4
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing

## Flags

- **All Players** (1) - Every player sees the text. Without this flag, only the player who triggered it does

## Notes

- It fires no target

## See also

- [`env_message`](env_message.md) - shows a message from `titles.txt`
- [`env_tutor`](env_tutor.md) - shows a message in the tutor window
- [`game_messagebox`](game_messagebox.md) - shows a box with a longer text
- [game_text on TWHL](https://twhl.info/wiki/page/game_text) - the Half-Life entity
