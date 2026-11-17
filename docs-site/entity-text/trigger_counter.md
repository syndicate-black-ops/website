A `trigger_counter` fires its target after you have triggered it a set number of times, and then removes itself.

## Attributes

- **Message** (`message`) - Sets text that the player who triggered it last sees when the counter fires
- **Count before activation** (`count`) - Sets how many triggers it takes before the counter fires its target. A
  [`game_counter`](game_counter.md) has more choices

## Flags

- **No console messages** (1) - The counter writes no countdown lines, such as "Only 1 more to go...", in the console.
  These lines only show with `developer 1` set in the console

## See also

- [`game_counter`](game_counter.md) - a counter with more choices
- [trigger_counter on TWHL](https://twhl.info/wiki/page/trigger_counter) - the Half-Life entity
