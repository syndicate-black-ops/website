A `trigger_sequence` runs an entry of the map's sequence file, `sequences/<map name>.seq`, or of
`sequences/global.seq`, when you trigger it. An entry is a list of timed commands that trigger and remove entities,
show HUD text to every player and play sounds, so a whole scripted scene can be in one text file. See [Sequence
files](../features/sequences.md) for more details.

## Attributes

- **Sequence name** (`sequence_id`) - Names the entry in the sequence file, written without the `%`

## Flags

- **Fire once** (1) - The entry can only start once, whether it finished or was stopped

## Notes

- On or Toggle starts the entry from its first command, and a running entry starts again. Off stops a running entry
- A round start doesn't stop a running entry, and an entry with **Fire once** stays used up until the map changes
- The game reads `sequences/global.seq` and the map's file when the map loads, and it writes errors in the files to
  the server console. Players download the map's file with the map

## See also

- [Sequence files](../features/sequences.md) - the format of the file
- [`trigger_relay`](trigger_relay.md) - starts or stops it with its **Trigger State**

## Changes since 1.38

- `trigger_sequence` is new
