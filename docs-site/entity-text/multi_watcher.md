---
description: "A multi_watcher watches the states of other entities and combines them into one true or false result, and it is a master."
---
A `multi_watcher` watches the states of other entities, such as a door being open or a monster being alive, and
combines them into one true or false result with a logical test like AND or OR. It is a
[master](../guide/masters-and-states.md#masters) that is on while the result is true, and it can fire a target
whenever the result changes.

Each entity has one of five states, On, Off, Turn On, Turn Off and In Use, so a door is On while it is open and Turn
On while it is opening. By default only On counts as true, and the flags choose other states that count. See [Entity
states](../guide/masters-and-states.md#entity-states) for what the states mean for each entity.

You list the entities to watch the way you list a [`multi_manager`](multi_manager.md)'s targets: turn SmartEdit off
and add one key per entity, with the entity's name as the key and any value, such as `0`. For a second key with the
same name, add `#2` to the name, like `door1#2`.

## Attributes

- **Name** (`targetname`) - The name you put in another entity's **Master** key. See
  [Common keys](common-keys.md#targetname)
- **Entity to watch** (`m_iszWatch`) - Names one more entity to watch, besides the extra keys
- **Logical test** (`m_fLogic`) - Picks how the watched entities give the result
    - All (AND) (0) - True when every watched entity is in a state that counts
    - Not all (NAND) (2) - True unless every watched entity is in a state that counts
    - At least one (OR) (1) - True when one or more of them is in a state that counts
    - None (NOR) (3) - True when none of them is in a state that counts
    - Exactly one (XOR) (4) - True when exactly one of them is in a state that counts
    - Any number but one (XNOR) (5) - True when none, or two or more, of them are in a state that counts
- **Entity to notify** (`target`) - The entity checks its test every 0.1 seconds, starting half a second after
  the map starts, and fires this with the [use type](../guide/trigger-modes.md) On when the result turns true and
  with Off when it turns false. Without a name here, the entity doesn't check by itself, but it still works as a
  master

## Flags

- **Send 'Toggle'** (1) - The entity fires **Entity to notify** with Toggle instead of On and Off
- **Don't send On** (2) - The entity doesn't fire **Entity to notify** when the result turns true
- **Don't send Off** (4) - The entity doesn't fire **Entity to notify** when the result turns false
- **NOT 'On'** (8) - The state On doesn't count as true
- **'Off'** (16) - The state Off counts as true
- **'Turn On'** (32) - The state Turn On counts as true, such as a door that is opening
- **'Turn Off'** (64) - The state Turn Off counts as true, such as a door that is closing or a monster that is dying
- **'In Use'** (128) - The state In Use counts as true, such as a charger that a player is using

## Notes

- The result starts as false, so if the test is already true at the first check, the entity fires On
- A name that matches no entity isn't part of the test, so a watched entity that was removed doesn't count either
  way, and AND of only missing entities is true
- If several entities share a name, the entity reads only the first one
- It watches up to 64 entities and leaves out every key after that. With `developer 1` set in the console, the
  console names each key it leaves out
- A name can be [`!activator` or `*player`](../guide/locus.md#entity-names-in-a-locus-key), which works when the
  entity is asked as a master: it then means the player who uses the locked entity
- If watchers watch each other in a loop, the check stops 32 levels deep, the result is false, and with `developer 1`
  set in the console, the console reports it

## See also

- [Masters and states](../guide/masters-and-states.md) - every master, and the states of each entity
- [`watcher_count`](watcher_count.md) - counts how many entities of one name aren't off
- [`calc_state`](calc_state.md) - combines two masters, and can use a `multi_watcher` as one of them
- [`env_state`](env_state.md) - an on or off state that you switch with triggers

## Changes since 1.38

- `multi_watcher` is new in SBO 2.1.0
