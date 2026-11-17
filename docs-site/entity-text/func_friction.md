A `func_friction` changes the friction of players and objects that touch it, so they slide more or less on the floor.
Players walk through the brush, and a player who leaves it gets the normal friction back.

## Attributes

- **Percentage of standard** (`modifier`) - Sets the friction, in percent of normal friction, from 0 for no
  friction at all, like ice, up to 100 for normal. With 15, the floor is slippery
    - If you leave this key empty, it is 0, so there is no friction at all

## Notes

- Bouncing objects, such as grenades, keep their own friction

## See also

- [`func_conveyor`](func_conveyor.md) - a brush that carries players and objects
- [`trigger_push`](trigger_push.md) - a brush that pushes what is inside it
- [func_friction on TWHL](https://twhl.info/wiki/page/func_friction) - the Half-Life entity

## Changes since 1.38

- A player who leaves the brush gets the normal friction back, where in SBO 1.38 the changed friction stayed with the
  player. This was a bug in Half-Life multiplayer that SBO 1.38 kept
