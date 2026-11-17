---
description: "An info_intermission is a camera point for players who join or spectate while there is nobody to watch, and for the Bounty Killer death camera."
---
An `info_intermission` is a camera point for the view of a player who joins, or starts to spectate, while there is
nobody to watch, and for the death camera of Bounty Killer. The view looks at the target of the point.

## Attributes

- **Look at** (`target`) - Names the entity the view looks at
    - If you leave this key empty, the spectator view looks along the **Pitch Yaw Roll** of the point, and the death
      camera looks east

## Notes

- A player who joins, or starts to spectate, while there is nobody to watch sees the map from one of these points,
  picked at random. When there is a player to watch, or the map has no point, spectating starts as usual
- The death camera of Bounty Killer uses one of the first four points

## See also

- [Spectating](../../playing/spectating.md) - how spectating works
- [info_intermission on TWHL](https://twhl.info/wiki/page/info_intermission) - the Half-Life entity

## Changes since 1.38

- A player who joins, or a new spectator, with nobody to watch starts at one of these points
