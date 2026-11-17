A `scripted_tanksequence` takes over a [`func_tank`](func_tank.md) for a moment, so the gun turns and fires without a
player at its controls.

## Attributes

- **Tank to affect** (`m_iszEntity`) - Names the `func_tank`
- **Turn to** (`m_iTurn`) - Sets where the gun turns
    - Don't turn (0) - The gun doesn't turn
    - Match sequence angle (1) - The gun turns to this entity's angles
    - Face sequence (2, default) - The gun aims at this entity
    - Face enemy (3) - The gun aims at the enemy, and if no enemy is found, the sequence doesn't start
    - If you leave this key empty, it is "Don't turn"
- **Enemy to face** (`m_iszEnemy`) - Names the enemy, as a name, `!activator` or a class name. A class name gives the
  nearest entity of that class within the gun's range, but never a spectator
    - If you leave this key empty, the enemy is the target the gun would pick by itself
- **Fire gun** (`m_iShoot`) - Sets when the gun fires during the sequence
    - If you leave this key empty, it is "Don't fire"
- **Halt condition** (`m_iUntil`) - Sets what ends the sequence by itself and fires **Trigger on halt**. With "None",
  only a trigger or the **Time limit** ends it
    - If you leave this key empty, it is "None"
- **Trigger on halt** (`target`) - Fires this target when the **Halt condition** happens
- **Time limit** (`m_fDuration`) - Sets how many seconds the sequence can run, and 0 means no limit. When the time
  runs out, the sequence ends and fires **Trigger on timeout**
- **Trigger on timeout** (`netname`) - Fires this target when the **Time limit** runs out
- **Tank state afterwards** (`m_iActive`) - Sets whether the gun is switched on, switched off or switched to the other
  state when the sequence ends
- **Control afterwards** (`m_iControllable`) - Sets whether players can take the gun's controls after the sequence.
  It sets, clears or switches the gun's flag **Controllable**

## Flags

- **Dump player** (1) - A player at the gun's controls is pushed off. Without this flag, a trigger does nothing while
  a player is using the gun, so the sequence doesn't start
- **Repeatable** (2) - You can use the entity again. Without this flag, it removes itself after one run

## Notes

- A player can't take the controls during a sequence
- A trigger with the [use type](../guide/trigger-modes.md) Toggle or Off ends a running sequence early, and it doesn't
  fire **Trigger on halt**

## See also

- [`func_tank`](func_tank.md) - the gun turret
- [`func_tankcontrols`](func_tankcontrols.md) - the controls players use
- [`monster_target`](monster_target.md) - a target that monsters and guns attack

## Changes since 1.38

- `scripted_tanksequence` is new
