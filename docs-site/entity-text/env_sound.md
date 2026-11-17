An `env_sound` sets the echo of a room, the sound effect players hear there, for each player who is within its radius
and in its line of sight.

## Attributes

- **Radius** (`radius`) - Sets how close, in units, a player must be for the room type to apply. The player must
  also be in the line of sight of the entity, and when several `env_sound` entities are in range, the nearest one
  sets the echo
    - If you leave this key empty, it is 0 and the room type never applies
- **Room Type** (`roomtype`) - Picks the echo players hear. It stays until they come into range of another
  `env_sound`
    - Normal (0) - No echo
    - Generic (1)
    - Metal Small (2)
    - Metal Medium (3)
    - Metal Large (4)
    - Tunnel Small (5)
    - Tunnel Medium (6)
    - Tunnel Large (7)
    - Chamber Small (8)
    - Chamber Medium (9)
    - Chamber Large (10)
    - Bright Small (11)
    - Bright Medium (12)
    - Bright Large (13)
    - Water 1 (14)
    - Water 2 (15)
    - Water 3 (16)
    - Concrete Small (17)
    - Concrete Medium (18)
    - Concrete Large (19)
    - Big 1 (20)
    - Big 2 (21)
    - Big 3 (22)
    - Cavern Small (23)
    - Cavern Medium (24)
    - Cavern Large (25)
    - Weirdo 1 (26)
    - Weirdo 2 (27)
    - Weirdo 3 (28)

## Notes

- A player keeps the echo after they leave the radius, until another `env_sound` takes over. When they come back
  into the radius of the same `env_sound`, they get its echo again, and the game sends the echo again after a
  respawn and at a map change

## See also

- [`ambient_generic`](ambient_generic.md) - plays a sound at its position
- [env_sound on TWHL](https://twhl.info/wiki/page/env_sound) - the Half-Life entity

## Changes since 1.38

- A player who leaves the radius of an `env_sound` and comes back gets its echo again. In SBO 1.38, they didn't
