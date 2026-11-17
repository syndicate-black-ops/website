A `multisource` is a [master](../guide/masters-and-states.md) that is on while every entity that targets it has
switched its input on. See the [Masters and multisource](../../guides/masters.md) guide for small setups that use its
inputs.

## Attributes

- **Target** (`target`) - Fires when every input is on, without an activator, so `!activator` finds nothing in what it
  triggers
- **Global State Master** (`globalstate`) - Names a global state that an [`env_global`](env_global.md) sets, and the
  multisource is only on while that state is On as well as all its inputs

## Notes

- Its inputs are the entities whose **Target** is its name, up to 32, and a
  [`multi_manager`](multi_manager.md) that lists it counts too
- Every trigger from an input flips that input, whether it is On, Off or Toggle
- An input with a **Delay before trigger** flips its own input when the delay is over
- An entity that triggers it without targeting it flips the input of the last entity that targets it, as in
  Half-Life

## See also

- [Masters and multisource](../../guides/masters.md) - a guide with small setups
- [`env_state`](env_state.md) and [`calc_state`](calc_state.md) - other masters
- [multisource on TWHL](https://twhl.info/wiki/page/multisource) - the Half-Life entity

## Changes since 1.38

- Fixed a `multisource` with a Delay before trigger flipping the wrong input. The delayed trigger was not one of its
  inputs, so it flipped the last one. This was a bug in SBO 1.38
