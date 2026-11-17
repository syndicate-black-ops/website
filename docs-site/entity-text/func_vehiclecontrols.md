A `func_vehiclecontrols` marks where a player stands to drive a [`func_vehicle`](func_vehicle.md). The brush itself is
removed when the map starts, and the space it marked then moves with the vehicle.

## Attributes

- **Vehicle Name** (`target`) - Names the `func_vehicle` that a player drives from this space. Without a vehicle of
  that name, the controls do nothing
- **Invisible** (`zhlt_invisible`) - Makes the map compiler keep the brush in the map as the control space but draw
  none of its faces
    - yes (1)

## See also

- [`func_vehicle`](func_vehicle.md) - the vehicle it drives

## Changes since 1.38

- `func_vehiclecontrols` is new in SBO 2.0.0
