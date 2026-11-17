A `trigger_copyvalue` copies a key of one entity into a key of other entities, once for each trigger or again and
again while it is on. It can combine the copied value with the current one, as a
[`trigger_changevalue`](trigger_changevalue.md) does.

## Attributes

- **Source entity** (`netname`) - Names the entity to read: the first entity with this name, or `!activator` or
  `!caller`
- **Source key** (`m_iszSrcValueName`) - Names the key to read
- **Destination entity** (`target`) - Names the entities to write: the first entity with this name, or every entity
  with this name with **Multiple destinations**, or `!activator` or `!caller`
- **Destination key** (`m_iszDstValueName`) - Names the key to write
- **Float conversion** (`m_iFloatConversion`) - Sets how the entity writes a number with decimals into a text key or
  a whole-number key: with a number of decimal places, or rounded
- **Copy interval** (`dmg`) - With **Constant**, sets how many seconds pass between two copies
- **Type of value** (`m_iszValueType`) - Sets the operation, as on a `trigger_changevalue`
- **Trigonometric funcs. behavior** (`m_trigonometricBehaviour`) - Sets the unit of the angle operations
    - Degrees (0, default) - Sin, Cos, Tan and Cot take the value in degrees, and Arcsin, Arccos, Arctan and Arccot
      give degrees, so the sine of 30 is 0.5
    - Radians (1) - Both are in radians
- **Append spaces** (`m_iAppendSpaces`) - For text, adds this many spaces after the result, up to 255
- **Trigger after operation** (`message`) - Fires this target after each copy. It can be a name, `!activator` or
  `!caller`

## Flags

- **Don't use X** (1) - The X of a vector stays as it is
- **Don't use Y** (2) - The Y of a vector stays as it is
- **Don't use Z** (4) - The Z of a vector stays as it is
- **Constant** (8) - A trigger turns the copying on or off. While the copying is on, the entity copies every **Copy
  interval** seconds
- **Start on** (16) - With **Constant**, the copying is on from the start
- **Invert target value** (32) - The current value becomes negative before the operation
- **Invert source value** (64) - The copied value becomes negative before the operation
- **Multiple destinations** (128) - The entity writes every entity named in **Destination entity**, not only the
  first

## Notes

- Each trigger copies once. With **Constant**, a trigger with On also turns the copying on, Off turns it off and
  Toggle switches it
- The entity writes nothing if a key names a model or a sound, or the destination key is `classname` or `headscale`.
  It also writes nothing if the source entity, the source key or the destination key is missing. With `developer 1`
  set in the console, the console says so
- Setups from Sven Co-op carry over, because the class names, key names, flags and operation numbers are the same

## See also

- [`trigger_changevalue`](trigger_changevalue.md) - writes a value into a key
- [Changing keys](../guide/changing-keys.md) - every operation and what can change

## Changes since 1.38

- `trigger_copyvalue` is new
