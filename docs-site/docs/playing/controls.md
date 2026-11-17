---
description: "These are the default keys when you install SBO for the first time, or when you use Options > Keyboard > Use Defaults."
---

# Controls

These are the default keys when you install SBO for the first time, or when you use **Options > Keyboard > Use
Defaults**. **Use Defaults** sets every action in the keyboard list back to its default keys. Keys you bound in the
console to commands that are not in that list stay as they are.

## Movement

| Key | Alt Key | Action |
|---|---|---|
| <kbd>W</kbd> | <kbd>Up</kbd> | Move forward |
| <kbd>S</kbd> | <kbd>Down</kbd> | Move back |
| <kbd>A</kbd> | <kbd>,</kbd> | Move left (strafe) |
| <kbd>D</kbd> | <kbd>.</kbd> | Move right (strafe) |
| <kbd>Left</kbd> | | Turn left |
| <kbd>Right</kbd> | | Turn right |
| <kbd>Space</kbd> | <kbd>Mouse 3</kbd> | Jump |
| <kbd>Ctrl</kbd> | | Duck |
| <kbd>Shift</kbd> | | Walk |
| <kbd>V</kbd> | <kbd>'</kbd> | Swim up |
| <kbd>C</kbd> | <kbd>/</kbd> | Swim down |
| <kbd>Page Up</kbd> | | Look up |
| <kbd>Page Down</kbd> | | Look down |
| <kbd>End</kbd> | | Look straight ahead |
| <kbd>Alt</kbd> | | Hold to strafe with the turn keys and the mouse |
| <kbd>Ins</kbd> | | Hold to look around with the movement keys |
| <kbd>;</kbd> | | Hold to look around with the mouse |

## Weapons and actions

| Key | Alt Key | Action |
|---|---|---|
| <kbd>Mouse 1</kbd> | | Primary attack |
| <kbd>Mouse 2</kbd> | | Secondary attack |
| <kbd>R</kbd> | | Reload |
| <kbd>E</kbd> | | Use buttons, doors, NPCs, and more |
| <kbd>F</kbd> | <kbd>L</kbd> | Flashlight |
| <kbd>T</kbd> | | [Spray your logo](sprays.md) |
| <kbd>1</kbd> to <kbd>5</kbd> | | Open the weapon menu at that key's [weapons](weapons-and-items.md) |
| <kbd>6</kbd> to <kbd>9</kbd>, <kbd>0</kbd> | | Used for in-game menus, such as the radio or loadout menus. SBO's weapons use only keys 1 to 5 |
| <kbd>Wheel up</kbd> | <kbd>[</kbd> | Previous weapon |
| <kbd>Wheel down</kbd> | <kbd>]</kbd> | Next weapon |
| <kbd>Q</kbd> | | The weapon you used last |

## Game specific settings

| Key | Alt Key | Command | Action |
|---|---|---|---|
| <kbd>P</kbd> | <kbd>Del</kbd> | `cloak` | Turns the [cloak](loadout.md#assassin) on and off. Only the Assassin cyberware has it |
| <kbd>J</kbd> | | `cybereye` | Turns night vision on and off. Available from the Cyberware menu individually as [Cyber eyes](loadout.md#cyberware), also comes included with the [Assassin](loadout.md#assassin) loadout |
| <kbd>H</kbd> | | `objectives` | Switches the [mission objectives panel](hud-and-scoreboard.md#hud) between short, full and hidden, which you can also set in [Options](options.md#player-cvars) |
| <kbd>M</kbd> | | `changemodel` | Opens the [selection menu](menus.md#loadout), where you change your loadout in Co-op and Bounty Killer. The new loadout applies the next time you spawn |
| <kbd>X</kbd> | | `radio` | Opens the radio menu for sending pre-defined [radio messages](chat-and-console.md#game-messages-in-the-chat) to teammates. Only available in Co-op and while your player is alive |
| <kbd>B</kbd> | | `showbriefing` | Opens the [map briefing](menus.md#map-briefing), whether you are alive, dead or spectating |
| <kbd>K</kbd> | | `gmon` | In Co-op, makes you the [Game Master](../game-modes/coop.md#game-master) (only if `mp_gmmode` is set to 1), and opens the GM spawn menus. There can only be one active Game Master at a time |

## Chat, voice and screen

| Key | Alt Key | Action |
|---|---|---|
| <kbd>Y</kbd> | | [Chat message](chat-and-console.md#sending-messages) |
| <kbd>O</kbd> | <kbd>Mouse 5</kbd> | Voice, which you hold down while you talk |
| <kbd>Tab</kbd> | | [Scoreboard](hud-and-scoreboard.md#scoreboard) |
| <kbd>&#96;</kbd> | <kbd>~</kbd> | [Console](chat-and-console.md#console) |
| <kbd>Esc</kbd> | | Close the current menu |
| <kbd>F5</kbd> | | Screenshot |
| <kbd>F12</kbd> | | Steam screenshot, which is Steam's default screenshot key |
| <kbd>Pause</kbd> | | Pause, which works only if the server sets `pausable` to 1 |

## Other defaults

| Setting | Value |
|---|---|
| `name` | `Sadako` |
| `con_color` | `17 244 136`, which makes the console text green |
| `cl_forwardspeed`, `cl_backspeed` | `2000` |
| `gamma`, `brightness` | `3` and `1`, the screen brightness SBO is made for |
| Mouse look | On |

Every other setting comes from your Half-Life settings.

## Changes since 1.38

- Team chat (`say_team`) has been removed, and <kbd>U</kbd> is no longer bound to it. In 1.38, the server ignored team
  messages, so they were never sent
- <kbd>B</kbd> opens the map briefing (`showbriefing`). In 1.38, the only way to see the map briefing was by hitting
  <kbd>Enter</kbd> in spectator, which was removed in 2.0.0
- Sane defaults were set (for example, in 1.38 <kbd>F12</kbd> was set to Quit, which also happens to be the default
  screenshot key for Steam)
- <kbd>H</kbd> opens the mission objectives panel for maps which place a
  [`trigger_objective`](../mapping/entities/trigger_objective.md) entity, new in 2.1.0

## See also

- [Downloading & Installing](installing.md) - how to install and update the game
- [Loadout](loadout.md) - the weapons, cyberware and armor you pick before you spawn
- [Chat and console](chat-and-console.md) - chat, voice and the console
