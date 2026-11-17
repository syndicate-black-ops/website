A `button_target` switches on or off when a player shoots it, and fires its **Target** each time.

While it is off, its brush shows the textures whose names start with `+0` to `+9`, and while it is on, it shows the
alternate textures whose names start with `+a` to `+j`.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches it like a shot does, and the
  [use types](../guide/trigger-modes.md) On and Off only switch it on or off. See
  [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger with the use type On when it switches on, and with Off when it
  switches off. Whoever shot or used it is passed on as the
  [activator](../guide/entity-triggering.md#target-selectors)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters). While the master is off,
  shooting, using and triggering the entity can't switch it on, but they can still switch it off

## Flags

- **Use Activates** (1) - Players can also switch it with their use key. This flag is set by default
- **Start On** (2) - The entity starts switched on and shows its alternate texture

## Notes

- Any damage switches it, so each bullet or explosion that hits it switches it again

## See also

- [`func_button`](func_button.md) - a button that moves when you press it
- [`func_rot_button`](func_rot_button.md) - a button that turns when you press it
- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity

## Changes since 1.38

- The **Master** key works. In SBO 1.38, a locked `button_target` still switched on, because SBO 1.38 never read
  the Master key that the editor offered
