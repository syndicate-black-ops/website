---
description: "A trigger_camera shows a player the view from the camera's position for a set time, looking at its target, and the camera can move along a path."
---
A `trigger_camera` shows a player the view from the camera's position for a set time, looking at its target, and the
camera can move along a path of [`path_corner`](path_corner.md) entities. It can also show the view to every player
and hide their HUD.

## Attributes

- **Look target** (`target`) - Names what the camera looks at, which is the first entity with this name. The camera
  also fires this target when it ends, unless you set **Don't fire look target**
    - If you leave this key empty and the camera has no player to follow, it does nothing
- **Hold time** (`wait`) - Sets how many seconds the camera keeps the player's view. With **Ignore Hold Time**, the
  camera ignores this key
    - If you leave this key empty or set 0, the camera ends at once
- **Path Corner** (`moveto`) - Names the first `path_corner` the camera moves along
    - If you leave this key empty, the camera doesn't move
- **Initial Speed** (`speed`) - Sets the camera's speed when it starts, in units per second. After that, the speeds
  of the path corners apply
- **Acceleration** (`acceleration`) - Sets how fast the camera speeds up to a corner's speed, in units per second per
  second
    - If you leave this key empty or set 0, it is 500
- **Stop Deceleration** (`deceleration`) - Sets how fast the camera slows down before a corner where it waits, in units
  per second per second
    - If you leave this key empty or set 0, it is 500
- **Camera Rotation Speed** (`turnspeed`) - Sets how fast the camera turns to its target. With **Instant Follow
  Turn**, the camera ignores this key
    - If you leave this key empty or set 0, it is 40
- **Stop by player input** (`stop_by_player_input`) - With "USE input", the player ends the camera with the use key
- **Target when turned off** (`m_iszTurnedOffTarget`) - Fires this target when the camera ends: its hold time is
  over, it is turned off or the player stops it. The activator is the player, or the camera itself if nobody had its
  view

## Flags

- **Start At Player** (1) - The camera starts at the eyes of the player who triggered it, facing where they look
- **Follow Player** (2) - The camera looks at the player who triggered it, instead of at its target
- **Freeze Player** (4) - The player can't move or use anything while the camera has their view
- **All Players** (8) - Every player who is alive when the camera starts gets its view, also if someone else turned
  it on. Each player gets their own view and controls back when it ends. **Freeze Player**, **Player Invulnerable**
  and **Stop by player input** apply to each player. The camera doesn't add players who join or respawn later
- **Instant Move** (64) - The camera moves from path corner to path corner in straight lines, at the path's speed from
  the start
- **Player Invulnerable** (256) - The player takes no damage while the camera has their view
- **Ignore Hold Time** (512) - The camera runs until you turn it off, so it ignores **Hold time**
- **Alive player only** (1024) - The camera only starts for an alive player, and it ends when that player dies or
  becomes a spectator. With **All Players**, it ends when none of its players is alive
- **Don't fire look target** (4096) - The camera doesn't fire its **Look target** when it ends
- **Don't slow down if not Freeze Player** (8192) - Without **Freeze Player**, the camera's speed isn't damped in every
  frame
- **Don't skip the first path corner** (16384) - The camera travels to the first path corner. Without this flag, it
  skips the first corner and moves to the second
- **Instant Initial Turn** (32768) - The camera faces its target at once when it starts
- **Instant Follow Turn** (65536) - The camera always looks straight at its target, without a turning speed
- **Hide HUD and crosshair** (131072) - While the camera has a player's view, the camera hides their HUD: health,
  armor, ammo, weapon selection, the crosshair, the kill feed, the objectives panel, the game timer and the status
  icons. The chat, text from a [`game_text`](game_text.md) or an [`env_message`](env_message.md), message boxes,
  tutor windows and [`env_overlay`](env_overlay.md) pictures stay. The HUD comes back with the view: when the camera
  ends, the player dies or starts to spectate, the round ends or the map changes

## Hiding the HUD for a scene

With **Hide HUD and crosshair** (131072), the camera shows the scene without the player's HUD, but a
[`game_text`](game_text.md) caption still shows:

![The same camera without the flag and with Hide HUD and crosshair: the caption stays, the HUD goes](../../assets/img/screens/camera-hide-hud.webp)

*A camera view with and without the HUD*

## Notes

- Without **All Players**, only the player who turns the camera on gets its view
- If a monster, a timer or another entity turns the camera on, or the player is dead or a spectator, nobody gets the
  view. The camera still moves, ends and fires its targets
- When nobody gets the view, **Start At Player** and **Follow Player** have no player to use. The camera starts where
  you placed it and looks at its **Look target**, and with **Alive player only**, it doesn't start
- The player gets the view back when the camera ends, or when it is removed while it has their view. They also get
  the controls back if **Freeze Player** took them
- At the end of a round, every camera gives its player the view and the controls back
- The turning speed doesn't depend on the server's frame rate
- With **Move with**, the camera moves with its parent and keeps its own aim and turning, so it still turns to look
  at its **Look target**. It ignores its own path while it has a parent. If you give it both, the console shows a
  message about it when `developer 1` is set in the console. See
  [Moving objects](../features/moving-objects.md#cameras-world-text-and-screens)

## See also

- [`path_corner`](path_corner.md) - the points the camera moves along
- [trigger_camera on TWHL](https://twhl.info/wiki/page/trigger_camera) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Camera Rotation Speed**, **Stop by player input** and **Target when turned off**
- You can use the new flags **Instant Move**, **Player Invulnerable**, **Ignore Hold Time**, **Alive player only**,
  **Don't fire look target**, **Don't slow down if not Freeze Player**, **Don't skip the first path corner**,
  **Instant Initial Turn** and **Instant Follow Turn**
- `trigger_camera` has new All Players and Hide HUD and crosshair flags
- Fixed a dead player or a spectator who turned a camera on keeping its view after the camera ended. Only living
  players get the camera's view now. This was a bug in SBO 1.38
- Fixed the camera turning faster or slower with the server's frame rate
- Fixed a `trigger_camera` started by a monster or a timer taking over the view of the player in the first server
  slot, even a spectator. When no player started the camera, the game gave the view to that slot
