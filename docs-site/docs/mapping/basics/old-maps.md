---
description: "Maps made for SBO 1.38 load and play in SBO 2.0.0 and later without a new compile, and a compatibility file that comes with the game keeps custom maps playing as they did in SBO 1.38."
---

# Old maps

Maps made for SBO 1.38 load and play in SBO 2.0.0 and later without a new compile, and a compatibility file that
comes with the game keeps custom maps playing as they did in SBO 1.38. SBO 2.0.0 reads some keys SBO 1.38 ignored,
and some custom maps have such a key by accident.

## The compatibility file

Some custom maps have a key SBO 1.38 ignored and SBO 2.0.0 reads, for example a key the editor showed and the mapper
filled in, but which did nothing at that time. On those maps, the key would change how the map plays, so the game
comes with the file `maps/map_compat.txt`, which removes or changes such keys while the map loads.

Each line of the file is one entry, like this:

```text
// <map> <crc32> drop <classname> <selector> <key>
// <map> <crc32> set  <classname> <selector> <key> <value>
co_aneki 31a9fe30 drop env_shooter fleshshot scale
```

| Part | Value |
|---|---|
| map | The map name, without `maps/` and `.bsp`, in upper or lower case |
| crc32 | The CRC-32 of the whole `.bsp` file, in 8 hexadecimal digits |
| `drop` | Removes the key, so the entity uses its default |
| `set` | Gives the key the value at the end of the line |
| classname | The class of the entities to change |
| selector | Which entities of the class to change: `*` for all of them, `#N` for the entity at position N of the map's entity list, where 0 is [`worldspawn`](../entities/worldspawn.md), or a name for every entity of the class with that name |
| key | The key to remove or change |

An entry only applies to the `.bsp` file with its checksum, so when an author updates a map, the new file has a
different checksum and the entry doesn't apply to it. An entry also only acts while the map loads, so it doesn't
change a key that changes later, for example through a
[`trigger_changevalue`](../entities/trigger_changevalue.md). With `developer 1` set in the console, the console shows
each change. A server can turn the file off with `mp_map_compat`.

Server setting (in `server.cfg` or the server console): [`mp_map_compat`](../../server/settings.md#maps)

## What SBO 2.0.0 does to every map

Two changes apply to old and new maps alike:

- Footsteps, bullet hit sounds and impact effects follow the [materials](../features/materials.md) of the
  textures, and this includes the SBO textures
- Models with a `scale` key show at that scale (see [Model scale](../features/model-scale.md))

## SBO 1.38 entities

SBO 2.0.0 replaced the SBO 1.38 rain and snow entity. If an old map has it, the game puts an
[`env_rain`](../entities/env_rain.md) or [`env_snow`](../entities/env_snow.md) with its default settings in its
place, so rain stays rain and snow stays snow, and with `developer 1` set in the console, a console message tells you
so. See [Weather and fog](../features/weather.md) for more details.

## See also

- [Server files](../../server/files.md#map-compatibility) - the format of the compatibility file for server operators
- [Compiler notes](compiler-notes.md) - what the compile tools change in SBO entities
- [Materials](../features/materials.md) - footsteps and hit effects by texture
- [Model scale](../features/model-scale.md) - the `scale` key on models
- [Weather and fog](../features/weather.md) - rain, snow and fog
