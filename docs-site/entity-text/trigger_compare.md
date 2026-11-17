A `trigger_compare` compares two numbers when you trigger it and fires targets for the result. It is also a
[master](../guide/masters-and-states.md) that is on while the comparison passes.

## Attributes

- **Base value** (`initial_value`) - Sets the first number, as a number or a [locus number](../guide/locus.md), such as
  a [`game_number`](game_number.md) or a `calc_` entity
- **Compare value** (`compare_value`) - Sets the number that the entity compares the **Base value** with. It takes a
  number or a [locus number](../guide/locus.md), which the entity reads each time
- **Comparison to pass** (`testtype`) - Sets the comparison for **Fire on comparison pass**, **Fire on comparison
  fail** and the master
- **Fire on comparison pass** (`pass_target`) - Fires this target when the **Comparison to pass** is true
- **Fire on comparison fail** (`fail_target`) - Fires this target when the **Comparison to pass** is false
- **Fire on equal** (`trigger_on_equal`) - Fires this target when the base value equals the compare value
- **Fire on not equal** (`trigger_on_not_equal`) - Fires this target when the base value differs from the compare value
- **Fire on less than** (`trigger_on_less`) - Fires this target when the base value is less than the compare value
- **Fire on greater than** (`trigger_on_greater`) - Fires this target when the base value is greater than the compare value
- **Fire on calc fail** (`trigger_on_fail`) - Fires this target when one of the numbers can't be worked out

## Notes

- Every target fires with the use type Toggle and gets the activator of the trigger
- The four targets from **Fire on equal** to **Fire on greater than** fire by the result, and **Comparison to pass**
  doesn't change them
- A target that triggers the same `trigger_compare` while it fires is ignored
- As a master, it compares at the moment the master is checked, and it is off when a number can't be worked out

## See also

- [`game_number`](game_number.md) - holds a number
- [`calc_eval_number`](calc_eval_number.md) - works out a number from others
- [`trigger_condition`](trigger_condition.md) - compares a key of an entity
- [Locus guide](../../guides/locus.md) - setups with `trigger_compare`

## Changes since 1.38

- `trigger_compare` is new
