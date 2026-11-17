---
description: "The compile tools change some of your map's keys and lighting while they build it, and they don't all do it the same way."
---

# Compiler notes

The compile tools change some of your map's keys and lighting while they build it, and they don't all do it the same
way. This page covers the five sets of tools in use today, [ZHLT](https://web.archive.org/web/20250119214513/http://zhlt.info/)
3.4, [VHLT](https://github.com/twhl-community/VHLT-V34) v34, [SDHLT](https://github.com/seedee/SDHLT),
[ReSDHLT](https://github.com/metita/ReSDHLT) and [hltools](https://github.com/speedrun-16/hltools), and Valve's
original tools where they differ. See [Compiling](../getting-started/compiling.md) for how the tools differ and which
ones we recommend.

## The `style` key on named entities

The CSG step gives each named light its own switchable light style, numbered from 32 up with one number for each
name, and it replaces the **Appearance** you gave a named light. Every compiler does this, Valve's original tools
included. ZHLT, VHLT, SDHLT, ReSDHLT and hltools also rewrite the `style` key of entities that aren't lights:

| `style` you write in the editor | What the compiled map has |
|---|---|
| 0, or no `style` key | 0, unchanged |
| -1 or -2 | A new switchable style for a texture light, from 32 up, with or without a name (-2 stores it as a negative number) |
| -3 | The style of the light with the same name, so the entity switches with that light |
| Any other value, on an entity that has a name | The switchable style of that name, from 32 to 63, the same one a light with this name gets |
| Any other value, on an entity without a name | Unchanged |

If you give an entity the key `zhlt_usestyle` with the value `null`, VHLT, SDHLT, ReSDHLT and hltools leave its
`style` as you wrote it, and with another name as the value, the entity gets the style of that name. ZHLT 3.4 doesn't
know this key. Valve's original CSG tool only changes entities whose class name starts with `light`.

This doesn't break any SBO entity: [`trigger_lightstyle`](../entities/trigger_lightstyle.md) reads its look from
the key `appearance`, which the compile tools leave alone, and doesn't read a `style` key at all.
[`func_recharge`](../entities/func_recharge.md), [`multisource`](../entities/multisource.md),
[`env_spark`](../entities/env_spark.md), [`monster_turret`](../entities/monster_turret.md),
[`monster_miniturret`](../entities/monster_miniturret.md) and [`monster_sentry`](../entities/monster_sentry.md)
accept a `style` key but ignore it, as they do in Half-Life, so a rewritten value does them no harm.

## Four light styles on a face

Each face of a compiled map can hold the light of up to four light styles, which is a limit of the map format. When
more than four styles light the same face, the compiler keeps four of them and leaves the rest out, so a light whose
style was left out doesn't light that face at all, and switching it on or off changes nothing there:

| Compiler | Which styles a face keeps |
|---|---|
| ZHLT and Valve's original tools | The first four styles that reach the face, in the order of the lights, with the warning "Too many light styles on a face" |
| VHLT, SDHLT, ReSDHLT and hltools | The normal light (style 0) and the three brightest other styles on that face, without a warning (VHLT, SDHLT and ReSDHLT report it only with `-verbose`) |

Each name and each **Appearance** other than the normal one is one style, so lights with the same name, or with the
same Appearance, share one. In a test room lit by six lights with six styles, SDHLT, ReSDHLT, VHLT and hltools all kept the normal light and the three
brightest styles on every face, and the two dimmest switchable lights lit nothing. See
[Light styles](../features/light-styles.md) for more details.

## The `env_sky` texture

A [3D sky](../features/sky.md) shows through faces with the `env_sky` texture, so a map with a 3D sky needs a compile
tool that knows this texture. ZHLT 3.4, VHLT, SDHLT, ReSDHLT and hltools all turn brushes with the `env_sky` texture
into sky, which lets the sunlight through, and leave their faces out of the `.bsp`. Valve's original compile tools
don't know this texture name, so they build these brushes as ordinary solid walls with a visible texture.

## ReSDHLT and `env_sky` areas

ReSDHLT gives no sunlight and no light from the sky to an area that is only lit through the `env_sky` texture when the
map also has faces with the normal `sky` texture that this area can't see, such as the `sky` faces of a sky room.
Such an area comes out black in the compiled map. To save time, the lighting step of ReSDHLT skips the sky for every
spot that can see no face with the `sky` texture, and the `env_sky` texture has no faces. Every ReSDHLT release does
this, up to v0.22.2 (the newest at the time of writing). A map whose only sky is the `env_sky` texture lights
correctly, and SDHLT, VHLT and hltools light these areas in both cases.

[ReSDHLT v0.22.2-envsky.1](https://github.com/MisterCalvin/ReSDHLT/releases/tag/v0.22.2-envsky.1) is ReSDHLT
v0.22.2 with a fix for this, which lights these areas like SDHLT. The fix is waiting to be added to ReSDHLT
([pull request](https://github.com/metita/ReSDHLT/pull/8)), so use ReSDHLT v0.22.2-envsky.1 for maps with a 3D sky
and the normal ReSDHLT release for every other map.

## Keys that only some compilers read

| Key | Read by |
|---|---|
| `_falloff` on lights | Only ZHLT 3.4 |
| **ZHLT Lightflags** (`zhlt_lightflags`) 1, Embedded Fix, and the Concave Fix part of 6 | Only ZHLT 3.4. VHLT, SDHLT, ReSDHLT and hltools only read Opaque (2), so for them 3 and 6 work like 2, and 1 works like 0 |
| `zhlt_usestyle`, `zhlt_stylecoring`, `zhlt_usemodel`, `zhlt_copylight`, `zhlt_embedlightmap` and `zhlt_embedlightmapresolution` | VHLT, SDHLT, ReSDHLT and hltools, not ZHLT 3.4 |
| `_spread`, `_diffuse_light2` and `_fake` on `light_environment` | VHLT, SDHLT, ReSDHLT and hltools, not ZHLT 3.4 |

Every `zhlt_` key that VHLT reads is also read by SDHLT and ReSDHLT. See
[Common keys](../entities/common-keys.md#compiler) for what each key does.

## See also

- [Compiling](../getting-started/compiling.md) - the compile tools, our recommendation and their settings
- [Light styles](../features/light-styles.md) - switchable and animated lights
- [3D sky](../features/sky.md) - how to build a sky room
- [`trigger_lightstyle`](../entities/trigger_lightstyle.md) - changes how lights look while the map runs
