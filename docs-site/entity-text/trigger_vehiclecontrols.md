A `trigger_vehiclecontrols` locks or unlocks the controls of a [`func_tracktrain`](func_tracktrain.md) or a
[`func_vehicle`](func_vehicle.md), so players can't drive a locked one.

## Attributes

- **Train or vehicle** (`target`) - Names the `func_tracktrain` or `func_vehicle`, as a name or `!activator`. It
  skips other entities with that name

## Notes

- On unlocks the controls, Off locks them and Toggle switches them. It does this with the vehicle's flag **No User
  Control**
- Without a target, it does nothing. With `developer 1` set in the console, the server console says so

## See also

- [`func_tracktrain`](func_tracktrain.md) and [`func_vehicle`](func_vehicle.md) - the vehicles it locks

## Changes since 1.38

- `trigger_vehiclecontrols` is new
