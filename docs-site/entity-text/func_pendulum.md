A `func_pendulum` swings back and forth around its origin like a pendulum. You set the origin with an origin brush.

## Attributes

- **Name** (`targetname`) - Triggering the entity starts or stops the swing. See
  [Common keys](common-keys.md#targetname)
- **Speed** (`speed`) - Sets the top speed of the swing, in degrees per second, and 0 means 100
- **Distance** (`distance`) - Sets how far the pendulum swings, in degrees
    - If you leave this key empty or set 0, it never swings
- **Damping** (`damp`) - Sets how quickly the swing dies down, from 0 for never up to 1000, and when the swing is slow
  enough, the pendulum stops
- **Damage inflicted when blocked** (`dmg`) - Sets the damage to anything the pendulum hits, and the faster it
  swings, the more damage it deals: this value at a speed of 100 degrees per second

## Flags

- **Start ON** (1) - The pendulum starts to swing when the map starts. Without this flag, it waits for a trigger
- **Passable** (8) - Players and objects pass through the pendulum
- **Auto-return** (16) - When you trigger the pendulum to stop, it swings back to its start and stops there, where
  normally it stops where it is
- **X Axis** (64) - The pendulum swings around the X axis, the east-west line of the map, instead of the vertical
  axis
- **Y Axis** (128) - The pendulum swings around the Y axis, the north-south line of the map, instead of the vertical
  axis
- **Swing both ways** (256) - The pendulum swings **Distance** to both sides of where you place it, where normally it
  swings from its placed angle to one side

## See also

- [`func_rotating`](func_rotating.md) - a brush that keeps turning
- [`func_door_rotating`](func_door_rotating.md) - a door that turns
- [func_pendulum on TWHL](https://twhl.info/wiki/page/func_pendulum) - the Half-Life entity
