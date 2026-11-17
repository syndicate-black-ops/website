A `player_capabilities` turns off or on what the player who triggered it can do: attack, jump, duck, use things, make
step sounds and move.

## Attributes

- **Attack capability** (`attack_capability`) - Sets whether the player can use the primary and the secondary attack
  of their weapons. A zoomed weapon stays zoomed while attacks are off
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it
- **Jump capability** (`jump_capability`) - Sets whether the player can jump
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it
- **Duck capability** (`duck_capability`) - Sets whether the player can duck
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it
- **Use capability** (`use_capability`) - Sets whether the player can use buttons, mounted guns and trains with the
  use key
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it
- **Step sounds** (`stepsound_capability`) - Sets whether the player makes footstep sounds
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it
- **Movement capability** (`movement_capability`) - Sets whether the player can walk, strafe and swim. Jumping and
  pushes still work
    - Copy use input (3) - On turns it on, Off turns it off and any other trigger switches it

## Notes

- It only changes the activator, and only if that is an alive player
- When a [`trigger_relay`](trigger_relay.md) fires it, the relay needs its flag **Forward activator** so the player
  stays the activator
- The change lasts until another `player_capabilities` changes it back or the player respawns
- The player's game gets the change at once, so their movement doesn't stutter

## See also

- [`player_speed`](player_speed.md) - changes a player's top speed
- [`trigger_playerfreeze`](trigger_playerfreeze.md) - freezes players in place

## Changes since 1.38

- `player_capabilities` is new
