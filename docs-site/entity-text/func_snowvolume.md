A `func_snowvolume` makes it snow only inside its brush, and with **Allow indoor**, under a roof too. The snow is the
same as the snow of [`env_snow`](env_snow.md), and each player's game draws it while the brush is in view.

With an [`env_rain`](env_rain.md) or an `env_snow` in the map, both are drawn, and volumes that overlap add up. Each
player's weather option, the client setting [`cl_weather`](../../playing/options.md#player-cvars), sets the amount
of snow, for the volumes too, and only the OpenGL renderer draws it.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the snow on or off, as the
  [use type](../guide/trigger-modes.md) says, and every player sees the change at once. Without a name, the snow is
  always on. See [Common keys](common-keys.md#targetname)
- **Snowflakes per update** (`intensity`) - Sets how many snowflakes each update makes, spread over the whole brush,
  so a bigger brush needs more for the same snow, up to 1000, and anything above 1000 works like 1000. Default 150
- **Update period** (`update_period`) - Sets how many seconds pass between two batches of snowflakes, down to 0.05. Default 0.5
- **Snowflake min size** (`snowflake_min_size`) - Sets the size of the smallest snowflakes, in units, and each
  snowflake gets a random size between this and **Snowflake max size**. Default 2.1
- **Snowflake max size** (`snowflake_max_size`) - Sets the size of the biggest snowflakes, in units. Default 2.6
- **Snowflake min falling speed** (`snowflake_min_speed`) - Sets the slowest speed a snowflake falls at, in units per
  second, and each snowflake gets a random speed between this and **Snowflake max falling speed**. Default 131
- **Snowflake max falling speed** (`snowflake_max_speed`) - Sets the fastest speed a snowflake falls at, in units per
  second. Default 210
- **Snowflake max life** (`snowflake_life`) - Sets the longest time a snowflake lasts, in seconds, before it
  disappears. Default 3.0
- **Wind X** (`wind_x`) [[ported:spirit]] - Sets a fixed wind, which is the sideways speed of every snowflake along
  the map's X axis, in units per second, so a negative value blows the other way. If you set **Wind X** or **Wind
  Y**, this snow drifts with that fixed wind instead of the random wind, which changes its direction every 15 to 30
  seconds, and every snowflake drifts the same way
    - If you leave **Wind X** and **Wind Y** empty, the snow uses the random wind
- **Wind Y** (`wind_y`) [[ported:spirit]] - Sets the sideways speed of every snowflake along the map's Y axis, in
  units per second, in the same way as **Wind X**
- **Wind spread X** (`wind_rand_x`) [[ported:spirit]] - Gives each snowflake a random extra sideways speed along X,
  from minus this value up to this value, in units per second, on top of the fixed or the random wind
    - If you leave this key empty, it is 0 and there is no spread
- **Wind spread Y** (`wind_rand_y`) [[ported:spirit]] - Gives each snowflake a random extra sideways speed along Y, in
  the same way as **Wind spread X**
    - If you leave this key empty, it is 0 and there is no spread

## Flags

- **Start Active** (1) - A volume with a **Name** is on when the map starts. A volume without a name is always on
- **Allow indoor** (2) - Snowflakes also fall where there is no sky above. Without this flag, a snowflake needs sky
  above it, as with `env_snow`
- **Snowflakes not affected by wind** (4) - The snowflakes fall straight down, with no wind and no spread
- **Snowflakes go through brush entities** (256) - Snowflakes fall through doors and other brush entities, and only
  land on the world
- **Don't dissolve in water** (512) - Snowflakes fall into water instead of melting on its surface

## Notes

- If you set a key to 0 or below, the volume uses the default for that key, except for the wind and spread keys,
  where 0 is no wind or no spread
- The wind keys work like the keys **Wind X**, **Wind Y**, **Rand X** and **Rand Y** of Spirit of Half-Life's
  `rain_modify`, and SBO also accepts their key names `m_flWindX`, `m_flWindY`, `m_flRandX` and `m_flRandY`
- You can change every key and flag while the map runs with a [`trigger_changevalue`](trigger_changevalue.md) or a
  [`trigger_copyvalue`](trigger_copyvalue.md), and every player sees the change at once. Setting **Start Active**
  this way switches a volume with a **Name** on, and clearing it switches the volume off
- The volume doesn't move with other entities, but if you change its `origin` with a `trigger_changevalue`, the
  snow jumps to the new place

## See also

- [`func_rainvolume`](func_rainvolume.md) - rain inside a brush
- [`env_snow`](env_snow.md) - snow over the whole map
- [Weather and fog](../features/weather.md) - fog, rain and snow
- [Changing keys](../guide/changing-keys.md) - how `trigger_changevalue` and `trigger_copyvalue` work

## Changes since 1.38

- `func_snowvolume` is new in SBO 2.0.0
- Since SBO 2.1.0, `func_snowvolume` has the wind keys **Wind X**, **Wind Y**, **Wind spread X** and **Wind
  spread Y**, and its keys can change while the map runs
