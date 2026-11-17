# Changes since 1.38

This page lists what Syndicate Black Ops 2.0.0, 2.1.0 and 2.2.0 change compared with version 1.38. Every fixed bug was
found in the 1.38 game code, and every new or changed feature was checked against it.

## Gameplay

- Fixed weapons and items briefly flashing in your view when a map, a command or a plugin gives them to you
- The Assassin's cloak now hides you from monsters, turrets and mounted guns, which only spot you within a range that
  shrinks the less you move, and shrinks further in the dark
- Footsteps and bullet impacts have their own sounds and effects for each surface, such as wood, grass, snow, carpet and
  gravel
- Bullet hits on walls throw chips, dust and sparks in the color of the surface. You can turn them off with **Options >
  Multiplayer > Bullet impact and gun effects**
- Bullets that hit water make a splash with a ripple and a splash sound, including shots from monsters, turrets and
  mounted guns
- When you fire a gun, a puff of smoke rises from its barrel in first person
- `thirdperson` and `firstperson` work in multiplayer
- Players pass through each other for the first 15 seconds of a round
- An AFK sign shows over idle players
- Boxes that you can push now move when you walk into them from any side, without holding forward. Hold Use to pull a
  box
- Bullet hits on monsters sound like flesh
- Weapons move with screen shake and recoil
- Fixed VERY BAD SHOT almost never happening. PERFECT SHOT, CRITICAL SHOT, FAIL SHOT and VERY BAD SHOT now each come one
  hit in 100. This was a bug in SBO 1.38
- Fixed the Cyber Minotaur shooting from a point far away from its gun, often behind it or inside a wall. The game
  placed its gun as if the Cyber Minotaur always faced the same way. This was a bug in SBO 1.38
- Fixed the Cyber Minotaur walking off after Feds behind walls instead of fighting the players it can see. It picked its
  targets without checking that it could see them. This was a bug in SBO 1.38
- Fixed the Cyber Minotaur ejecting no shell casings. The game never set its shell casing model. This was a bug in SBO
  1.38
- Fixed Cyborgs being unable to move about 50% of the time. Their model has a second walk animation with no ground
  movement, and the game picked it at random. This was a bug in SBO 1.38
- Fixed Werewolves being unable to move about 50% of the time. Their model has a second walk animation with no ground
  movement, and the game picked it at random
- Fixed Demon Slaves and Werewolves losing the flags that the map gives them, such as Fade Corpse, as soon as they wake
  up. The game cleared their flags the first time they moved. This was a bug in SBO 1.38
- Demon Slaves on HardCore monster health have 900 health, not 9000. This was a bug in SBO 1.38
- Fixed Assassins stuttering after they land
- Fixed all Assassins sharing one footstep timer
- Rappelling Feds no longer shoot at walls. This was a bug in SBO 1.38
- The Gargantua's eye glow stays on its head. This was a bug in SBO 1.38
- Fixed ichthyosaurs steering into walls. They checked for walls at the wrong points around them. This was a bug in SBO
  1.38
- A falling Apache explodes when it lands on a player or a monster. This was a bug in SBO 1.38
- Fixed the Apache and Osprey rotor sound changing pitch for everyone whenever the first player on the server moved
- Fixed automatic mounted guns hardly aiming or firing at anyone when two or more players are on the server. Each gun
  looked at only one player at a time and then waited 2 seconds. This was a bug in SBO 1.38
- Fixed laser turrets keeping their beam on while something blocks them. A blocked turret stopped its own updates, so it
  never turned the beam off. This was a bug in SBO 1.38
- Destroyed turrets, sentry guns and ichthyosaur bodies fade away when the map sets the Fade Corpse flag. Their own
  death code never read the flag. This was a bug in SBO 1.38
- Fixed random models showing where a zoomed plasma sniper shot or a Heavy Weapons Fed's bullet hits. The hit flare used
  a sprite number that was set only when a plasma ball hit something, so on a new map it could point at another model.
  This was a bug in SBO 1.38
- Fixed the server crashing when a Pitbull keeps biting for a long time. Each bite added to its lifetime, and its
  sounds play lower as its lifetime grows, until the sound pitch went below zero. This was a bug in SBO 1.38
- The G-Man moves at the end of a mission. This was a bug in SBO 1.38
- Fixed nuclear explosions never showing their afterglow. The game set up the afterglow but never gave it a time to
  start. This was a bug in SBO 1.38
- Fixed gibs that keep rolling or spinning on an edge staying for the whole map. They now fade away. This was a bug in
  SBO 1.38
- Fixed a satchel charge or a trip mine under a door jamming the door. The door now sets it off. This was a bug in SBO
  1.38
- Fixed trains and elevators that a button stops playing their moving sound in a loop. The sound stopped only when a
  train reached a stop on its path, not when a button stopped it. This was a bug in SBO 1.38
- Fixed the sound of turnable valve wheels and levers continuing to play after you let go of them
- Fixed monsters breaking objects that only a trigger should break. The object took damage from monster attacks without
  checking that only a trigger may break it. This was a bug in SBO 1.38
- Fixed ice floors staying slippery after you step off them. The game set the floor grip back to normal only in single
  player. This was a bug in SBO 1.38
- Map cameras give your view back when you die or start spectating. This was a bug in SBO 1.38
- Fixed players losing their weapons and HUD when a mounted gun they use is removed from the map
- Fixed dead players leaving empty weapon boxes on the floor. The game made a weapon box even when there was nothing to
  put in it. This was a bug in SBO 1.38
- Fixed dead players being able to turn on the cloak. The cloak checked only that you were not spectating, not that you
  were alive. This was a bug in SBO 1.38
- Fixed the cyber eyes light flashing on servers. The game sent the light so often that the network delivered it in
  bursts. This was a bug in SBO 1.38
- Fixed the green tint of the cyber eyes going away for good after a screen flash. The game sent the tint only once.
  This was a bug in SBO 1.38
- Fixed maps without a sky set showing the sky of the previous map. They now show the desert sky by default
- Fixed maps without sky light using the sky light of the previous map. The game never reset the sky light between maps.
  This was a bug in SBO 1.38
- Fixed chapter titles showing only to the first player on the server. Every player sees them now, including players who
  join later
- Fixed on-screen map text (`game_text`) disappearing too early when the map shows it again before the first one has
  faded out. The repeated text now restarts and stays for its full time
- Fixed on-screen map text sometimes not showing when it replaced another text that was still on the screen
- Fixed radiation (Geiger counter) clicks carrying over into the next map

## Co-op

See [Co-op](game-modes/coop.md) for the full rules.

- Game Master mode is built into the game: on [Co-op](game-modes/coop.md#game-master) maps the Game Master can fly
  around, spawn monsters by tier, place weapon and ammo drops and teleporters, select monsters and give them orders, and
  see health bars over players and monsters
- The Game Master can select and remove monsters placed by the map, not only the ones the Game Master spawned
- With **New in-game menus** on, the loadout menu grays out a launcher when none are free
- After a failed mission the server goes to the next map
- A player who has not chosen a loadout, or **go** in Battle Royale, holds up the round start for at most 45 seconds. In
  SBO 1.38 the round waited for that player with no time limit
- Levels can go below -40, but speed stops dropping at -40
- In Co-op, your speed after the speed penalties of your loadout is never below 80. In 1.38, a player at level −40 with
  a heavy loadout couldn't move
- The speed you lose for team kills and suicides applies right away
- The speed you gain from leveling up applies right away. In SBO 1.38 the new speed took effect only after your next
  weapon switch
- The spawn health penalty never takes you below 10 health. In SBO 1.38 a spawn health of 27 to 35 dropped to 2 to 10
- Cops give XP for every hit, not only the killing one. In SBO 1.38 a Cop gave XP only for hits during its death
  animation
- The medikit gives XP only when it heals a player. In SBO 1.38 it also gave XP for hitting a wall, a monster or a body
- A player who leaves frees their place for the grenade launcher or the nuke launcher. This was a bug in SBO 1.38
- Fixed the limit message saying "2 grenade launchers max / team" when the limit is 3. This was a bug in SBO 1.38
- Fixed an empty server counting rounds, so the first real round could be round 2 or later. With nobody on the server,
  the game started and counted a new round every 20 seconds
- Fixed a round being lost too early when a player who was not in the round left the server. When any player left, the
  game took one player off the round's count, even a player who was not in the round. This was a bug in SBO 1.38
- No new round starts during the mission end or the map vote. This was a bug in SBO 1.38
- Fixed a mission result reached between two rounds starting a new round first, which respawned everyone. The game acted
  on a mission result only during a round
- Fixed a Co-op player banned for teamkills (`mp_ban 1`) looking like a normal agent instead of wearing the hunted model
- Fixed a joining player canceling a mission success. When a player joined, the game cleared the record that a player
  had reached the mission exit. This was a bug in SBO 1.38
- Fixed a Co-op mission showing both FAILED MISSION and SUCCESSFULL MISSION when the map triggers both. The game showed
  every result and could count the second one. Now only the first result shows and counts. This was a bug in SBO 1.38

## Battle Royale and Bounty Killer

See [Battle Royale](game-modes/battle-royale.md) and [Bounty Killer](game-modes/bounty-killer.md).

- Suicides no longer cost points in Battle Royale and Bounty Killer. In SBO 1.38 a suicide cost 5 points in Battle
  Royale and 10 in Bounty Killer, which only made matches last longer
- In Bounty Killer, a death from a fall, water or a hazard no longer costs points. A kill by a monster still costs 5
- In Bounty Killer, the first player spawns once, as the Hunted. This was a bug in SBO 1.38
- Fixed the radio key opening an empty radio menu in Bounty Killer. The radio only works in Co-op
- Fixed a single player in Battle Royale losing their weapons and respawning with "ROUND START" every 10 seconds. The
  game now waits for a second player

## Weapons and items

- **Left-handed weapons** in **Advanced > General**, or `cl_righthand 1` in the console, holds your weapon in the left
  hand
- Most weapons lying on the floor have new models
- Fixed the Pitbull pickup showing Half-Life's snark nest world model instead of the Pitbull world model
- With `sv_cheats 1`, the [cheat commands](mapping/getting-started/cheat-commands.md) work in multiplayer, for example
  `impulse 101` for every weapon, noclip and god mode. `sv_infinite_ammo 1` gives every weapon endless ammo
- Croon Armor Skin absorbs 60% of the damage, as its original description says. In SBO 1.38 it absorbed 57%
- Croon Cyber Torso Armor also protects the stomach, as its original description says. In SBO 1.38 it protected the chest only
- Croon Cyber Torso and Skull Armor absorbs 70% and also protects the stomach, as its original description says. In SBO 1.38 it
  absorbed 67% and left the stomach out
- A satchel charge deals 200 to 300 damage, as its original description says. In SBO 1.38 it always dealt 200
- The Adrenaline Surge gives 75 extra health in every mode. In SBO 1.38 Bounty Killer gave 50
- The descriptions of the Canon, Benelli, rocket launcher, minigun and RC 28 show their real damage and fire rates. The
  descriptions gave other numbers than the code used, so they now match the code
- Fixed not being able to pick up satchels, from the map or a dead player's backpack, while you have satchels deployed
- When your weapon runs out of ammo, the game no longer switches you to the RPG
- You can throw Pitbulls while looking straight up. This was a bug in SBO 1.38
- Fixed the Vindico grenade launcher and the RC 28 firing an extra shot when you hold both fire buttons
- Fixed the Vindico grenade launcher not reloading when one grenade is left in the magazine
- Fixed the fire rate of weapons changing with your frame rate. Each shot counted the wait for the next shot from the
  frame it fired in, not from the time the shot was due. This was a bug in SBO 1.38
- Fixed the PM66's alternate fire shooting faster for players with a higher frame rate. The alternate fire had no wait
  time between bursts, so it fired one burst every frame. This was a bug in SBO 1.38
- Fixed the K444, Federal, RC 28, SW, NM33 and PM66 freezing on the first frame of their idle animation
- Fixed an empty minigun playing its firing animation for as long as you hold the fire button
- Fixed the next hand grenade popping into your hand without its draw animation after a throw
- Fixed a primed hand grenade being thrown by itself as soon as you took it out again, after you switched to another
  weapon or used a mounted gun while it was primed. Putting the grenade away did not cancel the throw, so it stayed
  primed. This was a bug in SBO 1.38
- Fixed the hand grenade's loadout description saying 250 damage, while a thrown grenade does 100
- Fixed the flashlight cutting off the chainsaw's sound when you switch it on or off
- Fixed the chainsaw's engine sound playing on after you die or lose the chainsaw. The chainsaw's own put-away step
  never ran, so only taking out another weapon stopped the sound. This was a bug in SBO 1.38
- Fixed the sniper zoom and the slow zoom walk staying on after you lose your weapons while zoomed. Losing your weapons
  did not reset the zoom or the speed. Only taking out your next weapon did. This was a bug in SBO 1.38
- Fixed other players not seeing your character play its shoot animation when you fire the RC 28. The RC 28 was the only
  pistol that did not play it. This was a bug in SBO 1.38
- Fixed the Benelli and the Saan Auto-Shotgun never playing their pump sound after a shot. The pump sound timer used a
  clock that stays at zero on the server, so the sound never played. This was a bug in SBO 1.38
- Fixed the FA18 reload missing part of its sound. One of its sound files was missing from the game. This was a bug in
  SBO 1.38
- Fixed the empty click playing twice for you. The server played the click to you, and your own game played it too. This
  was a bug in SBO 1.38
- Fixed the satchel's draw animation and the RPG's idle animation being cut short. The satchel's draw time was cut from
  2 seconds to 1, and the RPG started its next idle animation after 3 seconds, although the animation is 6 seconds long.
  This was a bug in SBO 1.38
- Fixed about one RPG rocket in five leaving only a small puff of smoke instead of a full smoke cloud. For strong
  rockets the smoke size went past its limit and wrapped around to a tiny one. This was a bug in SBO 1.38
- The K444 crosshair is centered. This was a bug in SBO 1.38
- Fixed the sniper scope not showing at resolutions of 1600 pixels wide and more, and not covering the screen between
  1281 and 1599 pixels wide. The game drew the scope only at the pixel size of its picture. This was a bug in SBO 1.38
- Fixed the sniper scope covering the screen while you are not zoomed when your field of view (`default_fov`) is below
  90. The game checked your own field of view instead of the weapon's zoom. This was a bug in SBO 1.38
- Fixed your field of view going back to 90 after a leg injury, a fall or a respawn. The game always set the field of
  view back to 90. This was a bug in SBO 1.38
- Assassin's speed no longer depends on the armor you picked before choosing Assassin. In SBO 1.38 the server kept the
  armor you had picked before Assassin and used its weight
- Picking another loadout after Assassin while dead no longer leaves you with only the blade. In SBO 1.38 the loadout
  menu spawned you before your new choice had arrived

## HUD, chat and menus

- Added an offline copy of the docs to the game in `syndicate/manual/`, with search
- A new chat box shows names in green while alive, red while dead and yellow without a loadout
- Chat has been completely reimplemented using VGUI2, and as a result now supports name and chat colors, copy + paste, multi-line
  messages, history, unicode characters, and more
- You can click links in the chat while the chat line is open
- You can pick your chat and name colors with a color wheel next to the chat line. Other players see your colors
- The **Chat** tab in **Advanced** sets the chat text size, colors, new message sound and message time
- The chat marks spectators with `*SPEC*`, players without a loadout with `*NOLOAD*` and the Game Master with `*GM*`. In
  SBO 1.38 only dead players had a mark, `*DEAD*`
- The scoreboard shows Steam avatars
- In Co-op, the scoreboard shows the level and XP of each player, and the round with the number of rounds
- In Battle Royale and Bounty Killer, the scoreboard shows the frags left
- Every row of the scoreboard has a mute button
- A right-click on a scoreboard row lets you mute the player, open the Steam profile, or copy the name or SteamID
- In Bounty Killer, the scoreboard shows the Hunted first in its group, with a "(Hunted)" tag
- The scoreboard shows uncategorized players in a Ghosts section
- At the end of the map vote, a gold border draws around the winning map
- The kill feed has an icon for every SBO weapon and a turret icon. SBO 1.38 had no kill feed icons for them, so the
  game used the default skull icon as a fallback each time
- The kill feed shows a headshot icon for kills by a headshot
- The kill feed shows kills by monsters and kills of monsters, with the monster's name
- In Co-op, when a player kills another player, the kill feed shows the weapon icon in green
- Players talking on voice show their Steam avatars
- The console keeps a copy of every chat line with its time, such as `[12:34:56]`, and also shows kill lines and server
  text in their respective colors
- `hud_scale 1` makes the HUD larger on big screens
- `m_rawinput 1` turns on raw mouse input
- You can play with a gamepad
- Advanced options has three new settings: field of view, weapon tilt, and view roll
- Animated sprays are new in 2.0.0
- Servers can show a web page as their message of the day
- Discord shows your game status
- The **Advanced** window has a **Version** tab with the game version, **Check for updates** and a link to the credits
- You can now update the mod in-game using the updater
- The server browser, Options, Create server and the joining screen are new, and Half-Life's default menu style is
  still available in Advanced options
- The loadout, map briefing and message of the day windows are new
- Linux is now natively supported (1.38 only had a Linux server binary, no client)
- Kills by mounted guns and turrets show a turret icon in the kill feed. In SBO 1.38 they showed a skull
- Kill lines in the console now show the full name of the weapon instead of its class name, for example "Fists" instead of
  "wong"
- You can send up to 3 chat messages quickly one after the other. In SBO 1.38 the game dropped every message that came
  less than 1 second after the one before
- When the game drops a chat message because you send too fast, your console shows a notice. In SBO 1.38 the message was
  dropped without a notice
- The messages you get when you are hit, such as "My chest !!!", show at most once every 10 seconds for each body part.
  In SBO 1.38 they showed in the chat at every hit
- The "has left the game" chat line no longer starts with a dash, and the "changed name to" line no longer starts with
  an asterisk
- The radio and other text menus are larger on big screens
- The SourceMod-style radio menus have a dark background, so you can read them on bright maps
- Server menus show their color codes, such as `\y` and `\r`, as colors. In SBO 1.38 they showed the codes as text
- Servers can no longer change your mouse sensitivity
- SBO no longer ships a `config.cfg`, so updates keep your settings
- A new install gets new default keys: <kbd>Space</kbd> jumps, <kbd>E</kbd> uses, <kbd>R</kbd> reloads and <kbd>M</kbd>
  opens the model menu. In SBO 1.38 there was no jump key on <kbd>Space</kbd> and <kbd>M</kbd> had no game function
- <kbd>B</kbd> opens the map briefing (`showbriefing`). In 1.38, the only way to see the map briefing was by hitting
  <kbd>Enter</kbd> in spectator, which was removed in 2.0.0
- No default key quits the game anymore. In 1.38, F10 opened the quit window and F12 quit the game
- A new install leaves <kbd>Enter</kbd> unbound. In SBO 1.38, a new install used it for Use
- Fixed players in the menus or waiting for the next round seeing no chat. The game only sent chat to players it counted
  as in the game, and SBO 1.38 counted waiting players as observers instead, so they were skipped
- Team chat (`say_team`) has been removed, and <kbd>U</kbd> is no longer bound to it. In 1.38, the server ignored team
  messages, so they were never sent
- Fixed one radio call playing its sound once for every player on the server, all at the same time. The game played the
  sound again for each player that got the radio message. This was a bug in SBO 1.38
- Fixed the ammo counter still showing the last weapon's ammo after all your weapons are taken away. The HUD cleared
  only the crosshair. This was a bug in SBO 1.38
- Fixed demos that you record in the middle of a game playing back without your HUD. The game ignored the request for
  the HUD state that the engine sends when a recording starts. This was a bug in SBO 1.38
- Fixed the Mute button of the main menu's **Mute Players** window doing nothing. The game did not give the window the
  link it needs to mute a player. This was a bug in SBO 1.38
- Fixed long map briefings being cut off in the map briefing window. The window had no scroll bar. The text now scrolls.
  This was a bug in SBO 1.38
- Fixed long item descriptions being cut off in the loadout menu. The description box had no scroll bar. The text now
  scrolls. This was a bug in SBO 1.38

## Spectating

- Spectators have six camera modes: free look, locked chase, free chase, first person, free map overview and chase map
  overview. In SBO 1.38 there were only free look and the two chase modes, so first person, the map overviews and
  picture-in-picture weren't available
- Spectator mode is new: `/spec` or `/spectate` in the chat, or `spectate` in the console, turns it on and off. SBO 1.38
  had no spectator mode
- A spectator does not count as a player of the round
- A spectator stays a spectator through map changes, reconnects and server restarts
- A box above the spectator bar shows the watched player's health, armor, weapon, legs and score. Turn it on and off
  with `spec_drawinfo` in the console or **Options > Settings > Target Info**
- In first person, you see the watched player's crosshair and scope
- You can pick the free map overview with nobody to watch, to look over the map
- Map overview pictures can have up to eight layers now
- The spectator **Options** menu has a **Map Briefing** entry
- When you watch a player in a chase mode or in first person, you also see that player's "LEVEL UP" message
- Free look has no crosshair. In SBO 1.38 it showed a white crosshair
- The spectator settings for names, the view cone and the status stay when you restart the game. In SBO 1.38 they went
  back to their defaults
- With nobody to watch, joining players and new spectators start at the map's intermission points. In SBO 1.38 they
  started at a spawn point
- Fixed the spectator timer always showing "00:00". The game never updated it. It now shows the time left on the map, or
  the time played on Co-op maps. This was a bug in SBO 1.38
- Fixed the clock icon of the spectator bar being far away from the time on big screens. The gap between them grew with
  the screen size. This was a bug in SBO 1.38
- Fixed free look moving at the speed you had in your last life, instead of the spectator speed
  (`sv_spectatormaxspeed`). The game kept the speed limit of your last life. This was a bug in SBO 1.38
- Fixed the flashlight icon showing while you are dead, waiting or spectating. The game turned the icon on for every
  player out of the game when the server allowed the flashlight. This was a bug in SBO 1.38
- Fixed radiation (Geiger counter) clicks going on after you die or start spectating near radiation. The game stopped
  updating the counter, so the last clicks played on. This was a bug in SBO 1.38
- Fixed <kbd>Enter</kbd> opening the map briefing while you spectate. The game took the key for itself. The key now does
  only what you bind it to. This was a bug in SBO 1.38
- Fixed spinning objects pushing spectators around and turning their view. The game still treated dead and waiting
  players as walking, so a spinning object they touched carried them along
- Fixed players who join as a spectator or are still in the menus not seeing the map's flames and smoke. The game sent
  the flames and smoke to a player only at their first spawn. This was a bug in SBO 1.38

## Maps and mapping

- **Stock maps**
  - Every stock map has a new overview, with a picture per floor where needed
  - `bk_mongolito`, `br_mongolito` and `co_carnage` have the new rain, and `co_kill-the-doc` the new snow
  - `co_siege` and `co_forgottenworld` show a countdown during their last stand
  - Fixed the last wave of Feds on `co_necropolis` never coming. Its monster makers asked for a monster type that does
    not exist in SBO
  - Fixed some mortar strikes on `co_dfs` and `co_rain_of_fire` never coming. Their `multi_manager` has 22 targets, but
    SBO 1.38 fired only the first 16
  - Fixed the Fed Hunters in the `co_escape` prison never coming. Their monster makers are named and set to Start ON, so
    their first trigger turned them off. This was a bug in SBO 1.38
  - Fixed a distant mortar sound on `co_escape` never playing. It is the 17th target of a `multi_manager`, and SBO 1.38
    fired only the first 16. This was a bug in SBO 1.38
  - Fixed the rain and snow on `bk_mongolito`, `br_mongolito`, `co_carnage` and `co_kill-the-doc` crashing the game when
    the view was outside the map, for example in spectator free look. The weather code called itself without end when
    its start point was inside a wall. This was a bug in SBO 1.38
  - Fixed `co_appart` and `co_impappart` crashing the game when a player touched the bathtub water. The water had no
    collision data. This was a bug in SBO 1.38
  - Fixed `co_gore` never playing two of its announcements. SBO 1.38 did not include their sound files. This was a bug
    in SBO 1.38
  - Fixed a machine gun sound on `co_bunker13` never playing. The map named a sound file that does not exist. This was a
    bug in SBO 1.38
  - Fixed the pipe tops on `co_fondery` and `co_post-fondery` showing the missing-texture pattern. The maps pointed
    those faces at an empty texture slot. This was a bug in SBO 1.38
  - Fixed the `co_aemos` artifact failing the mission when someone shot it after a player took it. Taking the artifact
    only made it invisible, so it could still take damage. This was a bug in SBO 1.38
- **Movewith (experimental)**
  - Any entity can be attached to another entity and moves and turns with it, as in Spirit of Half-Life. Put the
    parent's name in the new Move with key (`movewith`)
  - [`trigger_changeparent`](mapping/entities/trigger_changeparent.md) gives an entity a new parent while the map runs
  - Movewith is experimental, test thoroughly when using it
- **Weather, fog and sky**
  - New entities: [`env_rain`](mapping/entities/env_rain.md), [`env_snow`](mapping/entities/env_snow.md),
    [`func_rainvolume`](mapping/entities/func_rainvolume.md), [`func_snowvolume`](mapping/entities/func_snowvolume.md),
    [`env_fog`](mapping/entities/env_fog.md), [`env_fogzone`](mapping/entities/env_fogzone.md),
    [`env_sky`](mapping/entities/env_sky.md)
  - `env_rain` and `env_snow` get the keys of the rain and snow volumes (amount, drop size, speed and more), and all
    four get wind keys to blow the rain or snow in a set direction
  - 3D skies (`env_sky`) now draw the entities in the sky room too, such as moving clouds, sprites and models, not only
    its brushes
- **Effects, lights and models**
  - [`color_correction`](mapping/entities/color_correction.md) and
    [`color_correction_volume`](mapping/entities/color_correction_volume.md): change the colors of the player's view
    (color grading), for the whole map or inside an area, with simple keys or `.raw` lookup files
  - [`env_overlay`](mapping/entities/env_overlay.md): show a static image, animated sprite, or a color tint over the
    player's screen
  - [`env_elight`](mapping/entities/env_elight.md): a dynamic light that lights models only
  - [`info_light_origin`](mapping/entities/info_light_origin.md): a model takes its lighting from this marker instead of
    beneath its origin
  - Other new entities: [`env_particle`](mapping/entities/env_particle.md),
    [`env_mirror`](mapping/entities/env_mirror.md), [`env_model`](mapping/entities/env_model.md),
    [`env_static`](mapping/entities/env_static.md), [`env_modeltrain`](mapping/entities/env_modeltrain.md),
    [`env_spritetrain`](mapping/entities/env_spritetrain.md), [`env_beamtrail`](mapping/entities/env_beamtrail.md),
    [`env_decal`](mapping/entities/env_decal.md), [`env_dlight`](mapping/entities/env_dlight.md),
    [`env_quakefx`](mapping/entities/env_quakefx.md), [`env_shockwave`](mapping/entities/env_shockwave.md),
    [`env_warpball`](mapping/entities/env_warpball.md),
    [`func_breakable_effect`](mapping/entities/func_breakable_effect.md),
    [`func_illusionary_toggle`](mapping/entities/func_illusionary_toggle.md),
    [`global_light_control`](mapping/entities/global_light_control.md),
    [`trigger_lightstyle`](mapping/entities/trigger_lightstyle.md), [`locus_beam`](mapping/entities/locus_beam.md)
  - Models can be scaled, can have fullbright textures, and can be placed with `env_model` and `env_static`
  - `env_model` has **Solid (model hitboxes)**, so a prop collides in the shape of its hitboxes
  - Light styles can change while the map runs, with `trigger_lightstyle` and `global_light_control`
  - The `objecthint` key works on any entity
- **Sound and music**
  - New entities: [`ambient_music`](mapping/entities/ambient_music.md),
    [`ambient_extraspeaker`](mapping/entities/ambient_extraspeaker.md),
    [`ambient_random`](mapping/entities/ambient_random.md), [`env_soundmark`](mapping/entities/env_soundmark.md)
  - `ambient_generic` plays MP3 files and has play modes
  - Buttons, doors and `momentary_door` can use custom sounds or sentences now
  - A map can have its own surface sounds and grass, with `materials_file` and the grass keys on `worldspawn`
- **Text, HUD and screens**
  - [`trigger_objective`](mapping/entities/trigger_objective.md): shows mission objectives in a panel on the player's
    screen, which players can switch between short, full and hidden with H. On maps that use it, the scoreboard also
    gets an objectives section that players can expand and collapse
  - [`info_waypoint`](mapping/entities/info_waypoint.md) marks a spot with an icon, a label and its distance in meters.
    It shows through walls and moves to the edge of the screen with an arrow when the spot is off the screen
  - Other new entities: [`point_worldtext`](mapping/entities/point_worldtext.md),
    [`vgui_screen`](mapping/entities/vgui_screen.md), [`vgui_control_proxy`](mapping/entities/vgui_control_proxy.md),
    [`game_playvideo`](mapping/entities/game_playvideo.md), [`game_messagebox`](mapping/entities/game_messagebox.md),
    [`game_timer`](mapping/entities/game_timer.md), [`env_tutor`](mapping/entities/env_tutor.md),
    [`trigger_sequence`](mapping/entities/trigger_sequence.md)
  - A map can have an HTML briefing, `maps/<map>.htm`
- **Logic and values**
  - [`info_alias`](mapping/entities/info_alias.md), [`multi_alias`](mapping/entities/multi_alias.md),
    [`trigger_changealias`](mapping/entities/trigger_changealias.md) and [`info_group`](mapping/entities/info_group.md):
    aliases, which are stand-in names that point to other entities and can be repointed while the map runs. Write
    `*name` in a Target, Kill target or Master to use whatever the alias `name` points to at that moment. For example,
    one button can open a different door after a `trigger_changealias` repoints its alias
    - `info_alias` points to one entity, and switches between two when it is turned on and off
    - `multi_alias` points to several entities at once, or picks one or some of them at random
    - `info_group` is a list of named members, used as `group.member`. When triggered, it points an alias at itself, so
      `*alias.member` switches to this group's members all at once
  - [`multi_watcher`](mapping/entities/multi_watcher.md) and [`watcher_count`](mapping/entities/watcher_count.md): watch
    other entities, for example whether a door is open, a monster is alive or a light is on, and fire their targets when
    that changes. They can also be used as a Master
  - Other new entities: [`trigger_changevalue`](mapping/entities/trigger_changevalue.md),
    [`trigger_copyvalue`](mapping/entities/trigger_copyvalue.md),
    [`trigger_compare`](mapping/entities/trigger_compare.md),
    [`trigger_condition`](mapping/entities/trigger_condition.md),
    [`trigger_random`](mapping/entities/trigger_random.md),
    [`trigger_random_unique`](mapping/entities/trigger_random_unique.md),
    [`trigger_timer`](mapping/entities/trigger_timer.md),
    [`trigger_entity_iterator`](mapping/entities/trigger_entity_iterator.md),
    [`game_number`](mapping/entities/game_number.md), [`calc_eval_number`](mapping/entities/calc_eval_number.md),
    [`calc_numfromvec`](mapping/entities/calc_numfromvec.md), [`calc_position`](mapping/entities/calc_position.md),
    [`calc_ratio`](mapping/entities/calc_ratio.md), [`calc_state`](mapping/entities/calc_state.md),
    [`calc_subvelocity`](mapping/entities/calc_subvelocity.md),
    [`calc_vecfromnums`](mapping/entities/calc_vecfromnums.md),
    [`calc_velocity_path`](mapping/entities/calc_velocity_path.md),
    [`calc_velocity_polar`](mapping/entities/calc_velocity_polar.md),
    [`locus_variable`](mapping/entities/locus_variable.md), [`env_state`](mapping/entities/env_state.md)
  - A target ending in `*`, for example `room1_*`, triggers every entity whose name starts with `room1_`
  - Target and Kill target accept `!activator`, the entity that started the chain (usually the player). Kill target
    `!caller` makes an entity remove itself
  - The game triggers entities named `game_round_start` and `game_round_end` at each round start and end,
    `game_round_<N>` when round N starts, `game_round_failed` when a round is lost, and `game_mission_success` or
    `game_mission_failed` when the mission ends
  - `multi_manager` can now fire up to 64 targets instead of 16 as in the original
  - `trigger_relay` has a Master
- **Triggers, movement and vehicles**
  - [`train_setspeed`](mapping/entities/train_setspeed.md): changes the speed of a moving `func_tracktrain`, at once or
    gradually, so a train can speed up, slow down or stop by itself
  - Other new entities: [`trigger_jump`](mapping/entities/trigger_jump.md),
    [`trigger_safe_fall`](mapping/entities/trigger_safe_fall.md), [`trigger_inout`](mapping/entities/trigger_inout.md),
    [`trigger_look`](mapping/entities/trigger_look.md), [`trigger_sensor`](mapping/entities/trigger_sensor.md),
    [`trigger_hurt_remote`](mapping/entities/trigger_hurt_remote.md),
    [`trigger_playerfreeze`](mapping/entities/trigger_playerfreeze.md),
    [`trigger_motion`](mapping/entities/trigger_motion.md), [`motion_manager`](mapping/entities/motion_manager.md),
    [`func_vehicle`](mapping/entities/func_vehicle.md),
    [`func_vehiclecontrols`](mapping/entities/func_vehiclecontrols.md),
    [`trigger_vehiclecontrols`](mapping/entities/trigger_vehiclecontrols.md)
  - `trigger_teleport` can use a landmark, so the player keeps their position and view relative to it (seamless
    teleports)
  - `trigger_gravity` can be switched on and off by name, has a Master, and has Start Off and Reset on leave options
  - `trigger_camera` has new All Players and Hide HUD and crosshair flags
  - Spawn points can be grouped into spawn sets by giving them a name, and the new Spawn set key of `multispawn`
    switches to any set, in any order
- **Monsters and monster makers**
  - New entities: [`monster_target`](mapping/entities/monster_target.md),
    [`scripted_action`](mapping/entities/scripted_action.md),
    [`scripted_schedule`](mapping/entities/scripted_schedule.md),
    [`scripted_following`](mapping/entities/scripted_following.md),
    [`scripted_tanksequence`](mapping/entities/scripted_tanksequence.md),
    [`trigger_startpatrol`](mapping/entities/trigger_startpatrol.md),
    [`trigger_killmonster`](mapping/entities/trigger_killmonster.md)
  - Monsters have an Unkillable key that keeps them from dying
  - Monsters have Classification and Is player ally keys. Feds dropped by an Osprey take the Osprey's Classification and
    Is player ally, so an allied Osprey drops allied Feds
  - Monster makers pass weapons, squads and spawnflags on to their monsters
  - A key written as `#name` on a monster maker is passed on as `name` to every monster it makes
  - `aiscripted_sequence` and `scripted_action` have an Idle Animation that the monster plays until the action is
    triggered, and `aiscripted_sequence` now has No Interruptions
  - `monster_apache` has a new Fire Rockets flag. In SBO 1.38 the Apache never fired rockets
  - `monster_apache` has a new No Wreckage flag (1024). Flag 8, which the editor called No Wreckage, is renamed Explode
    sooner, because that is what it always did
- **Players and items**
  - [`item_pickup`](mapping/entities/item_pickup.md), [`player_inventory`](mapping/entities/player_inventory.md) and
    [`player_hasinventory`](mapping/entities/player_hasinventory.md): items players pick up and carry, such as keys and
    keycards, and checks for whether a player carries them
  - Other new entities: [`player_hasweapon`](mapping/entities/player_hasweapon.md),
    [`game_player_settings`](mapping/entities/game_player_settings.md),
    [`player_capabilities`](mapping/entities/player_capabilities.md),
    [`player_speed`](mapping/entities/player_speed.md), [`player_flicker`](mapping/entities/player_flicker.md),
    [`player_calc_ratio`](mapping/entities/player_calc_ratio.md)
  - `game_player_settings` can set a player's `level` and `xp`
  - Spawn On Break of `func_breakable` and `func_pushable` accepts any item, weapon or ammo class name, not only the
    fixed list
- **Editors and testing tools**
  - In-game editors that you open from the console and use while you look at your map: `colorcorrectionui` for color
    correction looks (`.raw` files for `color_correction`), `particleeditorui` for particle effects (`.aur` files for
    `env_particle`) and `worldscreeneditorui` for world screen layouts (`.res` files for `vgui_screen`). They work in
    single player, in a game you host, and on a server with `sv_cheats 2`
  - New console commands for testing maps with `sv_cheats 1`, for example `cheat_noclip`, `ent_create` and `ent_fire`.
    The [cheat commands](mapping/getting-started/cheat-commands.md) guide lists all of them
  - Fixed a map started with `maxplayers 1` restarting when you pressed Go in the loadout menu. SBO 1.38
    treated a one-player game as Half-Life single player, which reloads the map when you spawn. You can now test a map
    alone with commands that only work in single player, such as `gl_wireframe`. This was a bug in SBO 1.38
- **Editor file and SDK**
  - The editor file is `syndicate.fgd`, with every entity of the game, editor icons and models
  - The editor file (FGD) uses the SBO monster names, has correct help text and defaults, and no longer lists keys and
    flags that do nothing
  - The sources of every shipped model and of `co_sbo_showcase` are included
  - Added an SDK download with example maps, prefabs and the FGD to each release
  - Removed `co_sbo_showcase` from the game download. It now comes with the SDK
  - Added `env_sky` tool texture to `sbo_tools.wad` for 3D skyboxes
  - Custom maps keep the behavior they had in 1.38
  - All file names are lower case, so `weapon_K444` is now `weapon_k444`. Linux servers treat upper and lower case as
    different names
- **Fixed: triggers, buttons and logic**
  - Fixed `trigger_changetarget` ignoring its Delay and its Kill target. It changed the target at once and never read
    either key
  - Fixed the Master key doing nothing on `button_target`, `trigger_hurt`, `trigger_push`, `trigger_monsterjump`,
    `momentary_rot_button` and a triggered `game_player_equip`. These entities never checked their Master, so they
    worked while locked
  - Fixed a `trigger_hurt` with only a Kill target not removing that target. It fired its targets only when it also had
    a Target
  - Fixed a healing `trigger_hurt` healing dead players. It did not check that the player was alive. This was a bug in
    SBO 1.38
  - Fixed `trigger_monsterjump` ignoring its Jump Speed and Jump Height. Every monster it threw went 200 units forward
    and 150 up. This was a bug in SBO 1.38
  - Fixed a `trigger_camera` started by a monster or a timer taking over the view of the player in the first server
    slot, even a spectator. When no player started the camera, the game gave the view to that slot
  - Fixed a `trigger_teleport` without a Target sending players to a random spot. An empty Target matched any entity
    without a name
  - Fixed `trigger_once` and `trigger_multiple` never playing their Sound to play. The game never loaded the sound. This
    was a bug in SBO 1.38
  - Fixed `game_zone_player` counting spectators as players inside or outside the zone. It counted every player slot.
    This was a bug in SBO 1.38
  - Fixed a delayed target losing its activator when a monster or another entity fired it. The game kept the activator
    only when it was a player. This was a bug in SBO 1.38
  - Fixed a `multisource` with a Delay before trigger flipping the wrong input. The delayed trigger was not one of its
    inputs, so it flipped the last one. This was a bug in SBO 1.38
  - Fixed entities with a Global Entity Name, such as some breakable objects, staying destroyed when the server changes
    back to their map. The game never cleared their saved state on a map change
  - Fixed `max_round` 1 and 2 being changed to 5. The game turned any value of 2 or less into 5
  - Fixed the Limitator giving 1 reserve ammo for a value of 0 or above 910. A value of 0 now gives none, and anything
    above 900 gives 900, the most a player can carry
  - Fixed a Limitator key that you leave out keeping the value of the map played before. The game never reset the values
    between maps. It now gives the amount of a map without a Limitator. This was a bug in SBO 1.38
- **Fixed: doors, buttons, trains and mounted guns**
  - Fixed rotating buttons never playing their locked and unlocked sounds. The game never loaded those sounds for
    rotating buttons
  - Fixed buttons with the Sparks flag never sparking. The spark timer used the wrong clock, so the sparks never came.
    Buttons on `co_aemos` and some custom maps have this flag. This was a bug in SBO 1.38
  - Fixed a `func_door_rotating` with Starts Open never opening again after it closed. Its open and closed angles ended
    up the same. This was a bug in SBO 1.38
  - Fixed `momentary_door` never playing its Stop Sound. The game read the key but never used it. This was a bug in SBO
    1.38
  - Fixed `momentary_door` playing its move sound on after it stopped. It never stopped the sound when it arrived. This
    was a bug in SBO 1.38
  - Fixed fans and other spinning objects always playing their sound at full volume, ignoring whatever volume the mapper
    set. The game read the volume key under a differently written name, so it never found it
  - Fixed a moving `func_guntarget` not stopping when triggered. It restarted from its next stop instead
  - Fixed the New Train rot. Speed key of `path_corner` being ignored. The game never read the key
  - Fixed a `func_trackautochange` crashing the server when a trigger without an activator used it. The game used the
    activator without checking that there was one
  - Fixed `func_trackchange` and `func_trackautochange` crashing the server after their train was removed. They still
    pointed to the removed train. This was a bug in SBO 1.38
  - Fixed the trigger of a removed `func_plat` crashing the server. The trigger still pointed to the removed platform.
    This was a bug in SBO 1.38
  - Fixed a laser gun (`func_tanklaser`) keeping its beam on after the player left the controls. The gun stopped its own
    updates, so it never turned the beam off. This was a bug in SBO 1.38
  - Fixed a laser gun (`func_tanklaser`) that a Kill target removes right after a shot leaving its beam on. The game
    removed the gun but not its beam. This was a bug in SBO 1.38
- **Fixed: monsters and monster makers**
  - Fixed a named monster maker with Start ON not starting with the map (its first trigger turned it off)
  - Fixed a bug in monster maker set to unlimited monsters (-1) stopping after about 4.29 billion monsters had been
    spawned. If anyone wants to confirm, run the any map for 138 years and let me know if it's fixed
  - Fixed a monster maker without a monster type stopping the server when the map loaded. It tried to load a monster
    with an empty name
  - Fixed a monster that a Kill target removes while alive keeping its place in its monster maker. The maker counted
    only monsters that died, so it made fewer monsters. This was a bug in SBO 1.38
  - Fixed a shot-down Apache or Osprey keeping its place in its monster maker. The maker never heard that it died. This
    was a bug in SBO 1.38
  - Fixed a destroyed turret or Sentry Gun keeping its place in its monster maker. The maker never heard that it died.
    This was a bug in SBO 1.38
  - Fixed an Apache from a monster maker with MonsterClip waiting for a trigger forever. The MonsterClip flag has the
    same value as the Apache's Wait for trigger flag. This was a bug in SBO 1.38
  - Fixed a monster maker of 1 monster making monsters without end when the server halves monster counts. Half of 1 is
    0, which the maker read as no limit. This was a bug in SBO 1.38
  - Fixed turrets, Sentry Guns, the Apache and the Osprey never firing their Trigger Condition. In SBO 1.38, their own
    AI code never checked it
  - Fixed Ignore Friendly Damage turning off on Feds, Heavy Weapons Feds, Fed Hunters, Assassins and Sentry Guns when
    the map gave another key after it. Every later key set it back to off. This was a bug in SBO 1.38
  - Fixed the Sentry Gun ignoring its Custom Turning Rate. It never read the key. This was a bug in SBO 1.38
  - Fixed Wait until provoked doing nothing on Sectum, Demon Slaves, Demon Slave Hunters, Werewolves and Werewolf
    Hunters. They attacked as soon as they saw a player. This was a bug in SBO 1.38
  - Fixed a Werewolf with a Target walking its path only after it calmed down. It started alert instead of idle. This
    was a bug in SBO 1.38
  - Fixed a triggered `monster_grunt_hunter_repel` crashing the server. It tried to create a monster type that does not
    exist in SBO. This was a bug in SBO 1.38
  - Fixed a dead Cop, Fed or Scientist with a Pose outside the list crashing the game when the map loaded. The game did
    not check the number. This was a bug in SBO 1.38
  - Fixed an Osprey on a closed path with no fast corner hanging the server. It searched the path for a fast corner
    without end. This was a bug in SBO 1.38
  - Fixed a hit Osprey smoking from its other engine. A hit on one engine made the other one smoke. This was a bug in
    SBO 1.38
  - Fixed a `scripted_sequence` with Move to Position "No - Turn to Face" hanging the script. The game did not know this
    choice. This was a bug in SBO 1.38
  - Fixed a `scripted_sequence` that a Kill target removes while its monster waits for it or plays it crashing the
    server. The monster still pointed to the removed sequence. This was a bug in SBO 1.38
  - Fixed a trip mine that a Kill target removes leaving its beam behind. The game removed the mine but not its beam.
    This was a bug in SBO 1.38
- **Fixed: effects, sound and map loading**
  - Fixed `env_blood` giving red blood for every color except yellow. The game knew only the yellow color and used red
    for all others. This was a bug in SBO 1.38
  - Fixed a removed `env_laser` leaving its end sprite behind. The game removed the laser but not its end sprite. This
    was a bug in SBO 1.38
  - Fixed Gibs Direction "Relative to Attack" on `func_breakable` and `func_pushable` doing nothing. The game read the
    value the editor writes as random, so the gibs flew in random directions. This was a bug in SBO 1.38
  - Fixed a removed `xen_plantlight` leaving its glow in the air, and a removed `xen_tree` leaving its attack area
    behind. The game removed the entity but not its parts. This was a bug in SBO 1.38
  - Fixed `trigger_cdaudio` and `target_cdaudio` playing their music only for the player in the first server slot. The
    game sent the music only to that slot. This was a bug in SBO 1.38
  - Fixed `item_sodacan` stopping the server unless the map also had an `env_beverage`. Only `env_beverage` loaded the
    can's model. This was a bug in SBO 1.38
  - Fixed a `game_player_equip` that gives an item the map does not place crashing the server. The game never loaded the
    item
  - Fixed `game_score` and `game_player_hurt` crashing the server when no player started the chain. The game used the
    player without checking that there was one. This was a bug in SBO 1.38
  - Fixed a `game_player_equip` with a very large count giving items until the server stopped responding. The count had
    no upper limit. This was a bug in SBO 1.38
  - Fixed `game_player_equip` keys that are not items being created on the player as entities. The game read every key
    it did not know as an item name. This was a bug in SBO 1.38
  - A `cycler`, `monster_generic`, `monster_furniture`, `change_touch` or `env_glow` with a missing model or sprite is
    removed when the map loads. In SBO 1.38 the map did not load

## Server

See [Server settings](server/settings.md) for every setting.

- The game's settings have SBO's defaults in the game itself, and `game.cfg` no longer overrides `server.cfg` on every
  map
- The default for `mp_hardcore` is now 100 instead of 80
- On a listen server, the default time limit is now 20 minutes instead of 15, and Game Master mode is now off by default. A dedicated
  server already got these values from `server.cfg`
- The default for `mp_autocrosshair` is now 0 instead of 1
- A server without a name is called "Syndicate Black Ops Server", not "Half-Life"
- New `server.cfg` and `listenserver.cfg` files explain every setting, and `mp_hardcore` defaults to 100
- The shipped `server.cfg` sets `sv_minrate 25000`, `sv_minupdaterate 30` and `sv_maxupdaterate 100`
- Older clients are refused with a message asking the player to update
- The next map loads `mp_chattime` seconds after the end-of-map scoreboard shows. In SBO 1.38 it also waited up to 2
  minutes for a key press, and a click on the scoreboard did not count as one
- A text message of the day can be 3072 bytes long. In SBO 1.38 the limit was 1536 bytes
- New settings: `mp_loadouttime`, `mp_missionendtime`, `mp_semiclip`, `mp_semiclip_time`, `mp_semiclip_effects`,
  `mp_afk_time`, `mp_afk_spectate_time`, `mp_killfeed_npc`, `sv_infinite_ammo`, `sv_allowbunnyhopping`,
  `sv_pushable_fixed_tick_fudge` and `mp_map_compat`
- The read-only settings `mp_round`, `mp_roundlimit` and `game_version` show the round, the round limit and the game
  version
- `mp_speedmon -1` turns off the map's monster makers
- The server command `gm_toggle <name or #userid>` turns a player's Game Master mode on or off
- `mp_allowmonsters` is removed. In SBO 1.38 the setting worked the wrong way round: 1 removed every monster
- `mp_XP` has been removed. XP and levels are always on, and Create server no longer shows the option
- `mp_falldamage` has been removed. It did nothing, fall damage always depends on the speed of the fall
- The server log has round and mission lines
- The server log writes a player killed by a monster as killed by that monster. In SBO 1.38 it wrote that death as a
  suicide
- The server log names each gun turret in its [kill lines](server/logs.md#kills)
- The server log has a line for each player with their game version, system, engine and renderer, and a line for each
  player it turns away for an old game version
- The Linux server library is `dlls/hl.so`
- Maps can use up to 2048 entities
- The server prints its version at startup
- Fixed the shipped `game.cfg` resetting the **Create server** choices of a listen server on every map. It forced its
  own values on every map load
- Fixed a dedicated server starting in LAN mode, without VAC. The shipped `game.cfg` set `sv_lan 1` before the server
  started
