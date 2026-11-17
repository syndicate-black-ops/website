The Pitbull is a small creature that runs at enemies, bites them and explodes after about 30 seconds. It uses
Half-Life's snark class name with the Pitbull model.

## Attributes

- **TriggerTarget** (`TriggerTarget`) - Names the entities that fire once when **Trigger Condition** or **Trigger
  Alternative Condition** happens
- **Trigger Condition** (`TriggerCondition`) - Sets the event that fires **TriggerTarget**, but the Pitbull only checks
  it when it dies, so "Take Damage" and "Death" both fire at that moment
- **Trigger Alternative Condition** (`TriggerAltCondition`) - Sets a second event that fires **TriggerTarget**, and the
  Pitbull also only checks it when it dies

## In combat

The Pitbull has 100 health. It explodes 30 seconds after it spawns, but every bite gives it 2 more seconds, up to 65
seconds left. Each bite deals 15 damage and adds 5 to the explosion, which deals 20 damage plus 5 for each bite. It
doesn't bite glass that can't break.

## See also

- [monster_snark on TWHL](https://twhl.info/wiki/page/monster_snark) - the Half-Life entity
