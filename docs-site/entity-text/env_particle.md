An `env_particle` shows a particle effect of the Aurora particle system, such as smoke, steam, sparks or fire. The
effect is a script file, `aurora/<name>.aur`, and each player's game draws it, but only with the OpenGL renderer.

Players who join later, spectators and demos see the effects as they are at that moment.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the effect on or off. Without a name, the effect is
  always on. See [Common keys](common-keys.md#targetname)
- **Particle script** (`message`) - Sets the script, as a path from the game folder, such as
  `aurora/steamvent.aur`, at most 63 characters long. Players download the script and the sprites it names with
  the map
- **Move with entity** (`target`) - Names an entity the effect moves and turns with, such as a
  [`func_train`](func_train.md), a [`func_door`](func_door.md) or a monster. The effect keeps the offset it has in
  the editor, and it turns with that entity. While that entity doesn't exist or can't be seen, the effect is hidden,
  and when the entity is removed, the effect follows the next entity that gets that name. If you leave this key
  empty and give the effect a `movewith` or `parent` key, as in maps made for Spirit of Half-Life or XashXT, that
  name is used instead
- **Attachment point** (`attachment`) - With **Move with entity** on a model, puts the effect on an attachment point
  of the model, a point the model maker placed. The points are numbered as in model viewers, and the point only
  moves while the model is drawn
    - None (-1) - At the entity's position, plus the offset
    - Attachment 0 (0) - The first attachment point
    - Attachment 1 (1) - The second attachment point
    - Attachment 2 (2) - The third attachment point
    - Attachment 3 (3) - The fourth attachment point

## Flags

- **Start On** (1) - An effect with a **Name** is on when the map starts. An effect without a name is always on
- **Spawn Use** (2) - Each trigger shows a one-time copy of the effect at the entity that started the chain of
  triggers, and doesn't switch the entity itself. Players who join later don't see the copies

## See also

- [Particles](../features/particles.md) - Aurora scripts and how to make them

## Changes since 1.38

- `env_particle` is new in SBO 2.0.0
