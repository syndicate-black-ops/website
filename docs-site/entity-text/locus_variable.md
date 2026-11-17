---
description: "A locus_variable records a position, a vector and a number each time you trigger it, and gives them back later to other entities."
---
A `locus_variable` records a position, a vector and a number each time you trigger it, and gives them back later to
the keys that the editor marks with **[LP]** for a position, **[LV]** for a vector and **[LR]** for a number. It can
also make a short-lived marker entity that holds the values instead of keeping them itself.

## Attributes

- **Name** (`targetname`) - The name you put in another entity's locus key so it reads the values, and triggering
  the entity by this name records them. See [Common keys](common-keys.md#targetname)
- **Position to record** (`m_iszPosition`) - Sets the position to record, a [locus position](../guide/locus.md).
  With `*locus` or `!activator`, it is the position of the entity that started the chain of triggers
    - If you leave this key empty, it works like `*locus`
- **Vector to record** (`m_iszVelocity`) - Sets the vector to record, a [locus vector](../guide/locus.md)
    - If you leave this key empty, it works like `*locus`, so it is the velocity of the entity that started the chain
- **Number to record** (`m_iszRatio`) - Sets the number to record, a [locus number](../guide/locus.md)
    - If you leave this key empty, it works like `*locus`
- **Child's name** (`m_iszTargetName`) - With a name, each trigger makes a new marker entity with this name, which
  holds the values
    - If you leave this key empty, the values are stored in the `locus_variable` itself
- **Fire on spawn** (`m_iszFireOnSpawn`) - The entity fires this after each recording, and passes on the marker as
  the [activator](../guide/entity-triggering.md#target-selectors), or the `locus_variable` when it makes none
- **Child removed after** (`m_fDuration`) - Sets how many seconds pass before the marker is removed, and with 0, it
  is removed on the next server frame, after **Fire on spawn** has fired
- **Reset at round start** (`round_reset`) - Sets whether the entity goes back to its state of the map start at each
  new round of Co-op, Battle Royale and Bounty Killer, before the players spawn
    - No (0) - The entity keeps its values
    - Yes (1) - The entity goes back to its values of the map start

## Notes

- Read as a position, the `locus_variable` or its marker gives the recorded position, read as a vector, the
  recorded vector, and read as a number, the recorded number
- If one of the three values can't be worked out, the trigger records nothing, makes no marker and fires nothing
- Each marker is an entity, and no marker is made when the map is within 64 entities of the limit

## See also

- [Locus guide](../../guides/locus.md) - how entities pass positions and numbers to each other
- [`calc_position`](calc_position.md) - works out a position from an entity
- [`calc_eval_number`](calc_eval_number.md) - works out a number from two or three numbers
- [Locus system](../guide/locus.md) - every locus rule

## Changes since 1.38

- `locus_variable` is new in SBO 2.0.0
