---
description: "Two entities let you change almost any key of another entity while the map runs: trigger_changevalue writes a value into a key, and trigger_copyvalue copies one."
---

# Changing keys [[ported:sevenkewp svencoop]]

Two entities let you change almost any key of another entity while the map runs:
[`trigger_changevalue`](../entities/trigger_changevalue.md) writes a value into a key, and
[`trigger_copyvalue`](../entities/trigger_copyvalue.md) copies one entity's key into another's. Both can also combine
the old value with the new one, so they can add, multiply, append text and more. See the
[Changing values](../../guides/value-triggers.md) guide for small setups that use them.

## `trigger_changevalue`

When you trigger a `trigger_changevalue`, it writes **New value** into the key **Key name** of its destination
entities.

| Key | What it holds |
|---|---|
| **Destination entity** (`target`) | Every entity with this name, or `!activator` or `!caller` |
| **Key name** (`m_iszValueName`) | The key to change, for example `health`, `rendercolor`, `scale` or `message`, or a [custom key](entity-keyvalues.md#custom-keys) |
| **New value** (`m_iszNewValue`) | A number, three numbers `x y z`, or text |
| **Type of value** (`m_iszValueType`) | The operation (see [Operations](#operations)). The default is Replace (0) |
| **Treat new value as** (`value_type`) | Literal value (0), the default, uses **New value** as you wrote it. Locus Ratio (1), Locus Position (2) and Locus Velocity (3) treat it as a [locus](locus.md) key, which the entity works out for the activator each time it fires |
| **Trigger after operation** (`message`) | The entity that gets a Toggle after the change, which can be a name, `!activator` or `!caller` |

**New value** can also be a named constant, such as `FL_ONGROUND`, `SOLID_NOT`, `EF_NODRAW`, `MOVETYPE_FLY`,
`kRenderTransAdd` or `CLASS_PLAYER`, in capital or small letters. If you put a `~` in front of a number or a
constant, the entity flips every bit of it, so together with the operation AND it clears those bits.

## `trigger_copyvalue`

When you trigger a `trigger_copyvalue`, it reads **Source key** of the source entity and writes it into
**Destination key** of the destination entity, with the same operations. With the flag **Constant**, it copies
again at an interval, so one key follows another.

| Key | What it holds |
|---|---|
| **Source entity** (`netname`) | The first entity with this name, or `!activator` or `!caller` |
| **Source key** (`m_iszSrcValueName`) | The key to read |
| **Destination entity** (`target`) | The first entity with this name, or every entity with it if you set **Multiple destinations**, or `!activator` or `!caller` |
| **Destination key** (`m_iszDstValueName`) | The key to write |
| **Float conversion** (`m_iFloatConversion`) | How a number with decimals becomes text or a whole number. The choices with 6, 5, 4, 3, 2 or 1 decimal places set the text, and they round a whole number down. The other choices round to the nearest whole number, round up or round down |
| **Copy interval** (`dmg`) | How many seconds pass between two copies in constant mode, where 0 copies every frame |

Its flags are:

- **Constant** (8) - Each trigger copies once. After an On, or a Toggle that turns it on, it also copies again
  every **Copy interval** seconds, until it gets an Off, or a Toggle that turns it off
- **Start on** (16) - Together with **Constant**, constant mode runs from the start of the map
- **Multiple destinations** (128) - Every entity with the destination name gets the value, and not only the first

## Operations

The operation decides how the key's old value and the new or copied value combine, and the destination key's type
decides the math:

- whole numbers stay whole, and numbers with decimals keep their decimals
- a vector key is worked out one part at a time, so three numbers such as `64 0 0` go into it part by part, and a
  single number goes into every part
- text keys only accept Replace and Append

| Value | Operation | Value | Operation |
|---|---|---|---|
| 0 | Replace | 11 | Append, for text |
| 1 | Add | 2 | Multiply |
| 3 | Subtract | 4 | Divide |
| 16 | Power | 12 | Modulo, on whole numbers |
| 5 | AND | 6 | OR |
| 13 | XOR | 15 | Clear bits |
| 7, 8, 14 | NAND, NOR, NXOR | 30, 31 | Min, Max |
| 9 | Direction to angles | 10 | Angles to direction |
| 17, 18, 19, 23 | Sine, cosine, tangent and cotangent of the new value | 20, 21, 22, 24 | Arcsine, arccosine, arctangent and arccotangent of the new value |

Direction to angles and Angles to direction turn the key's old value into the other form and ignore the new value.
**Trigonometric funcs. behavior** (`m_trigonometricBehaviour`) sets the unit of the angle functions, Degrees (0), the
default, or Radians (1), and with Degrees, the sine of 30 is 0.5. **Append spaces** (`m_iAppendSpaces`) is the number
of spaces the entity adds after a text result. If an operation divides by zero, the key keeps its old value.

Both entities share these flags, which change the values before the operation:

- **Don't use X** (1), **Don't use Y** (2) and **Don't use Z** (4) - That part of a vector stays as it is
- **Invert target value** (32) - The old value becomes negative before the operation
- **Invert source value** (64) - The new value becomes negative before the operation

## What can change

A key the entity reads each time it uses it takes effect at once. These keys are `health`, `max_health`,
`dmg`, `speed`, `wait`, `delay`, `target`, `message`, `frags`, the render keys, `spawnflags`, `solid`, `movetype`,
`effects`, `gravity`, `origin`, `angles`, `velocity`, the `unkillable` key of a monster, in both directions, and
custom keys.

Some keys do more than store a value:

- `scale` changes the size of the model and its collision box at once (see
  [Model scale](../features/model-scale.md))
- the keys of a [`point_worldtext`](../entities/point_worldtext.md) and a [`game_timer`](../entities/game_timer.md)
  change the text or the timer for every player (see [World text](../features/world-text.md) and
  [HUD timer](../features/game-timer.md))
- every key and flag of [`env_rain`](../entities/env_rain.md), [`env_snow`](../entities/env_snow.md),
  [`func_rainvolume`](../entities/func_rainvolume.md) and [`func_snowvolume`](../entities/func_snowvolume.md) changes
  the weather for every player at once (see
  [Weather and fog](../features/weather.md#changing-the-weather-while-the-map-runs))

Some entities copy a key when they spawn, or only pass it on to the players' games when you trigger them. These
entities apply a change to the keys below themselves, with the same defaults and limits as when the map loads:

| Entity | Keys | What a change does |
|---|---|---|
| [`env_fog`](../entities/env_fog.md), [`env_fogzone`](../entities/env_fogzone.md) | Every key and flag, and the position of an `env_fogzone` | Every player sees the new fog at once |
| [`ambient_generic`](../entities/ambient_generic.md) | Volume, Pitch, WAV Name | A looping sound that plays changes its volume or pitch at once, and a new sound stops the old one and plays at once |
| [`func_rotating`](../entities/func_rotating.md) | Rotation Speed | It spins at the new speed at once, and 0 stops it |
| [`func_conveyor`](../entities/func_conveyor.md) | Conveyor Speed | The texture scrolls at the new speed too |
| [`trigger_push`](../entities/trigger_push.md) | Its angles (Pitch Yaw Roll), Speed of push | It pushes in the new direction and at the new speed, and a speed of 0 is 100, as at spawn |
| Monsters | Health, Max health | A health above the monster's maximum raises the maximum, and a maximum below its health lowers the health |
| [`monstermaker`](../entities/monstermaker.md) | Number of Monsters | A maker that made its last monster starts again |
| [`light`](../entities/light.md), [`light_spot`](../entities/light_spot.md) | Custom Appearance | A light that is on shows the new pattern at once |
| [`env_explosion`](../entities/env_explosion.md) | Magnitude | The fireball of the next explosion has the new size |
| [`env_overlay`](../entities/env_overlay.md) | Every key but the picture and the channel | The players who see it get the new values at once |
| [`color_correction`](../entities/color_correction.md), [`color_correction_volume`](../entities/color_correction_volume.md) | Every key but the file | Every player gets the new values at once, and a fade goes on from where it is |
| [`env_dlight`](../entities/env_dlight.md), [`env_elight`](../entities/env_elight.md) | Radius, Light color | A light that is on changes at once |
| [`env_sky`](../entities/env_sky.md) | Parallax scale, Sky fog color, Sky fog density, Skybox fog, its position | The 3D sky changes at once while it is the sky |
| [`multi_manager`](../entities/multi_manager.md) | A target's delay | The target fires at the new time, still once |
| [`func_tank`](../entities/func_tank.md) | Rate of Fire, Bullet accuracy | A rate of 0 is one shot a second and an accuracy outside the list is Perfect, as at spawn |

If an entity only reads a key when it spawns, a change sets the stored value but doesn't change what the entity
does, for example a door's `lip`. The speed of a [`func_tracktrain`](../entities/func_tracktrain.md) is one of these
keys, so use a [`train_setspeed`](../entities/train_setspeed.md) to change a train's speed. If the entity can't tell
what a key holds, only Replace works on it, and any other operation leaves the key as it is. With
`developer 1` set in the console, the console then shows `trigger_changevalue "<name>": key "<key>" of <class> "<name>" can't be
read, so only Replace works on it (nothing changed)`, with `trigger_copyvalue` at the start for that entity.

Both entities refuse the keys `model`, `viewmodel`, `weaponmodel`, `noise`, `noise1`, `noise2` and `noise3`,
because the game would have to precache (load) a new file. With `developer 1` set in the console, the console then
shows `Key "<key>" of <class> "<name>" can't be changed at run time (it would need a precache)`. The `noise` keys of
[`calc_ratio`](../entities/calc_ratio.md), the calc velocity entities and [`env_state`](../entities/env_state.md)
hold numbers and target names, not sounds, so you can change them.

Both entities also refuse the key `classname`, because the entity would keep the behavior of its own class under the
name of another class. With `developer 1` set in the console, the console then shows `<class>: classname "<value>"
ignored (an entity's class can't be changed)`.

A few more keys are refused because changing them would break the entity:

- The sound of an `ambient_generic`, unless the map has already loaded that sound, for example because another
  entity uses it, because a new sound would have to be precached. An MP3 can't be changed either
- **Appearance** (the style number) of a `light` or `light_spot`, because the light would then switch the lights of
  another style number
- **Channel** of an `env_overlay`, because the players' screens keep it on its channel

Some entities keep a model or a sprite in a key of their own and refuse a change to that key after they spawn, with
the same kind of console line, and keep working with the old value. These keys are:

- **Model or Sprite name** (`shootmodel`) of an [`env_shooter`](../entities/env_shooter.md)
- **Smoke Sprite** (`spritesmoke`) and **Flash Sprite** (`spriteflash`) of the [`func_tank`](../entities/func_tank.md)
  family
- **Sprite 2 Name** (`model2`) of an [`env_warpball`](../entities/env_warpball.md)
- the `#` keys of a [`monstermaker`](../entities/monstermaker.md)
- the files of an [`env_overlay`](../entities/env_overlay.md) and a [`color_correction`](../entities/color_correction.md)

The **Monster Type** (`monstertype`) of a monstermaker and a new item key of a
[`game_player_equip`](../entities/game_player_equip.md) only accept a class the map already loads: a class the map
places or a maker makes, a morph monster, or a weapon. The entities refuse any other class with the same console
line, and a maker with `#` keys keeps its class.

## Changes since 1.38

- `trigger_changevalue` and `trigger_copyvalue` are new

## See also

- [Changing values](../../guides/value-triggers.md) - a guide with small setups
- [Entity keyvalues](entity-keyvalues.md) - how keys and custom keys work
- [`trigger_condition`](../entities/trigger_condition.md) - compares a key with a value and fires a target
- [Locus system](locus.md) - keys that ask another entity for a value
