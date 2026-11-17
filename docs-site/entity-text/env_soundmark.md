An `env_soundmark` makes a sound or a smell each time you trigger it, which only monsters notice. With the sound type
Danger, monsters that know about grenades run from the spot, and with Combat, they come to it.

Calm monsters within the radius that care about the sound type react at once, even when they were busy with
something else, such as greeting a player. A monster that is fighting or plays a script doesn't react this way.

## Attributes

- **Name** (`targetname`) - Triggering the entity makes the sound. See [Common keys](common-keys.md#targetname)
- **Sound Radius** (`radius`) - Sets how far the sound reaches, in units, and monsters within it notice it
    - If you leave this key empty or set 0, it is 384
- **Sound Duration** (`duration`) - Sets how many seconds the sound lasts
    - If you leave this key empty or set 0, it is 0.3
- **Position** (`position`) - Sets where the sound is. It takes a [locus position](../guide/locus.md), so you can use
  a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain of triggers
    - If you leave this key empty, the sound is at the `env_soundmark` itself
- **Sound Type** (`type`) - Picks the kind of sound. Each monster reacts only to the kinds it listens for
    - Combat (1) - The sound of a fight, which draws monsters in
    - World (2) - A noise of the world
    - Player (4) - A sound a player makes
    - Carcass (8) - The smell of a dead body
    - Meat (16) - The smell of meat
    - Danger (32) - A danger such as a grenade, which monsters run from
    - Garbage (64) - The smell of garbage

## Flags

- **Remove On fire** (1) - The entity is removed after it is used once

## Making monsters run

A monster that runs from Danger needs an [`info_node`](info_node.md) at least the radius away and hidden from the
sound, and without one it stays where it is. Monsters side by side can block each other's way.

## Notes

- If the entity can't find the position that **Position** names, it makes no sound for that trigger

## See also

- [`scripted_schedule`](scripted_schedule.md) - gives a monster a task such as moving to a spot
- [`monster_target`](monster_target.md) - a target that monsters attack
- [`info_node`](info_node.md) - the points monsters walk along

## Changes since 1.38

- `env_soundmark` is new in SBO 2.0.0
