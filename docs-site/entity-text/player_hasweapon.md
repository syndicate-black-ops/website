A `player_hasweapon` checks whether the player who triggered it has a weapon, and fires **Pass Target** if they have
it and **Fail Target** if they don't. As the [master](../guide/masters-and-states.md) of another entity, such as a
[`trigger_multiple`](trigger_multiple.md), a button or a door, it is on while the activator has the weapon.

## Attributes

- **Weapon classname** (`weapon_name`) - Names the weapon by its class name, such as `weapon_sword` or `weapon_rpg`
    - If you leave this key empty, any weapon counts, the fists too
- **Pass Target** (`pass_target`) - Fires this target if the player has the weapon, with that player as the activator
- **Fail Target** (`fail_target`) - Fires this target if the player doesn't have the weapon, with that player as the
  activator

## Notes

- It only checks an alive player. For anyone else it fires nothing, and as a master it is off

## See also

- [`player_hasinventory`](player_hasinventory.md) - the same check for an inventory item
- [`player_weaponstrip`](player_weaponstrip.md) - takes weapons away
- [Masters and states](../guide/masters-and-states.md) - entities that lock others

## Changes since 1.38

- `player_hasweapon` is new
