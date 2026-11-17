A `weapon_satchel` gives a player who walks onto it a satchel charge, which players set down and set off from a
distance. It fires its **Target** when a player takes it, and it doesn't come back after that. Its world model is the
weapon box.

## Notes

- Only living players pick it up
- A player who already has this weapon takes only its ammo. A player who also has full ammo leaves it on the floor
- It falls to the floor when the map starts and lies flat there

## See also

- [`game_player_equip`](game_player_equip.md) - gives weapons to players
- [`player_hasweapon`](player_hasweapon.md) - checks whether a player carries a weapon
- [`player_weaponstrip`](player_weaponstrip.md) - takes weapons away
