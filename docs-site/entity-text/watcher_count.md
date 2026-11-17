---
description: "A watcher_count counts how many entities with one name aren't off and compares the count with a number, and it is a master."
---
A `watcher_count` counts how many entities with one name aren't off, such as how many monsters are still alive or how
many doors are open, and compares the count with a number. It is a [master](../guide/masters-and-states.md#masters)
that is on while the comparison is true, and it fires targets when the count goes up or down and when the comparison
turns true or false.

An entity counts while its [state](../guide/masters-and-states.md#entity-states) is anything but Off, so a monster
counts while it is alive or dying and a door while it is open, opening or closing. Entities without a state of their
own, such as an [`info_target`](info_target.md), are always off and never count. The entity checks the count every 0.1
seconds, starting half a second after it spawns.

## Attributes

- **Name** (`targetname`) - The name you put in another entity's **Master** key. See
  [Common keys](common-keys.md#targetname)
- **Count entities named...** (`noise`) - Sets the name of the entities to count
- **Comparison number** (`impulse`) - Sets the number the count is compared with
- **Type of comparison** (`m_iMode`) - Sets when the comparison is true
    - 'On' when count = number (0) - True when the count equals the number
    - 'On' when count != number (3) - True when the count is anything but the number
    - 'On' when count > number (1) - True when the count is more than the number
    - 'On' when count >= number (5) - True when the count is the number or more
    - 'On' when count < number (2) - True when the count is less than the number
    - 'On' when count <= number (4) - True when the count is the number or less
- **Fire on changing state** (`target`) - The entity fires this with the [use type](../guide/trigger-modes.md) On
  when the comparison turns true, and with Off when it turns false
- **Fire on turning on** (`netname`) - The entity fires this with Toggle when the comparison turns true
- **Fire on turning off** (`message`) - The entity fires this with Toggle when the comparison turns false
- **Fire when count increases** (`noise1`) - The entity fires this with Toggle each time the count goes up
- **Fire when count decreases** (`noise2`) - The entity fires this with Toggle each time the count goes down

## Flags

- **Fire at startup** (1) - At its first check, the entity fires **Fire on turning on** if the comparison is true,
  and **Fire on turning off** if it is false

## Notes

- At its first check, the entity only notes the count and fires nothing, unless **Fire at startup** is set
- The targets get the `watcher_count` as their [activator](../guide/entity-triggering.md#target-selectors)
- A broken [`func_breakable`](func_breakable.md) loses its name at once, so it stops counting as soon as it breaks
- A dead monster stops counting once its death animation ends, and a player counts only while alive

## See also

- [Masters and states](../guide/masters-and-states.md) - every master, and the states of each entity
- [`multi_watcher`](multi_watcher.md) - combines the states of several entities with AND, OR and other tests
- [`game_counter`](game_counter.md) - counts triggers instead of entities

## Changes since 1.38

- `watcher_count` is new in SBO 2.1.0
