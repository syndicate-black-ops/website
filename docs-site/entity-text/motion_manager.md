A `motion_manager` keeps moving or turning an entity in every frame until you turn it off.

## Attributes

- **Target to affect** (`target`) - Names the entities to move, as a name or `!activator`
- **Position** (`m_iszPosition`) - Sets where or how fast the target moves, as a [locus position](../guide/locus.md)
  or a locus vector, which **Meaning of Position** decides, and speeds are in units per second
    - If you leave this key empty, the position doesn't change
- **Meaning of Position** (`m_iPosMode`) - Sets what **Position** does to the target in each frame
    - Set position [LP] (0) - It places the target at the position
    - Offset position, units per second [LV] (1) - It moves the target by the vector each second
    - Set velocity [LV] (2) - It sets the target's velocity to the vector
    - Accelerate by [LV] (3) - It adds the vector to the target's velocity each second
    - Follow position [LP] (4) - It moves the target toward the position, fast while it is far away and slower as it
      gets close
- **Facing** (`m_iszFacing`) - Sets which way or how fast the target turns, as a locus vector or as three numbers in
  the order Y Z X, which **Meaning of Facing** decides, and turns are in degrees per second
    - If you leave this key empty, the angles don't change
- **Meaning of Facing** (`m_iFaceMode`) - Sets what **Facing** does to the target in each frame
    - Face direction [LV] (0) - It turns the target to face the direction, and a zero direction leaves the angles as
      they are
    - Rotate by a direction's angles, per second [LV] (1) - It turns the target by the angles of the direction each
      second
    - Rotate by (Y Z X), per second (2) - It turns the target by the three angles each second
    - Set avelocity (Y Z X) (3) - It sets the target's turning speed to the three angles
    - Set angles to an entity's angles (4) - It copies the angles of the entity that **Facing** names

## Flags

- **Debug** (1) - With `developer 1` set in the console, the server console shows each change
- **Obey Trigger Mode** (16) - On starts it, Off stops it and Toggle switches it, while without this flag, On adds the
  movement to each target, Off removes it and Toggle starts it again
- **Start On** (32) - It is on from the start of the map, and without a name, it is always on

## Notes

- Each target keeps moving until the `motion_manager` is turned off or the target is gone, or for a key that uses
  `!activator`, until the activator is gone
- It stops moving a player who dies or becomes a spectator
- When it moves a brush that players stand on, those players jerk, because nothing predicts the movement
- It doesn't move the entities that move along with the target
- Each moving target costs the server a little work in every frame, but only while it runs
- If the entity it moves has **Move with**, a new position or new angles are where it goes now, and it keeps that
  place on its parent from then on, while a velocity is its own movement on top of its parent's. On a solid child,
  the position modes move it in jumps, so players standing on it aren't carried, while the velocity modes carry them. See
  [Moving objects](../features/moving-objects.md#cameras-world-text-and-screens)

## See also

- [`trigger_motion`](trigger_motion.md) - makes one change for each trigger
- [Locus system](../guide/locus.md) - the positions and vectors these keys accept

## Changes since 1.38

- `motion_manager` is new
