A `func_button` moves in and fires its targets when a player uses it, shoots it or touches it, and then comes back
out. While it is pressed, it shows its alternate textures, the `+a` frames.

## Attributes

- **Name** (`targetname`) - Triggering the entity presses it like a player does, but not with the flag **Touch
  Activates**. See [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger when the button is pressed, with the use type that **Use type** sets, and
  passes on the player who pressed it as the [activator](../guide/entity-triggering.md#target-selectors)
- **Speed** (`speed`) - Sets how fast the button moves, in units per second, and 0 means 40
- **Health** (`health`) - Sets whether players shoot the button instead of using it. Above 0, any damage presses
  it, and players can't press it with their use key
- **Lip** (`lip`) - Sets how many units of the button stay out when it is pressed in, and 0 means 4
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  the button is locked and plays its locked sound
- **Sounds** (`sounds`) - Picks the sound the button plays when it is pressed
    - None (0)
    - Big zap & Warmup (1)
    - Access Denied (2)
    - Access Granted (3)
    - Quick Combolock (4)
    - Power Deadbolt 1 (5)
    - Power Deadbolt 2 (6)
    - Plunger (7)
    - Small zap (8)
    - Keycard Sound (9)
    - Buzz (10)
    - Buzz Off (11)
    - Lightswitch (14)
- **Delay before reset** (`wait`) - Sets how many seconds the button stays pressed before it comes back out and can be
  pressed again, and -1 keeps it pressed for good. With 0, it waits 1 second
- **Delay before trigger** (`delay`) - Sets how many seconds pass between the press and the firing of its targets
- **Trigger before move** (`trigger_before_move`) - Names the entities to trigger when the button starts to move in
- **Trigger on return** (`trigger_on_return`) - Names the entities to trigger when the button is back out
- **Target when locked** (`target_on_locked`) - Names the entities to trigger when a player uses it while its master keeps
  it locked, at most every 2 seconds
- **Use type** (`usetype`) - Sets the [use type](../guide/trigger-modes.md) its **Target** gets
    - Off (-1) - The **Target** gets Off
    - Toggle (0) - The **Target** gets Toggle
    - On (1) - The **Target** gets On
    - On/Off (2) - With **Toggle**, On when the button goes in and Off when it comes out
    - Off/On (3) - With **Toggle**, Off when the button goes in and On when it comes out
- **Wait before toggling again** (`wait_toggle`) - With **Toggle**, sets how many seconds pass before players can
  use the button again
- **Custom sound** (`noise`) - Sets a sound file that the button plays instead of the **Sounds** choice
- **Player use policy** (`directuse`) - Sets how a player must look at the button to use it
    - Default (0) - As for any object
    - Direct only (1) - The player must look straight at the button
    - Not through walls (2) - The player can't use the button through a wall

## Flags

- **Don't move** (1) - The button doesn't move when it is pressed
- **Toggle** (32) - The button stays pressed until it is used again, which brings it back out, and it fires its
  targets each time
- **Sparks** (64) - The button gives off sparks while it isn't pressed
- **Touch Activates** (256) - Players press the button by walking into it, not with their use key, and triggering
  the button does nothing
- **Player Can't Use** (16384) - Players can't press the button with their use key, but shooting it, touching it and
  triggers still work

## Notes

- A [`scripted_sentence`](scripted_sentence.md) can make the button speak, and the sentence then plays from the
  button
- Each player can turn the object hints off, or keep only the hint on what their use key would use, with the client
  setting [`cl_objecthint`](../../playing/options.md#player-cvars)

## See also

- [`func_rot_button`](func_rot_button.md) - a button that turns
- [`button_target`](button_target.md) - a button that players shoot
- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [func_button on TWHL](https://twhl.info/wiki/page/func_button) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Object Hint Template**, **Hint Distance**, **Trigger before move**, **Trigger on
  return**, **Target when locked**, **Use type**, **Wait before toggling again**, **Custom sound**, **Player use
  policy** and the custom locked and unlocked sounds and sentences, and the new flag **Player Can't Use**
- A [`scripted_sentence`](scripted_sentence.md) can make a button speak, as in the Half-Life 25th Anniversary
  Update. In SBO 1.38, only monsters spoke
