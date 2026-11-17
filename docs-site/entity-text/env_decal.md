An `env_decal` sprays a decal on a wall each time you trigger it, such as a bullet hole, blood, a scorch mark or a
decal of your choice.

The decal goes where a line from the entity, in the spray direction, first hits a wall, up to 4000 units away.
Monsters and players don't stop the line, and if it hits nothing, nothing is sprayed.

## Attributes

- **Name** (`targetname`) - Triggering the entity sprays a decal. See [Common keys](common-keys.md#targetname)
- **Position** (`target`) - Sets where the line starts. It takes a [locus position](../guide/locus.md), so you can use
  a point such as `0 0 64`, the name of an entity, or `!activator` for the entity that started the chain of triggers
    - If you leave this key empty, the line starts at the `env_decal` itself
- **Spray direction** (`netname`) - Sets the direction of the line. It takes a [locus vector](../guide/locus.md), so
  you can use three numbers such as `0 0 -1` for down, or the name of an entity, which gives the direction that
  entity moves in
    - If you leave this key empty, the entity sprays in the direction of **Pitch Yaw Roll**
- **Pitch Yaw Roll** (`angles`) - Sets the spray direction when **Spray direction** is empty, as pitch, yaw and roll
  in degrees. `0 0 0` sprays east, and a pitch of 90 sprays straight down
- **Decal group** (`impulse`) - Picks the kind of decal, and each spray picks one decal of the group at random
    - Gunshot (1) - Bullet holes
    - Blood (2) - Red blood
    - Alien blood (3) - Yellow blood
    - Glass cracks (4) - Cracks in glass
    - Big gunshot (5) - Large bullet holes
    - Scorch marks (6) - Large scorch marks
    - Bullsquid splat (7) - Green spit
    - Small scorch marks (8) - Small scorch marks
    - Spore splat (9) - Yellow blood
    - Shock scorch (10) - Large scorch marks
    - Small shock scorch (11) - Small scorch marks
    - Custom (0) - The decal named in **Custom decal texture**
- **Custom decal texture** (`noise`) - With the group Custom, names the decal to spray, as a texture name in
  `decals.wad`

## Notes

- If the custom decal doesn't exist, the entity sprays nothing, and with `developer 1` set in the console, the console
  names it when the map starts
- If the entity can't find the position or the direction that these keys name, it sprays nothing for that trigger
- Players who join later don't see the decals sprayed before they joined
- You can only use decals that ship in SBO's `decals.wad`, and a map can't add its own: the game loads decals only
  from `decals.wad`, and a replaced `decals.wad` among a server's downloads would break the decals of every other map.
  For a picture of your own on one map, you can use a `{` texture on a [`func_illusionary`](func_illusionary.md) or an
  [`env_sprite`](env_sprite.md)

## See also

- [`infodecal`](infodecal.md) - a decal that the map places when it starts
- [`env_blood`](env_blood.md) - sprays blood that can leave a stain
- [Locus system](../guide/locus.md) - the positions and vectors these keys take

## Changes since 1.38

- `env_decal` is new in SBO 2.0.0
