A `Limitator` sets how much reserve ammo Co-op players get with the weapons of their loadout, and how much ammo each
[`ammo_reserve`](ammo_reserve.md) gives. A map needs only one, because it sets these amounts for the whole map.

Players get these amounts at every spawn with the weapons of their loadout, where the magazine comes full as usual,
and again from each `ammo_reserve` they pick up, but the spawn amounts only apply on Co-op maps. A player carries at
most 900 of each ammo type, and the grenade launcher and the nuclear launcher aren't limited.

## Attributes

- **Croon RC 28 reserve ammo** (`weap1`) - Sets the reserve ammo of the Croon RC 28
- **.444k Bear Killer reserve ammo** (`weap2`) - Sets the reserve ammo of the .444k Bear Killer
- **Canon of Terror reserve ammo** (`weap3`) - Sets the reserve ammo of the Canon of Terror
- **Croon PM 66 reserve ammo** (`weap4`) - Sets the reserve ammo of the Croon PM 66
- **Croon FA 18 reserve ammo** (`weap5`) - Sets the reserve ammo of the Croon FA 18
- **Vindico Federal reserve ammo** (`weap6`) - Sets the reserve ammo of the Vindico Federal
- **Saan Auto-Shotgun reserve ammo** (`weap7`) - Sets the reserve ammo of the Saan Auto-Shotgun
- **Benelli reserve ammo** (`weap8`) - Sets the reserve ammo of the Benelli
- **Vindico Plasma Sniper Rifle reserve ammo** (`weap9`) - Sets the reserve ammo of the Vindico Plasma Sniper Rifle
- **Croon NM 33 Sniper Rifle reserve ammo** (`weap10`) - Sets the reserve ammo of the Croon NM 33 Sniper Rifle
- **Vindico Avenger Minigun reserve ammo** (`weap11`) - Sets the reserve ammo of the Vindico Avenger Minigun

## Notes

- A value of 0 or a negative value gives no reserve ammo, and a value above 900 gives 900
- If you leave a key empty, it gives the same amount as a map without a `Limitator`, which is the key's default

## See also

- [`ammo_reserve`](ammo_reserve.md) - an ammo box that players pick up
- [Loadout](../../playing/loadout.md) - the weapons players choose

## Changes since 1.38

- 0 gives no reserve ammo, where in SBO 1.38 0 or a negative value counted as 1
- If you leave a key empty, it gives the amount of a map without a `Limitator`. In SBO 1.38 it kept the value of the
  last map that set it, or 1, so no default in the editor could match it
- A value above 900 gives 900, the most a player carries. SBO 1.38 gave 1 reserve ammo for a value above 910, which was a bug
