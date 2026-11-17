A `game_player_equip` gives weapons, ammo and items to players, either to every player when they spawn or to the
player who triggers it.

The editor offers a count key for each weapon, and you add ammo and items as keys of your own: the class name, such as
`ammo_rpgclip`, and how many to give.

## Attributes

- **Name** (`targetname`) - Triggering the entity equips the player who started the chain of triggers. See
  [Common keys](common-keys.md#targetname)
- **Team Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is
  off, the entity gives nothing, at spawn or when you trigger it
- **weapon_ben** (`weapon_ben`) - Sets how many of the Benelli the entity gives, and an empty key gives none
- **weapon_canon** (`weapon_canon`) - Sets how many of the Canon of Terror the entity gives, and an empty key gives none
- **weapon_chaingun** (`weapon_chaingun`) - Sets how many of the Vindico Avenger Minigun the entity gives, and an empty key gives none
- **weapon_chainsaw** (`weapon_chainsaw`) - Sets how many of the Chainsaw Sword the entity gives, and an empty key gives none
- **weapon_fa18** (`weapon_fa18`) - Sets how many of the Croon FA 18 the entity gives, and an empty key gives none
- **weapon_federal** (`weapon_federal`) - Sets how many of the Vindico Federal the entity gives, and an empty key gives none
- **weapon_glauncher** (`weapon_glauncher`) - Sets how many of the Vindico grenade launcher the entity gives, and an empty key gives none
- **weapon_handgrenade** (`weapon_handgrenade`) - Sets how many hand grenades the entity gives, and an empty key gives none
- **weapon_k444** (`weapon_k444`) - Sets how many of the .444k Bear Killer the entity gives, and an empty key gives none
- **weapon_medikit** (`weapon_medikit`) - Sets how many of the Medikit the entity gives, and an empty key gives none
- **weapon_nm33** (`weapon_nm33`) - Sets how many of the Croon NM 33 Sniper Rifle the entity gives, and an empty key gives none
- **weapon_pm66** (`weapon_pm66`) - Sets how many of the Croon PM 66 the entity gives, and an empty key gives none
- **weapon_rc28** (`weapon_rc28`) - Sets how many of the Croon RC 28 the entity gives, and an empty key gives none
- **weapon_rpg** (`weapon_rpg`) - Sets how many of the Nuclear RPG the entity gives, and an empty key gives none
- **weapon_satchel** (`weapon_satchel`) - Sets how many satchel charges the entity gives, and an empty key gives none
- **weapon_snark** (`weapon_snark`) - Sets how many Pitbulls the entity gives, and an empty key gives none
- **weapon_spa** (`weapon_spa`) - Sets how many of the Saan Auto-Shotgun the entity gives, and an empty key gives none
- **weapon_sw** (`weapon_sw`) - Sets how many of the Vindico Plasma Sniper Rifle the entity gives, and an empty key gives none
- **weapon_sword** (`weapon_sword`) - Sets how many of the Energy Sword the entity gives, and an empty key gives none
- **weapon_tripmine** (`weapon_tripmine`) - Sets how many tripmines the entity gives, and an empty key gives none
- **weapon_warhammer** (`weapon_warhammer`) - Sets how many of the Fusion warhammer the entity gives, and an empty key gives none
- **weapon_wong** (`weapon_wong`) - Sets how many Fists the entity gives, and an empty key gives none

## Flags

- **Use Only** (1) - The entity only gives its items when you trigger it, to the player who triggered it. Without
  this flag, every player gets them each time they spawn, and triggering it still equips the player who triggered it

## Notes

- Players always get their fists at spawn as well, because the entity only adds items
- A player who already has the fists, a blade or the medikit doesn't get a second one, so a count above 1 for these
  gives one
- A count of 0 or 1 gives one, and a count above 100 gives 100
- Only keys that name a `weapon_`, `ammo_` or `item_` class give anything, and the game ignores every other key
- The entity loads every item it gives with the map, so an item that the map doesn't place, such as `item_battery`,
  works too
- A key that [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) adds once
  the map runs only gives its item if the map already loads that class, such as a weapon or an item the map places.
  Any other class is refused, and with `developer 1` set in the console, the console says why

## See also

- [`player_weaponstrip`](player_weaponstrip.md) - takes the weapons of a player away
- [`Limitator`](Limitator.md) - sets the ammo of the loadout weapons
- [game_player_equip on TWHL](https://twhl.info/wiki/page/game_player_equip) - the Half-Life entity

## Changes since 1.38

- Players get their fists at every spawn on a map with this entity too. In SBO 1.38, in Co-op and Battle Royale, any
  `game_player_equip` on the map, even one with **Use Only** set, took the fists away at spawn. Fists are every
  player's own weapon, and taking weapons away is the job of [`player_weaponstrip`](player_weaponstrip.md)
- A count above 100 gives 100. In SBO 1.38, a very large count gave items until the server stopped responding
- Keys that aren't a `weapon_`, `ammo_` or `item_` class are ignored. In SBO 1.38, the game created any key as an
  entity on the player, and some keys crashed the server
- A **Team Master** that is off also stops a trigger from equipping the player. In SBO 1.38, it only stopped the
  equipment at spawn
- An item that the map doesn't place, such as `item_battery`, is given. In SBO 1.38, as in Half-Life, the first player
  to get it crashed the server
