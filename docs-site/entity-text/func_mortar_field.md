A `func_mortar_field` drops mortar shells into its area each time you trigger it. Players hear the whistle of the
shells everywhere on the map, and about 2.5 seconds later the shells land on the ground below and explode one after
the other.

## Attributes

- **Name** (`targetname`) - Triggering the entity drops the shells. See [Common keys](common-keys.md#targetname)
- **Spread Radius** (`m_flSpread`) - Sets how far, in units, each shell can land at random from the aim point
    - If you leave this key empty, it is 0 and every shell lands on the same spot
- **Repeat Count** (`m_iCount`) - Sets how many shells fall each time you trigger the entity
    - If you leave this key empty, it is 0 and no shell falls, but the incoming sound still plays
- **Targeting** (`m_fControl`) - Picks the aim point of the shells
    - Random (0) - A random spot in the brush
    - Activator (1) - The spot of the player or monster that started the chain of triggers
    - Table (2) - The spot that the **X Controller** and the **Y Controller** pick across the brush
- **X Controller** (`m_iszXController`) - With Table, names the entity, usually a
  [`momentary_rot_button`](momentary_rot_button.md), whose position from 0 up to 1 sets where along the X axis of the
  brush the shells land
- **Y Controller** (`m_iszYController`) - With Table, names the entity whose position from 0 up to 1 sets where along
  the Y axis of the brush the shells land

## Notes

- Each shell deals 200 blast damage, which reaches up to 500 units
- The player who triggered the field counts as the attacker, so they get the kills of the shells
- Monsters near the aim point hear a danger sound and run from it

## See also

- [`func_tankmortar`](func_tankmortar.md) - a gun that fires mortar shells
- [`env_explosion`](env_explosion.md) - an explosion with a fireball and damage
- [func_mortar_field on TWHL](https://twhl.info/wiki/page/func_mortar_field) - the Half-Life entity
