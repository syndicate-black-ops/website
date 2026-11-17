---
description: "A scripted_action works like a scripted_sequence, but its monster does an action, such as an attack, a reload or a jump."
---
A `scripted_action` works like a [`scripted_sequence`](scripted_sequence.md), but when its monster is in place, it
does an action instead of an animation, such as an attack, a reload or a jump.

## Attributes

- **Entity to attack** (`m_iszAttack`) - Names what the monster turns to and attacks. You can use a name,
  `!activator`, or a class name that the script looks for within its **Search Radius**
    - If you leave this key empty, the monster attacks the `scripted_action` itself
- **Idle Animation** (`m_iszIdle`) - Sets the animation that the monster plays while it waits at the script for the
  trigger. With this key set, a named script takes its monster when the map starts
    - If you leave this key empty, a script that has a **Name** doesn't take its monster until you trigger it
- **Action to perform** (`m_fAction`) - Sets the action. If the monster doesn't have the action, the script ends at
  once, as with "No action"

## Flags

- **Repeatable** (4) - The script stays after it finishes, so it can run again. Without this flag, it removes itself
  when the action ends
- **Leave Corpse** (8) - A monster that dies during the script leaves its corpse where it fell, instead of fading out
- **No Interruptions** (32) - The monster finishes the script even when it is hurt or sees an enemy
- **Override AI** (64) - The monster takes the script also while it is fighting or alert, not only when it is idle
- **Auto-search** (1024) - The script looks for its monster within its radius when the map starts, as a script
  without a name does, also if it has a name
- **Try search once** (4096) - When you trigger the script, it looks for its monster once. If the monster isn't there,
  the script stops and doesn't look again every second

## Notes

- When the action starts, the monster turns to the target at once. The target is its enemy for the action, so a
  monster that shoots aims at it
- The `scripted_action` fires its **Target** when the action is done

Which actions a monster has depends on its model:

| Action | Monsters |
|---|---|
| Ranged Attack | Feds, Zombie Grunts, the Cop, the Sectum, Demon Slaves, Werewolves, the Imp, the Cyborg, the Cyber Minotaur, the Gargantua and the Assassin |
| Ranged Attack 2 | Feds, Zombie Grunts and the Assassin |
| Melee Attack | Feds, Zombie Grunts, the Sectum, Demon Slaves, Werewolves, the Cyber Minotaur, Zombies, the Gargantua and the Assassin |
| Melee Attack 2 | The Imp, the Gargantua and the Assassin |
| Special Attack | Feds and Zombie Grunts |
| Special Attack 2 | None |
| Reload | Feds, Zombie Grunts, the Cop, Demon Slaves and Werewolves |
| Jump | The Imp and the Assassin |

## See also

- [`scripted_sequence`](scripted_sequence.md) - a script that plays an animation
- [`scripted_schedule`](scripted_schedule.md) - makes a monster run one of its AI schedules

## Changes since 1.38

- `scripted_action` is new
