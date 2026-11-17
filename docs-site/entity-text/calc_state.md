---
description: "A calc_state combines the states of two masters with a logic operation such as AND or OR, and is a master itself."
---
A `calc_state` combines the states of two [masters](../guide/masters-and-states.md#masters) with a logic operation
such as AND or OR. It is a master itself, and it is on while the result is true.

Every time an entity checks whether its **Master** lets it work, a `calc_state` it names checks both of its
operands again at that moment. When you trigger the `calc_state`, it also works out the result and fires its
targets.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's **Master** key, and triggering the entity by
  this name works out the result and fires its targets. See [Common keys](common-keys.md#targetname)
- **Operand 1** (`left_operand`) - Names the first master, such as an [`env_state`](env_state.md), a
  [`multisource`](multisource.md) or another `calc_state`. With `!activator`, `*locus` or `*player`, it uses the
  entity that started the chain of triggers. A `~` in front of the name doesn't turn the state around, so use NAND or NOR for
  that
    - If you leave this key empty, the entity has no result
- **Operand 2** (`right_operand`) - Names the second master, in the same way as **Operand 1**
    - If you leave this key empty, the entity has no result
- **Operation** (`operation`) - Picks how the two states give the result
    - AND (0) - True when both operands are on
    - OR (1) - True when at least one operand is on
    - NAND (2) - True unless both operands are on
    - NOR (3) - True when both operands are off
    - XOR (4) - True when one operand is on and the other is off
    - NXOR (5) - True when both operands are on or both are off
- **Operand 1 missing** (`left_fallback`) - Sets what counts as the state of **Operand 1** when no entity has that
  name
    - Treat as error (0) - There is no result, so the master is off and the entity fires nothing
    - Treat as Off (1) - The operand counts as off
    - Treat as On (2) - The operand counts as on
- **Operand 2 missing** (`right_fallback`) - Sets what counts as the state of **Operand 2** when no entity has that
  name
    - Treat as error (0) - There is no result, so the master is off and the entity fires nothing
    - Treat as Off (1) - The operand counts as off
    - Treat as On (2) - The operand counts as on
- **Target when triggered** (`target`) - Names the entities to trigger when you trigger the entity, with the
  [use type](../guide/trigger-modes.md) On if the result is true and with Off if it is false
- **Fire when false** (`fire_when_false`) - Names the entities to trigger when you trigger the entity and the result
  is false
- **Fire when true** (`fire_when_true`) - Names the entities to trigger when you trigger the entity and the result
  is true

## Flags

- **Debug Mode** (2) - When you trigger the entity, the console shows the state of each operand and the result, if
  `developer 1` is set in the console

## Notes

- An operand that names an entity which isn't a master counts as on
- If the entity has no result, the master is off and the entity fires none of its targets, and with `developer 1` set
  in the console, the console reports why
- If `calc_state` entities use each other as operands in a loop, the check stops after 32 steps and the result is
  false, and with `developer 1` set in the console, the console reports it

## See also

- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [Masters guide](../../guides/masters.md) - setups with masters and states
- [`env_state`](env_state.md) - an on or off state that you switch with triggers
- [`multisource`](multisource.md) - a master that is on while all of its inputs are on
- [`trigger_compare`](trigger_compare.md) - a master that compares two numbers

## Changes since 1.38

- `calc_state` is new in SBO 2.0.0
