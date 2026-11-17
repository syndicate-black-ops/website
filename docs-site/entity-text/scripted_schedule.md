A `scripted_schedule` tells monsters what to do about a spot: move away from it, take cover from it, investigate it,
turn to it or go to it.

## Attributes

- **Affected monster** (`entity`) - Names the monsters, as a name or `!activator`
- **Suggested schedule** (`schedule`) - Sets what the monsters are told to do about the spot
    - Clear suggested schedule (0) - It stops an order that the monsters are running
    - Move away from spot (1, default) - The monster goes to an [`info_node`](info_node.md) away from the spot. If
      it finds none, it goes to a point straight away from the spot
    - Cover or retreat from spot (2) - The monster first looks for an `info_node` that is hidden from the spot. If it
      finds none, it does as with "Move away from spot"
    - Investigate spot (3) - The monster looks at the spot, walks there and waits
    - Turn to spot (4) - The monster turns to the spot
    - Move to spot (5) - The monster goes to the spot
- **Min distance** (`mindist`) - With "Move away from spot" and "Cover or retreat from spot", sets the shortest
  distance the monster goes
- **Max distance** (`maxdist`) - With "Move away from spot" and "Cover or retreat from spot", sets the longest
  distance the monster goes
    - If you leave this key empty, it is 784
- **Spot entity** (`spot_entity`) - Names the entity that is the spot
    - If you leave this key empty, the spot is the monster itself for "Move away from spot" and "Cover or retreat from
      spot", and this entity for the others
- **Move preference** (`move_preference`) - Sets whether the monster walks or runs. A monster without a run
  animation, such as a Zombie, the Cyborg or the Cyber Minotaur, always walks
    - Auto (0, default) - It runs for "Move away from spot" and "Cover or retreat from spot", and walks for the others
- **Spot preference** (`spot_preference`) - The game ignores this key. It always takes the spot at the place where it
  is when the entity fires

## Notes

- A monster that is busy gets the order when it is free again. A monster is busy when it is in a script, fighting or
  afraid
- A newer order or a "Clear suggested schedule" replaces an order that is still waiting
- Damage or a new enemy stops a running order. A monster that follows a player keeps following after the order

## See also

- [`scripted_sequence`](scripted_sequence.md) - plays an animation on a monster
- [`env_soundmark`](env_soundmark.md) - makes a sound that monsters hear
- [`info_node`](info_node.md) - the nodes monsters move between

## Changes since 1.38

- `scripted_schedule` is new
