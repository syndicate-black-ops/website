# Discord [[ported:openag discordrpc]]

While the Discord desktop app is running, SBO shows what you are doing in your Discord profile, which Discord calls
Rich Presence. The game only talks to the Discord app on your own computer and sends nothing anywhere else.

## What Discord shows

| Field | In the main menu | In a game |
|---|---|---|
| First line | "In the main menu" | The server's name, or "Playing online" for a server without a name |
| Second line | Nothing | The game mode and the map, for example `Co-op \| co_aemos`. While you spectate, `\| Spectating` is added |
| Party | Nothing | The number of players on the server and its number of slots |
| Time | Nothing | How long you have been on the current map |
| Image | The SBO logo, with the tooltip "Syndicate Black Ops" | The SBO logo, with the map's name as its tooltip |

The game mode is taken from the map name: `co_` maps show **Co-op**, `br_` maps show **Battle Royale** and `bk_`
maps show **Bounty Killer**.

## Settings {#turning-it-off}

| Cvar | Default | Effect |
|---|---|---|
| `cl_discord_rpc` | 1 | Shows your current game details in your Discord profile. Setting it to 0 turns Rich Presence off, and Discord stops showing your game right away. The same setting can be found in **Advanced > General > Discord Rich Presence** |

## Changes since 1.38

- Discord shows your game status

## See also

- [Options](options.md) - the Advanced options, where you turn it off
- [Menus](menus.md) - the game's menus and windows
