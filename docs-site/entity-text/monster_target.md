A `monster_target` is invisible, and monsters see it as a monster of the side you choose, so the monsters that hate
that side attack it.

## Attributes

- **Classification** (`frags`) - Sets the class the other monsters see it in, and with the default "Player ally",
  the enemies of the players attack it. See [Monster classes](../guide/monster-classes.md) for which classes attack
  which
    - Ignored (0) - Monsters ignore it

## Flags

- **Start inactive** (1) - It starts inactive, so monsters ignore it until you turn it on

## Notes

- Triggering it turns it on or off, as the [use type](../guide/trigger-modes.md) says
- It isn't solid and takes no damage, so shots go through it to what is behind it
- Automatic [`func_tank`](func_tank.md) guns shoot at it while it counts as "Player" or "Player ally", just as they
  shoot at players

## See also

- [`env_soundmark`](env_soundmark.md) - makes a sound that monsters hear
- [`func_tank`](func_tank.md) - a gun turret that can shoot at it

## Changes since 1.38

- `monster_target` is new
