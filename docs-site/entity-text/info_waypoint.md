---
description: "An info_waypoint puts a marker on the player's screen to lead them to a spot, with an icon, a label and the distance, also through walls."
---
An `info_waypoint` puts a marker on the screen of every player, or of one player, to show them where a spot is. The
marker is an icon with an optional label and an optional distance in meters, in a color you choose, and it shows
through walls and floors. When the spot is off the screen, the marker sits on the edge of the screen with an arrow
pointing toward it.

![A gold diamond with the label VAULT and 20 m, seen through a wall, and two more markers on the edges of the screen](../../assets/img/screens/waypoint-through-wall.webp)

*A marker seen through a wall, and two markers on the edges of the screen*

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the marker on or off, as the
  [use type](../guide/trigger-modes.md) says. See [Common keys](common-keys.md#targetname)
- **Icon Sprite** (`model`) - Sets the sprite the marker shows, which is always drawn at the same size on the screen,
  tinted with the **Color**. A white sprite takes the color best, and an additive sprite is added to the picture
  behind it
    - If you leave this key empty, the marker is a diamond
- **Label** (`message`) - Sets the text under the icon, up to 63 characters
    - If you leave this key empty, the marker has no text
- **Color (R G B)** (`rendercolor`) - Sets the color of the icon, the arrow and the text, as red, green and blue from 0
  up to 255
- **Follow Entity** (`target`) - Names an entity the marker moves with, such as a train, a monster or a crate. The
  marker keeps the distance from the middle of the entity that it has where you placed it, and if several entities
  have this name, it follows the first one. When the entity is removed, the marker stays where it was last, and when
  another entity takes the name or a `trigger_changevalue` names another entity, the marker moves onto that entity at
  the same distance
    - If you leave this key empty, the marker stays where you placed it
- **Reached Radius** (`radius`) - Sets how close, in units, a living player has to come for the marker to turn off.
  It turns off for everyone, or with **Only the activator sees it** only when that player comes this close. Players
  who are spectating never reach it. 0 means the marker never turns off this way
- **Target When Reached** (`netname`) - Names the entities to trigger when a player reaches the marker, with that
  player as the activator
- **Hide Closer Than** (`min_range`) - Hides the marker from a player who is closer than this many units. 0 means no
  limit
- **Hide Farther Than** (`max_range`) - Hides the marker and its edge arrow from a player who is farther than this
  many units. 0 means no limit
- **Duration (seconds)** (`duration`) - Sets how many seconds the marker stays on each time it turns on, and 0 keeps
  it on until you turn it off. With **Only the activator sees it**, the time starts again when another player takes
  the marker over
- **Reset at round start** (`round_reset`) - Sets whether the marker goes back to how it was when the map loaded at
  each new round
    - No (0) - The marker keeps its state from one round to the next
    - Yes (1) - The marker is on or off as at map load, with its original **Label**, **Color**, **Follow Entity** and
      place

## Flags

- **Only the activator sees it** (1) - Only the player who triggers the marker sees it, for example as a hint for one
  player. The marker is off until a player triggers it, and when another player triggers it while it is on, it moves
  to that player
- **Start on** (2) - The marker is on from the start of the map. Without this flag, it is off until you trigger it
- **Show distance** (4) - Shows the distance from the player to the marker in meters under the label
- **No edge arrow** (8) - The marker shows only while its spot is in view, and it doesn't move to the edge of the
  screen with an arrow when the spot is off the screen

## Notes

- A [`trigger_changevalue`](trigger_changevalue.md) can change **Label**, **Color**, **Follow Entity**, **Reached
  Radius**, **Hide Closer Than**, **Hide Farther Than** and **Duration** while the map runs, and every player who sees
  the marker sees the change at once. **Icon Sprite** can't change while the map
  runs
- The marker is part of the HUD, so it is hidden whenever the HUD is hidden, for example with `hud_draw 0` typed in
  the console or by a [`trigger_camera`](trigger_camera.md) with **Hide HUD and crosshair**
- The icon and the arrow grow with the HUD when a player turns on HUD scaling
- Markers in about the same direction move apart along the edge of the screen, so they don't cover each other
- Players who use the software renderer see the label and the distance, but not the icon or the arrow
- A Follow Entity that has no model, such as an `info_target`, moves the marker in steps, about every half second
- A marker on a monster stays on its body when it dies, until the body is removed, so turn the marker off from the
  monster's **TriggerTarget** with the **Trigger Condition** Death if it should go away then
- If the server doesn't have the **Icon Sprite** file, the marker is removed when the map starts, and a console line
  says why when `developer 1` is set in the console
- Without **Reset at round start**, a marker keeps its state when a Co-op round restarts
- A spectator who watches a player sees that player's **Only the activator sees it** markers while watching from
  the player's eyes, in the main view or the small first-person view in the corner. Other spectators and players
  don't see them
- **Hide Closer Than** and **Hide Farther Than** are measured from each player's own view, so one player can see a
  marker that another player doesn't

## See also

- [Waypoints](../features/waypoints.md) - how to lead players to an objective with a marker
- [`trigger_objective`](trigger_objective.md) - shows the mission objectives on the HUD
- [`env_entity_glow`](env_entity_glow.md) - draws an outline or a halo around entities, also through walls

## Changes since 1.38

- `info_waypoint` marks a spot with an icon, a label and its distance in meters. It shows through walls and moves to the edge of the screen with an arrow when the spot is off the screen
