A `game_player_hurt` hurts the player who triggers it, or heals that player with a negative damage, and then fires its
target.

## Attributes

- **Name** (`targetname`) - Triggering the entity hurts the player who started the chain of triggers. See
  [Common keys](common-keys.md#targetname)
- **Target** (`target`) - Names the entities to trigger after the entity hurts the player, with the same
  [use type](../guide/trigger-modes.md), and passes on the player as the
  [activator](../guide/entity-triggering.md#target-selectors)
- **Damage To Apply** (`dmg`) - Sets the damage dealt to the player, and a negative value heals the player by that
  much instead, up to their maximum health
    - If you leave this key empty, it is 0 and the player takes no damage
- **Master** (`master`) - Names a [master](../guide/masters-and-states.md#masters), and while the master is off,
  triggering the entity does nothing

## Flags

- **Remove On fire** (1) - The entity is removed after it is used once

## Notes

- If no player started the chain of triggers, nobody is hurt, but the entity still fires its target

## See also

- [`trigger_hurt`](trigger_hurt.md) - a brush that hurts or heals what is inside it
- [`trigger_hurt_remote`](trigger_hurt_remote.md) - hurts or heals entities by name or class
- [game_player_hurt on TWHL](https://twhl.info/wiki/page/game_player_hurt) - the Half-Life entity

## Changes since 1.38

- If no player started the chain of triggers, the entity fires its target and hurts nobody. In SBO 1.38, as in
  Half-Life, this crashed the server
