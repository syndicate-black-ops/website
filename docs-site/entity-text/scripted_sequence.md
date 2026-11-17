A `scripted_sequence` makes a monster go to a point and play an animation. The script takes its monster when you
trigger it, or when the map starts if the script has no name.

## Attributes

- **Action Animation** (`m_iszPlay`) - Sets the animation that the monster plays when you trigger the script. If the
  script has no name, the monster plays it at once
- **Idle Animation** (`m_iszIdle`) - Sets the animation that the monster plays while it waits at the script for the
  trigger
    - If you leave this key empty, a script that has a **Name** doesn't take its monster until you trigger it

## Flags

- **Repeatable** (4) - The script stays after it finishes, so it can run again. Without this flag, it removes itself
  when its animation ends
- **Leave Corpse** (8) - A monster that dies during the script leaves its corpse where it fell, instead of fading out
- **No Interruptions** (32) - Nothing interrupts the monster during the script, neither damage nor enemies
- **Override AI** (64) - The script takes the monster also when it is alert or fighting. Without this flag, it only
  takes an idle monster
- **No Script Movement** (128) - After the animation, the monster stays where it started, and doesn't move to where
  the animation ended
- **Auto-search** (1024) - The script looks for its monster within its radius when the map starts, as a script
  without a name does, also if it has a name
- **Try search once** (4096) - When you trigger the script, it looks for its monster once. If the monster isn't there,
  the script stops and doesn't look again every second
- **Don't reset head turn** (8192) - A Scientist or a Cop keeps its head turned the same way while the script plays,
  and doesn't look straight ahead
- **Force idle animation looping** (16384) - The **Idle Animation** starts again each time it ends, also if the model
  doesn't loop it
- **Remove on interruption** (32768) - The script removes itself when its monster breaks out of it, for example when
  the monster is hurt or sees an enemy
- **Don't Drop to Floor** (65536) - After the animation, the monster stays at the height where the animation ended,
  and doesn't drop to the floor
- **Allow stuck** (131072) - After the animation, the monster keeps its end position also if it is inside a wall or
  another solid. Without this flag, it goes back to where it started
- **Allow unnamed idle** (262144) - A script without a name that has an **Idle Animation** plays the idle and waits
  for a trigger before its action. Without this flag, it starts at once
- **Allow Take Damage TriggerCondition** (524288) - The monster's **Trigger Condition** "Take Damage" fires when it is
  hurt during the script, also while the script ignores interruptions

## See also

- [`aiscripted_sequence`](aiscripted_sequence.md) - a script that doesn't take the monster out of its AI
- [`scripted_action`](scripted_action.md) - a script that makes the monster attack, reload or jump
- [`scripted_sentence`](scripted_sentence.md) - makes a monster say a sentence
- [scripted_sequence on TWHL](https://twhl.info/wiki/page/scripted_sequence) - the Half-Life entity

## Changes since 1.38

- Fixed a `scripted_sequence` with Move to Position "No - Turn to Face" hanging the script. The game did not know this
  choice. This was a bug in SBO 1.38
- You can use the new **Move to Position** choice "Teleport"
- Fixed a `scripted_sequence` that a Kill target removes while its monster waits for it or plays it crashing the
  server. The monster still pointed to the removed sequence. This was a bug in SBO 1.38
- You can use the new keys **Fire on Possession**, **Fire after moving**, **Fire on Animation start**, **Master**,
  **Interruption policy**, **TakeDamage policy**, **Search target monster by...**, **Test against search radius**,
  **Required MonsterState**, **Move to target's radius**, **Turn mode**, **Priority** and **Repeat action X more
  times**
- You can use the new flags **Auto-search**, **Try search once**, **Don't reset head turn**, **Force idle animation
  looping**, **Remove on interruption**, **Don't Drop to Floor**, **Allow stuck**, **Allow unnamed idle** and **Allow
  Take Damage TriggerCondition**
