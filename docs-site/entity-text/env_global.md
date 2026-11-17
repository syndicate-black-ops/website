An `env_global` sets a global state each time you trigger it. A global state is a named state, On, Off or Dead, that
belongs to no single entity, and it also holds a number that you can change and read. A
[`multisource`](multisource.md) with that name in its **Global State Master** turns on only while the state is On.

## Attributes

- **Name** (`targetname`) - Triggering the entity changes the global state, as **Trigger Mode** says. With **Act as
  Master**, other entities can also use this name as their **Master**. See [Common keys](common-keys.md#targetname)
- **Global State to Set** (`globalstate`) - Sets the name of the global state this entity changes.
  `multisource` entities and other `env_global` entities find the state by this name
    - If you leave this key empty, the entity removes itself when the map starts
- **Trigger Mode** (`triggermode`) - Sets what each trigger does to the global state
    - Off (0) - Sets the state to Off
    - On (1) - Sets the state to On
    - Dead (2) - Sets the state to Dead
    - Toggle (3) - Switches the state from On to Off or from Off to On, and a Dead state stays Dead
    - Modify / Set value (4) - Changes the number of the state instead of the state: a trigger with the
      [use type](../guide/trigger-modes.md) On or Toggle adds 1, Off takes 1 away, and Set puts in the number the
      trigger brings
    - Set state: obey use type (5) - The use type of the trigger decides: On sets the state to On, Off sets it to
      Off, and any other use type works like Toggle
- **Initial State** (`initialstate`) - Sets the state the global state starts with when this entity creates it,
  which happens at the map start with **Set Initial State**, or at the first trigger with the trigger mode
  "Modify / Set value"
    - Off (0)
    - On (1)
    - Dead (2)
- **Initial Value** (`initialvalue`) - Sets the number the global state starts with when this entity creates it.
  Keys that take a [locus number](../guide/locus.md) can name this entity to read the number

## Flags

- **Set Initial State** (1) - At the map start, the global state is created with **Initial State** and **Initial
  Value**, unless it already exists
- **Act as Master** (4) - The `env_global` is a [master](../guide/masters-and-states.md#masters) itself, which is
  on while the global state is On, and off while the state is Off, Dead or not set yet. Other entities must name the
  `env_global` in their **Master** key, not the global state

## Notes

- Each map starts with no global states, so a state set on one map doesn't carry over to the next map, or to the
  next time the same map is played
- A key that reads the number gets nothing while the global state doesn't exist yet
- An entity that spawns while the map runs, and whose **Global Entity Name** is the name of a Dead global state, is
  removed at once

## See also

- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [`env_state`](env_state.md) - an on or off state that you switch with triggers
- [`calc_state`](calc_state.md) - combines two masters with a logic operation
- [`multisource`](multisource.md) - a master that is on while all of its inputs are on

## Changes since 1.38

- You can use the new key **Initial Value**, the new trigger modes "Modify / Set value" and "Set state: obey use
  type", and the new flag **Act as Master**
- Each map starts with no global states. In SBO 1.38, a state stayed set when the server changed maps, which could
  keep an entity removed when a map came back
