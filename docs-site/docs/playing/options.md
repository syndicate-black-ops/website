# Options

New settings in SBO 2.0.0 have been added to a new **Advanced** window to help separate them from the default
options. You can set any option from these menus as a console variable (cvar) as well, and the game saves them in
`config.cfg` in the root of your `syndicate/` directory. The normal **Options** window holds the regular settings you
would find in most Half-Life mods (player name, controls, spray, etc). See [Menus](menus.md) for more details.

## Advanced

The Advanced window groups SBO's settings on these tabs:

- **General** - Discord Rich Presence (`cl_discord_rpc`), Left-handed weapons (`cl_righthand`), Enable on-screen
  objectives (`hud_objectives`), New GameUI menus (`cl_experimental_menus`), New in-game menus
  (`cl_new_ingame_menus`) and Check for updates at start (`cl_check_for_updates`)
- **Chat** - Text size, Chat color, Name and chat colors, Message sound and Message time. See
  [Chat and console](chat-and-console.md#settings) for more details
- **Voice** - Max voice boost (`voice_maxgain`) and Voice leveling (`voice_avggain`)
- **Version** - the game's version, the newest version, **Check for updates** and a link to the SBO repository for
  the credits

With **New GameUI menus** on, the Advanced window has only the tabs General, Chat and Version, and the voice settings
are in **Options > Voice** instead.

## Settings {#player-cvars}

| Cvar | Default | Effect |
|---|---|---|
| `cl_righthand` | 0 | [[ported:openag]] Swaps your weapon to the left side of the screen when set to 1. Spectators who watch you in first person see it on the same side. The same setting can be found in **Advanced > General > Left-handed weapons** |
| `cl_discord_rpc` | 1 | Shows your current game details in your Discord profile. Setting it to 0 turns Rich Presence off. The same setting can be found in **Advanced > General > Discord Rich Presence**. See [Discord](discord.md) for more details |
| `hud_scale` | 0 | [[ported:hlu]] Scales the HUD up to fit your screen when set to 1. It applies at the next map load or video change |
| `cl_effectsdetail` | 1 | Enables the new material debris and smoke of bullet impact effects, the new water splashes of bullets, and the smoke from your gun's barrel. Setting it to 0 turns them off. The same setting can be found in **Options > Multiplayer > Bullet impact and gun effects** |
| `cl_weather` | 1 | [[ported:cs16client]] How much rain and snow you see, from 0 for none up to 3. Higher values draw more drops and flakes, which may strain older systems |
| `hud_objectives` | 1 | The mission objectives panel at the top left: 0 for hidden, 1 for short and 2 for full. The objectives key (Default: <kbd>H</kbd>) will also toggle through these modes. The same setting can be found in **Advanced > General > Enable on-screen objectives**. This panel only shows on maps with a [`trigger_objective`](../mapping/entities/trigger_objective.md) entity. See [HUD and scoreboard](hud-and-scoreboard.md#hud) for more details |
| `mat_colorcorrection` | 1 | Enables the color correction some maps use to change the colors of the view. Setting it to 0 turns it off |
| `cl_objecthint` | 1 | [[ported:featureful]] Shows hints on items and buttons you can use: 0 for off, 1 for all of them and 2 for only the hint on the item or button you can use right now |
| `cl_disablehtmlmotd` | 0 | Shows the message of the day and the map briefings as plain text instead of web pages when set to 1. It applies the next time one of these windows opens |
| `cl_autowepswitch` | 1 | [[ported:hlu]] Switches to a weapon when you pick it up. Setting it to 0 turns this off. Your loadout always selects a weapon when you spawn |
| `default_fov` | 90 | The field of view, from 1 to 179. The same setting can be found in **Options > Multiplayer > Field of view** |
| `cl_rollangle` | 0 | [[ported:hlu]] How far the view tilts while you strafe, from 0 for no tilt up to 360. The same setting can be found in **Options > Multiplayer > View roll angle when strafing** |
| `cl_rollspeed` | 200 | [[ported:hlu]] How fast you must strafe to get the full tilt of `cl_rollangle`. The same setting can be found in **Options > Multiplayer > View roll speed** |
| `cl_bobtilt` | 0 | [[ported:hlu]] Tilts the weapon in your hands while you walk when set to 1. The same setting can be found in **Options > Multiplayer > Weapon tilt while moving** |
| `cl_experimental_menus` | 1 | Uses SBO's new main menu windows. Setting it to 0 uses Half-Life's default window style. The same setting can be found in **Advanced > General > New GameUI menus**. See [Menus](menus.md) for more details |
| `cl_new_ingame_menus` | 1 | Uses SBO's new in-game windows. Setting it to 0 uses the old selection menu with lists and text menus. The same setting can be found in **Advanced > General > New in-game menus**. See [Menus](menus.md) for more details |
| `cl_check_for_updates` | 1 | Checks for a new version when the game starts. Setting it to 0 only checks when you press **Check for updates** yourself. The same setting can be found in **Advanced > General > Check for updates at start**. See [Updates](installing.md#updates) for more details |
| `voice_maxgain` | 5 | How much quiet microphones are boosted, from 1 to 10 times. The same setting can be found in **Options > Voice > Max voice boost** |
| `voice_avggain` | 0.5 | How strongly loud and quiet voices are evened out, from 0 to 1. The same setting can be found in **Options > Voice > Voice leveling** |
| `namecolor` | 0 | The color of your name. The same setting can be found in **Options > Multiplayer > Name color**. See [Chat and console](chat-and-console.md#name-color-and-chat-color) for more details |

The HUD, chat, kill feed, scoreboard and spectator cvars are on their own pages:
[HUD and scoreboard](hud-and-scoreboard.md), [Chat and console](chat-and-console.md) and
[Spectating](spectating.md).

## Changes since 1.38

- A new **Advanced** window holds the settings added in SBO 2.0.0
- New settings: left-handed weapons, Discord Rich Presence, HUD scaling, bullet impact and gun effects, weather amount,
  on-screen objectives, color correction, object hints, plain-text MOTD, automatic weapon switching, view roll, weapon
  tilt, name color, name and chat colors, the new menus and update checks

## See also

- [Menus](menus.md) - the Options and Advanced windows and the other menus
- [Chat and console](chat-and-console.md) - the chat settings and colors
- [HUD and scoreboard](hud-and-scoreboard.md) - the HUD, scoreboard and kill feed settings
- [Discord](discord.md) - what Discord shows while you play
