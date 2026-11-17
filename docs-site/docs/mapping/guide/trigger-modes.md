---
description: "Every trigger one entity sends to another has a use type (On, Off, Toggle or Set), and with Obey Trigger Mode, doors, trains and triggers follow it instead of switching on every trigger."
---

# Trigger modes

Every trigger one entity sends to another has a use type (On, Off, Toggle or Set), and with **Obey Trigger Mode**,
doors, trains and triggers follow it instead of switching on every trigger. The entity that gets the trigger decides
what the use type means, and many entities treat every use type the same way unless you set that key.

## Use types

| Use type | Number | What it usually means |
|---|---|---|
| Off | 0 | Turn off, close or stop |
| On | 1 | Turn on, open or start |
| Set | 2 | Set a value, which entities such as [`calc_eval_number`](../entities/calc_eval_number.md) and [`game_counter_set`](../entities/game_counter_set.md) send together with a number |
| Toggle | 3 | Switch to the other state |

## What sends which use type

Most entities send Toggle, and the entities below send something else or let you choose:

| Entity | What it sends |
|---|---|
| [`trigger_once`](../entities/trigger_once.md), [`trigger_multiple`](../entities/trigger_multiple.md), [`multi_manager`](../entities/multi_manager.md) | Toggle |
| [`func_button`](../entities/func_button.md), [`func_rot_button`](../entities/func_rot_button.md) | The use type you choose in their key **Use type**, Toggle by default. With the **Toggle** flag, the choices On/Off and Off/On send one use type when the button goes in and the other when it comes back out |
| [`trigger_relay`](../entities/trigger_relay.md), [`trigger_auto`](../entities/trigger_auto.md), [`game_team_master`](../entities/game_team_master.md) | The use type you choose in their key **Trigger State** |
| [`trigger_entity_iterator`](../entities/trigger_entity_iterator.md) | The use type you choose in its key **Trigger state for each entity** |
| [`env_state`](../entities/env_state.md) | On and Off to its **Target**, and Toggle to its other targets |
| [`calc_state`](../entities/calc_state.md) | On to its **Target** when the result is true, and Off when it is false |
| [`trigger_inout`](../entities/trigger_inout.md) | On when something enters and Off when it leaves, to its **Fire on/off** target, and Toggle to its other targets |
| [`multi_watcher`](../entities/multi_watcher.md), [`watcher_count`](../entities/watcher_count.md) | On to their **Target** when their result becomes true, and Off when it becomes false. A `multi_watcher` with the flag **Send 'Toggle'** sends Toggle |
| Doors, platforms and trains | The use type you choose for each of their "Fire On" keys, such as **Fire On Start use type**, Off by default |

### Trigger State

The key **Trigger State** (`triggerstate`) sets the use type an entity sends. Its default in the editor is Off, and
an entity without the key sends Off too, so set it to On or Toggle for the target to switch on.

| Value | What it sends |
|---|---|
| 0 | Off, which is the default |
| 1 | On |
| 2 | Toggle |
| -1 | Copy Input, which is the use type the relay got, and only works on a `trigger_relay` |
| -2 | Reverse Input, which sends On when the relay got Off and Off when it got On, passes Toggle and Set on as they came, and only works on a `trigger_relay` |

## Obey Trigger Mode

Without this key, the entities below treat every use type the same way, so a door opens or closes when you trigger
it with On, Off, Toggle or Set. With **Obey Trigger Mode** (`m_iObeyTriggerMode`) set, they follow the use type
instead:

| Entity | No (0), the default | Yes (1) |
|---|---|---|
| [`func_door`](../entities/func_door.md), [`func_door_rotating`](../entities/func_door_rotating.md), [`func_water`](../entities/func_water.md) | Any trigger opens the door when it is closed, and closes it when it is open and has the **Toggle** flag | On opens the door, Off closes it and Toggle opens or closes it, but only while the door stands still |
| [`func_train`](../entities/func_train.md), [`env_modeltrain`](../entities/env_modeltrain.md), [`env_spritetrain`](../entities/env_spritetrain.md) | Any trigger starts or stops the train | On starts it, Off stops it and Toggle switches it |
| [`func_rotating`](../entities/func_rotating.md) | Any trigger starts or stops it | On starts it, Off stops it and Toggle switches it |
| [`trigger_hurt`](../entities/trigger_hurt.md), [`trigger_push`](../entities/trigger_push.md), [`trigger_monsterjump`](../entities/trigger_monsterjump.md) | Any trigger turns it on or off | On turns it on, Off turns it off and Toggle switches it |
| [`monster_apache`](../entities/monster_apache.md) | The first trigger starts it, and later triggers do nothing | On starts it, Off stops it in the air and Toggle switches it |

With **Yes**, an On sent to an entity that is already on, or an Off sent to an entity that is already off, does
nothing. For the trains, `func_rotating` and the triggers in the table, Set works like Toggle.

Doors have a third choice, **Yes, even when currently moving** (2), which also acts while the door is moving:

- Toggle always acts
- On opens a closing door again, and Off closes an opening door if it has the **Toggle** flag, while a door without
  that flag keeps opening
- While the door stands still, On opens it and Off closes it, as with **Yes**

## Changes since 1.38

- **Obey Trigger Mode** is new, because SBO 1.38 ignored the key on every entity, and the
  [compatibility file](../basics/old-maps.md) removes it from the custom maps that had it
- The **Trigger State** choices Copy Input (-1) and Reverse Input (-2) are new
- The **Use type** key of `func_button` and `func_rot_button` is new, and so are the use type keys of the "Fire On"
  keys of doors, platforms and trains

## See also

- [Masters and states](masters-and-states.md) - entities that lock others or hold a state
- [Round hooks](round-hooks.md) - the names the game triggers at round starts and ends
- [`trigger_relay`](../entities/trigger_relay.md) - passes a trigger on with another use type
- [Entity triggering](entity-triggering.md) - target names, wildcards and selectors
