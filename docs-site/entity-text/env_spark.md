An `env_spark` makes sparks with a crackling sound, either at random times or when you trigger it.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the sparks on or off with **Toggle**, or makes one spark
  with **Cyclic**. Without either flag, triggering it does nothing. See [Common keys](common-keys.md#targetname)
- **Max Delay** (`MaxDelay`) - Sets the longest wait between two sparks, in seconds, and each wait is a random time
  up to it. With **Cyclic**, it sets how long after a spark the next trigger has to wait
    - If you leave this key empty or set 0, the longest wait is 1.5 seconds, and with **Cyclic** there is no wait
- **Spark Silent** (`spark_silent`) - Sets whether the sparks make a sound
    - No (0) - The sparks crackle
    - Yes (1) - The sparks make no sound
- **Spark Volume Factor** (`spark_volume`) - Multiplies the volume of the spark sound, so 2 is twice as loud
    - If you leave this key empty, the sound has its normal volume
- **Sound radius** (`soundradius`) - Sets how far players hear the spark sound
    - Small (-2) - Up to about 500 units away
    - Medium (-1) - Up to about 800 units away
    - Default (0) - Up to about 1250 units away
    - Huge (1) - Up to about 2000 units away
    - Enormous (2) - Up to about 4000 units away
    - Play Everywhere (3) - Anywhere on the map, equally loud everywhere

## Flags

- **Cyclic** (16) - Each trigger makes one spark. A trigger during the wait of **Max Delay** makes one more spark
  when the wait ends
- **Toggle** (32) - Triggering the entity switches the sparks on and off. Without this flag, the entity makes sparks
  from the start of the map, and triggering it does nothing
- **Start ON** (64) - With **Toggle**, the sparks are on when the map starts

## See also

- [`env_beam`](env_beam.md) - a beam that can make sparks at its ends
- [env_spark on TWHL](https://twhl.info/wiki/page/env_spark) - the Half-Life entity

## Changes since 1.38

- You can use the new keys **Spark Silent**, **Spark Volume Factor** and **Sound radius** and the new flag
  **Cyclic**
