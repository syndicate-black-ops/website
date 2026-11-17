An `aiscripted_sequence` makes a monster move to its position and play an animation there.

It works like a [`scripted_sequence`](scripted_sequence.md), with three differences: it takes a monster in any state,
even a monster that is fighting, it can run without an **Action Animation**, and other scripts with the same **Name**
don't wait for it.

## Attributes

- **Action Animation** (`m_iszPlay`) - Sets the name of the animation the monster plays once it reaches the
  script, as the model names it
    - If you leave this key empty, the monster plays nothing, and the script ends at once and fires its **Target**
- **Idle Animation** (`m_iszIdle`) - Sets the animation the monster plays once it reaches the script, until you
  trigger the script. With an idle animation, a script that has a **Name** takes its monster when the map starts
    - If you leave this key empty, a script that has a **Name** doesn't take its monster until you trigger it
- **AI Schedule when done** (`m_iFinishSchedule`) - Sets what the monster does when the script ends
    - Default AI (0) - The monster goes back to what it was doing
    - Ambush (1) - The monster stays where it is and waits until it sees an enemy

## Flags

- **Repeatable** (4) - The script stays after it ends, so you can run it again. Without this flag, it removes
  itself when its animation ends
- **Leave Corpse** (8) - A monster that dies during the script leaves its body where it fell. Without this flag,
  the body fades out
- **No Interruptions** (32) - The monster finishes the script even when it is hurt or sees an enemy
- **Auto-search** (1024) - The script looks for its monster in its **Search Radius** when the map starts, as a
  script without a **Name** does, even though it has a name
- **Try search once** (4096) - When you trigger the script, it looks for its monster only once, and if the monster
  isn't there, it gives up. Without this flag, it looks again every second
- **Don't reset head turn** (8192) - A Scientist or a Cop keeps their head turned the way it was while the script
  plays. Without this flag, they look straight ahead
- **Force idle animation looping** (16384) - The **Idle Animation** starts again each time it ends, even when the
  model doesn't loop it
- **Remove on interruption** (32768) - The script removes itself when its monster breaks out of it, for example
  when the monster is hurt or sees an enemy
- **Don't Drop to Floor** (65536) - After the animation, the monster stays at the height where the animation ended.
  Without this flag, it drops to the floor
- **Allow stuck** (131072) - After the animation, the monster keeps its end position even inside a wall or another
  solid. Without this flag, it goes back to where it started
- **Allow unnamed idle** (262144) - A script without a **Name** that has an **Idle Animation** plays the idle and
  waits for a trigger before its action. Without this flag, it starts at once
- **Allow Take Damage TriggerCondition** (524288) - The monster's **Take Damage** trigger condition fires when the
  monster is hurt during the script, even while the script ignores interruptions

## Notes

- If the monster's model has no animation with the name in **Action Animation**, the monster plays its first
  animation, and with `developer 1` set in the console, the console reports it

## See also

- [`scripted_sequence`](scripted_sequence.md) - the same, with the monster under the script's full control
- [`scripted_action`](scripted_action.md) - makes a monster do an action, such as an attack, instead of an
  animation
- [`scripted_schedule`](scripted_schedule.md) - gives a monster a task such as moving to a spot
- [Scripted sequence on TWHL](https://twhl.info/wiki/page/aiscripted_sequence) - the Half-Life entity this one is
  based on

## Changes since 1.38

- You can use the new keys and flags that every scripted sequence has in SBO 2.0.0, from **Fire on Possession** to
  **Repeat action X more times**, and the flags from **Auto-search** on
- A script removed by a **KillTarget** while its monster waits for it or plays it lets the monster go. In SBO 1.38,
  the monster kept a link to the removed script, which could crash the server
