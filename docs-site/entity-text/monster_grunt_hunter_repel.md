A `monster_grunt_hunter_repel` sends a Fed Hunter down a rope when you trigger it, and the Fed Hunter then joins the
fight as a [`monster_grunt_hunter`](monster_grunt_hunter.md). It works once.

## Attributes

- **Preview Sequence** (`sequence`) - Only sets the pose of the model preview in the editor, because in the game
  this entity has no model and the Fed picks its own animations

## Notes

- Each entity sends one Fed and is then removed
- The Fed appears at the entity with its angles, and the rope hangs from 112 units above the entity, so the entity
  needs a clear drop below it
- The entity only has a name and angles, so the Fed starts with its default keys

## See also

- [`monster_grunt_hunter`](monster_grunt_hunter.md) - the Fed it sends
- [`monster_grunt_repel`](monster_grunt_repel.md) - the same for a Fed

## Changes since 1.38

- Fixed a triggered `monster_grunt_hunter_repel` crashing the server. It tried to create a monster type that does not
  exist in SBO. This was a bug in SBO 1.38
