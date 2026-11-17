An `env_shake` shakes the view of players when you trigger it.

## Attributes

- **Name** (`targetname`) - Each time you trigger the entity, it starts a shake. See
  [Common keys](common-keys.md#targetname)
- **Amplitude** (`amplitude`) - Sets how strong the shake is, from 0 for no shake up to 16 for a very strong one,
  and anything above 16 works like 16. Default 4
    - If you leave this key empty, it is 0 and nothing shakes
- **Effect radius** (`radius`) - Sets how far the shake reaches from its position: players inside this distance
  shake and players outside it don't, and 0 makes every player shake. Default 500
    - If you leave this key empty, it is 0 and every player shakes
- **Duration** (`duration`) - Sets how many seconds the shake lasts, up to 16, and the shake gets weaker toward the
  end. Default 1
    - If you leave this key empty, it is 0 and nothing shakes
- **Frequency** (`frequency`) - Sets how fast the view moves back and forth, from 0.1 for a single jolt up to 255
  for a fast rumble. Default 2.5
    - If you leave this key empty, it is 0 and nothing shakes
- **Position** (`message`) [[ported:featureful]] - Sets where the shake is, which is the point **Effect radius** is
  measured from. It takes a [locus position](../guide/locus.md), so you can use:
    - `x y z` - a point on the map, given as three coordinates
    - the name of an entity - the shake is at that entity's position
    - the name of a [`calc_position`](calc_position.md) - the shake is at the position it works out
    - [`!activator`](../guide/locus.md#entity-names-in-a-locus-key) - the shake is at the entity that started the
      chain of triggers
    - nothing - the shake is at the `env_shake` itself

## Flags

- **GlobalShake** (1) - Every player shakes, and the entity ignores **Effect radius**

## Notes

- Only players standing on the ground shake, so a player who is jumping or falling at that moment feels nothing
- Every player inside the **Effect radius** feels the same shake, so a player near the edge feels it as strongly
  as a player at the center
- Every trigger starts a shake, even a trigger with the [use type](../guide/trigger-modes.md) Off, and you can't
  stop a shake once it has started
- If **Position** names an entity that doesn't exist, nothing shakes

## See also

- [Locus system](../guide/locus.md) - the positions that **Position** accepts
- [Trigger modes](../guide/trigger-modes.md) - the use types On, Off, Toggle and Set
- [`env_fade`](env_fade.md) - colors the screen of players

## Changes since 1.38

- You can set where the shake is with the new key **Position**
