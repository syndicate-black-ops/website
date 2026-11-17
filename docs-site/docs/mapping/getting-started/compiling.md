---
description: "The compile tools turn your map's .map file into a .bsp file the game can load."
---

# Compiling

The compile tools turn your map's `.map` file into a `.bsp` file the game can load. Any compiler that works for
Half-Life maps also works for SBO maps. Compiling runs in four steps, called CSG, BSP, VIS and RAD.

## Choosing your compile tools

Several sets of compile tools exist for Half-Life, and I recommend them in this order:

1. **[ReSDHLT](https://github.com/metita/ReSDHLT)** ([downloads](https://github.com/metita/ReSDHLT/releases)) is a
   faster version of SDHLT, with the same tool names, every SDHLT option and more of its own. With its default
   settings, the lighting step (RAD) runs about 1.65 times faster than SDHLT's, and it uses all the cores of your
   processor on Windows and Linux. With `-gpu` or `-gpuauto`, it can also do part of the lighting on your graphics
   card, which saves the most time on maps with many lights. Its releases also come in an AVX2 build, whose lighting
   step is another 4 to 5% faster on processors from about 2013 and later. When your map leaks, ReSDHLT marks the hole
   itself in the pointfile, and it stops before the lighting step when the map has more lightmaps than the game can
   hold. The SBO example and test maps are compiled with ReSDHLT.
2. **[SDHLT](https://github.com/seedee/SDHLT)** ([downloads](https://github.com/seedee/SDHLT/releases)) is the set of
   tools ReSDHLT is based on. It adds ambient occlusion, shadows from models, new compiler entities in its own FGD,
   larger map size limits, and brighter lighting: light can reach full brightness, where older compilers stop at
   about three quarters of it.

If your map has a [3D sky](../features/sky.md), compile it with
[ReSDHLT v0.22.2-envsky.1](https://github.com/MisterCalvin/ReSDHLT/releases/tag/v0.22.2-envsky.1), which is
ReSDHLT v0.22.2 with a fix for black areas under the `env_sky` texture.
See [ReSDHLT and env_sky areas](../basics/compiler-notes.md#resdhlt-and-env_sky-areas) for more details.

[hltools](https://github.com/speedrun-16/hltools) is a newer rewrite of SDHLT as one program, `hltools`, which runs
the four steps with `hltools compile` or one at a time with `hltools csg`, `bsp`, `vis` and `rad`. The GPU lighting,
leak markers and lightmap check of ReSDHLT come from hltools. Its author lists it as still under development, so its
results may still differ from SDHLT's on some maps.

### Historical compile tools

[ZHLT](https://web.archive.org/web/20250119214513/http://zhlt.info/) (Zoner's Half-Life Tools, last version 3.4 from
2006) and [VHLT](https://github.com/twhl-community/VHLT-V34) (Vluzacn's version of ZHLT, last version v34 from 2015)
are historical tools: neither has had a new version since, and SDHLT continues from VHLT's code. Many mappers still
compile with VHLT. When you move to SDHLT or ReSDHLT, your `zhlt_` keys keep
working, light can reach full brightness instead of stopping at about three quarters of it, and you get everything
SDHLT and ReSDHLT add above. Their tools are named `sdHLCSG`, `sdHLBSP`,
`sdHLVIS` and `sdHLRAD` instead of `hlcsg`, `hlbsp`, `hlvis` and `hlrad`, so you set the new paths in your editor's
compile settings.

See [Compiler notes](../basics/compiler-notes.md) for how each compiler treats light styles, the `env_sky` texture and
some `zhlt_` keys.

## The four steps

Each step is a separate program that works on the output of the step before it:

| Step | SDHLT and ReSDHLT tool | What it does |
|---|---|---|
| CSG | `sdHLCSG` | Builds the world's faces from your brushes and writes the list of entities |
| BSP | `sdHLBSP` | Builds the BSP tree, which is how the engine stores the map, and finds leaks |
| VIS | `sdHLVIS` | Works out which parts of the map can see which other parts |
| RAD | `sdHLRAD` | Works out the lighting |

To compile a map named `co_mymap` from the command line, type these commands:

```
sdHLCSG -chart co_mymap
sdHLBSP -chart co_mymap
sdHLVIS -chart co_mymap
sdHLRAD -bounce 2 -chart co_mymap
```

These are the options you are most likely to need:

| Option | Tool | What it does |
|---|---|---|
| `-chart` | All | Prints how much of each part of the BSP the map uses, next to its limit |
| `-fast` | VIS, RAD | Compiles faster, with less exact visibility or lighting |
| `-bounce N` | RAD | Sets how many times light bounces off surfaces |
| `-wadinclude name` | CSG | Copies the textures of the WAD `name` into the `.bsp` |

## Textures and WADs

A `.bsp` lists the WADs its textures come from, and the game loads each texture that isn't copied into the `.bsp`
from its WAD on the player's computer. Every SBO player has the SBO WADs in `syndicate/` (`anzymut.wad`, `roux.wad`,
`co_escape.wad` and `sbo_tools.wad`) and Half-Life's own WADs, such as `halflife.wad` and `liquids.wad`, so their
textures need nothing more. A WAD of
your own only reaches players if you copy it into the `.bsp` with `-wadinclude` or list it in the map's `.res` file.
See [Custom content](../basics/custom-content.md) for more details.

## The compiled map

The compiled map is `syndicate/maps/<map>.bsp`, and the files that belong to it, such as the
[briefing](../basics/briefing.md) `maps/<map>.txt`, use the same name. The start of the map name sets the game mode.
See [Map names and spawns](../basics/map-names-and-spawns.md) for more details.

## See also

- [Editor setup](editor-setup.md) - the J.A.C.K. game profile and the WADs
- [Testing a map](testing.md) - how to start and test your map
- [Compiler notes](../basics/compiler-notes.md) - what each compiler does to light styles, the `env_sky` texture and
  `zhlt_` keys
- [Custom content](../basics/custom-content.md) - how players get your map's own files
