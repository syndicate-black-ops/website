A `calc_numfromvec` takes one number out of a vector, such as its X part or its length, and hands it to the entity
that asks for it.

Triggering it does nothing. Instead, you put its name in a key that takes a number, marked **[LR]** in the editor, and
each time that key needs a number, the `calc_numfromvec` works it out again at that moment. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's number key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Vector to use** (`target`) - Sets the vector to read, and **Vector value is** sets how the entity reads it. You
  can use three numbers such as `0 0 100`, or the name of an entity. With `*locus` or `!activator`, it uses the
  entity that started the chain of triggers
    - If you leave this key empty, it works like `*locus`
- **Number to get** (`impulse`) - Picks the number to take out of the vector. For a color, the X, Y and Z parts are
  its red, green and blue
    - X (0) - The X part, or the red of a color
    - Y (1) - The Y part, or the green of a color
    - Z (2) - The Z part, or the blue of a color
    - Length (3) - The length of the vector, so for a velocity it is the speed in units per second
    - Pitch (4) - How far the vector points up, in degrees from 0 up to 90, and a vector that points down gives a
      value from 270 up to 360
    - Yaw (5) - The compass direction the vector points to, in degrees from 0 up to 360, where 0 is east and 90 is
      north
- **Vector value is** (`vector_type`) - Sets how **Vector to use** is read
    - Velocity (0) - As a [locus vector](../guide/locus.md#value-types), so an entity name gives that entity's
      velocity
    - Position (1) - As a [locus position](../guide/locus.md#value-types), so an entity name gives that entity's
      position
    - Color (2) - As a color, so an entity name gives that entity's **FX Color**

## Notes

- If **Vector to use** gives no vector, the `calc_numfromvec` gives no number, so the entity that asked does nothing
  that time, and with `developer 1` set in the console, the console reports it
- A key that takes a position or a vector doesn't get the number. It gets the position of the `calc_numfromvec`
  itself or a vector of 0 0 0

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_vecfromnums`](calc_vecfromnums.md) - makes a vector out of three numbers
- [`calc_ratio`](calc_ratio.md) - works out a number from one number
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a vector

## Changes since 1.38

- `calc_numfromvec` is new in SBO 2.0.0
