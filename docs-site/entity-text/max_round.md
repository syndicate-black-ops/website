A `max_round` sets how many rounds a Co-op map has, which is how many tries the team gets to finish the mission. It
only has an effect on Co-op maps.

## Attributes

- **Maximum rounds** (`nbmaxround`) - Sets the number of rounds, and any value of 0 or less counts as 5. If the
  server setting [`mp_easymode`](../../server/settings.md#rounds-and-missions) is 1, which is its default, the map
  gets 1.5 times this number, rounded up. You set `mp_easymode` in `server.cfg` or in the server console

## Notes

- A Co-op map without a `max_round` has 10 rounds if `mp_easymode` is 1, and 7 rounds if it is 0

## See also

- [Co-op: number of rounds](../../game-modes/coop.md#number-of-rounds) - how the round count works
- [`mission_failed`](mission_failed.md) - ends the mission with a failure

## Changes since 1.38

- Fixed `max_round` 1 and 2 being changed to 5. The game turned any value of 2 or less into 5
