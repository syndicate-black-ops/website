An `item_sodacan` is a soda can that gives a player who touches it 1 health. An [`env_beverage`](env_beverage.md)
drops these cans.

## Attributes

- **Beverage Type** (`skin`) - Picks the look of the can
    - Hai! (0) - A green can
    - Glub (1) - A brown can
    - Grope (2) - A purple can
    - Outhrie (3) - A blue can
    - Yuck (4) - A green and brown can
    - Dante (5) - A can with flames

## See also

- [`env_beverage`](env_beverage.md) - drops a can each time you trigger it
- [item_sodacan on TWHL](https://twhl.info/wiki/page/item_sodacan) - the Half-Life entity

## Changes since 1.38

- A can placed in a map works on its own, where in SBO 1.38 it stopped the server unless the map also had an
  `env_beverage`. This was a bug in SBO 1.38: only an `env_beverage` loaded the can's model
