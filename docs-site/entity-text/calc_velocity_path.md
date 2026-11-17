---
description: "A calc_velocity_path works out the vector from a start position to a destination, and can cut it short where something blocks the line."
---
A `calc_velocity_path` works out the vector from a start position to a destination and hands it to the entity that
asks for it. It can change the vector's length and cut it short where something blocks the line.

Triggering it does nothing. Instead, you put its name in a key that takes a vector, marked **[LV]** in the editor, and
each time that key needs a vector, the `calc_velocity_path` works it out again at that moment. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's vector key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Start position** (`target`) - Sets where the vector starts, a [locus position](../guide/locus.md), so it can be
  a point such as `0 0 64`, the name of an entity or of a [`calc_position`](calc_position.md). With `*locus` or
  `!activator`, it is the position of the entity that started the chain of triggers
    - If you leave this key empty, it works like `*locus`
- **Destination** (`netname`) - Sets where the vector goes, and **Destination is** sets how it is read
    - If you leave this key empty, the entity gives no vector
- **Destination is** (`armorvalue`) - Sets how **Destination** is read
    - Position (0) - As a locus position, so the result is the vector from **Start position** to that point
    - Offset (1) - As a locus vector, which is the result itself, measured from **Start position**
- **Length calculation** (`health`) - Changes the length of the vector before **Length factor** multiplies it,
  and the direction stays the same. In the list, X is the length
    - None (0) - The length stays as it is
    - Normalize (1) - The vector is 1 unit long
    - Reciprocal (2) - The length becomes 1 divided by the length
    - Inverse square (3) - The length becomes 1 divided by the square of the length
    - Square (4) - The length becomes the square of the length
- **Length factor** (`noise`) - Multiplies the vector by a [locus number](../guide/locus.md)
    - If you leave this key empty, the factor is 1
- **Line is blocked by** (`frags`) - Cuts the vector short where a line from **Start position** along it first hits
  something, so the result ends at that point
    - Nothing (0) - Nothing cuts the vector short
    - Walls (1) - Walls cut it short, but the line passes through glass and monsters
    - Walls & glass (2) - Walls and glass cut it short
    - Walls & monsters (3) - Walls, monsters and players cut it short
    - Walls, monsters & glass (4) - Walls, glass, monsters and players cut it short

## Notes

- If the start and the destination are at the same point, the result is `0 0 0`, and **Length calculation** leaves
  it at that
- If a position it needs gives no value, the `calc_velocity_path` gives no vector, so the entity that asked does
  nothing that time
- Maps made with Spirit of Half-Life 1.8 may call this entity `calc_vecfrompos`, and SBO accepts that name too

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_position`](calc_position.md) - a position on an entity
- [`calc_subvelocity`](calc_subvelocity.md) - an entity's velocity or the direction it faces
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a vector

## Changes since 1.38

- `calc_velocity_path` is new in SBO 2.0.0
