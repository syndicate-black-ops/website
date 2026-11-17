# Server files

You set up the server, choose its maps and write the texts players see with these files in the server's `syndicate`
folder.

## Config files

| File | When it runs |
|---|---|
| `game.cfg` | First at every map start. It sets nothing |
| `server.cfg` | At every map start on a dedicated server, after `game.cfg` |
| `listenserver.cfg` | At every map start on a listen server, after `game.cfg` |

`server.cfg` and `listenserver.cfg` list the game's settings with their default values and a comment for each. See
[Server settings](settings.md) for more details. They also set engine settings such as `sv_aim 0`,
`sv_maxspeed 2000`, `sv_spectatormaxspeed 500`, `pausable 0` and the rates. To name your server, remove the `//` in
front of the `hostname` line of `server.cfg`, or add a `hostname "My Server"` line to `listenserver.cfg`. A server
without a name is called "Syndicate Black Ops Server". To make the server run other files instead, name them in the
engine cvars `servercfgfile` and `lservercfgfile`.

On a listen server, a value that `listenserver.cfg` sets replaces the value you chose in **Create server**. To choose a
setting in the menu, leave its line commented out in the file.

When the game [updates itself](../playing/installing.md#updates), it replaces `server.cfg`, `listenserver.cfg`,
`mapcycle.txt` and `motd.txt` if you haven't changed them. If you have changed one of them, the update keeps your file
and writes the new version next to it as `<name>.new`.

## Map cycle

`mapcycle.txt` lists the maps the server plays in turn, one map per line, in Half-Life's format. You can name another
file in the engine cvar `mapcyclefile`.

A Co-op map changes to the next map of the cycle when its mission ends, whether the mission succeeded or failed. Bounty
Killer and Battle Royale maps change when they reach `mp_timelimit` or `mp_fraglimit`. In every mode, the next map
loads `mp_chattime` seconds after the end-of-map scoreboard shows.

## Message of the day [[ported:bhl]]

The message of the day (MOTD) is the file that the engine cvar `motdfile` names, `motd.txt` by default. Every player
who joins sees it before the map briefing, and the server sends at most 3072 bytes of it.

The players' game looks at the first characters of the MOTD to decide how to show it:

| The MOTD starts with | Shown as |
|---|---|
| `http://` or `https://` | The web page at that address |
| `<!DOCTYPE html` or `<html`, in any case | A web page |
| Anything else | Plain text |

The game draws web pages with the Steam client's browser, so players who don't have Steam running, or who set
`cl_disablehtmlmotd 1`, see the MOTD as text. An HTML MOTD written for Counter-Strike 1.6 works without changes.

## Map briefings

A map's briefing is the file `maps/<map>.txt`. The briefing window shows it after the MOTD, and players can open it
again with the map briefing key (Default: <kbd>B</kbd>). See [Menus](../playing/menus.md#map-briefing) for more
details.

You can also write a web page version of the briefing as `maps/<map>.htm`. Players who can see web pages get the
`.htm` file, and the others get the `.txt` file. A few rules apply to it:

- The extension must be `.htm`, because players can't download `.html` files from a server
- The game looks for pictures and style sheets next to the page, so `<img src="co_mymap_1.png">` loads
  `maps/co_mymap_1.png`
- You must list the `.htm` file and its pictures in `maps/<map>.res`, or players won't download them
- If a map has a `.htm` file but no `.txt` file, players who can't see web pages get "No description for this map"

## Map compatibility

`maps/map_compat.txt` keeps some custom maps playing the way they did in SBO 1.38. These maps happen to carry keys
that SBO 2.0.0 and later read, so each entry in the file drops such a key, or changes its value, on the map's entities
while the map loads. The game ships the file and the server reads it from its game folder, so players don't download
anything.

An entry names the map and the CRC-32 checksum of its `.bsp` file. An updated map has a different checksum, so the
entries for the old version don't apply to it.

```
// comment
<map> <crc32> drop <classname> <selector> <key>
<map> <crc32> set  <classname> <selector> <key> <value>
```

| Selector | Entities |
|---|---|
| `*` | Every entity of the class |
| `#N` | The entity at index N of the map's entity list, where 0 is [`worldspawn`](../mapping/entities/worldspawn.md) |
| A name | Every entity of the class with that `targetname` |

The parts of a line are separated by spaces or tabs, and a part in quotes can contain spaces. The game skips lines it
can't read. With `developer 1` set in the server console, the console prints one note about skipped lines, each change,
and how many entities each entry changed. A line can have up to 511 characters and each part up to 127, a map
can have up to 64 entries, and a `#N` or name selector can match up to 64 entities.

You can turn the file off with the server setting [`mp_map_compat`](settings.md#maps) in the server console or `server.cfg`.

## Spectator list

`spectators.txt` in the game folder lists the Steam IDs of the players in spectator mode, one per line. It keeps up to
256 IDs, and when it is full the game forgets the oldest one. The game writes the file when a player enters or leaves
spectator mode and reads it when the server starts, so players stay in spectator mode through a server restart.

## Changes since 1.38

- Servers can show a web page as their message of the day
- Map briefings can be web pages (`maps/<map>.htm`)
- A text message of the day can be 3072 bytes long. In SBO 1.38 the limit was 1536 bytes
- New `server.cfg` and `listenserver.cfg` files explain every setting, and `mp_hardcore` defaults to 100
- The shipped `server.cfg` sets `sv_minrate 25000`, `sv_minupdaterate 30` and `sv_maxupdaterate 100`
- A server without a name is called "Syndicate Black Ops Server", not "Half-Life"
- Fixed a dedicated server starting in LAN mode, without VAC. The shipped `game.cfg` set `sv_lan 1` before the server
  started
- `maps/map_compat.txt` keeps some custom maps playing the way they did in SBO 1.38
- `spectators.txt` keeps players in spectator mode through a server restart

## See also

- [Server settings](settings.md) - every setting, with its default
- [Menus](../playing/menus.md) - the game's menus, the MOTD and the briefing window
