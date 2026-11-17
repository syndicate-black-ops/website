A `player_speed` changes how fast the player who triggered it can move.

## Attributes

- **Maxspeed value** (`maxspeed`) - Sets the new speed, and 0 resets it. With "Fraction of the player's own speed",
  0.5 halves the player's speed. With "Set absolute", it is their speed in units per second while nothing slows them
  down
- **Value mode** (`value_notion`) - Sets how **Maxspeed value** is read
    - Fraction of the player's own speed (0) - A share of the speed that the player's class, level and legs give
      them, so it follows that speed when it changes
    - Set absolute (1) - A speed in units per second, which stays the same when the player's class, level or legs
      change. Slowdowns such as a zoom still lower it

## Notes

- It only changes the activator, and only if that is an alive player
- The change lasts until another `player_speed` changes it, a **Maxspeed value** of 0 resets it or the player
  respawns
- The server's top speed still limits it. That is the setting `sv_maxspeed` (set in `server.cfg` or in the server console)
- The player's game predicts with the new speed, so their movement doesn't stutter

## See also

- [`player_capabilities`](player_capabilities.md) - turns off what a player can do
- [`player_calc_ratio`](player_calc_ratio.md) - reads a player's speed as a number

## Changes since 1.38

- `player_speed` is new
