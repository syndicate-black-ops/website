---
description: "A calc_vecfromnums makes a vector out of three numbers, or takes a vector and replaces some of its parts with numbers."
---
A `calc_vecfromnums` makes a vector out of three numbers, or takes a vector and replaces some of its parts with
numbers, and hands the result to the entity that asks for it. A key that takes a position reads the same three numbers
as a point on the map.

Triggering it does nothing. Instead, you put its name in a key that takes a vector or a position, marked **[LV]** or
**[LP]** in the editor, and each time that key needs one, the `calc_vecfromnums` works it out again at that moment.
See the [Locus guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's vector or position key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Base vector** (`base_vector`) - Sets the vector to start from, and **Base vector is** sets how it is read. You
  can use three numbers such as `0 0 100`, or the name of an entity. With `*locus` or `!activator`, it uses the
  entity that started the chain of triggers
    - If you leave this key empty, the vector starts as `0 0 0`
- **Base vector is** (`vector_type`) - Sets how **Base vector** is read
    - Velocity (0) - As a [locus vector](../guide/locus.md#value-types), so an entity name gives that entity's
      velocity
    - Position (1) - As a [locus position](../guide/locus.md#value-types), so an entity name gives that entity's
      position
    - Color (2) - As a color, so an entity name gives that entity's **FX Color**
- **X value** (`x_value`) - Replaces the X part of the vector with a [locus number](../guide/locus.md)
    - If you leave this key empty, the X part of **Base vector** stays
- **Y value** (`y_value`) - Replaces the Y part of the vector with a locus number
    - If you leave this key empty, the Y part of **Base vector** stays
- **Z value** (`z_value`) - Replaces the Z part of the vector with a locus number
    - If you leave this key empty, the Z part of **Base vector** stays

## Notes

- If **Base vector** or one of the numbers gives no value, the `calc_vecfromnums` gives no vector, so the entity
  that asked does nothing that time

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_numfromvec`](calc_numfromvec.md) - takes one number out of a vector
- [`calc_velocity_polar`](calc_velocity_polar.md) - turns a vector and changes its length
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a vector

## Changes since 1.38

- `calc_vecfromnums` is new in SBO 2.0.0
