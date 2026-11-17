---
description: "A train_setspeed changes the speed of a moving func_tracktrain, at once or step by step, so the train can speed up, slow down or stop by itself."
---
A `train_setspeed` changes the speed of a moving [`func_tracktrain`](func_tracktrain.md), at once or step by step over
a time you set, so the train can speed up, slow down or stop without a player at its controls.

## Attributes

- **Name** (`targetname`) - Triggering the entity by this name changes the train's speed. See
  [Common keys](common-keys.md#targetname)
- **Track train** (`train`) - Names the `func_tracktrain`. If several entities have that name, the entity uses the
  first `func_tracktrain` among them
- **New speed** (`speed`) - Sets the speed in units per second, from -2000 to 2000. A value below 0 makes the train
  run backward, and 0 stops it, which also stops its sound
- **How** (`mode`) - Picks how the speed changes
    - At once (0) - The train runs at the new speed from its next move on
    - Step by step over the time (1) - The speed changes a little every 0.1 seconds, so it reaches the new speed when
      **Time** is over
- **Time** (`time`) - Sets how many seconds a step-by-step change takes, and 0 or less means 10 seconds
- **Fire when the speed is reached** (`target`) - The entity fires this target with the
  [use type](../guide/trigger-modes.md) Toggle when the train runs at the new speed. With "At once", that is at once

## Notes

- A train that is standing still stays where it is, and the entity fires nothing
- If the train is stopped or removed while its speed changes step by step, the change ends and nothing fires
- Triggering the entity again during a step-by-step change starts the change again from the train's speed at that
  moment
- The train's sound follows its speed
- The targets get the [activator](../guide/entity-triggering.md#target-selectors) of the trigger
- If no `func_tracktrain` has the name, nothing happens. With `developer 1` set in the console, the console shows a
  message about it

## See also

- [`func_tracktrain`](func_tracktrain.md) - the train it changes
- [`trigger_vehiclecontrols`](trigger_vehiclecontrols.md) - locks or unlocks a train's controls

## Changes since 1.38

- `train_setspeed` is new in SBO 2.1.0
