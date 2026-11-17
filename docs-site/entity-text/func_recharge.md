---
description: "A func_recharge is a wall charger that gives armor to a player who holds their use key on it."
---
A `func_recharge` is a wall charger that gives armor to a player who holds their use key on it, until it is empty, and
it fills up again after a while.

## Notes

- With the **charger** template of **Object Hint Template**, the brackets turn green when a player's use key would
  use the charger, or red if the charger is empty
- Each player can turn the object hints off, or keep only the hint on what their use key would use, with the client
  setting [`cl_objecthint`](../../playing/options.md#player-cvars)

## See also

- [`item_battery`](item_battery.md) - a battery that gives armor
- [func_recharge on TWHL](https://twhl.info/wiki/page/func_recharge) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Object Hint Template** and **Hint Distance**, the three **Trigger On** keys, the custom
  sounds and **Custom Juice Amount**
