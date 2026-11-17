A `gibshooter` shoots body gibs, the pieces of flesh and bone of a monster that blew apart, each time you trigger it.

## Attributes

- **Name** (`targetname`) - Triggering the entity shoots its gibs. See [Common keys](common-keys.md#targetname)

## Notes

- **Gib Velocity**, **Position** and **Direction and speed** are worked out again for each gib, for the entity that
  started the chain of triggers
- If one of those keys can't be worked out, that gib is skipped, but it still counts toward **Number of Gibs**

## See also

- [`env_shooter`](env_shooter.md) - shoots a model or a sprite of your choice
- [gibshooter on TWHL](https://twhl.info/wiki/page/gibshooter) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Position**, **Direction and speed** and **Fire on spawn**, and the new flag **Start
  instantly**
- **Gib Velocity** also takes a range or the name of a `calc_` entity
