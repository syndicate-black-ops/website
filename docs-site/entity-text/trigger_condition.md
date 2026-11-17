A `trigger_condition` compares a key of an entity with a value, or with a key of another entity, and fires its "true"
or its "false" target. With **Cyclic**, it checks once for each trigger, and without it, it keeps checking while it is
on, so it can watch a key such as a monster's health or the position of a train. See the [Changing
values](../../guides/value-triggers.md) guide for a setup with it.

## Attributes

- **Monitored entity** (`target`) - Names the entity whose key it checks, as a name, `!activator` or `!caller`
- **Monitored key** (`m_iszValueName`) - Names the key it checks
- **Compare-entity** (`m_iszSourceName`) - Names an entity to compare with. If you set it and **Compare-key**, the
  entity ignores **Compare-value**
- **Compare-key** (`m_iszSourceKey`) - Names the key of the **Compare-entity**
- **Compare-value** (`m_iszCheckValue`) - Sets the value to compare with when there is no **Compare-entity**
    - If you leave this key empty, it is 0
- **Comparator** (`m_iCheckType`) - Sets how the entity compares the monitored value with the compare value. `&` only
  works on keys that hold whole numbers
- **Target for 'true'-case** (`netname`) - Fires this target when the comparison is true
- **Target for 'false'-case** (`message`) - Fires this target when the comparison is false
- **In constant mode fire when** (`m_iCheckBehaviour`) - While the entity is on, sets when the targets fire. "Result
  has changed" only fires when the result differs from the last check
    - When the entity turns on, the last result counts as true. So with "Result has changed", a first result of true
      fires nothing
- **Check interval** (`m_fCheckInterval`) - While it is on, sets how many seconds pass between two checks, at least
  0.01
- **Reset at round start** (`round_reset`) - With Yes, the entity goes back to the way it was when the map loaded, at
  each round start before the players spawn. See
  [Round hooks](../guide/round-hooks.md) for more details

## Flags

- **Start Off** (1) - The entity starts off, and a trigger turns it on
- **Don't use X** (2) - The X of a vector isn't compared
- **Don't use Y** (4) - The Y of a vector isn't compared
- **Don't use Z** (8) - The Z of a vector isn't compared
- **Cyclic** (32) - Each trigger checks once, and the entity has no on and off state
- **Keep activator** (64) - The targets get the activator of the trigger. Without this flag, the `trigger_condition`
  itself is the activator
- **Ignore initial result** (128) - The first check after it turns on fires nothing

## Notes

- Without **Start Off** or **Cyclic**, it is on from the start and checks every **Check interval**
- A trigger with On turns it on, a trigger with Off turns it off, and a trigger with Toggle switches it
- A target that triggers the same `trigger_condition` while it fires is ignored
- For vectors, "Equal" and "Not equal" compare all three numbers when the compare value is a vector. The other
  comparisons use the vector's length
- Without a **Monitored entity** or a **Monitored key**, the entity removes itself. With `developer 1` set in the
  console, the console says so
- Setups from Sven Co-op carry over, because the class name, key names, flags and comparison numbers are the same

## See also

- [`trigger_compare`](trigger_compare.md) - compares two numbers
- [`trigger_changevalue`](trigger_changevalue.md) - changes a key
- [Changing values](../../guides/value-triggers.md) - a guide with small setups

## Changes since 1.38

- `trigger_condition` is new
