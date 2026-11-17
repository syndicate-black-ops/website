An `env_message` shows a message from `titles.txt` on the HUD each time you trigger it, and it can play a sound with
it.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows the message. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger after it shows the message. The `env_message` passes itself
  on as the [activator](../guide/entity-triggering.md#target-selectors), not the player who triggered it
- **Message Name** (`message`) - Sets the name of a message in `titles.txt` to show, which also sets the color, the
  position and the effects of the text (see [Titles.txt](https://twhl.info/wiki/page/Tutorial:_Titles.txt) on TWHL).
  Text that matches no name there is shown as it is, in the lower middle of the screen, for 5 seconds
- **Sound Effect** (`messagesound`) - Sets a sound that plays at the entity each time it shows the message
    - If you leave this key empty, it plays no sound
- **Volume** (`messagevolume`) - Sets how loud **Sound Effect** is, from 0 for silent up to 10 for full volume
    - If you leave this key empty or set 0, the sound plays at full volume
- **Sound Radius** (`messageattenuation`) - Sets how far the sound carries from the entity
    - Small Radius (0) - Players hear it up to about 500 units away
    - Medium Radius (1) - Players hear it up to about 800 units away
    - Large Radius (2) - Players hear it up to about 1250 units away
    - Play Everywhere (3) - Every player hears it at full volume, anywhere on the map

## Flags

- **Play Once** (1) - The entity is removed after it shows its message once
- **All Clients** (2) - Every player sees the message. Without this flag, only the player who triggered it sees
  it, or the first player when no player triggered it

## See also

- [`game_text`](game_text.md) - shows a text that you write in the entity itself
- [`env_tutor`](env_tutor.md) - shows a message in the tutor window
- [`game_messagebox`](game_messagebox.md) - shows a message box

