---
description: "Players download your map's models, sounds, sprites, textures and scripts when they join, and SBO puts the files of its own features on the download list for you."
---

# Custom content

Players download your map's models, sounds, sprites, textures and scripts when they join, and SBO puts the files of
its map features on the download list for you. The server sends every file on that list: the files the map
precaches (loads when it starts), the files SBO features add, and the files in the map's `.res` file. A file on none
of these lists stays on the server, so players who don't have it see or hear nothing.

## Files that download by themselves

The server sends every model, sprite and sound the map's entities precache, and SBO also puts the files of these
features on the download list:

| File | Which feature adds it |
|---|---|
| `sequences/<map>.seq` | The map's [sequence file](../features/sequences.md) |
| `materials/maps/<map>.txt` or the file the [`worldspawn`](../entities/worldspawn.md) key **Materials file** names, with the files it includes and the sprites and sounds it names | [Materials](../features/materials.md) |
| The worldspawn's grass sprite | [Materials](../features/materials.md) |
| An `.mp3` file of an [`ambient_music`](../entities/ambient_music.md) or [`ambient_generic`](../entities/ambient_generic.md) | [Music and sound](../features/music.md) |
| The `aurora/*.aur` scripts and their sprites | [Particles](../features/particles.md), with [`env_particle`](../entities/env_particle.md) |
| The `.mdl` of an [`env_static`](../entities/env_static.md), with its texture file and sequence group files | [Props and fades](../features/props-and-fades.md) |
| The custom icon `.tga` and the custom sound of an [`env_tutor`](../entities/env_tutor.md) | [Tutor messages](../features/tutor.md) |
| The `ui/scripts/screens/<name>.res` and `<name>_anims.txt` of a [`vgui_screen`](../entities/vgui_screen.md), if the server has them | [World screens](../features/world-screens.md) |
| The video file of a [`game_playvideo`](../entities/game_playvideo.md), its sound file, and the video file of a video `vgui_screen` | [Video](../features/video.md) |
| The color correction file of a [`color_correction`](../entities/color_correction.md) or a [`color_correction_volume`](../entities/color_correction_volume.md) | [Color correction](../features/color-correction.md) |
| The picture of an [`env_overlay`](../entities/env_overlay.md) | [`env_overlay`](../entities/env_overlay.md) |

## The `.res` file

If a file isn't on the download list, players only get it if you list it in `maps/<map>.res`. These are the files
you will most often need to list:

- The [briefing](briefing.md) `maps/<map>.txt`, and a web page briefing with its pictures
- Your map's WAD, if you didn't copy its textures into the `.bsp` (see [Compiling](../getting-started/compiling.md))
- The sky images, `gfx/env/<sky>*.tga`
- The images of a world screen layout
- The [overview](overviews.md) files
- The [map picture](map-picture.md), `gfx/mapimages/<map>.jpg`
- Detail textures

The file has one path per line, starting from the game folder, and lines that start with `//` are comments. Listing a
file that already downloads by itself does no harm. See [Useful tools](../getting-started/useful-tools.md) for tools
that write the `.res` file for you.

```text
// maps/co_mymap.res
maps/co_mymap.txt
gfx/env/mysky_up.tga
gfx/env/mysky_dn.tga
mymap.wad
ui/gfx/vgui/mymap_logo.tga
gfx/mapimages/co_mymap.jpg
```

## File names

Write every folder and file name in lower case, and write the paths in your map the same way:
`sound/mymap/door1.wav`, not `Sound/MyMap/Door1.WAV`. On a Linux server, `Door1.wav` and `door1.wav` are two
different files, so if a sound or model name's case differs from the path in the map, the server can't find the file
and players don't download it. Resguy, a tool that writes `.res` files, also reads names with their case and reports
such a file as missing. The game mode also comes from the start of the map name in lower case, so `CO_mymap.bsp`
isn't a Co-op map. See [Map names and spawns](map-names-and-spawns.md) for more details.

Players only download a file if it follows three rules:

| Rule | Why |
|---|---|
| A path has at most 63 characters | The engine can't handle a longer name |
| A path has only one dot, the one before the extension | The engine doesn't let players download a file with more than one dot in its path |
| The extension has three letters | The engine doesn't let players download a file with a longer or shorter extension, such as `.html` |

## Precache limits

The engine has fixed limits for each map, and a map that goes over a limit doesn't load:

| Resource | Limit |
|---|---|
| Models (studio models, sprites and the brush models of the map) | 511 |
| Sounds | 511 |
| Generic files (the other files the game precaches, such as an `env_static` model) | 511 |
| All resources together (models, sounds, generic files, decals and events) | 1280 |

Each kind of monster precaches its own models and sounds, so each new kind you add uses more slots. An `env_static`
model is a generic file, so it counts toward the 1280 but not toward the models. A map's
[materials](../features/materials.md) only precache the step and hit sounds of the materials its textures use, plus
the concrete, flesh and slosh materials, which every map loads.

## Folders of a map package

A map's files keep the layout of the game folder, starting from `Half-Life/syndicate/`. Put your map's files in
folders named after the map, so they never share a name with another map's files:

```text
maps/co_mymap.bsp
maps/co_mymap.txt               the briefing
maps/co_mymap.res               the download list
overviews/co_mymap.txt          the spectator overview, with its image
gfx/mapimages/co_mymap.jpg      the map picture
sequences/co_mymap.seq
materials/maps/co_mymap.txt
sound/mymap/...
models/mymap/...
sprites/mymap/...
gfx/env/mysky_up.tga            sky images, one per side
mymap.wad                       only when the textures are not in the .bsp
```

A server copies the package into its `syndicate/` folder. A player who installs a map by hand copies it into
`Half-Life/syndicate_addon/`, which the game reads when **Allow custom addon content** in **Options > Content** is
on. Files players download from a server go into `Half-Life/syndicate_downloads/` automatically.

To make your own models, you write a QC file for the model compiler, see
[the QC guide on the303.org](https://the303.org/tutorials/gold_qc.htm) for more details. See
[Useful tools](../getting-started/useful-tools.md) for the tools that make models, sprites and WADs.

## Changes since 1.38

- Sequence files, materials files, `ambient_music`, `env_particle`, `env_static`, `env_tutor`, `vgui_screen`,
  `game_playvideo`, color correction and `env_overlay` are new, and the game puts their files on the download list

## See also

- [Briefing](briefing.md) - the map's description file
- [Overviews](overviews.md) - the spectator map images
- [Map picture](map-picture.md) - the picture the menus show of the map
- [Compiling](../getting-started/compiling.md) - the compile tools and copying textures into the `.bsp`
- [Materials](../features/materials.md) - the materials file and its sounds
- [Sequence files](../features/sequences.md) - the map's sequence file
