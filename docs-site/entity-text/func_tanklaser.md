A `func_tanklaser` is a mounted laser that fires the beam of an [`env_laser`](env_laser.md). It aims at targets by
itself, or a player controls it from a [`func_tankcontrols`](func_tankcontrols.md), and it has the keys of a
[`func_tank`](func_tank.md).

## Attributes

- **env_laser Entity** (`laserentity`) - Names the `env_laser` that this gun fires
    - If you leave this key empty, or it names no `env_laser`, the gun removes itself when the map starts
- **Bullet accuracy** (`firespread`) - Sets how far the laser strays from where the gun points, in a cone that gets
  wider with each choice
    - Perfect Shot (0) - Every shot goes where the gun points
    - Small cone (1)
    - Medium cone (2)
    - Large cone (3)
    - Extra-large cone (4)

## Notes

- The player at the controls gets the kills of the gun: the frags, the Co-op XP and the line in the kill feed. While
  nobody is at the controls, no player gets them
- The beam goes off when the player leaves the controls and when something blocks the gun

## See also

- [`func_tank`](func_tank.md) - a mounted gun
- [`func_tankcontrols`](func_tankcontrols.md) - the place where a player takes the controls
- [`env_laser`](env_laser.md) - the beam it fires
- [func_tanklaser on TWHL](https://twhl.info/wiki/page/func_tanklaser) - the Half-Life entity

## Changes since 1.38

- You can use the new keys and flags of [`func_tank`](func_tank.md#changes-since-138)
- The player at the controls gets the kills. In SBO 1.38, as in Half-Life, the kills went to the beam and the player
  got nothing
- The beam goes off when the player leaves the controls. In SBO 1.38, it stayed on
- The beam goes off when something blocks the gun. In SBO 1.38, it stayed on while the gun was blocked
- The beam goes off when a trigger removes the gun right after a shot. In SBO 1.38, the beam could stay on for good
