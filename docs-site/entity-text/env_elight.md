---
description: "An env_elight makes a light that only lights models, such as monsters, players, weapons and props, and never the walls or the floor."
---
An `env_elight` makes a light that only lights models, such as monsters, players, weapons and props, and never the
walls or the floor.

This is how it compares with an [`env_dlight`](env_dlight.md):

| | [`env_dlight`](env_dlight.md) | `env_elight` |
|---|---|---|
| Lights | Walls, floor and models, so you see a glow around it | Only models, so walls and floor stay as they are |
| Cost | More, because the engine works out the light on the walls and the floor it reaches again every frame | Less, because it only lights the models near it, at each corner of their shape |
| Reach | Its radius | Full brightness up to its radius, and in the dark you still see it at 6 to 7 times the radius. Walls don't block it |

![A dark room: on the left an env_dlight lights the floor and the models, on the right an env_elight lights only the models](../../assets/img/screens/elight-vs-dlight.webp)

*An env_dlight on the left and an env_elight on the right*

The engine lights each model from the light baked into the map under it, plus up to four entity lights near it,
each from its own direction, so a model next to an `env_elight` gets a bright, colored side toward the light. The
light reaches every model in its range, players and monsters passing by too, and it shines through walls.

![Scientists lit red, green and blue by three env_elight; the floor and the walls stay dark](../../assets/img/screens/elight-colors.webp)

*Scientists lit red, green and blue by three env_elight*

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the light on or off, as the
  [use type](../guide/trigger-modes.md) says. Without a name, the light is on from the start of the map. See
  [Common keys](common-keys.md#targetname)
- **Entity to follow** (`target`) - Names the entity the light sits on, and the light moves with it smoothly on every
  player's screen. When the entity is removed, the light goes out
    - If you leave this key empty, the light stays at **Position**
- **Attachment on that entity** (`impulse`) - Picks where on the followed model the light sits
    - None (0) - At the entity's own position, which for a monster is at its feet
    - 1 (1) - At the first attachment point of the model, a point the model maker placed, such as a monster's hand
      or gun
    - 2 (2) - At the second attachment point
    - 3 (3) - At the third attachment point
    - 4 (4) - At the fourth attachment point
- **Position** (`message`) - Sets where the light is when it follows no entity, in the same way as the **Position**
  of [`env_dlight`](env_dlight.md)
    - If you leave this key empty, the light is at the `env_elight` itself
- **Light color** (`rendercolor`) - Sets the color of the light, as red, green and blue from 0 up to 255
- **Radius** (`renderamt`) - Sets how far, in units from 0 up to 1023, the light has its full brightness. Past it,
  the light fades with the square of the distance, so in the dark a light with a radius of 48 still tints a model
  270 units away
- **Duration** (`health`) - Sets how many seconds the light stays on after it turns on, and 0 keeps it on until you
  switch it off

## Flags

- **Only once** (1) - The entity is removed when its **Duration** ends
- **Start on** (2) - The light is on from the start of the map
- **Track position updates** (4) - While the light is on, the entity finds its **Position** again every 0.1
  seconds, so the light follows a moving position
- **Position is Locus Entity** (8) - The light sits on the entity named in **Position** and moves with it when that
  entity has a model you can see. On an entity without a model, such as an [`info_target`](info_target.md), it stays
  where the entity was when the light turned on, unless you also set **Track position updates**

## Lights that follow an entity

![A yellow env_elight follows a moving func_train and lights the scientists it passes](../../assets/img/clips/elight-follow-train.webp)

*A yellow `env_elight` follows a moving [`func_train`](func_train.md) and lights the scientists that it passes*

## Notes

- A light inside a model only lights the inner faces of the model, so the model looks dark
- Each player's game has 64 entity lights, and muzzle flashes and other effects use them too. At most 32 of them can
  be `env_elight` lights at the same time, and a light whose place an effect took comes back within half a second
- If **Entity to follow** names an entity that doesn't exist, the light stays off, and with `developer 1` set in the
  console, the console reports it
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes
  **Radius**, **Light color** or the attachment while the light is on, every player sees the change at once. See
  [Changing keys](../guide/changing-keys.md)

## See also

- [`env_dlight`](env_dlight.md) - lights the world and the models
- [`info_light_origin`](info_light_origin.md) - where a placed model takes its light from
- [Lights on models](../features/model-lights.md) - how models are lit

## Changes since 1.38

- `env_elight` is new in SBO 2.1.0
