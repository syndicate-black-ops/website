---
description: "A calc_eval_number works out a number from two or three other numbers, for example their sum, product, smallest or largest."
---
A `calc_eval_number` works out a number from two or three other numbers: it adds, subtracts, multiplies or divides
them, or takes the remainder, the smallest or the largest of them.

You can use it in two ways. A key that takes a number, marked **[LR]** in the editor, can name the `calc_eval_number`,
and it then works out the number again each time that key needs it. When you trigger it, it works out the number,
stores it in the entity named in **Store result in**, and fires its targets. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's number key so it reads this one, and
  triggering the entity by this name works out the number and fires its targets. See
  [Common keys](common-keys.md#targetname)
- **First operand** (`left_operand`) - Sets the first number, a [locus number](../guide/locus.md), so it can be a
  number such as `5`, a range such as `1..10` for a random number in it, or the name of an entity that gives a
  number. With `!activator` or `*locus`, it is the number of the entity that started the chain of triggers, which
  for a player or a monster is their health divided by their maximum health
    - If you leave this key empty, the entity gives no number
- **Second operand** (`right_operand`) - Sets the second number, in the same way as **First operand**
    - If you leave this key empty, the entity gives no number
- **Third operand** (`third_operand`) - Sets a third number, in the same way. The operation is done again with
  the result and this number, so with Add, the result is the sum of all three. Leave it empty to work with two
  numbers
- **Operation** (`operation`) - Picks what the entity does with the numbers
    - Add (0) - The first number plus the second
    - Subtract (1) - The first number minus the second
    - Multiply (2) - The first number times the second
    - Divide (3) - The first number divided by the second, and dividing by 0 fails
    - Mod (4) - The remainder when you divide the first number by the second, so 7 and 3 give 1, and 0 as the
      second number fails
    - Find min (5) - The smaller of the two numbers
    - Find max (6) - The larger of the two numbers
- **Store result in** (`store_result`) - Names the entities that get the result when you trigger the entity, with
  the [use type](../guide/trigger-modes.md) Set, so a [`game_number`](game_number.md) or a
  [`game_counter`](game_counter.md) takes the result as its value
- **Trigger after operation** (`target`) - Names the entities to trigger when you trigger the entity and it works
  out a number, after it has stored the result
- **Trigger on calculation fail** (`trigger_on_fail`) - Names the entities to trigger instead when you trigger the
  entity and it can't work out a number. That happens when an operand is missing or gives no number, when it divides
  by 0, or when the result is too large to use
- **Min** (`min_value`) - Sets the lowest result, a locus number. **If outside range** sets what happens to a result
  below it
- **Max** (`max_value`) - Sets the highest result, a locus number. **If outside range** sets what happens to a
  result above it
- **If outside range** (`clamp_policy`) - Sets what happens to a result outside **Min** and **Max**, when you set
  both of them. With only one of them set, a result past it always becomes that limit
    - Pick nearest value (0) - The result becomes the limit it went past
    - Wrap around (1) - The result comes back in at the other end, so with **Min** 0 and **Max** 10, 12 becomes 2
    - Bounce back (2) - The result bounces back off the limit it went past, so with **Min** 0 and **Max** 10, 12
      becomes 8
- **Report as vector** (`vector_mode`) - Lets keys that take a [vector or a position](../guide/locus.md#value-types)
  read the result too, as one of the three parts of a vector
    - No (0) - Keys that take a vector or a position get nothing
    - X 0 0 (1) - The result is the X part, and Y and Z are 0
    - 0 Y 0 (2) - The result is the Y part, and X and Z are 0
    - 0 0 Z (3) - The result is the Z part, and X and Y are 0
- **Cast first operand** (`first_cast_mode`) - Turns the first number into a whole number before the operation
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2
- **Cast second operand** (`second_cast_mode`) - Turns the second number into a whole number before the
  operation
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2
- **Cast third operand** (`third_cast_mode`) - Turns the third number into a whole number before the operation
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2
- **Cast result** (`result_cast_mode`) - Turns the result into a whole number after **Min** and **Max** have been
  applied
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2

## Notes

- A number in a key must start with a digit or a minus sign, so write `0.5` and not `.5`, because `.5` is read as
  the name of an entity
- If a target triggers the same `calc_eval_number` again while it fires its targets, that trigger is ignored, and with
  `developer 1` set in the console, the console reports it

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`game_number`](game_number.md) - holds a number you can store and read
- [`calc_ratio`](calc_ratio.md) - works out a number from one number, with functions such as square root and sine
- [`trigger_compare`](trigger_compare.md) - compares two numbers and fires a target
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a number

## Changes since 1.38

- `calc_eval_number` is new in SBO 2.0.0
