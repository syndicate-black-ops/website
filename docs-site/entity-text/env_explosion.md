An `env_explosion` makes an explosion each time you trigger it, with a fireball, smoke, sparks, a scorch mark and
damage around it.

## Attributes

- **Name** (`targetname`) - Triggering the entity sets off the explosion. See
  [Common keys](common-keys.md#targetname)
- **Position** (`target`) - Sets where it explodes. It takes a [locus position](../guide/locus.md), so you can use a
  point such as `0 0 64`, the name of an entity, the name of a [`calc_position`](calc_position.md), `!activator` for
  the entity that started the chain of triggers, or `*player` for that entity only when it is a player
    - If you leave this key empty, it explodes at the `env_explosion` itself
- **Magnitude** (`iMagnitude`) - Sets the damage at the center of the blast and the size of the fireball. The damage
  reaches 2.5 times this value in units, unless you set **Damage radius**
    - If you leave this key empty, it is 0 and you get a small fireball that does no damage
- **Damage radius** (`iradius`) - Sets how far the damage reaches, in units, and 0 makes it 2.5 times the
  **Magnitude**
- **Custom Fireball Sprite** (`model`) - Sets the sprite drawn as the fireball
    - If you leave this key empty, it is the normal fireball
- **Custom Smoke Sprite** (`smokesprite`) - Sets the sprite drawn as the smoke
    - If you leave this key empty, it is the normal smoke
- **Custom sprite scale** (`scale`) - Sets the size of the fireball and the smoke, where 1 is the size of the sprite
    - If you leave this key empty or set 0, the **Magnitude** sets the size

## Flags

- **No Damage** (1) - The explosion is only an effect, so it hurts nothing and breaks nothing
- **Repeatable** (2) - You can set it off again and again. Without this flag, the entity is removed after it
  explodes once
- **No Fireball** (4) - No fireball is drawn, but the explosion still makes its sound unless you set **No Sound**
- **No Smoke** (8) - No smoke rises after the blast
- **No Decal** (16) - The explosion leaves no scorch mark
- **No Sparks** (32) - No sparks fly out of the blast
- **No Sound** (64) - The explosion makes no sound
- **Activator is attacker** (128) - The entity that set off the explosion counts as the attacker, so a player who
  set it off gets the kills

## Notes

- If a floor or a wall lies up to 32 units below the **Position**, the explosion moves away from it a little, and
  only then does it leave a scorch mark on it
- If the entity can't find the position that **Position** names, for example because it names an entity that
  doesn't exist, nothing explodes for that trigger
- Only players near enough to hear the spot see the fireball and the smoke
- If [`trigger_changevalue`](trigger_changevalue.md) or [`trigger_copyvalue`](trigger_copyvalue.md) changes
  **Magnitude** or the sprite scale, the next explosion has the new fireball and smoke size as well as the new damage.
  See [Changing keys](../guide/changing-keys.md)

## See also

- [`nuclear_explosion`](nuclear_explosion.md) - a huge explosion with a mushroom cloud and a shock wave
- [`env_shooter`](env_shooter.md) - shoots models or sprites, such as gibs
- [`env_shake`](env_shake.md) - shakes the view of players
- [env_explosion on TWHL](https://twhl.info/wiki/page/env_explosion) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Position**, **Damage radius**, **Custom Fireball Sprite**, **Custom Smoke Sprite** and
  **Custom sprite scale**
- You can use the new flags **No Sound** and **Activator is attacker**
