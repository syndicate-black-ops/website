An `env_beverage` drops a soda can each time you trigger it, like a vending machine. You can't see the entity itself,
and a player who picks up the can gets 1 health.

## Attributes

- **Name** (`targetname`) - Triggering the entity drops a can. See [Common keys](common-keys.md#targetname)
- **Capacity** (`health`) - Sets how many cans it drops in all, and once they are used up, triggering it does
  nothing
    - If you leave this key empty or set 0, it holds 10 cans
- **Beverage Type** (`skin`) - Picks the look of the cans
    - Hai! (0) - A green can
    - Glub (1) - A brown can
    - Grope (2) - A purple can
    - Outhrie (3) - A blue can
    - Yuck (4) - A green and brown can
    - Dante (5) - A can with flames
    - Random (6) - Each can gets one of the other looks, picked at random

## Notes

- It drops no new can while the last can is still there, so the next trigger works only after a player picks up
  the can
- The can falls from the entity's position, and players can pick it up half a second after it drops

## See also

- [`item_sodacan`](item_sodacan.md) - the can it drops

