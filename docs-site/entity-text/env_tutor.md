An `env_tutor` shows a message in the tutor window of Counter-Strike: Condition Zero, a small window with an icon, a
colored frame and a sound. Each player sees one message at a time, and the others wait in a queue.

A trigger with the [use type](../guide/trigger-modes.md) On or Toggle shows the message, and Off closes it for the
players who see it and takes it out of their queues. Only alive players get the message.

## Attributes

- **Name** (`targetname`) - Triggering the entity shows or closes the message. See
  [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger each time the message is shown to a player, and passes on that player
  as the [activator](../guide/entity-triggering.md#target-selectors)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing. **Show on player spawn** doesn't check the master
- **Text** (`message`) - Sets the text. `\n` starts a new line, `%n` is the player's name, `%+command%` is the key
  the player has bound to a command, such as `%+reload%`, and `#Token` is a text from the game's language files. The
  text can be at most 1023 bytes long
- **Type** (`type`) - Picks the type of the message, which sets the color of the text, and the icon and the sound
  when **Icon** and **Sound** are left on "Type's"
    - Default (1) - Green
    - FriendDeath (2) - Red, with a skull and its own sound
    - EnemyDeath (4) - Blue, with a skull and its own sound
    - Scenario (8) - Yellow
    - Buy (16) - Green
    - Career (32) - Green
    - Hint (64) - Green
    - InGameHint (128) - Green
    - EndGame (256) - Yellow
- **Icon** (`icon`) - Picks the icon shown in the window, and a **Custom icon .tga** replaces it
    - Type's (0) - The icon of the **Type**, an "i", or a skull for the two death types
    - None (1) - No icon
    - i (2) - An "i"
    - ! (3) - A "!"
    - Skull (4) - A skull
    - i (bigger, colored) (5) - A bigger "i" in color
    - ! (bigger, colored) (6) - A bigger "!" in color
- **Custom icon .tga** (`iconfile`) - Sets a `.tga` image as the icon, as a path from the game folder, such as
  `gfx/mymap/hint.tga`, and players download it with the map
- **Sound** (`sound`) - Picks the sound played when the message appears, and a **Custom sound** replaces it
    - Type's (0) - The sound of the **Type**
    - None (1) - No sound
    - events/tutor_msg.wav (2)
    - events/friend_died.wav (3)
    - events/enemy_died.wav (4)
- **Custom sound** (`soundfile`) - Sets a sound file played instead of **Sound**, and players download it with the
  map
- **Text color** (`color`) - Sets the color of the text, as red, green and blue from 0 up to 255
    - If you leave this key empty, it is the color of the **Type**
- **Icon color** (`iconcolor`) - Tints the icon, and `255 255 255` keeps the icon's own colors
    - If you leave this key empty, the gray icons take the text color, and the bigger and custom icons keep their
      own colors
- **Background R G B A** (`bgcolor`) - Sets the background of the window, as red, green, blue and opacity, where an
  opacity of 0 is see-through and 255 is opaque
    - If you leave this key empty, it is `0 0 0 200`
- **Border R G B A** (`bordercolor`) - Sets the outline of the window, and `0 0 0 0` gives no outline
    - If you leave this key empty, it is the green outline of the game's look
- **Alignment** (`align`) - Picks where on the screen the window appears, when **X** and **Y** are -1
    - Top right (0)
    - Top left (1)
    - Top center (2)
    - Center left (3)
    - Center (4)
    - Center right (5)
    - Bottom left (6)
    - Bottom center (7)
    - Bottom right (8)
- **X** (`x`) - Sets where the window is across the screen, from 0 for the left edge up to 1 for the right edge, and
  **Alignment** says which edge of the window, or its middle, is placed there. With -1, the window is at the place
  of its alignment, 10 pixels from the edge of the screen or in the middle
- **Y** (`y`) - Sets where the window is down the screen, from 0 for the top up to 1 for the bottom, in the same way
  as **X**
- **Hold Time** (`holdtime`) - Sets how many seconds the message stays, and 0 keeps it until you trigger the entity
  off
- **Priority** (`priority`) - Sets which waiting message is shown next: the one with the highest priority, and with
  the same priority, the oldest one
- **Interrupt** (`interrupt`) - Sets whether the message waits for the window
    - No (0) - The message waits in the queue
    - Yes (1) - The message replaces a shown message of the same or a lower priority at once
- **Queue lifetime** (`lifetime`) - Sets how many seconds a message waits in the queue before it is dropped, and 0
  means no limit. With -1, the message doesn't wait, so it is only shown when the window is free or when it may
  interrupt the shown message
- **Max shows per player** (`maxshows`) - With **Repeatable**, sets how many times one player sees the message, and
  0 means no limit
- **Target when closed** (`closetarget`) - Names the entities to trigger when the message closes for a player, and passes on
  that player as the activator

## Flags

- **Activator only** (1) - Only the player who started the chain of triggers gets the message, if they are alive
- **Show on player spawn** (4) - Each player gets the message when they spawn
- **Repeatable** (8) - A player can see the message more than once, as **Max shows per player** sets. Without this
  flag, each player sees it once

## Notes

- A player who goes into spectator mode loses their shown and waiting messages
- While a message is shown, only a waiting message with **Interrupt** replaces it, even when a message without
  **Interrupt** has a higher priority

## See also

- [Tutor messages](../features/tutor.md) - how the tutor window looks and works
- [`game_text`](game_text.md) - a text on the HUD
- [`game_messagebox`](game_messagebox.md) - a box with a longer text in the middle of the screen

## Changes since 1.38

- `env_tutor` is new in SBO 2.0.0
