---
description: "A calc_subvelocity takes a vector from another entity, such as how fast it moves, and can change its length and add an offset."
---
A `calc_subvelocity` takes a vector from another entity, such as how fast it moves or the direction it faces, and
hands it to the entity that asks for it. It can change the vector's length and add an offset first.

Triggering it does nothing. Instead, you put its name in a key that takes a vector, marked **[LV]** in the editor, and
each time that key needs a vector, the `calc_subvelocity` works it out again at that moment. See the [Locus
guide](../../guides/locus.md) for more details and some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's vector key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Entity to use** (`netname`) - Names the entity to take the vector from. With `*locus` or `!activator`, it uses
  the entity that started the chain of triggers, such as the player who pressed a button
    - If you leave this key empty, it works like `*locus`
- **Value to calculate from** (`impulse`) - Picks which vector of the entity it takes
    - Movement velocity (0) - How fast and in which direction the entity moves, in units per second
    - Angles (1) - The direction the entity faces, as a vector 1 unit long
    - View angles (2) - The direction a player looks, as a vector 1 unit long
    - Calc Velocity of the entity (10) - Asks the named entity for its own vector, so you can chain this to another
      `calc_` entity or read the vector a [`locus_variable`](locus_variable.md) stored. That entity works out its
      vector for itself, so `*locus` in its keys means that entity and not the activator
- **Scale factor** (`noise`) - Multiplies the vector by a [locus number](../guide/locus.md). In this key,
  `*locus` and `!activator` stand for the **Entity to use**, not for the entity that started the chain
    - If you leave this key empty, the factor is 1
- **Add offset** (`message`) - Adds a [locus vector](../guide/locus.md) after the scaling. In this key too,
  `*locus` and `!activator` stand for the **Entity to use**

## Flags

- **Normalize before scaling** (1) - The vector is made 1 unit long before **Scale factor** multiplies it, so the
  factor sets its exact length
- **Flip vertical** (2) - The Z part of the result is turned around, so up becomes down
- **Discard X** (4) - The X part of the result is 0
- **Discard Y** (8) - The Y part of the result is 0
- **Discard Z** (16) - The Z part of the result is 0

## Notes

- The flags work on the result after the offset is added
- If the entity named in **Entity to use** doesn't exist, the `calc_subvelocity` gives no vector, so the entity that
  asked does nothing that time, and with `developer 1` set in the console, the console reports it
- Maps made with Spirit of Half-Life 1.8 may call this entity `calc_vecfroment`, and SBO accepts that name too

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [`calc_position`](calc_position.md) - a position on an entity
- [`calc_velocity_path`](calc_velocity_path.md) - the vector from one position to another
- [`calc_velocity_polar`](calc_velocity_polar.md) - turns a vector and changes its length
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a vector

## Changes since 1.38

- `calc_subvelocity` is new in SBO 2.0.0
