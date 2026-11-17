An `env_bubbles` makes bubbles rise inside its brush, in bursts.

## Attributes

- **Name** (`targetname`) - Triggering the entity turns the bubbles on or off, as the
  [use type](../guide/trigger-modes.md) says. See [Common keys](common-keys.md#targetname)
- **Bubble density** (`density`) - Sets how many bubbles each burst makes, up to 255
    - If you leave this key empty, it is 0 and each burst makes the fewest bubbles
- **Bubble frequency** (`frequency`) - Sets how often a burst comes. At 0, a burst comes every 2.5 seconds, and
  each point of this key takes a tenth of a second off, so at 20 or more a burst comes every half second
    - If you leave this key empty, it is 0 and a burst comes every 2.5 seconds
- **Speed of Current** (`current`) - Pushes the bubbles sideways toward the yaw of **Pitch Yaw Roll**, which is the
  compass direction, and a negative number pushes them the other way. With 0, they rise straight up
- **Custom Bubble Sprite** (`bubble_model`) [[ported:featureful]] - Sets the sprite the bubbles are drawn with
    - If you leave this key empty, it is `sprites/bubble.spr`

## Flags

- **Start Off** (1) - The bubbles don't start with the map, but wait for a trigger

## Notes

- The first burst comes 2 seconds after the map starts, or 0.1 seconds after a trigger turns the bubbles on
- Only players who can hear the area of the entity see the bubbles

## Changes since 1.38

- You can use the new key **Custom Bubble Sprite**
