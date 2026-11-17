---
description: "These are the tools for making SBO maps, models, textures and sprites, including newbspguy, resguy and studiomdlPlusPlus, which MrCalvin updated with bug fixes and new features."
---

# Useful tools

These are the tools for making SBO maps, models, textures and sprites, including newbspguy, resguy and
studiomdlPlusPlus, which MrCalvin updated with bug fixes and new features. You can download MrCalvin's versions of these
three tools as zip files from the SBO website's GitHub page. Use these versions rather than the original tools for
SBO maps. See [Editor setup](editor-setup.md) and [Compiling](compiling.md) for the setup steps.

## Maps

- [J.A.C.K.](https://jack.hlfx.ru/en/) - The map editor the SBO docs use for every editor step
- [ReSDHLT](https://github.com/metita/ReSDHLT) ([downloads](https://github.com/metita/ReSDHLT/releases)) - The map
  compilers the SBO maps are compiled with, a faster version of SDHLT with the same tool names, every SDHLT option
  and more of its own. For maps with a [3D sky](../features/sky.md), use
  [ReSDHLT v0.22.2-envsky.1](https://github.com/MisterCalvin/ReSDHLT/releases/tag/v0.22.2-envsky.1), which fixes
  black areas under the `env_sky` texture
- [SDHLT](https://github.com/seedee/SDHLT) - The map compilers ReSDHLT is based on, which you can use instead of
  ReSDHLT

### newbspguy

[Download](https://github.com/syndicate-black-ops/website/releases/download/tools/newbspguy-sbo.zip)

newbspguy opens a compiled map (`.bsp`) so you can look at it and change it. It is based on
[newbspguy](https://github.com/UnrealKaraulov/newbspguy) by UnrealKaraulov, and MrCalvin's updates are mostly for
making [spectator overview](../basics/overviews.md) pictures:

- Added the `overview` command, which makes an overview picture and its `.txt` file from the command line
- Added the `-zmax` and `-zmin` options, which leave out everything above or below a height, so a roof doesn't hide
  the floor under it and each floor can have its own picture
- Added the `-models` option and the "Render Studio Models" setting in the editor's Overview widget, which draw the
  map's studio models in the picture
- Added the `-fullbright` option, which draws the textures' plain colors without the map's lighting, and the
  `-mipmaps` option, which removes the grain of textures drawn much smaller than their size. Both are also settings in
  the Overview widget
- Fixed the picture's framing, which is now a true top-down view of exactly the area the `.txt` file gives the game,
  so the picture lines up in the game on maps that aren't square
- Fixed a crash when you save a `.tga` overview from the editor, and green wireframe lines that stayed in the picture
  and the 3D view after making an overview
- Studio models in the editor are drawn faster, because their animation frames are cached instead of rebuilt each
  time

### resguy

[Download](https://github.com/syndicate-black-ops/website/releases/download/tools/resguy-sbo.zip)

resguy writes a map's `.res` file, the list of files a player downloads with the map. It is based on
[resguy](https://github.com/wootguy/resguy) by wootguy, and MrCalvin updated it to fix bugs and to write the files
SBO maps need. Most of this is its SBO mode, which turns on by itself when resguy runs in a `syndicate` or
`syndicate_addon` folder, or with the `-sbo` option:

- Lists the map's sequence file and the sounds it plays, and every layer picture the map's overview file names
- Lists the map's material files and the sounds and sprites they name
- Lists the videos of `game_playvideo` and `vgui_screen` entities, and the layouts and pictures of world screens
- Lists color correction tables, particle scripts and their sprites, `env_overlay` and `env_tutor` pictures, and the
  briefing with its web page
- Lists the map picture (`gfx/mapimages/<map>.jpg`) when the map has one
- Lists only files the engine sends to players, which are files with one dot in their path and a three-letter
  extension
- Fixed text such as a `point_worldtext` label ending in `.wav` being listed as a sound: in SBO mode, only the keys
  that take sounds are read as sounds, including SBO's sound keys
- Fixed every `.res` file being left out of the list, including world screen layouts. Only the map's own
  `maps/<map>.res` is left out now

The download's `resguy_default_content.txt` is the list of files that ship with SBO, so resguy never lists them in a
map's `.res` file.

## Models

- [Half-Life Asset Manager](https://github.com/SamVanheer/HalfLifeAssetManager)
  ([downloads](https://github.com/SamVanheer/HalfLifeAssetManager/releases)) - Opens a model (`.mdl`) and shows its
  animations, attachment points, hitboxes and textures, some of which you can change
- [The303's QC guide](https://the303.org/tutorials/gold_qc.htm) - Explains every command of a QC file

### studiomdlPlusPlus

[Download](https://github.com/syndicate-black-ops/website/releases/download/tools/studiomdlplusplus-sbo.zip)

studiomdlPlusPlus compiles a model from its QC file and SMD files. It is based on
[studiomdlPlusPlus](https://github.com/G2Pavon/studiomdlPlusPlus) by G2Pavon, and MrCalvin made a large number of
improvements over the original. The main ones are:

- Fixed crashes while reading QC files, wrong model file sizes, bones that were lost or rejected at the 128-bone
  limit, and 1024x1024 textures
- Models keep the precision of their vertices, normals and bone rotations
- Works like Valve's compiler: it stores the AX, AY, AZ, AXR, AYR and AZR motion options, reads LY linear motion
  correctly, and doesn't make a texture fullbright because its name contains "bright"
- Reads nested `$include` files, several `$cdtexture` folders, the `nomips` and `alpha` texture render modes, sequence
  groups and indexed PNG textures
- Compiles a single SMD file as a static model without a QC file, splits body meshes that are too large
  (`--split`), and makes a missing `$bbox` and `$cbox` (`--auto-boxes`)
- Gives an error above 128 hitboxes, and a warning for `$flags 512` (hitbox collision) without `$hbox` lines
- Has new options to replace textures (`-t`), print the hitboxes as QC lines (`-h`), and check the normals and face
  winding of the source files (`--check-normals`, `--check-winding`)

If you would rather not use studiomdlPlusPlus, MrCalvin recommends the studiomdl in the Sven Co-op team's SDK. See
[StudioMDL (GoldSrc)](https://developer.valvesoftware.com/wiki/StudioMDL_(GoldSrc)) on the Valve Developer Wiki for
studiomdl's history and download links.

## Textures and sprites

- [WadMaker](https://github.com/pwitvoet/wadmaker) ([downloads](https://github.com/pwitvoet/wadmaker/releases)) -
  Makes a texture file (`.wad`) from a folder of pictures, and gets the pictures out of a `.wad`. The same download
  includes SpriteMaker, which does the same for sprites (`.spr`)
- [Half-Life Texture Tools](https://github.com/yuraj11/HL-Texture-Tools)
  ([downloads](https://github.com/yuraj11/HL-Texture-Tools/releases)) - Opens texture files (`.wad`) and sprites
  (`.spr`) so you can look at them and save their pictures, and makes new ones from pictures

## SBO editors

- [Aurora particle editor](https://github.com/syndicate-black-ops/aurora-editor) - Makes and changes the particle
  scripts (`.aur`) of an [`env_particle`](../entities/env_particle.md) in your browser
- In-game editors, which you open by typing their command in the console while your map runs:
  - `particleeditorui` - the particle editor, see [Particles](../features/particles.md)
  - `colorcorrectionui` - the color correction editor, see [Color correction](../features/color-correction.md)
  - `worldscreeneditorui` - the world screen editor, see [World screens](../features/world-screens.md)
