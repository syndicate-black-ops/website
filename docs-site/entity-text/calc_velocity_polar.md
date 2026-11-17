A `calc_velocity_polar` turns a vector by angles you set and hands the result to the entity that asks for it. It can
also change the vector's length and add an offset.

Triggering it does nothing. Instead, you put its name in a key that takes a vector, marked **[LV]** in the editor, and
each time that key needs a vector, the `calc_velocity_polar` works it out again at that moment. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's vector key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Based on vector** (`netname`) - Sets the vector to turn, a [locus vector](../guide/locus.md), so it can be three
  numbers such as `100 0 0` or the name of an entity, which gives that entity's velocity. With `*locus` or
  `!activator`, it is the velocity of the entity that started the chain of triggers
    - If you leave this key empty, it works like `*locus`
- **Rotated by angle** (`angles`) - Sets how far to turn the vector, as three angles in degrees: the pitch, the yaw
  and the roll. A yaw of 90 turns a vector that points east so it points north, and a positive pitch turns it
  up. With `0 0 0`, the result points the same way as **Based on vector**
- **Length factor** (`noise`) - Sets the length of the result as a [locus number](../guide/locus.md): the length of
  **Based on vector** times this number
    - If you leave this key empty, the factor is 1
- **Add offset** (`message`) - Adds a [locus vector](../guide/locus.md) after the turn

## Flags

- **Normalize** (1) - The length of the result is **Length factor** itself, and the length of **Based on vector**
  doesn't count, so only its direction is used

## Notes

- If **Based on vector** gives no vector, the entity works with `0 0 0`, so without **Normalize** the result is only
  the offset
- Maps made with Spirit of Half-Life 1.8 may call this entity `calc_vecfromvec`, and SBO accepts that name too

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_subvelocity`](calc_subvelocity.md) - an entity's velocity or the direction it faces
- [`calc_vecfromnums`](calc_vecfromnums.md) - makes a vector out of three numbers
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a vector

## Changes since 1.38

- `calc_velocity_polar` is new in SBO 2.0.0
- Changed in SBO 2.1.0: the result keeps the up or down direction of **Based on vector**
  1.8. In SBO 2.0.0 a vector that pointed up came out pointing down, because the two angle steps it uses count the
  pitch in opposite directions
