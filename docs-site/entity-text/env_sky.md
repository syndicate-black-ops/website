---
description: "An env_sky turns on a 3D sky: where the map's sky brushes use the env_sky texture, players see a small sky room of the map instead."
---
An `env_sky` turns on a 3D sky. Where the sky brushes of the map use the `env_sky` tool texture, every player sees a
small sky room of the map instead, drawn from the point where the `env_sky` stands and turned the way the player
looks.

## Attributes

- **Name** (`targetname`) - Triggering the entity makes it the 3D sky of the map, and a trigger with the
  [use type](../guide/trigger-modes.md) Off turns the 3D sky off. See [How it works](#how-it-works) and
  [Common keys](common-keys.md#targetname) for more details
- **Parallax scale** (`frags`) - Sets how the sky moves when the player moves. With a number N from 1 up to 255, the
  point the sky is seen from moves 1/N of the distance between the player and the point `0 0 0` of the map, so the
  sky room is a model of the map around that point at a scale of 1 to N. With 0, the sky stays in place, like a 2D
  skybox
- **Sky fog color** (`rendercolor`) - Sets the color of the sky fog, as red, green and blue from 0 up to 255. It is
  only used when **Sky fog density** is above 0
- **Sky fog density** (`density`) - Gives the sky room a fog of its own, which works like the density of
  [`env_fog`](env_fog.md) but over the distances of the sky room, so a sky room built at 1/16 scale needs about 16
  times the density of the map for the same look. You can type any value from 0 up to 0.01, and 0, a negative value
  or a value above 0.01 gives no sky fog, which is the default
- **Skybox fog** (`fogskybox`) - Sets how much the sky fog covers the 2D skybox behind the sky room. Partial, the
  default, tints the skybox so its picture still shows, Full fogs it as if it were 2048 units away, so far scenery
  fades into the fog color, and None leaves it clear
    - None (0)
    - Partial (1)
    - Full (2)

## Flags

- **Start off** (1) - The entity isn't the 3D sky of the map when the map starts

## How it works

You put the `env_sky` in a sky room that you close with `sky` brushes, and you give the sky faces of the playable
map the `env_sky` tool texture. Faces with the normal `sky` texture still show the 2D skybox. Rain and snow fall
under `env_sky` faces as they do under `sky`.

The entities in the sky room are part of the sky, so moving clouds made with a
[`func_conveyor`](func_conveyor.md), sprites, a [`func_rotating`](func_rotating.md), trains and models such as an
[`env_model`](env_model.md), a [`cycler`](cycler.md) or monsters are drawn in the 3D sky, at their scale and lit by
the sky room, and never where they really are. An entity that comes into the sky room after the start shows in the
sky within a second. An [`env_static`](env_static.md) with the **In the 3D sky** flag is drawn there too, with no
network traffic. Beams and lasers, [`point_worldtext`](point_worldtext.md), [`env_particle`](env_particle.md)
effects, weather and players in the sky room are not drawn.

Only one `env_sky` is on at a time, and when the map starts, it is the first one without **Start off**. Triggering
another `env_sky` makes it the 3D sky of the map and turns off the one that was on, while triggering the one that is
on with the use type Off, or removing it, turns the 3D sky off. Players who join later get the 3D sky that is on.

The fog of the map, from [`env_fog`](env_fog.md) or an [`env_fogzone`](env_fogzone.md), never reaches the sky room,
because its distances would wash out a sky room built at a small scale. Instead, each `env_sky` can have a sky fog of
its own, set with **Sky fog color** and **Sky fog density**, which fogs the brushes, entities and props of the sky
room by their distance from the `env_sky` point, and **Skybox fog** sets how much of it also covers the 2D skybox
behind them, so far scenery fades into the sky. Since every `env_sky`
has its own sky fog, switching to another `env_sky` also switches to its fog.

![Walking sideways in the showcase courtyard: the walls and the tower slide past, the 3D skyline barely moves](../../assets/img/clips/sky-parallax.webp)

*The walls slide past while the 3D skyline barely moves*

## Notes

- Every entity in the sky room is sent to every player in each update, as if it were in their view
- A map without an `env_sky`, or with none that is on, sends the same as a map without a 3D sky
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes the
  parallax scale, the sky fog or the position of the entity while it is the sky, every player sees the change at
  once. See [Changing keys](../guide/changing-keys.md)

## See also

- [3D sky](../features/sky.md) - how to build the sky room
- [`env_fog`](env_fog.md) - fog over the whole map

## Changes since 1.38

- `env_sky` is new in SBO 2.0.0
- New in SBO 2.1.0: the entities in the sky room are drawn in the 3D sky
- `env_static` has a new In the 3D sky flag, which shows the model in the sky room of an `env_sky` without any network
  cost
- `env_sky` has new Sky fog color, Sky fog density and Skybox fog keys, which give the sky room of a 3D sky its own fog, while the map's fog stays out of it
