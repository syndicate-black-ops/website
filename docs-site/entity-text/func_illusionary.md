A `func_illusionary` is drawn like a wall, but it isn't solid, so players, monsters and shots pass through it.

## Attributes

- **Contents** (`skin`) - Picks what the brush is filled with for the engine
    - Empty (-1) - Open air
    - Volumetric Light (-7) - A choice from Half-Life's entity list, which no map compiler reads and which adds
      nothing in the game
    - If you leave this key empty, it works like Empty
- **Generate Cliphulls** (`zhlt_noclip`) - Sets whether the map compiler builds collision hulls for the brush.
  Players pass through a `func_illusionary` either way
    - Yes (0) - The compiler builds the hulls
    - No (1) - The compiler builds no hulls, which keeps the map smaller

## See also

- [`func_illusionary_toggle`](func_illusionary_toggle.md) - the same, which you can show and hide
- [`func_wall`](func_wall.md) - a brush that is solid
- [func_illusionary on TWHL](https://twhl.info/wiki/page/func_illusionary) - the Half-Life entity
