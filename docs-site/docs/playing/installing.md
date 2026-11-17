# Downloading & Installing

SBO 2.0.0 and newer require the Half-Life 25th Anniversary update on Steam. Using `steam_legacy` or any other Steam
beta has not been tested, so you may have odd bugs or a reduced experience.

## Downloading releases

[Download the latest release (v<LatestRelease />)](https://github.com/syndicate-black-ops/syndicate-black-ops/releases/latest).
The zip holds two folders:

| Folder | What it is |
|---|---|
| `syndicate/` | The game folder, with the Windows and Linux game libraries, the FGD, the editor models and sprites, and an offline copy of these docs in `manual/` (open `index.html`) |
| `syndicate_addon/` | An empty folder with a short readme that tells you how to add your own content, which [Other game folders](#other-game-folders) explains |

Each GitHub release also has these files. You don't need them to play, so if you don't know what they are, you can skip
them:

| File | What it is |
|---|---|
| `sbo-sdk-v<version>.zip` | The SDK for mappers: the FGD, the example maps with their readmes, prefabs, an example sequence and an example video. See [Editor setup](../mapping/getting-started/editor-setup.md) for more details |
| `SHA256SUMS` | The SHA-256 checksums of the zips, so you can check that each file downloaded correctly |
| `manifest.json` and `manifest.json.sig` | The signed list of files that the game's updater reads. The game installs an update only if the SBO release key signed this list, so nobody else can send you an update. It also checks each file it downloads against the list, and it doesn't install a file that is damaged or changed |

## Windows

1. Open your Half-Life folder, which usually is `C:\Program Files (x86)\Steam\steamapps\common\Half-Life`. You
   can also right-click Half-Life in your Steam library and pick **Manage > Browse local files**
2. Copy the `syndicate` and `syndicate_addon` folders from the zip into the Half-Life folder. If you already have
   these folders, copy over them
3. If this is the first time you install SBO, restart Steam, so that the game shows in your library
4. Start the game from your Steam library, where it is called "Syndicate Black Ops", or with
   `hl.exe -game syndicate`

## Linux

Each release includes the Linux game libraries. On Linux, the game folder is usually
`~/.local/share/Steam/steamapps/common/Half-Life/syndicate`.

## Updates

The game looks for a new version when it starts. If one is available, a window opens over the main menu showing the new
version and its release notes, with three options:

- **Update** - downloads only the files that changed and checks them, and then **Install and quit** quits the game
  to install them. You must start the game again afterwards
- **Skip this version** - hides that version until a newer one comes out
- **Later** - asks again at the next start

An update only replaces the files that come with SBO, so your own maps and settings stay. If you replace game files
with your own, for example models or sounds, put them in [`syndicate_addon`](#other-game-folders) and not in
`syndicate`, because the next update can overwrite them there.

If you set `cl_check_for_updates` to 0, you can check yourself: press **Check for updates** on the **Version** tab of
**Advanced**, or type `update_check` in the console.

### Update settings

| Cvar | Default | Effect |
|---|---|---|
| `cl_check_for_updates` | 1 | Checks for a new version every time the game starts. Set it to 0, and the game checks only when you press **Check for updates** yourself |

## Other game folders

Half-Life reads files from several folders in the order below. If two folders hold a file with the same name, the
game uses the one from the folder that comes first.

| Folder | What it holds |
|---|---|
| `syndicate_lv` | Low-violence files, which the game uses while the content lock is on |
| `syndicate_addon` | Your own content, which the game uses when **Allow custom addon content** in **Options > Content** is on, or when you start the game with `-addons` |
| `syndicate_<language>` | Translated files, which the game uses when Steam runs Half-Life in that language |
| `syndicate_hd` | HD models, which the game uses unless **Use the original Half-Life models** in **Options > Content** is on. SBO ships no HD models, but this setting also turns on the HD models that Valve ships with Half-Life, such as the Scientist models, G-Man, and others |
| `syndicate` | The game itself |
| `syndicate_downloads` | Files the game downloads from servers, such as custom maps |
| `valve` | Half-Life's own files, for anything SBO doesn't have |

If you change either of the two **Content** settings, the game restarts to apply it.

## Notes

- If you copy a new release over an older `syndicate` folder, the copy doesn't delete the files that the new release
  no longer has, so they stay in the folder. The in-game updater deletes them if you didn't change them

## Changes since 1.38

- Linux is now natively supported (1.38 only had a Linux server binary, no client)
- You can now update the mod in-game using the updater

## See also

- [Controls](controls.md) - the default keys and how to change them
- [Options](options.md) - the game's settings, including the update settings
