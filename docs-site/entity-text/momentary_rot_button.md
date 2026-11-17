---
description: "A momentary_rot_button is a brush wheel or lever that turns while a player holds the use key on it, and moves its target along with it."
---
A `momentary_rot_button` is a brush wheel or lever that turns while a player holds the use key on it, and it moves its
target, such as a [`momentary_door`](momentary_door.md), along with it.

## Attributes

- **Target** (`target`) - Names the entities it moves, which get its position as a number from 0 at the start up to
  1 at the end, with the use type Set. The wheel needs a target, because it doesn't turn without one, and wheels with
  the same target turn together
- **Speed** (`speed`) - Sets how fast the wheel turns while a player holds the use key, in degrees per second
    - If you leave this key empty or set 0, it is 100
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md), and while the master is off, the use key
  doesn't turn the wheel and its target gets nothing
- **Sounds** (`sounds`) - Sets the sound the wheel plays each time a player starts turning it
- **Custom sound** (`noise`) - Sets a sound file that plays each time a player starts turning the wheel, and if you
  set one, the wheel ignores **Sounds**
- **Distance** (`distance`) - Sets how far the wheel turns from its start to its end, in degrees, and a negative
  value turns it the other way. The wheel needs a distance, because with 0 it doesn't turn
- **Auto-return speed** (`returnspeed`) - With **Auto Return**, sets how fast the wheel turns back to its start when
  the player lets go, in degrees per second, and with 0 it doesn't turn back

## Flags

- **Door Hack** (1) - The wheel is solid, and players can't turn it with the use key, so it only turns when something
  triggers it, and each trigger turns it for a tenth of a second
- **Auto Return** (16) - When the player lets go, the wheel turns back to its start at **Auto-return speed** and moves
  its target back with it
- **X Axis** (64) - The wheel turns around the X axis, the map's east-west line, instead of the vertical axis
- **Y Axis** (128) - The wheel turns around the Y axis, the map's north-south line, instead of the vertical axis

## Notes

- Each time a player starts turning the wheel again, it turns the opposite way to last time, so one use opens the
  door a bit and the next closes it again. With **Auto Return** and an **Auto-return speed** set, it always turns
  toward its end
- The wheel stops at its start and at its end
- The turning sound stops when the player lets go of the wheel

## See also

- [`momentary_door`](momentary_door.md) - a door that follows the wheel
- [`func_rot_button`](func_rot_button.md) - a rotating button that you press once
- [momentary_rot_button on TWHL](https://twhl.info/wiki/page/momentary_rot_button) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Custom sound**, **Object Hint Template** and **Hint Distance**
- Fixed the Master key doing nothing on `button_target`, `trigger_hurt`, `trigger_push`, `trigger_monsterjump`,
  `momentary_rot_button` and a triggered `game_player_equip`. These entities never checked their Master, so they
  worked while locked
- Fixed the sound of turnable valve wheels and levers continuing to play after you let go of them
