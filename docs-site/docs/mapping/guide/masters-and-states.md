---
description: "A master locks an entity, so a door, a button or a trigger with a Master only works while its master is on, and SBO has named states, logic gates and watchers that can all be masters."
---

# Masters and states

A master locks an entity, so a door, a button or a trigger with a **Master** only works while its master is on, and
SBO has named states, logic gates and watchers that can all be masters:

- named states that are on or off, switched with triggers
- logic gates that combine two states
- watchers that read the states of doors, monsters, lights and other entities

See the [Masters and multisource](../../guides/masters.md) guide for small setups that use them.

## Masters

The **Master** key (`master`) holds the name of a master entity. These entities can be masters:

| Master | It is on while |
|---|---|
| [`multisource`](../entities/multisource.md) | Every entity that targets it has switched its input on, and its global state is On if you set one |
| [`env_state`](../entities/env_state.md) | It is on |
| [`calc_state`](../entities/calc_state.md) | Its logic result is true |
| [`trigger_compare`](../entities/trigger_compare.md) | Its comparison passes, worked out for the activator of the locked entity |
| [`player_hasweapon`](../entities/player_hasweapon.md) | The activator is a player who carries the weapon it names, or any weapon if you leave the weapon empty |
| [`player_hasinventory`](../entities/player_hasinventory.md) | The activator carries the item it names, or the team has it when the item is shared |
| [`env_global`](../entities/env_global.md) with the flag **Act as Master** (4) | Its global state is On |
| [`multi_watcher`](../entities/multi_watcher.md) | The logical test of the states it watches is true |
| [`watcher_count`](../entities/watcher_count.md) | Its comparison of how many entities aren't off is true |

The game looks at the first entity with the master's name. If the name matches no entity, or matches an entity that
can't be a master, nothing is locked and the entity works, and with `developer 1` set in the console, the console
shows `Master was null or not a master!`. For an `env_global` master, put the name of the `env_global` in **Master**,
not the name of its global state. A global state that is Off, Dead or not set yet counts as off.

### Inverted masters

A `~` in front of the master's name makes the master work the other way round, so a door with the master `~alarm`
only opens while the `env_state` named `alarm` is off.

## `env_state` [[ported:featureful spirit]]

An `env_state` is a named state that is either on or off. Other entities can use it as a master, and it fires targets
when it changes. Triggers switch it like this:

| Trigger | What it does |
|---|---|
| On | Turns it on, or does nothing if it is already on |
| Off | Turns it off, or does nothing if it is already off |
| Toggle | Switches it to the other state |

| Key | What it does |
|---|---|
| `turnontime`, `turnofftime` | How many seconds it takes to turn on or off. As a master, it only counts as on once the turn-on time is over, and it counts as off from the moment it starts turning off |
| `target` | Gets On when the state turns on and Off when it turns off |
| `noise1`, `noise2` | `noise1` gets Toggle when the state turns on, and `noise2` gets Toggle when it turns off |
| `master` | While its own master is off, it ignores every trigger |
| `round_reset` | If you set Yes, it goes back to the state it had when the map loaded at each round start, without firing anything. See [Round hooks](round-hooks.md) for more details |

While it turns on, an On does nothing and an Off turns it off again, and while it turns off, an Off does nothing and
an On turns it on again.

![An env_state timeline: after an On it is turning on for its Turn on time and still counts as off as a master, then it is on and its target gets On. After an Off it counts as off at once and its target gets Off when the Turn off time is over. An On while it turns off starts the full Turn on time again, and the target gets no Off | 480](../../assets/img/diagram-env-state.webp)

*How an env_state turns on and off over time*

Its flags are **Start On** (1) and **Debug Mode** (2). The targets it fires at the end of a turn-on or turn-off time
get the `env_state` itself as their activator, and the other targets get the trigger's activator.

## `calc_state` [[ported:featureful]]

A `calc_state` is a logic gate that combines two operands. As a master, it is on while its result is true. When you
trigger it, it sends On to its **Target** if the result is true and Off if it is false, and it also fires **Fire
when true** or **Fire when false**.

| Key | Values |
|---|---|
| `left_operand`, `right_operand` | The names of two entities, and `!activator` and `*player` work too. An operand that is a master gives its state, and any other entity counts as on |
| `operation` | AND (0), OR (1), NAND (2), NOR (3), XOR (4) or NXOR (5) |
| `left_fallback`, `right_fallback` | What an operand that doesn't exist counts as. With Error (0), nothing fires and the `calc_state` is off as a master. Off (1) counts the operand as off, and On (2) counts it as on |

It has the flag **Debug Mode** (2). If `calc_state` entities use each other in a loop, the game stops after 32 levels
and the result is false.

## `trigger_inout` [[ported:featureful spirit]]

A [`trigger_inout`](../entities/trigger_inout.md) is a brush trigger that fires for each entity that enters it and
each entity that leaves it, with that entity as the activator. It isn't a master itself, but its **Fire on/off**
target can switch an `env_state`, or count with a [`game_counter`](../entities/game_counter.md).

| Key | What it does |
|---|---|
| `target` | Gets Toggle when an entity enters |
| `m_iszAltTarget` | Gets Toggle when an entity leaves |
| `m_iszBothTarget` | Gets On when an entity enters and Off when it leaves |
| `netname` | If you set it, only an entity with this class name or name counts, and the trigger ignores its flags |

By default it reacts to players. Its flags add monsters (1), pushables (4) and everything else (8), and **No
Clients** (2) leaves players out. It checks which entities have left every 0.1 seconds, and keeps track of up to 64
entities at once. A player only counts while they are alive, so a player inside who dies, becomes a spectator or
leaves the server counts as having left. While its master is off, nothing fires, but it still keeps track of the
entities that enter and leave.

## Entity states [[ported:spirit]]

Every entity is in one of five states: On, Off, Turn On, Turn Off and In Use. A
[`multi_watcher`](../entities/multi_watcher.md) and a [`watcher_count`](../entities/watcher_count.md) read these
states, so they can react when a door opens or the last monster dies without those entities having to trigger
anything. The **Master** key doesn't read states: it asks the master entity, and an entity that can't be a master
lets everything through.

| Entity | On | Off | Turn On | Turn Off | In Use |
|---|---|---|---|---|---|
| Doors (`func_door`, `func_door_rotating`, `func_water`) | Open | Closed | Opening | Closing | |
| `momentary_door` | Open, even a little, and standing | Closed | Moving open | Moving closed | |
| Buttons (`func_button`, `func_rot_button`) | Pressed in | Out | Going in | Coming back | |
| `momentary_rot_button` | Turned away from its start | At its start | | Turning back by itself | A player turns it |
| Plats (`func_plat`, `func_platrot`, `func_trackchange`, `func_trackautochange`) | At the top | At the bottom | Going up | Going down | |
| Trains (`func_train`, `env_spritetrain`, `env_modeltrain`) | Moving | Standing, also while waiting at a corner | | | |
| `func_guntarget` | On its way, also while waiting at a corner | Stopped: not started yet, triggered off, shot down or at the end of its path | | | |
| `func_tracktrain` | Moving at any speed | Standing | | | |
| `func_rotating` | Turning | Standing | Speeding up | Slowing down | |
| `func_pendulum` | Swinging | Standing | | Swinging back to its start to stop | |
| `func_wall` | Showing its second texture | Showing its first texture | | | |
| `func_wall_toggle`, `func_illusionary_toggle` | There | Gone | | | |
| `func_breakable`, `func_pushable` | Whole | Broken | | | |
| `light`, `light_spot` | Lit | Switched off | | | |
| Tanks (`func_tank` and the others) | Active, aiming by itself | Inactive | | | A player controls it |
| `func_tankcontrols` | A player uses them | Not in use | | | |
| `func_recharge` | Has charge left | Empty | | | Charging a player |
| Triggers (`trigger_multiple`, `trigger_once`, `trigger_hurt`, `trigger_push` and the others) | A touch would set it off | Switched off, or waiting after it fired | | | |
| `trigger_inout` | Something it counts is inside | Empty | | | |
| `multi_manager` | Firing its targets | Waiting to be triggered | | | |
| `scripted_sequence`, `aiscripted_sequence`, `scripted_action` | Its monster plays the action | Idle | Its monster goes to it or waits there | It lets go of its monster | |
| `scripted_sentence` | Its speaker says the sentence | Otherwise | | | |
| `scripted_tanksequence` | Running | Otherwise | | | |
| Monsters | Alive | Dead | | Dying | |
| Players | Alive | Dead, spectating or Game Master | | | |
| `monster_target` | Active | Inactive | | | |
| `env_state` | On | Off | Turning on | Turning off | |
| Masters (`multisource`, `calc_state`, `trigger_compare`, `env_global` with **Act as Master**, `player_hasweapon`, `player_hasinventory`, `game_team_master`, `multi_watcher`, `watcher_count`) | It passes | It locks | | | |
| Effects (`env_beam`, `env_laser`, `env_sprite`, `env_bubbles`, `env_spark`, `env_model`, `env_beamtrail`, `env_dlight`, `env_elight`, `env_mirror`, `env_fog`, `env_rain`, `env_snow`) | On | Off | | | |
| `env_beverage` | Has cans left | Empty | | | |
| Every other entity | | Always | | | |

A door with **Starts Open** is On while it is open, like any other door. A `func_breakable` loses its name at the
moment it breaks, so a watcher doesn't find it after that.

## `multi_watcher` [[ported:spirit]]

A [`multi_watcher`](../entities/multi_watcher.md) watches up to 64 entities, which you add as extra keys like the
targets of a [`multi_manager`](../entities/multi_manager.md), and combines their states with one of these tests: All
(AND), At least one (OR), Not all (NAND), None (NOR), Exactly one (XOR) or Any number but one (XNOR).

As a master, it is on while the result is true. If it has an **Entity to notify**, it checks the result every 0.1
seconds and fires that entity with On or Off when the result changes. With the flag **Send 'Toggle'** it sends Toggle
instead, and the flags **Don't send On** and **Don't send Off** stop one of the two. By default, only the state On
counts as true, and the other flags make Off, Turn On, Turn Off or In Use count, or stop On from counting.

## `watcher_count` [[ported:spirit]]

A [`watcher_count`](../entities/watcher_count.md) counts the entities with one name whose state isn't Off and
compares the count with a number. As a master, it is on while the comparison is true. It fires targets when the
count goes up or down, and when the comparison becomes true or false.

## Changes since 1.38

- `env_state`, `calc_state`, `trigger_compare` and `trigger_inout` are new
- Inverted masters with `~` and `env_global` as a master are new
- `multi_watcher` and `watcher_count`: watch other entities, for example whether a door is open, a monster is alive
  or a light is on, and fire their targets when that changes. They can also be used as a Master

## See also

- [Masters and multisource](../../guides/masters.md) - a guide with small setups
- [Locus system](locus.md) - keys that ask another entity for a value
- [Trigger modes](trigger-modes.md) - the use types On, Off, Toggle and Set
- [Round hooks](round-hooks.md) - putting states back at each round start
