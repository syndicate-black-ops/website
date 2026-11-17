An `ammo_reserve` is an ammo box that gives a player ammo of every SBO ammo type at once when they touch it. The box
is used up when a player picks it up, and it doesn't come back.

How much ammo it gives depends on whether the map has a [`Limitator`](Limitator.md):

| Ammo | With a `Limitator` | Without one |
|---|---|---|
| Croon RC 28 | the `Limitator`'s amount | 900 |
| .444k Bear Killer | the `Limitator`'s amount | 900 |
| Canon of Terror | the `Limitator`'s amount | 900 |
| Croon PM 66 | the `Limitator`'s amount | 900 |
| Croon FA 18 | the `Limitator`'s amount | 150 |
| Vindico Federal | the `Limitator`'s amount | 180 |
| Saan Auto-Shotgun | the `Limitator`'s amount | 200 |
| Benelli | the `Limitator`'s amount | 210 |
| Vindico Plasma Sniper Rifle | the `Limitator`'s amount | 100 |
| Croon NM 33 Sniper Rifle | the `Limitator`'s amount | 210 |
| Vindico Avenger Minigun | the `Limitator`'s amount | 500 |

## Attributes

- **Name** (`targetname`) - Gives the box a name, so other entities can remove it, for example with a **KillTarget**. See
  [Common keys](common-keys.md#targetname)

## Notes

- A player carries at most 900 of each ammo type, and the box gives no more than that
- A player who already carries full ammo still picks the box up, so it is used up
- Only players pick the box up
- The box's pick-up area grows and shrinks with **Model scale**

## See also

- [`Limitator`](Limitator.md) - sets how much ammo players get from a box and with their loadout
- [`game_player_equip`](game_player_equip.md) - gives weapons and ammo to players

## Changes since 1.38

- You can use the new keys **Object Hint Template** and **Hint Distance**
- **Model scale** draws the box bigger or smaller. SBO 1.38 always drew models at their normal size
