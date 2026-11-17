A `trigger_push` is a brush trigger that pushes what touches it in a direction. It fires nothing, so it has no target,
delay or kill target, and while its master is locked for the entity that touches it, it doesn't push that entity.

## Attributes

- **Speed of push** (`speed`) - Sets how hard the trigger pushes, in units per second, in the direction of its angles
    - If you leave this key empty or set 0, it is 100
- **Speed factor** (`m_iszPushSpeed`) - Sets a [locus number](../guide/locus.md) that multiplies the push. The
  trigger works it out for each entity that touches it, and `*locus` and `!activator` stand for that entity
- **Push direction** (`m_iszPushVel`) - Sets the push direction as a [locus vector](../guide/locus.md), which the
  trigger uses instead of its angles. The push is this vector times **Speed of push**. If the vector gives no value,
  the trigger doesn't push the entity
    - If you leave this key empty, the trigger pushes in the direction of its angles
- **Obey Trigger Mode** (`m_iObeyTriggerMode`) - Sets how triggers switch it
    - No (0, default) - Every trigger turns it on or off
    - Yes (1) - On turns it on, Off turns it off and Toggle switches it

## Flags

- **Push Once Only** (1) - The trigger gives one push to the first player or object that touches it, and then removes
  itself
- **Start Off** (2) - The trigger starts off, and triggering it switches it on and off
- **No clients** (8) - Players aren't pushed
- **No monsters** (16) - Monsters aren't pushed

## Notes

- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes its angles
  (**Pitch Yaw Roll**) while the map runs, it pushes in the new direction at once. See [Changing
  keys](../guide/changing-keys.md)

## See also

- [`trigger_jump`](trigger_jump.md) - launches an entity on an arc to a point
- [calc_ entities guide](../../guides/calc-entities.md) - a push field away from a center
- [trigger_push on TWHL](https://twhl.info/wiki/page/trigger_push) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Speed factor**, **Push direction** and **Obey Trigger Mode**, and the new flags **No
  clients** (8) and **No monsters** (16)
- Fixed the Master key doing nothing on `button_target`, `trigger_hurt`, `trigger_push`, `trigger_monsterjump`,
  `momentary_rot_button` and a triggered `game_player_equip`. These entities never checked their Master, so they
  worked while locked
