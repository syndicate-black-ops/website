A `func_rot_button` turns around its origin, set with an origin brush, when a player uses it, shoots it or touches it,
and fires its targets. It turns back after its delay.

While its master keeps it locked, a use plays **Locked Sound** and **Locked Sentence**, and once it is unlocked, a use
plays **Unlocked Sound** and **Unlocked Sentence**.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns it like a player does, but not with the flag **Touch
  Activates**. See [Common keys](common-keys.md#targetname)
- **Targeted object** (`target`) - Names the entities to trigger when the button is used, or when it turns back with **Toggle**,
  with the use type that **Use type** sets
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  the button is locked, so a use plays its locked sound and fires nothing
- **Speed** (`speed`) - Sets how fast the button turns, in degrees per second, and 0 means 40
- **Health** (`health`) - Sets whether players shoot the button instead of using it. Above 0, any damage turns it,
  and players can't use it with their use key
- **Sounds** (`sounds`) - Picks the sound the button plays when it is pressed
    - Squeaky (21)
    - Squeaky Pneumatic (22)
    - Ratchet Groan (23)
    - Clean Ratchet (24)
    - Gas Clunk (25)
    - If you leave this key empty, the button plays no sound
- **Delay before reset** (`wait`) - Sets how many seconds the button stays turned before it turns back and can be used
  again, and 0 means 1 second
    - Stays pressed (-1) - The button stays turned for good
- **Delay before trigger** (`delay`) - Sets how many seconds pass between the use and the firing of **Targeted
  object**
- **Distance** (`distance`) - Sets how far the button turns, in degrees
    - If you leave this key empty or set 0, it doesn't turn, but it still fires its targets
- **Trigger before move** (`trigger_before_move`) - Names the entities to trigger when the button starts to turn
- **Trigger on return** (`trigger_on_return`) - Names the entities to trigger when the button is back where it started
- **Target when locked** (`target_on_locked`) - Names the entities to trigger when a player uses it while its master keeps
  it locked, at most every 2 seconds
- **Use type** (`usetype`) - Sets the [use type](../guide/trigger-modes.md) that **Targeted object** gets
    - Off (-1) - **Targeted object** gets Off
    - Toggle (0) - **Targeted object** gets Toggle
    - On (1) - **Targeted object** gets On
    - On/Off (2) - With **Toggle**, On when the button turns and Off when it turns back
    - Off/On (3) - With **Toggle**, Off when the button turns and On when it turns back
- **Wait before toggling again** (`wait_toggle`) - With **Toggle**, sets how many seconds pass before players can
  use the button again
- **Custom sound** (`noise`) - Sets a sound file that the button plays instead of the **Sounds** choice
- **Player use policy** (`directuse`) - Sets how a player must look at the button to use it
    - Default (0) - As for any object
    - Direct only (1) - The player must look straight at the button
    - Not through walls (2) - The player can't use the button through a wall

## Flags

- **Not solid** (1) - Players, monsters and shots pass through the button
- **Reverse Dir** (2) - The button turns the other way
- **Toggle** (32) - The button stays turned after a use, and the next use turns it back, so **Delay before reset**
  isn't used
- **X Axis** (64) - The button turns around the X axis instead of the vertical axis
- **Y Axis** (128) - The button turns around the Y axis instead of the vertical axis
- **Touch Activates** (256) - A player who touches the button turns it, and the use key and triggers do nothing
- **Player Can't Use** (16384) - Players can't press the button with their use key, but shooting it, touching it and
  triggers still work

## Notes

- A [`scripted_sentence`](scripted_sentence.md) can make the button speak, and the sentence then plays from the
  button
- Each player can turn the object hints off, or keep only the hint on what their use key would use, with the client
  setting [`cl_objecthint`](../../playing/options.md#player-cvars)

## See also

- [`func_button`](func_button.md) - a button that moves in
- [`momentary_rot_button`](momentary_rot_button.md) - a button that turns as long as a player holds it
- [func_rot_button on TWHL](https://twhl.info/wiki/page/func_rot_button) - the Half-Life entity

## Changes since 1.38

- You can use the same new keys as on [`func_button`](func_button.md#changes-since-138) and the new flag **Player
  Can't Use**
- A [`scripted_sentence`](scripted_sentence.md) can make a button speak, as in the Half-Life 25th Anniversary
  Update. In SBO 1.38, only monsters spoke
- The button plays its locked and unlocked sounds and sentences. In SBO 1.38, a `func_rot_button` played none of
  them
