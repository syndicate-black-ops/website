A `trigger_safe_fall` is a brush trigger that cancels fall damage, so a player who falls through it takes no fall
damage when they land.

## Notes

- It only affects an alive player who is in the air when they touch it
- A hard landing after it also plays no fall sound and doesn't break the player's legs
- While its master is locked, it does nothing. It has no on and off state, so a trigger by name does nothing

## See also

- [`trigger_jump`](trigger_jump.md) - a jump pad
- [Teleports and jump pads](../features/teleports-and-jump-pads.md) - jump pads and safe falls

## Changes since 1.38

- `trigger_safe_fall` is new
