A `trigger_changevalue` changes a key of other entities while the map runs. It replaces the value, or it combines the
current value with a new one, for example by adding, multiplying or appending text. See [Changing
keys](../guide/changing-keys.md) for every rule, and the [Changing values](../../guides/value-triggers.md) guide for
small setups.

## Attributes

- **Destination entity** (`target`) - Names the entities to change: every entity with this name, or `!activator` or
  `!caller`
- **Key name** (`m_iszValueName`) - Names the key to change by its key name, such as `health`, `rendercolor` or
  `target`, or a [custom key](../guide/entity-keyvalues.md#custom-keys) such as `$i_count`
- **New value** (`m_iszNewValue`) - Sets the new value, as a number, three numbers `x y z` or text. A single value can
  also be a named constant, in capitals or not, such as `FL_ONGROUND`, `SOLID_NOT`, `EF_NODRAW`, `MOVETYPE_FLY`,
  `kRenderTransAdd` or `CLASS_PLAYER`. A `~` in front of a constant flips all its bits
- **Type of value** (`m_iszValueType`) - Sets the operation
    - Whole numbers stay whole numbers, and numbers with decimals keep their decimals. Mod works on whole numbers,
      so 6.5 mod 4 is 2
    - The entity works out a vector one part at a time
    - "Direction to Angles" and "Angles to Direction" turn the key's own value into the other form. They don't use
      **New value** or the flags **Don't use X**, **Don't use Y** and **Don't use Z**
    - Text keys only take Replace and Append
- **Trigonometric funcs. behavior** (`m_trigonometricBehaviour`) - Sets the unit of the angle operations
    - Degrees (0, default) - Sin, Cos, Tan and Cot take the value in degrees, and Arcsin, Arccos, Arctan and Arccot
      give degrees, so the sine of 30 is 0.5
    - Radians (1) - Both are in radians
- **Append spaces** (`m_iAppendSpaces`) - For text, adds this many spaces after the result, up to 255
- **Trigger after operation** (`message`) - Fires this target after the change. It can be a name, `!activator` or
  `!caller`
- **Treat new value as** (`value_type`) - Sets whether the entity uses **New value** as you wrote it or as a
  [locus](../guide/locus.md) key. A locus key is worked out for the activator each time the entity fires

## Flags

- **Don't use X** (1) - The X of a vector stays as it is
- **Don't use Y** (2) - The Y of a vector stays as it is
- **Don't use Z** (4) - The Z of a vector stays as it is
- **Invert target value** (32) - The current value becomes negative before the operation
- **Invert source value** (64) - The new value becomes negative before the operation

## Notes

- Any use type triggers the change. The entity writes the new value the way the map loader writes a key, so it works
  on every key that the entity reads from the map
- If you put three numbers such as `0 0 50` into a key that holds a single number, the key gets the vector's length,
  here 50. If the second and the third number are 0, as in `-30 0 0`, the key gets the first number, here -30
- Three numbers go into a vector key part by part, so `64 0 0` with Add moves an `origin` 64 units along X only. A
  single number such as `2` goes into every part
- A division or a modulo by zero leaves the value as it was
- You can only replace a key that the game can't read back. Any other operation leaves it as it is, and with
  `developer 1` set in the console, the console says so
- The entity refuses keys that name a model or a sound, because nothing can be precached while the map runs. It also
  refuses `classname` and `headscale`. With `developer 1` set in the console, the console shows each refused key
- Setups from Sven Co-op carry over, because the class names, key names, flags and operation numbers are the same

## See also

- [`trigger_copyvalue`](trigger_copyvalue.md) - copies a key of one entity into others
- [`trigger_condition`](trigger_condition.md) - compares a key with a value
- [Changing keys](../guide/changing-keys.md) - every operation and what can change

## Changes since 1.38

- `trigger_changevalue` is new
