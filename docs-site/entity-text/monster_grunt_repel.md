A `monster_grunt_repel` sends a Fed down a rope when you trigger it, and the Fed then joins the fight as a
[`monster_human_grunt`](monster_human_grunt.md). It works once.

## Attributes

- **Preview Sequence** (`sequence`) - Only sets the pose of the model preview in the editor, because in the game
  this entity has no model and the Fed picks its own animations

## Notes

- Each entity sends one Fed and is then removed
- The Fed appears at the entity with its angles, and the rope hangs from 112 units above the entity, so the entity
  needs a clear drop below it
- The entity only has a name and angles, so the Fed starts with its default keys

## See also

- [`monster_human_grunt`](monster_human_grunt.md) - the Fed it sends
- [`monster_grunt_hunter_repel`](monster_grunt_hunter_repel.md) - the same for a Fed Hunter
- [monster_grunt_repel on TWHL](https://twhl.info/wiki/page/monster_grunt_repel) - the Half-Life entity

