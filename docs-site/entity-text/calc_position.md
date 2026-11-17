---
description: "A calc_position works out a position from another entity, such as where it is or where its eyes are, and can add an offset."
---
A `calc_position` works out a position from another entity, such as where that entity is, where its eyes are or the
middle of its body, adds an offset if you give one, and hands the result to the entity that asks for it.

Triggering it does nothing. Instead, you put its name in a key that takes a position, marked **[LP]** in the editor,
such as the **Position** of an [`env_explosion`](env_explosion.md), and each time that key needs a position, the
`calc_position` works it out again at that moment. See the [Locus guide](../../guides/locus.md) for more details and
some setups.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's position key so it reads this one. See
  [Common keys](common-keys.md#targetname)
- **Entity to use** (`netname`) - Names the entity to take the position from. With `*locus` or
  [`!activator`](../guide/entity-triggering.md#target-selectors), it uses the entity that started the chain of
  triggers, such as the player who pressed a button. Default `*locus`
    - If you leave this key empty, it works like `*locus`
- **Position to calculate** (`impulse`) - Picks which point of that entity the position is
    - Origin (0, default) - The entity's own position. For a brush entity without an origin brush, this is the
      point 0 0 0 of the map, so pick Center instead
    - Eyes (1) - Where the entity's eyes are, which for a player is where they look from. An entity without eyes
      gives its Origin
    - Top (2) - The middle of the top of the entity's box
    - Center (3) - The middle of the entity's box
    - Bottom (4) - The middle of the bottom of the entity's box, which for a monster or a player is about where
      their feet are
    - Attachment point 0 (5) - The first attachment point of the entity's model, a point the model maker placed,
      such as a hand or the end of a gun barrel
    - Attachment point 1 (6) - The second attachment point
    - Attachment point 2 (7) - The third attachment point
    - Attachment point 3 (8) - The fourth attachment point
    - Random (in its box) (9) - A random point inside the entity's box, which is different every time something asks
    - Calc Position of the entity (10) - Asks the named entity for its own position, so you can chain this to
      another `calc_position` or read the position a [`locus_variable`](locus_variable.md) stored
    - Body (11) - The point monsters aim at when they shoot at the entity, which for a monster is between its middle
      and its eyes, and for a player is a point that changes at random between their chest and their eyes
- **Add offset** (`message`) - Adds a vector to the point, such as `0 0 50` to go 50 units up. It takes a
  [locus vector](../guide/locus.md), so it can also name a `calc_` entity

## Notes

- If the entity named in **Entity to use** doesn't exist, the `calc_position` gives no position, so the entity that
  asked does nothing that time, and with `developer 1` set in the console, the console names the `calc_position`
- Attachment points only exist on studio models, the `.mdl` files, that have them, and asking for one that the model
  doesn't have gives no position
- Maps made with Spirit of Half-Life 1.8 may call this entity `calc_posfroment`, and SBO accepts that name too

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and values to each other
- [calc_ entities guide](../../guides/calc-entities.md) - setups that chain `calc_` entities
- [Locus system](../guide/locus.md) - every locus rule, and the keys that take a position
- [`calc_subvelocity`](calc_subvelocity.md) - an entity's velocity or the direction it faces
- [`calc_velocity_path`](calc_velocity_path.md) - the vector from one position to another
- [`locus_variable`](locus_variable.md) - records a position so you can use it later

## Changes since 1.38

- `calc_position` is new in SBO 2.0.0
