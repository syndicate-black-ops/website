A `trigger_gravity` is a brush trigger that sets the gravity of a player who touches it, and it only affects players.

## Attributes

- **Gravity Multiplier** (`gravity`) - Sets the player's gravity as a multiple of the server setting `sv_gravity` (set in `server.cfg` or in the server console). 0.5 is half, 2 is double and 0.01 is almost no gravity.
  Without **Reset on leave**, a player keeps the gravity after they leave, until they touch another
  `trigger_gravity` or respawn
    - If you leave this key empty or set 0, the player gets normal gravity

## Flags

- **Start Off** (2) - With a name, it starts off
- **Reset on leave** (4) - The gravity goes back to 1 when the player leaves the brush, dies, becomes a spectator or
  the Game Master, or disconnects. It also goes back when the trigger is turned off or removed while they are inside.
  If something else changed their gravity in the meantime, such as another `trigger_gravity`, it stays as it is. With
  this flag, the trigger only changes alive players

## Notes

- Triggers turn a named `trigger_gravity` on and off: On turns it on, Off turns it off and Toggle switches it
- While its master is locked for the player, touching it does nothing

## See also

- [`trigger_push`](trigger_push.md) - pushes the entities that touch it
- [trigger_gravity on TWHL](https://twhl.info/wiki/page/trigger_gravity) - the Half-Life entity

## Changes since 1.38

- `trigger_gravity` can be switched on and off by name, has a Master, and has Start Off and Reset on leave options
