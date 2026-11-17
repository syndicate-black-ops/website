---
description: "A game_player_settings changes the player who triggers it: their weapons, ammo, health, armor, Co-op level and XP."
---
A `game_player_settings` changes the player who triggers it: it gives or takes weapons and ammo, sets their health,
maximum health and armor, and changes their Co-op level and XP, and then it fires its target. It only works for an
alive player, and for anyone else it changes nothing and fires nothing.

## Attributes

- **Name** (`targetname`) - Triggering the entity changes the player who started the chain of triggers. See
  [Common keys](common-keys.md#targetname)
- **Fire on equip** (`target`) - Names the entities to trigger after the change, and passes on the player as the
  [activator](../guide/entity-triggering.md#target-selectors)
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing
- **Set health** (`health`) - Sets the player's health to this value when it is above 0. A value can also start
  with a sign: see [Values with a sign](#values-with-a-sign) for more details
- **Allow OverHeal** (`allow_overheal`) - Sets whether the health can go above the maximum health
    - No (0) - The health this entity sets stays at most the maximum health
    - Yes (1) - The health can go above the maximum health, and a lower maximum doesn't cut it
- **Set max health** (`max_health`) - Sets the maximum health, with the same signs
- **Set armor** (`armorvalue`) - Sets the armor, with the same signs
- **Allow armor above 100** (`allow_overcharge`) - Sets whether the armor can go above 100
    - No (0) - The armor this entity sets stays at most 100
    - Yes (1) - The armor can go above 100
- **Long jump** (`longjump`) - Gives or takes the long jump module, which makes the player jump far when they jump
  while they duck
    - Remove (-1) - Takes the module away
    - No change (0) - Changes nothing
    - Give (1) - Gives the module
- **Set Co-op level** (`level`) - Sets the Co-op level of the player, with the same signs: `=5` sets 5, `+2` adds two
  levels, `-2` takes two away, `<10` makes it at most 10 and `>0` at least 0. A value with no sign is set, 0 too,
  but a value that starts with `-` takes levels away, so to set a negative level, write `=-3`. Each level gained
  works like a normal level-up, with more speed and more health at spawn. Each level taken works the other way, like
  the penalty for killing a teammate, and the scoreboard shows the change at once
- **Set Co-op XP** (`xp`) - Sets the XP toward the next level, with the same signs. Each full 5000 XP is a level-up
  and the rest stays, so `+12000` at 0 XP gives two levels and 2000 XP. Taking XP stops at 0 and never takes a level away

The ammo keys, such as **Hand grenades** or **K444 ammo**, give the player that much ammo, up to the most the player
can carry, and a negative value takes ammo away. The weapon keys, such as **weapon_ben**, give or take a weapon.

## Values with a sign

A value of **Set health**, **Set max health**, **Set armor**, **Set Co-op level** or **Set Co-op XP** can start with
one of these signs:

- `=` - Sets the value
- `+` - Adds to the value
- `-` - Takes away from the value
- `<` - Sets the value if the current one is higher
- `>` - Sets the value if the current one is lower

## Notes

- Taking health with `-` can kill the player, but setting the health never does, because the lowest result is 1
- When the weapon in the player's hands is taken away, they switch to their best other weapon
- Only the game's own weapons and ammo work, and with `developer 1` set in the console, the server console reports any
  other weapon name
- The long jump module is lost when the player respawns

## See also

- [`game_player_equip`](game_player_equip.md) - gives weapons and items to players
- [`player_weaponstrip`](player_weaponstrip.md) - takes the weapons of a player away
- [`player_hasweapon`](player_hasweapon.md) - checks whether a player has a weapon

## Changes since 1.38

- `game_player_settings` is new in SBO 2.0.0
- New in SBO 2.1.0: the keys **Set Co-op level** and **Set Co-op XP**
