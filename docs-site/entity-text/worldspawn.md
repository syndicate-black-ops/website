The `worldspawn` is the world entity, and its keys are the map's settings. Every map has exactly one, which the
compiler makes from all the world brushes (every brush that isn't part of a brush entity).

## Attributes

- **Map Description / Title** (`message`) - The game ignores this key
- **environment map** (`skyname`) - Names the sky of the map from the skies in `gfx/env/`, such as `desert`, `dusk`,
  `night` or `space`
    - If you leave this key empty, the map shows Half-Life's default sky, `desert`
- **CD track to play** (`sounds`) - Sets the number of a Half-Life soundtrack track. The engine plays it in a loop for
  each player who joins the map
- **Default Wave Height** (`WaveHeight`) - Sets how high the waves on water surfaces are, and 0 keeps the water flat.
  The map sets the engine setting `sv_wateramp` to this value divided by 8
- **Max viewable distance** (`MaxRange`) - Sets how far players can see, in units. The game doesn't draw anything
  farther away
    - If you leave this key empty or set 0, it is 4096
- **Chapter Title Message** (`chaptertitle`) - Sets text, or the name of a message in `titles.txt`. Each player sees
  it once on this map when they first enter the game, whether they spawn, spectate or become the Game Master. Players
  who join later see it too
- **Level Fade In** (`startdark`) - With Yes, the view fades in from black when the map starts. The game does this
  with the engine's `v_dark` setting on the server, so only the player who hosts a listen server sees it
- **Display game title** (`gametitle`) - The game ignores this key
- **New Level Unit** (`newunit`) - The game ignores this key
- **Grass: density** (`grassDensity`) - Sets how many grass pieces grow around each player on the map's grass
  textures, up to 1000. The grass textures are the textures with the material **A** in the materials files
    - If you leave this key empty or set 0, there is no grass
- **Grass: sprite** (`grassSprite`) - Names the grass sprite, as a `.spr` path from the game folder. Players download
  the sprite with the map
    - If you leave this key empty, it is `sprites/grass_01.spr` and `sprites/grass_03.spr`
- **Grass: fade distance** (`grassFadeDist`) - Sets the distance from the player at which the grass has faded out,
  from 128 to 4096
    - If you leave this key empty or set 0, it is 800
- **Grass: minimum height** (`grassMinHeight`) - Sets the smallest height of a grass piece, from 4 to 256
    - If you leave this key empty or set 0, it is 16
- **Grass: maximum height** (`grassMaxHeight`) - Sets the largest height of a grass piece, up to 256 and never below
  the minimum
    - If you leave this key empty or set 0, it is 32
- **Monsters freeroam** (`freeroam`) - With Yes, idle monsters whose **Freeroam** is "Map default" walk from node to
  node
- **Materials file** (`materials_file`) - Names the map's materials file, which sets the footsteps, hit sounds and
  impact effects of its textures. It wins over the materials files of the game. It is a `.txt` path from the game
  folder, such as `materials/maps/mymap.txt`, with letters, digits, `_`, `-` and `/`, one dot and fewer than 64
  characters. Players download it with the map. See [Materials](../features/materials.md) for more details
    - If you leave this key empty, the game uses `materials/maps/<map name>.txt`, if the map has one

## Notes

- Grass only grows on maps whose textures include one with the material **A**
- A map without a [`light_environment`](light_environment.md) uses the engine's default sky light and sky direction

## See also

- [Materials](../features/materials.md) - the materials file and the grass
- [`light_environment`](light_environment.md) - the sunlight
- [worldspawn on TWHL](https://twhl.info/wiki/page/worldspawn) - the Half-Life entity

## Changes since 1.38

- You can use the new grass keys, **Materials file** and **Monsters freeroam**
- Fixed chapter titles showing only to the first player on the server. Every player sees them now, including players
  who join later
- Fixed maps without sky light using the sky light of the previous map. The game never reset the sky light between
  maps. This was a bug in SBO 1.38
- Fixed maps without a sky set showing the sky of the previous map. They now show the desert sky by default
