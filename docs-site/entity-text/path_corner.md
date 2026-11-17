A `path_corner` marks a stop on the path of a [`func_train`](func_train.md), an [`env_modeltrain`](env_modeltrain.md),
a [`func_guntarget`](func_guntarget.md), a [`trigger_camera`](trigger_camera.md) or a monster.

## Attributes

- **Next stop target** (`target`) - Names the next `path_corner` on the path
- **Fire On Pass** (`message`) - The corner fires this target when a train, a `func_guntarget` or a
  `trigger_camera` reaches it
- **Wait here** (`wait`) - Sets how many seconds a train or camera waits at this corner before it moves on to the
  next one
- **New Train Speed** (`speed`) - From this corner on, the train or camera moves at this speed, in units per second
    - If you leave this key empty or set 0, the speed doesn't change
- **New Train rot. Speed** (`yaw_speed`) - From this corner on, a `func_train` or an `env_modeltrain` turns around its
  vertical axis at this many degrees per second while it moves. A negative value turns it the other way. The train
  doesn't turn while it is stopped, and a `func_train` turns around its origin brush
    - If you leave this key empty or set 0, the turning doesn't change

## Flags

- **Wait for retrigger** (1) - The train stops at this corner and waits until you trigger it again
- **Teleport** (2) - A train heading for this corner jumps to it at once instead of moving there
- **Fire once** (4) - **Fire On Pass** only fires the first time something reaches this corner

## See also

- [`path_track`](path_track.md) - the path of a `func_tracktrain`
- [`func_train`](func_train.md) - a brush train that follows these corners
- [path_corner on TWHL](https://twhl.info/wiki/page/path_corner) - the Half-Life entity

## Changes since 1.38

- Fixed the New Train rot. Speed key of `path_corner` being ignored. The game never read the key
