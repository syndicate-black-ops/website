A `trigger_monsterjump` is a brush trigger that throws a monster that touches it forward and up, and then turns itself
off. A trigger without a name throws once, and a trigger with a name starts off and has to be turned on for each
throw, as **Obey Trigger Mode** says.

## Attributes

- **Jump Speed** (`speed`) - Sets the forward speed of the throw, in the trigger's direction, in units per second
    - If you leave this key empty or set 0, it is 200
- **Jump Height** (`height`) - Sets the upward speed added to the throw, in units per second
    - If you leave this key empty or set 0, it is 150
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how triggers switch it
    - No (0, default) - Any trigger turns it on or off
    - Yes (1) - On turns it on, Off turns it off and Toggle switches it

## Notes

- While its master is locked for the monster, it throws nothing

## See also

- [`trigger_jump`](trigger_jump.md) - a jump pad with a target point
- [trigger_monsterjump on TWHL](https://twhl.info/wiki/page/trigger_monsterjump) - the Half-Life entity

## Changes since 1.38

- Fixed `trigger_monsterjump` ignoring its Jump Speed and Jump Height. Every monster it threw went 200 units forward
  and 150 up. This was a bug in SBO 1.38
- Fixed the Master key doing nothing on `button_target`, `trigger_hurt`, `trigger_push`, `trigger_monsterjump`,
  `momentary_rot_button` and a triggered `game_player_equip`. These entities never checked their Master, so they
  worked while locked
- You can use the new key **Obey Trigger Mode**
