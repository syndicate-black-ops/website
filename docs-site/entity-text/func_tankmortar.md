A `func_tankmortar` is a mounted mortar whose shots are explosions where it aims. It aims at targets by itself, or a
player controls it from a [`func_tankcontrols`](func_tankcontrols.md), and it has the keys of a
[`func_tank`](func_tank.md).

## Attributes

- **Explosion Magnitude** (`iMagnitude`) - Sets the damage of each explosion, and its damage reaches 2.5 times this
  value in units
    - If you leave this key empty, it is 0 and each shot is a small blast that does no damage
- **Bullet accuracy** (`firespread`) - Sets how far each explosion can land from where the gun points, in a cone
  that gets wider with each choice
    - Perfect Shot (0) - Every shot goes where the gun points
    - Small cone (1)
    - Medium cone (2)
    - Large cone (3)
    - Extra-large cone (4)

## Notes

- The player at the controls gets the kills of the gun: the frags, the Co-op XP and the line in the kill feed. While
  nobody is at the controls, no player gets them

## See also

- [`func_tank`](func_tank.md) - a mounted gun
- [`func_tankcontrols`](func_tankcontrols.md) - the place where a player takes the controls
- [`func_mortar_field`](func_mortar_field.md) - drops mortar shells into an area
- [func_tankmortar on TWHL](https://twhl.info/wiki/page/func_tankmortar) - the Half-Life entity

## Changes since 1.38

- You can use the new keys and flags of [`func_tank`](func_tank.md#changes-since-138)
- The player at the controls gets the kills. In SBO 1.38, as in Half-Life, the kills went to the explosion and the
  player got nothing
