An `env_snow` makes it snow over the whole map, as in Counter-Strike 1.6, and its position doesn't matter.

Each player's game draws the snow around their view wherever the sky is above, so no snow falls indoors. Each player
sets the amount of snow with the weather option, the client setting
[`cl_weather`](../../playing/options.md#player-cvars), and only the OpenGL renderer draws it.

## Attributes

- **Name** (`targetname`) - Without a name, the snow is always on. With a name, it is a snow of its own that starts
  off unless you set **Start Active**, and triggering the entity switches it on or off, as the
  [use type](../guide/trigger-modes.md) says, so every player sees the change at once. See
  [Common keys](common-keys.md#targetname)
- **Snowflakes per update** (`intensity`) [[ported:featureful]] - Sets how many snowflakes each update makes, spread
  within 1024 units around each player's view, up to 1000, and anything above 1000 works like 1000. Default 512
- **Update period** (`update_period`) [[ported:featureful]] - Sets how many seconds pass between two batches of
  snowflakes, down to 0.05. Default 0.5
- **Snowflake min size** (`snowflake_min_size`) [[ported:featureful]] - Sets the size of the smallest snowflakes, in
  units, and each snowflake gets a random size between this and **Snowflake max size**. Default 2.1
- **Snowflake max size** (`snowflake_max_size`) [[ported:featureful]] - Sets the size of the biggest snowflakes, in
  units. Default 2.6
- **Snowflake min falling speed** (`snowflake_min_speed`) [[ported:featureful]] - Sets the slowest speed a snowflake
  falls at, in units per second, and each snowflake gets a random speed between this and **Snowflake max falling
  speed**. Default 131
- **Snowflake max falling speed** (`snowflake_max_speed`) [[ported:featureful]] - Sets the fastest speed a snowflake
  falls at, in units per second. Default 210
- **Snowflake max life** (`snowflake_life`) [[ported:featureful]] - Sets the longest time a snowflake lasts, in
  seconds, before it disappears. Default 3.0
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

- **Start Active** (1) [[ported:featureful]] - A snow with a **Name** is on when the map starts. A snow without a
  name is always on
- **Allow indoor** (2) [[ported:featureful]] - Snowflakes also fall where there is no sky above, for example under a
  roof
- **Snowflakes not affected by wind** (4) [[ported:featureful]] - The snowflakes fall straight down, with no wind and
  no spread
- **Snowflakes go through brush entities** (256) [[ported:featureful]] - Snowflakes fall through doors, walls and
  other brush entities, and only land on the world
- **Don't dissolve in water** (512) [[ported:featureful]] - Snowflakes fall into water instead of melting on its
  surface

## Notes

- If you leave every key empty, the snow looks exactly like the snow of Counter-Strike 1.6
- If you set a key to 0 or below, the snow uses the default for that key, except for the wind and spread keys, where
  0 is no wind or no spread
- With the random wind, a few snowflakes drift at half its speed, while a fixed wind drifts every snowflake alike
- The wind keys work like the keys **Wind X**, **Wind Y**, **Rand X** and **Rand Y** of Spirit of Half-Life's
  `rain_modify`, and SBO also accepts their key names `m_flWindX`, `m_flWindY`, `m_flRandX` and `m_flRandY`
- You can change every key and flag while the map runs with a [`trigger_changevalue`](trigger_changevalue.md) or a
  [`trigger_copyvalue`](trigger_copyvalue.md), and every player sees the change at once. Setting **Start Active**
  this way switches a snow with a **Name** on, and clearing it switches the snow off
- Only the first `env_snow` without a name counts, and more of them do nothing. If a map has an
  [`env_rain`](env_rain.md) and an `env_snow` without names, it gets the rain and no snow
- Each `env_snow` with a name is drawn on top of the weather without a name, so you can switch a snowfall on later in
  the map, for example

## See also

- [`func_snowvolume`](func_snowvolume.md) - snow only inside a brush
- [`env_rain`](env_rain.md) - rain over the whole map
- [`env_fog`](env_fog.md) - fog over the whole map
- [Weather and fog](../features/weather.md) - fog, rain and snow
- [Changing keys](../guide/changing-keys.md) - how `trigger_changevalue` and `trigger_copyvalue` work

## Changes since 1.38

- `env_snow` is new in SBO 2.0.0
- Since SBO 2.1.0, `env_snow` has the keys and flags of [`func_snowvolume`](func_snowvolume.md), and a name to
  switch it on and off
- Since SBO 2.1.0, `env_snow` has the wind keys **Wind X**, **Wind Y**, **Wind spread X** and **Wind spread Y**, and
  its keys can change while the map runs
