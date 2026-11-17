A `game_team_master` is a [master](../guide/masters-and-states.md#masters) for one team, and it passes its triggers on
to its target. The game modes have no teams, so the team check always passes.

## Attributes

- **Name** (`targetname`) - Sets the name you put in another entity's **Master** key, and triggering the entity by
  this name fires its target. See [Common keys](common-keys.md#targetname)
- **Team Index** (`teamindex`) - Sets the team that the player who started the chain of triggers must be on, for
  this master to be on and its **Target** to fire, and -1 means any team. The game modes have no teams, so every
  player passes with any value
- **Master** (`master`) - Names a master, and while that master is off, triggering the entity does nothing

## Flags

- **Remove On fire** (1) - The entity is removed after it fires its **Target** once

## Notes

- It fires its target at once and removes nothing, because it has no **Delay** and no **KillTarget**

## See also

- [Masters and states](../guide/masters-and-states.md) - how a **Master** locks an entity
- [`multisource`](multisource.md) - a master that is on while all of its inputs are on
- [`trigger_relay`](trigger_relay.md) - passes a trigger on, with a delay if you set one
- [game_team_master on TWHL](https://twhl.info/wiki/page/game_team_master) - the Half-Life entity
