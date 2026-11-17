A `trigger_motion` sets or changes the position, angles, speed and spin of an entity once for each trigger, and a key
that you leave empty changes nothing.

## Attributes

- **Target to affect** (`target`) - Names the entity, as a name or `!activator`
- **Position** (`m_iszPosition`) - Sets the new position as a [locus position](../guide/locus.md), or with "Add offset",
  a locus vector to add
- **Meaning of Position** (`m_iPosMode`) - Sets whether **Position** moves the target there or adds it as an offset
- **Angles** (`m_iszAngles`) - Sets the angles as a locus vector, or with "Rotate by (Y Z X)", as three numbers
- **Meaning of Angles** (`m_iAngMode`) - Sets whether **Angles** turns the target to face a direction or turns it by
  angles
- **Velocity** (`m_iszVelocity`) - Sets the velocity as a locus vector, or with "Rotate velocity (Y Z X)", as three
  numbers
- **Meaning of Velocity** (`m_iVelMode`) - Sets whether **Velocity** sets the target's speed, adds to it or turns its
  current velocity
- **AVelocity** (`m_iszAVelocity`) - Sets the turning speed as three numbers in the order Y Z X. For a number written
  as `a..b`, the entity picks a random number between a and b
- **Meaning of AVelocity** (`m_iAVelMode`) - Sets whether **AVelocity** sets the target's turning speed or adds to it

## Flags

- **Debug** (1) - With `developer 1` set in the console, the server console shows each change

## Notes

- It only changes a player while they are alive. A player whose speed changes on the server sees a small correction
  on their screen
- It doesn't move the entities that move along with the target
- If the entity it moves has **Move with**, it goes to the new position or angles, and after that it keeps that place
  on its parent. A velocity is its own movement on top of its parent's movement
- On a solid child, the position modes move it in jumps, so the child doesn't carry players who stand on it. The
  velocity modes carry them. See
  [Moving objects](../features/moving-objects.md#cameras-world-text-and-screens)

## See also

- [`motion_manager`](motion_manager.md) - keeps changing them in every frame
- [Locus system](../guide/locus.md) - the positions and vectors these keys accept

## Changes since 1.38

- `trigger_motion` is new
