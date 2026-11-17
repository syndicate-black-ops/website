A `func_rainvolume` makes it rain only inside its brush, and with **Allow indoor**, under a roof too. The rain is the
same as the rain of [`env_rain`](env_rain.md), and each player's game draws it while the brush is in view.

With an `env_rain` or an [`env_snow`](env_snow.md) in the map, both are drawn, and volumes that overlap add up. Each
player's weather option, the client setting [`cl_weather`](../../playing/options.md#player-cvars), sets the amount
of rain, for the volumes too, and only the OpenGL renderer draws it.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the rain on or off, as the
  [use type](../guide/trigger-modes.md) says, and every player sees the change at once. Without a name, the rain is
  always on. See [Common keys](common-keys.md#targetname)
- **Raindrops per update** (`intensity`) - Sets how many raindrops each update makes, spread over the whole brush,
  so a bigger brush needs more for the same rain, up to 1000, and anything above 1000 works like 1000. Default 150
- **Update period** (`update_period`) - Sets how many seconds pass between two batches of raindrops, down to 0.05. Default 0.3
- **Raindrop width** (`raindrop_width`) - Sets the width of a raindrop, in units. Default 2
- **Raindrop tallness** (`raindrop_height`) - Sets the length of a raindrop, in units. Default 80
- **Raindrop min falling speed** (`raindrop_min_speed`) - Sets the slowest speed a raindrop falls at, in units per
  second, and each raindrop falls at a random speed between this and **Raindrop max falling speed**. Default 500
- **Raindrop max falling speed** (`raindrop_max_speed`) - Sets the fastest speed a raindrop falls at, in units per
  second. Default 1800
- **Raindrop max life** (`raindrop_life`) - Sets how many seconds a raindrop that hasn't hit anything lasts. Default 1.0
- **Wind X** (`wind_x`) [[ported:spirit]] - Sets a fixed wind, which is the sideways speed of every raindrop along
  the map's X axis, in units per second, so a negative value blows the other way. If you set **Wind X** or **Wind
  Y**, this rain blows with that fixed wind instead of the random wind, which changes its direction every 15 to 30
  seconds, and every raindrop slants the same way
    - If you leave **Wind X** and **Wind Y** empty, the rain uses the random wind
- **Wind Y** (`wind_y`) [[ported:spirit]] - Sets the sideways speed of every raindrop along the map's Y axis, in
  units per second, in the same way as **Wind X**
- **Wind spread X** (`wind_rand_x`) [[ported:spirit]] - Gives each raindrop a random extra sideways speed along X,
  from minus this value up to this value, in units per second, on top of the fixed or the random wind
    - If you leave this key empty, it is 0 and there is no spread
- **Wind spread Y** (`wind_rand_y`) [[ported:spirit]] - Gives each raindrop a random extra sideways speed along Y, in
  the same way as **Wind spread X**
    - If you leave this key empty, it is 0 and there is no spread

## Flags

- **Start Active** (1) - A volume with a **Name** is on when the map starts. A volume without a name is always on
- **Allow indoor** (2) - Raindrops also fall where there is no sky above. Without this flag, a raindrop needs sky
  above it, as with `env_rain`
- **Raindrops not affected by wind** (4) - The raindrops fall straight down, with no wind and no spread, and only
  the puffs of dust still blow with the wind
- **No wind puffs** (32) - No puffs of dust blow across the ground
- **No rain splashes** (64) - Raindrops make no splashes where they hit the ground
- **No ripples on water** (128) - Raindrops make no ripples where they hit water
- **Raindrops go through brush entities** (256) - Raindrops fall through brush entities and only stop at the world
- **Don't stop at the water surface** (512) - Raindrops fall on through water instead of stopping at its surface

## Notes

- The rain makes no sound
- If you set a key to 0 or below, the volume uses the default for that key, except for the wind and spread keys,
  where 0 is no wind or no spread
- The wind keys work like the keys **Wind X**, **Wind Y**, **Rand X** and **Rand Y** of Spirit of Half-Life's
  `rain_modify`, and SBO also accepts their key names `m_flWindX`, `m_flWindY`, `m_flRandX` and `m_flRandY`
- You can change every key and flag while the map runs with a [`trigger_changevalue`](trigger_changevalue.md) or a
  [`trigger_copyvalue`](trigger_copyvalue.md), and every player sees the change at once. Setting **Start Active**
  this way switches a volume with a **Name** on, and clearing it switches the volume off
- The volume doesn't move with other entities, but if you change its `origin` with a `trigger_changevalue`, the
  rain jumps to the new place

## See also

- [`func_snowvolume`](func_snowvolume.md) - snow inside a brush
- [`env_rain`](env_rain.md) - rain over the whole map
- [Weather and fog](../features/weather.md) - fog, rain and snow
- [Changing keys](../guide/changing-keys.md) - how `trigger_changevalue` and `trigger_copyvalue` work

## Changes since 1.38

- `func_rainvolume` is new in SBO 2.0.0
- Since SBO 2.1.0, `func_rainvolume` has the wind keys **Wind X**, **Wind Y**, **Wind spread X** and **Wind
  spread Y**, and its keys can change while the map runs
