The Ichthyosaur is a large sea creature that swims in water and bites.

## Attributes

- **Target** (`target`) - Names the [`path_corner`](path_corner.md) the Ichthyosaur swims to first, and from there it
  follows the path while it is idle
- **Preview Sequence** (`sequence`) - Only sets the animation of the model preview in the editor, because in the game
  the Ichthyosaur's AI picks its animations

## Notes

- With **Fade Corpse** (512), the corpse fades out once its death animation ends, and so does the corpse of one that a
  [`monstermaker`](monstermaker.md) made, unless the maker's **Number of Monsters** is 1

## See also

- [`monstermaker`](monstermaker.md) - makes monsters while the map runs
- [monster_ichthyosaur on TWHL](https://twhl.info/wiki/page/monster_ichthyosaur) - the Half-Life entity

## Changes since 1.38

- Destroyed turrets, sentry guns and ichthyosaur bodies fade away when the map sets the Fade Corpse flag. Their own
  death code never read the flag. This was a bug in SBO 1.38
- Fixed ichthyosaurs steering into walls. They checked for walls at the wrong points around them. This was a bug in
  SBO 1.38
