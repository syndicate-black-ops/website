An `env_smoker` makes puffs of smoke as soon as the map starts and then removes itself. Triggering it does nothing.

## Attributes

- **Puffs** (`health`) - Sets how many puffs of smoke it makes before it removes itself, and it makes one puff every
  0.1 to 0.2 seconds
- **Smoke sprite scale** (`scale`) - Sets the size of each puff, in tenths of the size of the smoke sprite, so 10 is
  its full size
- **Dispersion of smoke particles** (`dmg`) - Sets how far from the entity, in units across the floor, each puff can
  appear, and 0 puts every puff at the entity

## Notes

- Only players who can see the area of the entity see the smoke

## See also

- [`cycler_wreckage`](cycler_wreckage.md) - a sprite that gives off smoke for as long as the map runs
- [`env_explosion`](env_explosion.md) - an explosion with a fireball and smoke
