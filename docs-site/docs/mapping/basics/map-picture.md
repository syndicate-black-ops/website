---
description: "A map picture shows players what your map looks like before they join it: the server browser shows it next to the server, the Create server window shows it on the map's tile, and the joining screen fills the whole screen with it while the map loads."
---

# Map picture

A map picture shows players what your map looks like before they join it: the server browser shows it next to the
server, the Create server window shows it on the map's tile, and the joining screen fills the whole screen with it
while the map loads. Every stock map has one, and you can ship one with your map or add it to the map pictures on
GitHub, which the game downloads for maps that come without one.

## Ship it with your map

| Map | Map picture |
|---|---|
| `maps/co_mymap.bsp` | `gfx/mapimages/co_mymap.jpg` |

The picture is a JPEG named after the map in lower case, and 512x288 is the size of every stock map picture and the
size the menus are made for. The game also reads other sizes, and it scales a larger picture down to fit in 512x384.

The picture doesn't download by itself, so list it in the map's `.res` file. The SBO version of resguy adds it to the
`.res` file for you when the picture is in the map's files. See [Custom content](custom-content.md) and
[Useful tools](../getting-started/useful-tools.md) for more details.

```text
// maps/co_mymap.res
gfx/mapimages/co_mymap.jpg
```

The game looks for the picture on the player's computer first, in their `syndicate`, `syndicate_addon` and
`syndicate_downloads` folders, so a picture you ship works without an internet connection and the game never asks
GitHub for a map that has one. A player who already has a picture with the same name, such as one the game downloaded
from GitHub before your map shipped its own, keeps it and doesn't download yours.

On a player's first join, the joining screen looks for the picture before the map's files download, so that first
time it shows the picture from GitHub if the map has one there, or the overview or the placeholder (see
[Without a picture](#without-a-picture)). Your picture shows in every window from the next time the player starts the
game.

## Taking a good picture

1. Start your map with `maxplayers 1` and `map co_mymap` typed in the console, and go to the spot you want to show.
2. Type these commands in the console to hide the HUD, the crosshair and your weapon, and `net_graph 0` as well if you
   have the net graph on:

   ```text
   hud_draw 0
   crosshair 0
   r_drawviewmodel 0
   ```

   Setting each of them back to 1 shows it again.
3. Close the console and press the screenshot key (Default: <kbd>F5</kbd>), which saves the screenshot as a `.bmp`
   file named after the map with a number, such as `co_aemos0000.bmp`, in your `syndicate` folder.
4. Crop the screenshot to a 16:9 shape, scale it to 512x288 and save it as a JPEG named after the map in lower case,
   such as `co_mymap.jpg`. A screenshot taken at a 16:9 resolution, such as 1920x1080, already has that shape and only
   needs scaling.

[GIMP](https://www.gimp.org/) is a free image editor that does all of step 4: select the area with the Rectangle
Select tool with **Fixed** set to **Aspect ratio** 16:9, then use **Image > Crop to Selection**,
**Image > Scale Image** to 512x288, and **File > Export As** with a `.jpg` name.

## Map pictures on GitHub

When a player has no picture for a map, the game downloads it once from
`https://syndicate-black-ops.github.io/map-images/<map>.jpg` and keeps it in
`syndicate_downloads/gfx/mapimages/`, where it finds it next time. This gives a picture to maps that players get
without one, such as maps released before SBO 2.0.0. The download goes through Steam, so it needs Steam running and
an internet connection, and the game asks for each map at most once each time it runs.

To add a picture there, open a pull request on
[syndicate-black-ops/map-images](https://github.com/syndicate-black-ops/map-images) with the picture at the root of
the repository. A check on the pull request fails unless the picture follows these rules:

- A JPEG file of exactly 512x288
- Named after the map in lower case with a `.jpg` extension, such as `co_mymap.jpg`
- At the root of the repository, with no folders and no other kinds of files

## Without a picture

Until a picture is found or downloaded, and for a map that has none, the menus show the map's overview image
`overviews/<map>.tga` instead, whole and centered, if the player has it. Only a 24-bit or 32-bit `.tga` overview is
used here, and a `.bmp` overview isn't. See [Overviews](overviews.md) for more details.

Without an overview, the menus show a **No map picture** placeholder with the map's name on it. The joining screen
only fills its background with a real map picture, never with the overview or the placeholder.

## See also

- [Custom content](custom-content.md) - the `.res` file and the files players download
- [Overviews](overviews.md) - the spectator map images, which the menus show when a map has no picture
- [Menus](../../playing/menus.md) - the server browser, Create server and the joining screen
