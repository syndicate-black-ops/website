---
description: "A calc_ratio works out a number from another number with a function, an offset, a multiplier and a range."
---
A `calc_ratio` works out a number from another number and hands the result to the entity that asks for it. It can
change the number with a function such as 1 minus the number, the square or the sine, then add an offset, multiply it
and keep it inside a range.

Triggering it does nothing. Instead, you put its name in a key that takes a number, marked **[LR]** in the editor, and
each time that key needs a number, the `calc_ratio` works it out again at that moment. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's number key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Based on number** (`target`) - Sets the number to start from, a [locus number](../guide/locus.md), so it can be
  a number such as `5`, a range such as `1..10` for a random number in it, or the name of an entity that gives a
  number. With `*locus` or `!activator`, it is the number of the entity that started the chain of triggers, which
  for a player or a monster is their health divided by their maximum health
    - If you leave this key empty, it works like `*locus`
- **Transformation** (`impulse`) - Picks a function that changes the number before the offset and the scale factor.
  The angles of the trigonometry functions are in degrees, and a result that isn't a number, such as 1 divided by 0
  or the square root of a negative number, gives no number
    - None (0) - The number stays as it is
    - Reversed (1) - 1 minus the number, so 0.25 becomes 0.75
    - Negative (2) - The number with its sign turned around, so 5 becomes -5
    - Reciprocal (3) - 1 divided by the number, so 4 becomes 0.25
    - Square (4) - The number times itself
    - Inverse Square (5) - 1 divided by the square of the number
    - Square root (6) - The square root of the number
    - Cosine (7) - The cosine of the number, as an angle
    - Sine (8) - The sine of the number, as an angle
    - Tangent (9) - The tangent of the number, as an angle
    - Inverse Cosine (10) - The angle whose cosine is the number, which only works from -1 up to 1
    - Inverse Sine (11) - The angle whose sine is the number, which only works from -1 up to 1
    - Inverse Tangent (12) - The angle whose tangent is the number
- **Offset by** (`netname`) - Adds a locus number to the result after the transformation
- **Scale factor** (`message`) - Multiplies the result by a locus number, after the transformation and the offset
- **Min** (`noise`) - Sets the lowest result, a locus number. **If outside range** sets what happens to a result
  below it
- **Max** (`noise1`) - Sets the highest result, a locus number. **If outside range** sets what happens to a result
  above it
- **If outside range** (`frags`) - Sets what happens to a result outside **Min** and **Max**, when you set both of
  them. With only one of them set, a result past it always becomes that limit
    - Pick nearest value (0) - The result becomes the limit it went past
    - Wrap around (1) - The result comes back in at the other end, so with **Min** 0 and **Max** 10, 12 becomes 2
    - Bounce back (2) - The result bounces back off the limit it went past, so with **Min** 0 and **Max** 10, 12
      becomes 8
- **Cast base** (`base_cast_mode`) - Turns the starting number into a whole number before the transformation
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2
- **Cast result** (`result_cast_mode`) - Turns the result into a whole number at the end, after **Min** and **Max**
    - No cast (0) - The number stays as it is
    - Round (1) - Rounds to the nearest whole number, so 2.5 becomes 3
    - Floor (2) - Rounds down, so 2.7 becomes 2 and -2.3 becomes -3
    - Ceil (3) - Rounds up, so 2.3 becomes 3
    - Trunc (4) - Cuts off the part after the point, so 2.7 becomes 2 and -2.7 becomes -2

## Notes

- A key that takes a position or a vector doesn't get the number. It gets the position of the `calc_ratio` itself or
  a vector of 0 0 0, so use [`calc_vecfromnums`](calc_vecfromnums.md) to turn numbers into a vector
- If any number it needs is missing, the `calc_ratio` gives no number, so the entity that asked does nothing that
  time
- Maps made with Spirit of Half-Life 1.8 may call this entity `calc_numfromnum`, and SBO accepts that name too
- You can change **Min** and **Max** with [`trigger_changevalue`](trigger_changevalue.md) or
  [`trigger_copyvalue`](trigger_copyvalue.md) while the map runs. See [Changing keys](../guide/changing-keys.md)

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_eval_number`](calc_eval_number.md) - works out a number from two or three numbers
- [`calc_numfromvec`](calc_numfromvec.md) - takes a number out of a vector, such as its length
- [`player_calc_ratio`](player_calc_ratio.md) - gives a number about a player
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a number

## Changes since 1.38

- `calc_ratio` is new in SBO 2.0.0
