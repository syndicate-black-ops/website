---
description: "A vgui_screen shows a menu panel on a rectangle in the world, called a world screen, which players aim at and click."
---
A `vgui_screen` shows a menu panel on a rectangle in the world, called a world screen, and players aim at it and click
its buttons with fire (the left click). The screen can also show a video. See [World
screens](../features/world-screens.md) for layouts, surfaces and animations.

## Attributes

- **Panel Name** (`panelname`) - Names the layout file `ui/scripts/screens/<name>.res`, from the game folder or the
  map's files. The file's `WorldScreen` section sets the panel's size in pixels, and without a size, the panel is
  512 x 256. The entity ignores this key if it has a **Movie File**
    - If you leave this key empty, the game removes the entity, unless it plays a **Movie File**
- **Movie File** (`moviefilename`) - Names an Ogg Theora video, a `.ogv` file in `video/`. The screen shows the video
  instead of a panel, with no cursor and no clicks
- **Movie Looping** (`looping`) - Sets whether the video starts over at its end or stops on its last frame
- **Movie Volume** (`health`) - Sets how loud the video's sound is, from 0 for silent up to 10 for full volume
    - If you leave this key empty or set 0, it is 10
- **Movie Sound Radius** (`radius`) - Sets the distance from the screen at which the video's sound fades out
  completely, in units
- **Surface** (`surface`) - Names a brush entity, such as a [`func_wall`](func_wall.md), a
  [`func_door`](func_door.md), a [`func_train`](func_train.md) or a [`func_rotating`](func_rotating.md). The screen is
  then drawn on the faces of that entity that have the `{screen` texture, and it moves with the entity. The
  `vgui_screen` then ignores **Angles**, **Width**, **Height** and its own origin
- **Width** (`width`) - Without a **Surface**, sets the width of the screen in units, to the viewer's right of the
  origin
- **Height** (`height`) - Without a **Surface**, sets the height of the screen in units, above the origin
- **Input Distance** (`inputdistance`) - Sets how far from the screen's surface a player can click it, in units, up to
  4096
- **Show Cursor** (`showcursor`) - Sets whether players see a mouse cursor on the screen while they aim at it

## Flags

- **Start Inactive** (1) - The screen is hidden and can't be used until you trigger the entity
- **Input Disabled** (2) - The screen only shows things, so it has no cursor and fire works as usual
- **Movie sound everywhere** (4) - Every player hears the video's sound at the same volume, from no direction
- **Movie without sound** (8) - The video plays without sound

## Notes

- Without a **Surface**, the origin is the screen's lower-left corner as seen from the front, and the screen faces
  along its angles
- With a **Surface**, one repeat of the `{screen` texture is the whole panel, and the texture's top-left corner is the
  panel's top-left corner. If you scale, rotate or shear the texture, the panel stretches the same way. The `{screen`
  faces are invisible in the game, and the other faces of the brush entity look as usual
- A click on a button fires **Target**, with the player who clicked as the activator. It also fires the target that
  the key `~<command>` names for the command of that button, for example the key `~hello` with the value `my_relay`
- Secondary fire is the right click, and buttons ignore it
- A click only counts from a living player who isn't spectating, who is in front of the screen and within **Input
  Distance**. Each player's clicks count up to 10 a second
- On makes the screen active, Off hides it so nobody can use it, and Toggle switches between the two
- A video plays from the start of the map, or from its beginning each time the screen turns on, and it stops when the
  screen turns off. Players who join later see it at the same point as the others
- With **Move with**, a screen without a **Surface** rides along and turns with its parent, and each player's game
  draws it there. A screen with a **Surface** moves with its brush, so to put it on a moving object, give the brush
  **Move with**.
  See [Moving objects](../features/moving-objects.md#cameras-world-text-and-screens)

## See also

- [`vgui_control_proxy`](vgui_control_proxy.md) - changes a control on the screen
- [`point_worldtext`](point_worldtext.md) - text in the world
- [World screens](../features/world-screens.md) - layouts, surfaces and animations
- [Video](../features/video.md) - video files

## Changes since 1.38

- `vgui_screen` is new
