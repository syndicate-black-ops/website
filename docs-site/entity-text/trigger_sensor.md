---
description: "A trigger_sensor finds the entities within a radius when you trigger it, and fires its target for each of them, or only for the closest or farthest."
---
A `trigger_sensor` finds the entities within a radius when you trigger it, and fires its target for each of them, or
only for the closest or the farthest one, with the found entity as `!activator`.

## Attributes

- **Target** (`target`) - Fires for each entity the sensor finds, or only for the closest or the farthest, with that
  entity as the activator
- **Radius** (`radius`) - Sets how far around its center the sensor looks, in units
- **Source Position** (`position`) - Sets the center of the search as a [locus position](../guide/locus.md)
    - If you leave this key empty, the center is this entity
- **Line is blocked by** (`line_blocked`) - Sets what blocks the line from the center to an entity. The sensor
  doesn't find an entity if its line is blocked, and "Nothing" means no line check
- **Trace line to** (`trace_to`) - Sets the point on the entity that the line goes to. The sensor also measures the
  distance to this point
- **Fire trigger for** (`fire_trigger_policy`) - Sets whether the target fires for every found entity, or only for the
  one closest to or farthest from the center
- **Entity is alive** (`alive_filter`) - Sets whether it only finds living or only dead entities
- **Entity is damageable** (`takedamage_filter`) - Sets whether the found entities must be able to take damage.
  "Yes, aimable" only finds entities that monsters aim at, such as monsters and players
- **Trigger Master** (`sensed_master`) - Names a [master](../guide/masters-and-states.md) that must be on for the
  found entity, with that entity as the activator
- **Required classname** (`sensed_classname`) - Only finds entities of this class
- **Act as Classify** (`classify`) - Sets the monster class that the sensor uses for **My relationship to entity**.
  See
  [Monster classes](../guide/monster-classes.md) for how each class sees the others
- **My relationship to entity** (`relationship_filter`) - Only finds entities that a monster of the **Act as
  Classify** class sees as neutral, an enemy or an ally, as you choose. "Enemy" also finds an entity that sees that
  class as its enemy

## Notes

- Each trigger searches once, and the target gets the use type Toggle
- It only finds alive players, so "Dead only" finds no players
- "Alive only" skips monsters that are dying, and it always skips entities that are being removed
- A target that triggers the sensor while it fires is ignored

## See also

- [`trigger_entity_iterator`](trigger_entity_iterator.md) - fires for each entity that passes a filter, anywhere

## Changes since 1.38

- `trigger_sensor` is new
