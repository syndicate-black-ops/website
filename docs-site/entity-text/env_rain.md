An `env_rain` makes it rain over the whole map, as in Counter-Strike 1.6, and its position doesn't matter.

Each player's game draws the rain around their view wherever the sky is above, so it stays dry indoors. Each player
sets the amount of rain with the weather option, the client setting
[`cl_weather`](../../playing/options.md#player-cvars), and only the OpenGL renderer draws it.

## Attributes

- **Name** (`targetname`) - Without a name, the rain is always on. With a name, it is a rain of its own that starts
  off unless you set **Start Active**, and triggering the entity switches it on or off, as the
  [use type](../guide/trigger-modes.md) says, so every player sees the change at once. See
  [Common keys](common-keys.md#targetname)
- **Raindrops per update** (`intensity`) [[ported:featureful]] - Sets how many raindrops each update makes, spread
  within 400 units around each player's view, up to 1000, and anything above 1000 works like 1000. Default 150
- **Update period** (`update_period`) [[ported:featureful]] - Sets how many seconds pass between two batches of
  raindrops, down to 0.05. Default 0.3
- **Raindrop width** (`raindrop_width`) [[ported:featureful]] - Sets the width of a raindrop, in units. Default 2
- **Raindrop tallness** (`raindrop_height`) [[ported:featureful]] - Sets the length of a raindrop, in units.
  Default 80
- **Raindrop min falling speed** (`raindrop_min_speed`) [[ported:featureful]] - Sets the slowest speed a raindrop
  falls at, in units per second, and each raindrop falls at a random speed between this and **Raindrop max falling
  speed**. Default 500
- **Raindrop max falling speed** (`raindrop_max_speed`) [[ported:featureful]] - Sets the fastest speed a raindrop
  falls at, in units per second. Default 1800
- **Raindrop max life** (`raindrop_life`) [[ported:featureful]] - Sets how many seconds a raindrop that hasn't hit
  anything lasts. Default 1.0
- **Wind X** (`wind_x`) [[ported:spirit]] - Sets a fixed wind, which is the sideways speed of every raindrop along the
  map's X axis, in units per second, so a negative value blows the other way. If you set **Wind X** or **Wind Y**,
  this rain blows with that fixed wind instead of the random wind, which changes its direction every 15 to 30
  seconds, and every raindrop slants the same way
    - If you leave **Wind X** and **Wind Y** empty, the rain uses the random wind
- **Wind Y** (`wind_y`) [[ported:spirit]] - Sets the sideways speed of every raindrop along the map's Y axis, in units
  per second, in the same way as **Wind X**
- **Wind spread X** (`wind_rand_x`) [[ported:spirit]] - Gives each raindrop a random extra sideways speed along X,
  from minus this value up to this value, in units per second, on top of the fixed or the random wind, so the drops
  don't all slant alike
    - If you leave this key empty, it is 0 and there is no spread
- **Wind spread Y** (`wind_rand_y`) [[ported:spirit]] - Gives each raindrop a random extra sideways speed along Y, in
  the same way as **Wind spread X**
    - If you leave this key empty, it is 0 and there is no spread

## Flags

- **Start Active** (1) [[ported:featureful]] - A rain with a **Name** is on when the map starts. A rain without a
  name is always on
- **Allow indoor** (2) [[ported:featureful]] - Raindrops also fall where there is no sky above, for example under a
  roof
- **Raindrops not affected by wind** (4) [[ported:featureful]] - The raindrops fall straight down, with no wind and
  no spread, and only the puffs of dust still blow with the wind
- **No wind puffs** (32) [[ported:featureful]] - No puffs of dust blow across the ground
- **No rain splashes** (64) [[ported:featureful]] - Raindrops make no splashes where they hit the ground
- **No ripples on water** (128) [[ported:featureful]] - Raindrops make no ripples where they hit water
- **Raindrops go through brush entities** (256) [[ported:featureful]] - Raindrops fall through brush entities and
  only stop at the world
- **Don't stop at the water surface** (512) [[ported:featureful]] - Raindrops fall on through water instead of
  stopping at its surface

## Notes

- If you leave every key empty, the rain looks exactly like the rain of Counter-Strike 1.6
- If you set a key to 0 or below, the rain uses the default for that key, except for the wind and spread keys, where
  0 is no wind or no spread
- The puffs of dust blow with the fixed wind when the rain has one
- The wind keys work like the keys **Wind X**, **Wind Y**, **Rand X** and **Rand Y** of Spirit of Half-Life's
  `rain_modify`, and SBO also accepts their key names `m_flWindX`, `m_flWindY`, `m_flRandX` and `m_flRandY`. The
  slant also depends on the falling speed, so a fast raindrop slants less than a slow one with the same wind
- You can change every key and flag while the map runs with a [`trigger_changevalue`](trigger_changevalue.md) or a
  [`trigger_copyvalue`](trigger_copyvalue.md), and every player sees the change at once. Setting **Start Active**
  this way switches a rain with a **Name** on, and clearing it switches the rain off
- Only the first `env_rain` without a name counts, and more of them do nothing. If a map has an `env_rain` and an
  [`env_snow`](env_snow.md) without names, it gets the rain and no snow
- Each `env_rain` with a name is drawn on top of the rain without a name, so you can switch a heavier rain on for a
  storm, for example
- The rain makes no sound

## See also

- [`func_rainvolume`](func_rainvolume.md) - rain only inside a brush
- [`env_snow`](env_snow.md) - snow over the whole map
- [`env_fog`](env_fog.md) - fog over the whole map
- [Weather and fog](../features/weather.md) - fog, rain and snow
- [Changing keys](../guide/changing-keys.md) - how `trigger_changevalue` and `trigger_copyvalue` work

## Changes since 1.38

- `env_rain` is new in SBO 2.0.0
- Since SBO 2.1.0, `env_rain` has the keys and flags of [`func_rainvolume`](func_rainvolume.md), and a name to
  switch it on and off
- Since SBO 2.1.0, `env_rain` has the wind keys **Wind X**, **Wind Y**, **Wind spread X** and **Wind spread Y**, and
  its keys can change while the map runs
