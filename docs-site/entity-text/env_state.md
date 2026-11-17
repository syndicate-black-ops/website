An `env_state` has an on and an off state, and it can take a set time to turn on and to turn off. It is a
[master](../guide/masters-and-states.md#masters) that is only on while the state is on, not while it is turning on or
off.

A trigger with the [use type](../guide/trigger-modes.md) On turns it on, Off turns it off and Toggle switches it,
but On does nothing when it is already on, and Off does nothing when it is already off. If you trigger it with
Toggle while it is still turning on or off, it turns back the other way.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's **Master** key, and triggering the entity by
  this name changes its state. See [Common keys](common-keys.md#targetname)
- **Fire on state change** (`target`) - Names the entities to trigger with the use type On when the entity turns on, and with Off
  when it turns off. Targets fired at once get the
  [activator](../guide/entity-triggering.md#target-selectors) of the trigger, and targets fired after a turn-on or
  turn-off time get the `env_state` as the activator
- **Fire when turned on** (`noise1`) - Names the entities to trigger with the use type Toggle when the entity turns on
- **Fire when turned off** (`noise2`) - Names the entities to trigger with the use type Toggle when the entity turns off
- **Time taken to turn on** (`turnontime`) - Sets how many seconds pass between the trigger and the state On, and as
  a master, the entity stays off until the time is over. With 0, it turns on at once
- **Time taken to turn off** (`turnofftime`) - Sets how many seconds pass between the trigger and the state Off, and
  as a master, the entity is off for the whole time. With 0, it turns off at once
- **Master** (`master`) - Names a master, and while that master is off, the entity ignores every trigger
- **Reset at round start** (`round_reset`) - Sets whether the entity goes back to its state of the map start at each
  new round of Co-op, Battle Royale and Bounty Killer, before the players spawn
    - No (0) - The entity keeps its state
    - Yes (1) - The entity goes back to its state of the map start, a turn on or off that hasn't happened yet is
      dropped, and nothing is fired

## Flags

- **Start On** (1) - The state is on when the map starts
- **Debug Mode** (2) - With `developer 1` set in the console, the console shows each change of the state and each
  trigger the entity ignores

## Notes

- While the entity is turning on, it counts as on for triggers: On does nothing and Off turns the change around.
  While it is turning off, it counts as off: Off does nothing and On turns the change around
- You can change both fire targets with [`trigger_changevalue`](trigger_changevalue.md) or
  [`trigger_copyvalue`](trigger_copyvalue.md) while the map runs. See [Changing keys](../guide/changing-keys.md)

## See also

- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [`calc_state`](calc_state.md) - combines two masters with a logic operation
- [`env_global`](env_global.md) - a state that every entity can read by its name
- [`multisource`](multisource.md) - a master that is on while all of its inputs are on

## Changes since 1.38

- `env_state` is new in SBO 2.0.0
- Changed in SBO 2.1.0: while it is turning on, On does nothing and Off turns it back. In SBO 2.0.0, On turned it
  back and Off did nothing, because only a finished turn-on counted as on
