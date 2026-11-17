A `player_flicker` makes the flashlight of the player who triggered it flicker, so it goes off and on at random.

## Notes

- On starts the flicker, Off stops it and Toggle switches it
- It only changes the activator, and only if that is an alive player
- The flashlight only flickers while the player has it switched on, and it counts as on while it flickers
- The flicker lasts until a `player_flicker` stops it or the player respawns

## See also

- [`player_capabilities`](player_capabilities.md) - turns off what a player can do

## Changes since 1.38

- `player_flicker` is new
