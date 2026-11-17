---
description: "An info_light_origin is a marker for placed models: a model that names it in its Light origin key is lit as if it stood at the marker."
---
An `info_light_origin` is a marker that sets where placed models take their lighting from. A model that names it in
its **Light origin** (`lightorigin`) key is lit as if it stood at the marker.

Without one, the engine lights a model from the floor right under its origin, so a model under a ledge, half inside a
wall or on a dark spot of a bright room is dark, and a large model, such as a vehicle or a piece of terrain, gets one
light for all of it.

![Two robots and two ammo boxes in a dark alcove: the left of each pair has Light origin set to a marker in the bright room and is lit; the right one is dark](../../assets/img/screens/light-origin.webp)

*Models lit from a light origin in another room, next to unlit copies*

The editor offers **Light origin** on [`env_model`](env_model.md), [`env_static`](env_static.md),
[`monster_furniture`](monster_furniture.md) and [`cycler`](cycler.md), and other entities with a model, such as items
and monsters, take the key too. Only the model with the key changes, so players and monsters that pass by are lit as
usual.

## Attributes

- **Name** (`targetname`) - Sets the name you put in the **Light origin** key of a model. See
  [Common keys](common-keys.md#targetname)

## Notes

- A name with no marker leaves the model lit as usual, and with `developer 1` set in the console, the console reports
  it
- The marker doesn't move, and dynamic lights and entity lights still light the model where it really is
- A model entity that later changes its model is lit as usual again
- Brush entities, such as a [`func_wall`](func_wall.md) or a door, are lit when the map is compiled, and for them the
  compiler key **Light Origin Target** (`light_origin`) does the same

## See also

- [Lights on models](../features/model-lights.md) - how models are lit
- [`env_elight`](env_elight.md) - a light that only lights models
- [`env_dlight`](env_dlight.md) - a light that lights the world and models

## Changes since 1.38

- `info_light_origin` is new in SBO 2.1.0
