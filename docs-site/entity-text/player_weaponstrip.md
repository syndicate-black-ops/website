A `player_weaponstrip` takes every weapon, all ammo and every inventory item away from the player who triggers it.
Items that came from an [`item_pickup`](item_pickup.md) go back to their place, unless the pickup has **Keep on
death**.

## See also

- [`game_player_equip`](game_player_equip.md) - gives players weapons
- [`player_hasweapon`](player_hasweapon.md) - checks whether a player has a weapon
- [player_weaponstrip on TWHL](https://twhl.info/wiki/page/player_weaponstrip) - the Half-Life entity

## Changes since 1.38

- Fixed the sniper zoom and the slow zoom walk staying on after you lose your weapons while zoomed. Losing your
  weapons did not reset the zoom or the speed. Only taking out your next weapon did. This was a bug in SBO 1.38
- Fixed the chainsaw's engine sound playing on after you die or lose the chainsaw. The chainsaw's own put-away step
  never ran, so only taking out another weapon stopped the sound. This was a bug in SBO 1.38
