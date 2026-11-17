A `trigger_playerfreeze` freezes players in place, so a frozen player can look around but can't move, shoot or use
anything.

## Attributes

- **Use type** (`use_type`) - Sets what a trigger does
    - Unfreeze (-1) - It frees the players
    - Toggle freeze (0, default) - Each player who is free gets frozen, and each frozen player gets free
    - Freeze (1) - It freezes the players
    - Copy input (2) - On freezes, Off frees and Toggle switches

## Flags

- **All players** (1) - It changes every alive player. Without this flag, it changes only the activator, and only
  if the activator is an alive player

## Notes

- A frozen player stays frozen until a `trigger_playerfreeze` frees them or until they respawn
- When a [`trigger_relay`](trigger_relay.md) fires it, the relay needs its flag **Forward activator** so the player
  stays the activator
- A [`trigger_camera`](trigger_camera.md) with **Freeze Player** also freezes the player who looks through it. If a
  `trigger_playerfreeze` frees that player, they stay frozen until the camera releases them

## See also

- [`player_capabilities`](player_capabilities.md) - turns off single things a player can do
- [`trigger_camera`](trigger_camera.md) - shows a player another view

## Changes since 1.38

- `trigger_playerfreeze` is new
