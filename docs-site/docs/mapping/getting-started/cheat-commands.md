---
description: "The cheat and entity commands let you test a map while you play it: you can become invulnerable or fast, fly through walls, and create, trigger, list, remove and show entities from the console."
---

# Cheat commands

The cheat and entity commands let you test a map while you play it: you can become invulnerable or fast, fly through
walls, and create, trigger, list, remove and show entities from the console. They work in every game mode on a
server with `sv_cheats 1`, which you set in `server.cfg` or in the server console. Each command only affects the
player who types it, and only prints to that player's console.

## Turning cheats on

The server's `sv_cheats` setting decides if the commands run. With `sv_cheats 0`, each command prints `The command
"<name>" can only be used when cheats are enabled` and does nothing, so the commands stay off on a public server. On
a listen server you host, and in a map you [start with `maxplayers 1`](testing.md#starting-the-map), type
`sv_cheats 1` in the console to turn them on. `sv_cheats 2` also runs the commands, and on a server it also lets
players open the in-game [color correction](../features/color-correction.md), [particle](../features/particles.md)
and [world screen](../features/world-screens.md) editors, which `sv_cheats 1` doesn't allow.

Every cheat ends when you respawn, so a new round, a map change or a reconnect turns all cheats off. Three cheat
impulses share their state with these commands:

- `impulse 200` is the same noclip as `cheat_noclip`
- `impulse 210` is the same godmode as `cheat_god`
- `impulse 211` is the same notarget as `cheat_notarget`

`impulse 101` gives you every weapon, full ammo and full armor.

## Cheat toggles [[ported:hlunified]]

Each command below is a toggle: type it once to turn the cheat on, and type it again to turn it off. The console
prints the new state, such as `cheat_god ON`, and adding `1` or `0` after the name, as in `cheat_god 1`, turns the
cheat on or off from any state.

| Command | What it does |
|---|---|
| `cheat_god` | You take no damage. It is the same godmode as `impulse 210` |
| `cheat_unkillable` | Damage still hurts you, but your health never drops below 1, so you can't die |
| `cheat_notarget` | Monsters don't target you, although they still hear you and turn to face you. It is the same notarget as `impulse 211` |
| `cheat_noclip` | You fly through walls and floors. It is the same noclip as `impulse 200`, and if you turn it off inside a wall, it moves you out to the nearest open space. It works only while you are alive and not spectating |
| `cheat_infiniteair` | Your air never runs out under water, so you take no drowning damage |
| `cheat_infinitearmor` | Your armor still protects you, but damage doesn't use it up |

## Speed

`cheat_speed <multiplier>` multiplies your top speed, so `cheat_speed 2` doubles it and `cheat_speed 0.5` halves it.
Type `cheat_speed` without a number, or `cheat_speed 1`, to get your normal speed back. The multiplier works on top
of the game's normal speed rules, so your level, your armor, a hurt leg, your weapon and a zoom still change your
speed, and when the cheat ends, you get the speed the game gives you at that moment.

The highest speed is 2000, the same speed `impulse 212` gives. The two don't add up, because they set the same speed
and the one you used last counts, so `cheat_speed` without a number, or `cheat_speed 1`, also ends `impulse 212`.
The speed also ends when you die or start to spectate. Your game predicts the new speed, so movement stays smooth.
If the server's `sv_maxspeed` is below 2000, it limits the speed to that value (the `server.cfg` that comes with SBO
sets `sv_maxspeed` to 2000).

## Entity commands [[ported:hlunified]]

The entity commands are one-time actions. "The entity you are looking at" is the first entity under your crosshair,
and a name can be an entity's `targetname` or its class name, with the command taking the first entity that matches
either. Lists show 10 entities per page, each with its index, class name, name and position.

| Command | What it does |
|---|---|
| `ent_create <class> [<key> <value> ...]` | Creates an entity of that class where you are looking, with the keys you give, as in `ent_create env_sprite model sprites/glow01.spr rendermode 5` |
| `npc_create <class> [<key> <value> ...]` | Creates a monster where you are looking, standing on the floor and facing your way. If there is no floor under it, the game removes it again |
| `ent_fire <name> [use type] [value]` | Triggers every entity with that name, with you as the activator. The use type is 0 for Off, 1 for On, 2 for Set or 3 for Toggle, and Toggle is the default. Names ending in `*` and the `!activator` keyword work as in [entity triggering](../guide/entity-triggering.md) |
| `ent_list [page]` | Lists every entity on the map |
| `ent_find_by_classname <class> [page]` | Lists the entities of that class |
| `ent_find_by_targetname <name> [page]` | Lists the entities with that name |
| `ent_remove [name]` | Removes the entity you are looking at, or the first entity with that name, but it never removes a player |
| `ent_remove_all <name>` | Removes every entity with that name or class name, and prints how many it removed |
| `ent_setname <new name> [name]` | Gives a new name to the entity you are looking at, or to the first entity with that name |
| `ent_show_bbox <name>` | Draws the entity's bounding box in blue for 10 seconds, one unit larger on each side than the entity |
| `ent_show_center <name>` | Shows a dot at the entity's center for 10 seconds and prints its position |
| `ent_show_origin <name>` | Shows a dot at the entity's origin for 10 seconds and prints its position. A brush entity without an origin brush has its origin at 0 0 0 |

Only you can see the boxes and dots the `ent_show_` commands draw.

### What ent_create and npc_create can create

`ent_create` and `npc_create` can only create what the map has already loaded. Half-Life can't load a model, sound
or sprite after the map has started, and it stops the server if the game tries, so if a monster, weapon or effect
needs a file this map doesn't use, the command prints
`Can't create "<class>": it needs "<file>", which this map has not loaded` and creates nothing. You can't create the
classes `player` and [`worldspawn`](../entities/worldspawn.md).

## Changes since 1.38

- New console commands for testing maps with `sv_cheats 1`, for example `cheat_noclip`, `ent_create` and `ent_fire`.
  The cheat commands guide lists all of them

## See also

- [Testing a map](testing.md) - how to start and test your map
- [Entity triggering](../guide/entity-triggering.md) - names, wildcards and keywords such as `!activator`
- [Server settings](../../server/settings.md) - the server's settings
