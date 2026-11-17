---
description: "An env_entity_glow draws an outline or a soft halo around models and brush entities, also through walls, so players can find an objective."
---
An `env_entity_glow` draws an outline or a soft halo around the entities named in its **Target Entity**, such as
monsters, items, props and brush entities like a `func_wall` or a door. Every player sees the glow, players who join
later too, and it can show through walls and floors to mark an objective on another floor.

![A scientist, a gun on the floor and a crate with an orange halo, seen through a low wall and a pillar](../../assets/img/screens/entity-glow-halo.webp)

*A halo around three targets, also where a wall hides them*

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the glow on or off, as the
  [use type](../guide/trigger-modes.md) says. See [Common keys](common-keys.md#targetname)
- **Target Entity** (`target`) - Names the entities that glow, and every entity with this name glows, up to 32 of
  them. A monster that dies and is removed stops glowing, and a new entity with the name, such as a monster from a
  `monstermaker`, starts glowing within half a second. Sprites don't glow
    - `!all` - Every alive monster and every other player in the game, up to the 64 nearest, looked up again every
      half second, so dead monsters and players drop out. Spectators never glow, and with **Only the activator sees
      it** the player who sees the glow doesn't glow
- **Glow Color (R G B A)** (`GlowColor`) - Sets the color of the glow as red, green and blue from 0 up to 255, and a
  fourth number from 0 up to 255 for its strength
    - If you leave out the fourth number, the glow has its full strength
- **Player Color (R G B A)** (`PlayerColor`) - With the **Target Entity** `!all`, sets the color of the players' glow,
  so players and monsters can have different colors
    - If you leave this key empty, players glow in the **Glow Color**
- **Glow Visibility Mode** (`Mode`) - Sets where the glow shows
    - Always (0) - Around the whole shape, through walls and floors too
    - Only when occluded (1) - Only around the parts a wall or another object hides, through walls and floors too
    - Only when visible (2) - Only around the parts the player can see
- **Glow Style** (`Style`) - Sets how the glow looks
    - Outline (0) - A sharp line along the edge of the shape
    - Halo (1) - A soft glow that fades out around the shape
- **Start Disabled** (`StartDisabled`) - Sets whether the glow is off until you trigger it
    - No (0) - The glow is on from the start of the map
    - Yes (1) - The glow is off until you trigger it
- **Duration (seconds)** (`duration`) - Sets how many seconds the glow stays on each time it turns on, and 0 keeps it
  on until you turn it off

## Flags

- **Only the activator sees it** (1) - Only the player who triggers the glow sees it, for example as a reward or a
  hint for one player. The glow is off until a player triggers it, and when another player triggers it while it is
  on, it moves to that player

## Notes

- A [`trigger_changevalue`](trigger_changevalue.md) can change **Glow Color**, **Glow Visibility Mode**, **Glow
  Style** and **Target Entity** while the map runs, and every player sees the change at once
- The glow never covers the target itself, only the space around it
- Players who use the software renderer don't see glows
- A target that the game draws invisible or nearly invisible, such as a cloaked Assassin, doesn't glow

## See also

- [Entity glow](../features/entity-glow.md) - how to mark an objective with a glow
- [`env_render`](env_render.md) - changes the render settings of other entities

## Changes since 1.38

- `env_entity_glow` draws an outline or a soft halo around models and brush entities, also through walls and floors, to mark an objective or anything else players should find
