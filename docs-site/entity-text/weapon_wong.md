A `weapon_wong` gives a player who walks onto it Fists. It fires its **Target** when a player takes it, and it doesn't
come back after that. It has no world model, so nothing shows on the floor, and players find it only by walking over
its spot. Every player already gets fists at every spawn, also on a map with a
[`game_player_equip`](game_player_equip.md).

## Notes

- Only living players pick it up
- A player who already has it leaves it on the floor
- It falls to the floor when the map starts and lies flat there

## See also

- [`game_player_equip`](game_player_equip.md) - gives weapons to players
- [`player_hasweapon`](player_hasweapon.md) - checks whether a player carries a weapon
- [`player_weaponstrip`](player_weaponstrip.md) - takes weapons away
