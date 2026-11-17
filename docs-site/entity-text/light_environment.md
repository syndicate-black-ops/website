A `light_environment` is the sun, which the map compiler uses to light every face that sees the sky. Its color, its
brightness and its angle also light the models in the game.

## Attributes

- **Name** (`targetname`) - Triggering the entity switches the sunlight on or off, and the map compiler gives a sun
  with a name its own light style. See [Common keys](common-keys.md#targetname)
- **Pitch** (`pitch`) - Sets the up and down angle of the sun, where a negative number points the sun down, and -90
  points straight down
    - If you leave this key empty, it is the pitch of **Pitch Yaw Roll**, and 0 puts the sun level with the horizon
- **Brightness** (`_light`) - Sets the color of the sun, as R G B, and its brightness. It also sets the light of the
  models in the game, the engine setting `sv_skycolor`, which the map sets from this key and which stays on when a
  sun with a name is dark
- **Sun Spread Angle** (`_spread`) - Sets the angle in degrees over which the map compiler spreads the sunlight for
  soft sun shadows, where 0 gives hard shadows. ZHLT doesn't read it
- **Ambient Color** (`_diffuse_light`) - Sets the color and the brightness the map compiler gives the light of the
  sky around the sun
    - If you leave this key empty, it is the light of the sun
- **Sun Diffuse** (`_diffuse_light2`) - Sets the color and the brightness of the light from the part of the sky
  opposite the sun. The map compiler blends the sky light from **Ambient Color** near the sun into this color on the
  other side. ZHLT doesn't read it
    - If you leave this key empty, it is **Ambient Color**
- **Only Dynamic** (`_fake`) - Sets whether the map compiler lets the sun light the faces of the map. ZHLT doesn't
  read it
    - No (empty) - The sun lights the faces and the models
    - Yes (1) - The sun only sets the light of the models
- **Appearance** (`style`) - Picks the pattern the brightness of the sunlight follows, because the map compiler puts
  the light in that light style and the game plays the pattern. A sun with a **Name** ignores it
- **Custom Appearance** (`pattern`) - For a sun with a **Name**, sets its own pattern of brightness, as letters from
  `a` for dark through `m` for normal up to `z` for the brightest, played at 10 letters a second, up to 63 letters.
  It replaces **Appearance**

## Flags

- **Initially dark** (1) - The sun starts off and turns on when you trigger it. It only works on a sun with a
  **Name**

## See also

- [`light`](light.md) - a light that shines in every direction
- [`env_sky`](env_sky.md) - a 3D sky
- [Light styles](../features/light-styles.md) - how light patterns work
- [light_environment on TWHL](https://twhl.info/wiki/page/light_environment) - the Half-Life entity
