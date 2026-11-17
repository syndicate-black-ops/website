---
description: "A func_conveyor carries the players and objects on it in one direction, while a scroll texture on it moves at the same speed."
---
A `func_conveyor` carries the players and objects on it in the direction of its **Pitch Yaw Roll**, while a texture
whose name starts with `scroll` scrolls along it at the same speed.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns its direction around, and a trigger with the
  [use type](../guide/trigger-modes.md) Set does what **Use Set Policy** says. See
  [Common keys](common-keys.md#targetname)
- **Conveyor Speed** (`speed`) - Sets how fast the conveyor carries players and objects, in units per second, and 0
  means 100. A negative speed goes the other way
- **Use Set Policy** (`useset_policy`) - Sets what a trigger with the use type Set does, with the number that the
  trigger brings
    - Reverse speed (0) - The conveyor turns its direction around, like any other trigger
    - Set speed to the value (1) - The number becomes the new speed
    - Add the value to the speed (2) - The number is added to the speed

## Flags

- **No Push** (1) - Only the texture scrolls, and the conveyor doesn't carry players and objects
- **Not Solid** (2) - Players and objects pass through the conveyor

## Notes

- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes **Conveyor
  Speed** while the map runs, the push and the texture scroll both change at once, and 0 is 100, as when the map
  loads. See [Changing keys](../guide/changing-keys.md)

## See also

- [3D sky](../features/sky.md) - moving clouds in a 3D sky, made of a `func_conveyor`
- [`func_train`](func_train.md) - a brush that moves along a path
- [func_conveyor on TWHL](https://twhl.info/wiki/page/func_conveyor) - the Half-Life entity

## Changes since 1.38

- You can use the new key **Use Set Policy**
