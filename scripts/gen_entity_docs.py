#!/usr/bin/env python3
"""Entity pages of the SBO documentation site, generated from sdk/syndicate.fgd.

    scripts/gen_entity_docs.py              write docs-site/docs/mapping/entities/
    scripts/gen_entity_docs.py --out DIR    write the pages into DIR instead
    scripts/gen_entity_docs.py --check      write nothing; exit 1 on a problem (list below)
    scripts/gen_entity_docs.py --icons      also rewrite the editor-sprite icons and the letter tiles in
                                            docs-site/static/img/entities/ (needs the Git LFS files of
                                            sdk/spritesrc/editor/ and gamedir/syndicate/sprites/editor/)
    scripts/gen_entity_docs.py --list-no-icon   the entities with no picture in docs-site/static/img/entities/

Output (Docusaurus MDX in .md files, so the pages' relative .md links stay valid), one page per FGD class (except
HIDDEN_CLASSES):

    docs-site/docs/mapping/entities/<class>.md         the entity page: front matter, the header (picture, type,
                                                       "Ported from"), the summary, the Attributes and Flags as
                                                       components (src/components/Entity), the other sections
    docs-site/docs/mapping/entities/index.md           the Entity List (src/components/EntityTable)
    docs-site/docs/mapping/entities/entity-index.json  its rows: class, summary, picture, type, group
    docs-site/docs/mapping/entities/common-keys.md     the keys and flags of the common base classes (COMMON), once
                                                       each, by topic (TOPICS below)
    docs-site/docs/mapping/entities/sidebar.json       the Entities part of the navigation (sidebars.ts), by group
    docs-site/docs/mapping/guide/monster-classes.md    the Monster classes page: the class relationship grid and the
                                                       class of each monster, read from src/dlls with
                                                       scripts/gen_monster_classes.py (template:
                                                       docs-site/templates/monster-classes.md; with --out, written
                                                       into DIR)

The pages are build output (docs-site/.gitignore): CI and a local build run this script before Docusaurus. They
are first put together as Markdown (the style checks read that), then turned into MDX (entity_mdx). The pictures
in docs-site/static/img/entities/ are committed (icon_source: an editor sprite, a model render or a letter
tile; docs-site/README.md).

An entity page is put together from four sources:

1. docs-site/provenance.yml: the "Ported from" icons (one per project) of the class, of
   single keys and of single flags. Format: the comment at the top of that file.
2. sdk/syndicate.fgd: the title, the keys (key name, editor name, default, choices, the FGD help text) and the
   flags. The rows of the Targetname, Target, Targetx and Master bases (INLINE_COMMON) are part of an entity's
   own table where the row's text or default differs from the key's row on common-keys.md (inline_repeats);
   the keys and flags of the other common base classes, and those rows, are on common-keys.md, and the entity
   page links its sections there with the keys it has (common_links). A common flag stays in the page's own Flags
   list only if its entity-text has a bullet for it.
3. docs-site/entity-text/<class>.md (hand-written, committed), in the layout of the approved samples:
   - an optional front matter block with a "description:" (at most 155 characters): the page's short
     description for link previews, where the summary's first sentence is longer than that;
   - the text before its first "## " heading is the summary, placed under the title and the icons;
   - a "## Attributes" section holds one bullet per key, in any order (the table keeps the editor's order):
         - **Plain name** (`key`) - What the key does.
             - Choice name (value) - what this choice does        (one line per choice; "(value, default)")
             - other list lines                                    (shown after the choices)
             - If you leave this key empty, ...                    (only where that differs from the default)
     Continuation lines are indented. The name must be the editor name or its start without the value hints;
     the Default column comes from the FGD (a "Default X" at the end of the text must agree with it); the icons
     come from provenance.yml (a [[ported:...]] marker after the name must agree with it). Any other text of
     the section is placed above the table;
   - a "## Flags" section the same way: "- **Name** (value) - what it does";
   - every other "## " section (topic sections, Notes, See also, Changes since 1.38), in its order, is placed
     after the tables, with the full stop at the end of each list line removed.
   The older format ("## Keys" with "- `key`: text", "- `8`: text" under "## Flags") is still read. A file with
   "## Attributes" or "## See also" counts as rewritten and gets the style checks.
   Without a text file, the page has the FGD title as its summary. A file with "## Attributes" is also checked
   for the words the style rules forbid and for list lines that end in a full stop (style_problems).
4. docs-site/key-help/*.yml: descriptions of key and flag rows that have no entity-text bullet, per class or base
   class (load_key_help); they win over the FGD help text. Every row must end up with a description:
   --list-empty prints the rows without one, and --check fails on them. --list-fgd-help prints the rows that
   still show the FGD's own help text. key-help/names.yml maps FGD labels that plain_name() can't clean to their
   plain names.

Entity class names and the keywords !activator, !caller, *locus and *player are linked wherever they appear in
the text (autolink), except the page's own class name.

--check fails (one line per problem) on: a class with no group, a text file or provenance entry for a class,
key, flag or project that does not exist, a Keys/Flags bullet that names no key or flag of the class, words
that must never appear on the site (FORBIDDEN). A class without a text file and a class without a picture are
listed as warnings.

Python 3; the only module outside the standard library is PyYAML.
"""

import argparse
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import fgd  # noqa: E402  (scripts/fgd.py: tokenizer and parser helpers)
import gen_monster_classes  # noqa: E402  (the Monster classes page, read from src/dlls)

FGD_PATH = os.path.join(REPO, "sdk", "syndicate.fgd")
SITE = os.path.join(REPO, "docs-site")
OUT_DIR = os.path.join(SITE, "docs", "mapping", "entities")
MONSTER_CLASSES_PATH = os.path.join(SITE, "docs", "mapping", "guide", "monster-classes.md")
TEXT_DIR = os.path.join(SITE, "entity-text")
DESCRIPTION_MAX = 155   # the short description of a link preview (docs-site/plugins/social-cards.mjs)
PROVENANCE_PATH = os.path.join(SITE, "provenance.yml")
KEY_HELP_DIR = os.path.join(SITE, "key-help")
ICON_DIR = os.path.join(SITE, "static", "img", "ported")
ENTITY_ICON_DIR = os.path.join(SITE, "static", "img", "entities")   # <class in lower case>.png, committed (--icons)
ENTITY_ICON_URL = "/img/entities/"
NAV_DIR = "mapping/entities"  # the pages' doc id prefix (relative to docs-site/docs/)

# The common base classes: their keys are linked on common-keys.md, not repeated on each entity page.
COMMON = ["Targetname", "Target", "Targetx", "Master", "Global", "Angles", "RenderFields", "Effects",
          "ModelScale", "BodySkin", "Body", "Skin", "ZHLT", "ZHLT_point", "Monster", "MonsterQuiet", "MonsterCore",
          "MonsterUnkillable", "MonsterFlags", "MonsterClip", "MonsterGag", "MonsterFadeCorpse",
          "MonsterNonSolidCorpse", "MonsterActOutOfPVS", "MonsterTriggers", "MonsterBody", "MonsterSound",
          "MonsterRoam", "TalkMonster"]

# common-keys.md, by topic: every key and flag of the common bases (and of the bases they include) once. A section is
# (anchor, heading level, heading, intro, items, old anchors). An item is "Base.key" or "Base#flag value", with the
# anchors of its row after a space (the first names the row; the others are anchors of the per-base page layout, so
# old links still land on the key). The level-2 sections (and the level-3 Compiler and Talking monsters sections)
# are what entity pages link to (TOPIC_LINKS).
TOPICS = [
    ("naming", 2, "Naming and triggering",
     "An entity page shows **Name**, **Target**, **Delay before trigger**, **KillTarget** and **Master** in its "
     "own key table only where the key does something of its own on that entity.",
     ["Targetname.targetname targetname", "Target.target target", "Targetx.delay delay targetx",
      "Targetx.killtarget killtarget", "Master.master master", "Global.globalname globalname global"], []),
    ("position", 2, "Position", "", ["Angles.angles angles"], []),
    ("appearance", 2, "Appearance",
     "These keys set how the engine draws the entity. No entity offers Half-Life's flag 2048 (Not in Deathmatch): "
     "the engine removes every entity that has it when an SBO server loads the map.",
     ["RenderFxChoices.renderfx renderfx renderfields", "RenderFields.rendermode rendermode",
      "RenderFields.renderamt renderamt", "RenderFields.rendercolor rendercolor", "Effects.effects effects",
      "ModelScale.scale scale modelscale", "Body.body body bodyskin", "Skin.skin skin"],
     ["flag-not-in-multiplayer", "appearflags"]),
    ("compiler", 2, "Compiler keys",
     "The map compiler reads these keys when it builds the map, and the game doesn't use them.", [], []),
    ("zhlt", 3, "Brush entities", "",
     ["ZHLTCopyTarget.zhlt_usemodel zhlt_usemodel", "ZHLTCopyTarget.zhlt_copylight zhlt_copylight",
      "ZHLTCopyTarget.light_origin light_origin", "ZHLT.zhlt_noclip zhlt_noclip",
      "ZHLT.zhlt_lightflags zhlt_lightflags", "ZHLT.zhlt_invisible zhlt_invisible",
      "ZHLT.zhlt_customshadow zhlt_customshadow", "ZHLT.zhlt_embedlightmap zhlt_embedlightmap",
      "ZHLT.zhlt_embedlightmapresolution zhlt_embedlightmapresolution", "ZHLT._minlight _minlight"], []),
    ("zhlt_point", 3, "Lights", "", ["ZHLT_point._fade _fade", "ZHLT_point._falloff _falloff"], []),
    ("monsters", 2, "Monsters",
     "Not every monster has all of these keys and flags. The page of each monster names the ones it has.", [],
     ["monster", "monsterquiet"]),
    ("monster-class", 3, "Class and side", "",
     ["MonsterCore.classify classify", "MonsterCore.is_player_ally is_player_ally",
      "MonsterCore.prisonerto prisonerto", "MonsterCore.ignoredby ignoredby", "MonsterFlags#16 flag-prisoner"],
     ["monstercore"]),
    ("monster-health", 3, "Health", "", ["MonsterUnkillable.unkillable unkillable monsterunkillable"], []),
    ("monster-senses", 3, "Sight, sound and movement", "",
     ["MonsterCore.field_of_view field_of_view", "MonsterSound.soundmask soundmask monstersound",
      "MonsterRoam.freeroam freeroam monsterroam", "MonsterRoam.active_alert active_alert",
      "MonsterFlags#1 flag-waittillseen monsterflags", "MonsterGag#2 flag-gag monstergag",
      "MonsterClip#4 flag-monsterclip monsterclip", "MonsterActOutOfPVS#1048576 flag-act-out-of-pvs monsteractoutofpvs"],
     []),
    ("monster-triggers", 3, "Triggers", "",
     ["MonsterCore.trigger_on_death trigger_on_death", "MonsterTriggers.triggertarget triggertarget",
      "MonsterTriggers.triggercondition triggercondition", "MonsterTriggers.triggeraltcondition triggeraltcondition"],
     ["monstertriggers"]),
    ("monster-body", 3, "Blood, gibs and corpse", "",
     ["MonsterBody.bloodcolor bloodcolor", "MonsterBody.gibmodel gibmodel", "MonsterBody.gib_policy gib_policy",
      "MonsterFadeCorpse#512 flag-fade-corpse monsterfadecorpse",
      "MonsterNonSolidCorpse#65536 flag-non-solid-corpse monsternonsolidcorpse"], ["monsterbody"]),
    ("talkmonster", 3, "Talking monsters", "{users} also have these keys and flags.",
     ["TalkMonster.usesentence usesentence", "TalkMonster.unusesentence unusesentence",
      "TalkMonster.voicepitch voicepitch", "TalkMonster.followage_policy followage_policy",
      "TalkMonster.followfailpolicy followfailpolicy", "TalkMonster.suspicious suspicious",
      "TalkMonster.tolerance tolerance", "TalkMonster.alert_friends alert_friends",
      "TalkMonster.refusalsentence refusalsentence", "TalkMonster.speakas speakas",
      "TalkMonster#256 flag-pre-disaster", "TalkMonster#524288 flag-ignore-move-away-requests"], []),
]
# Keys of a common base that are the same key as an item above: the row of that item describes them too (the
# key-help text of the alias is added to the row as its own paragraph).
TOPIC_ALIASES = {"Monster.target": "Target.target", "MonsterQuiet.target": "Target.target"}
# The sections an entity page links to: (anchor, link text). Every other section belongs to the last one above it.
TOPIC_LINKS = [("naming", "Naming and triggering"), ("position", "Position"), ("appearance", "Appearance"),
               ("zhlt", "Compiler keys of brush entities"), ("zhlt_point", "Compiler keys of lights"),
               ("monsters", "Monsters"), ("talkmonster", "Talking monsters")]
COMMON_NAMES = set(COMMON)
# Common bases whose keys are rows of an entity's own Attributes table when the row says something of its own
# (their section on common-keys.md stays). A row whose text and default are those of the key's row on common-keys.md
# is left out, and the key is named in the page's common-keys list instead (INLINE_ITEMS, inline_repeats).
INLINE_COMMON = {"Targetname", "Target", "Targetx", "Master"}
# The keys of INLINE_COMMON: key -> its item on common-keys.md
INLINE_ITEMS = {"targetname": "Targetname.targetname", "target": "Target.target", "delay": "Targetx.delay",
                "killtarget": "Targetx.killtarget", "master": "Master.master"}

# Site pages that the FGD's "docs/X.md" references point to (paths relative to docs-site/docs/).
DOC_PAGES = {
    "WEATHER.md": ("mapping/features/weather.md", "Weather and fog"),
    "ENV_SKY.md": ("mapping/features/sky.md", "3D sky"),
    "ENV_MIRROR.md": ("mapping/features/mirrors.md", "Mirrors"),
    "WORLD_SCREENS.md": ("mapping/features/world-screens.md", "World screens"),
    "POINT_WORLDTEXT.md": ("mapping/features/world-text.md", "World text"),
    "MODEL_SCALE.md": ("mapping/features/model-scale.md", "Model scale"),
    "ENV_RENDER.md": ("mapping/features/props-and-fades.md", "Props, models and fades"),
    "ENV_MODEL.md": ("mapping/features/props-and-fades.md", "Props, models and fades"),
    "ENV_STATIC.md": ("mapping/features/props-and-fades.md", "Props, models and fades"),
    "AURORA.md": ("mapping/features/particles.md", "Particles"),
    "MATERIALS.md": ("mapping/features/materials.md", "Materials"),
    "SEQUENCES.md": ("mapping/features/sequences.md", "Sequence files"),
    "TUTOR_PORT.md": ("mapping/features/tutor.md", "Tutor messages"),
    "MESSAGE_BOX.md": ("mapping/features/message-boxes.md", "Message boxes"),
    "GAME_TIMER.md": ("mapping/features/game-timer.md", "HUD timer"),
    "MAP_MUSIC.md": ("mapping/features/music.md", "Music and sound"),
    "VIDEO_PLAYER.md": ("mapping/features/video.md", "Video"),
    "LOGIC_ENTITIES.md": ("mapping/guide/round-hooks.md", "Round hooks"),
    "TRIGGER_CHANGEVALUE.md": ("mapping/guide/changing-keys.md", "Changing keys"),
    "STATE_LOGIC.md": ("mapping/guide/masters-and-states.md", "Masters and states"),
    "LOCUS.md": ("mapping/guide/locus.md", "Locus system"),
    "OBJECT_HINTS.md": ("mapping/guide/entity-keyvalues.md", "Entity keyvalues"),
    "LIGHT_STYLES.md": ("mapping/features/light-styles.md", "Light styles"),
    "TELEPORT.md": ("mapping/features/teleports-and-jump-pads.md", "Teleports and jump pads"),
    "TRIGGER_JUMP.md": ("mapping/features/teleports-and-jump-pads.md", "Teleports and jump pads"),
    "MAP_COMPAT.md": ("mapping/basics/old-maps.md", "Old maps"),
    "MOVEWITH.md": ("mapping/features/moving-objects.md", "Moving objects"),
    "MAP_DEBUGGING.md": ("mapping/getting-started/testing.md", "Testing a map"),
    "ROUNDS.md": ("game-modes/coop.md", "Co-op"),
    "COMPILER_BUGS.md": ("mapping/basics/compiler-notes.md", "Compiler notes"),
}

# Groups: (id, title, intro, classes). A class is in the first group that lists it; the rules in group_of()
# (prefixes) catch the rest. The index page and the nav list the groups in this order.
GROUPS = [
    ("world-and-spawns", "World and spawns",
     "The world entity, spawn points and helper points. The start of the map name sets the game mode, and "
     "each mode uses its own spawns.",
     ["worldspawn", "info_player_deathmatch", "info_player_start", "info_player_go2", "info_player_go3",
      "info_player_go4", "info_player_go5", "multispawn", "info_intermission", "info_landmark",
      "info_teleport_destination", "info_target", "info_null", "info_node", "infodecal"]),
    ("missions", "Missions, rounds and players",
     "The mission entities: the number of rounds of a Co-op map, the end of the mission in success or "
     "failure, the objectives on the HUD and the ammo players get. Then the entities that change a player: their "
     "weapons, items, health, speed and what they can do",
     ["max_round", "game_end", "change_touch", "mission_failed", "Limitator", "ammo_reserve",
      "game_player_equip", "player_weaponstrip", "game_player_settings", "player_hasweapon",
      "player_capabilities", "player_speed", "player_flicker", "trigger_playerfreeze", "trigger_objective",
      "info_waypoint",
      "player_inventory", "player_hasinventory"]),
    ("monsters", "Monsters",
     "Monsters, and the entities that spawn them, script them, steer them or kill them",
     ["monstermaker", "monster_furniture", "monster_generic", "scripted_sequence", "aiscripted_sequence",
      "scripted_sentence", "scripted_action", "scripted_schedule", "scripted_following", "scripted_tanksequence",
      "trigger_startpatrol", "trigger_killmonster", "env_soundmark", "dark_grunt", "cycler", "cycler_wreckage"]),
    ("items", "Items",
     "Things players pick up: batteries, air tanks, soda cans and inventory items such as keycards",
     []),
    ("weapons", "Weapons",
     "Weapons players pick up: blades, pistols, rifles, shotguns, launchers, grenades, mines, satchels, Pitbulls "
     "and the Medikit",
     []),
    ("hud-and-screens", "HUD, text and screens",
     "Entities that show text, video, pictures or menus to players: HUD messages, the tutor window, message "
     "boxes, the HUD countdown, screen overlays, text in the world, world screens and videos",
     ["game_text", "env_message", "env_tutor", "game_messagebox", "game_timer", "env_overlay", "point_worldtext",
      "vgui_screen", "vgui_control_proxy", "game_playvideo", "env_fade"]),
    ("weather-fog-sky", "Weather, fog and sky",
     "Rain, snow, fog and the 3D sky",
     ["env_rain", "env_snow", "func_rainvolume", "func_snowvolume", "env_fog", "env_fogzone", "env_sky"]),
    ("lights", "Lights",
     "Light entities for the compiler, the entities that change light styles while the map runs, dynamic "
     "lights, and the lights and light origins of models",
     ["light", "light_spot", "light_environment", "trigger_lightstyle", "global_light_control", "env_elight",
      "info_light_origin", "env_dlight"]),
    ("sound-and-music", "Sound and music",
     "Sounds, map music and sequence files",
     ["ambient_generic", "ambient_random", "ambient_extraspeaker", "ambient_music", "speaker", "env_sound",
      "trigger_sequence", "trigger_cdaudio", "target_cdaudio"]),
    ("effects-and-models", "Effects and models",
     "Visual effects, particles, beams, decoration models, sprites and models that run along a path, and render "
     "changes",
     ["env_particle", "env_static", "env_model", "env_render", "env_mirror", "env_entity_glow", "env_spritetrain", "env_modeltrain",
      "nuclear_explosion", "gibshooter", "env_beam", "env_beamtrail", "locus_beam", "env_beverage", "env_blood",
      "env_bubbles", "env_decal", "env_explosion", "env_funnel", "env_glow", "env_laser", "env_quakefx",
      "env_shake", "env_shockwave", "env_shooter", "env_smoker", "env_spark", "env_sprite", "color_correction", "color_correction_volume", "env_warpball"]),
    ("logic", "Logic",
     "Relays, counters, conditions, timers, random triggers, value changes, masters, the locus calculators, and "
     "the entities that move, hurt or lock other entities",
     ["trigger_relay", "multi_manager", "multisource", "trigger_auto", "trigger_changetarget", "trigger_counter",
      "info_alias", "multi_alias", "trigger_changealias", "info_group",
      "trigger_changeparent",
      "trigger_changevalue", "trigger_copyvalue", "trigger_condition", "trigger_entity_iterator",
      "trigger_random", "trigger_random_unique", "trigger_timer", "trigger_compare", "trigger_camera",
      "env_global", "env_state", "calc_state", "multi_watcher", "watcher_count", "locus_variable",
      "player_calc_ratio", "game_number",
      "game_counter", "game_counter_set", "game_score", "game_team_master", "game_player_hurt",
      "trigger_motion", "motion_manager", "trigger_hurt_remote", "trigger_vehiclecontrols", "train_setspeed",
      "path_corner",
      "path_track"]),
    ("triggers", "Brush triggers",
     "Brush volumes that react to what touches or enters them",
     ["game_zone_player", "trigger_sensor"]),
    ("brush-entities", "Brush entities",
     "Doors, buttons, trains, vehicles, breakables, water and the other `func_` entities",
     ["button_target", "momentary_door", "momentary_rot_button"]),
]

# Left out of the reference: entities and keys that only work in a mode mappers are not told about.
HIDDEN_CLASSES = {"game_player_team", "game_team_set"}
HIDDEN_KEYS = {"worldspawn": {"mapteams", "defaultteam"}}

# Words the generated pages must never contain (the build fails on a match): another map editor's name, map
# prefixes and modes left out of the docs, server plugins, British spelling.
FORBIDDEN = re.compile(r"\bs[p]_|\br[c]_|team ?pl[a]y|\bHamm[e]r\b|\bV[H]E\b|Trench[B]room|\bSl[e]dge\b"
                       r"|\bAMX[X]?\b|AMX Mod|Metam[o]d|col[o]ur|behavi[o]ur", re.I)


_CODE = re.compile(r"`[^`]*`")


def group_of(name, kind):
    for gid, _title, _intro, classes in GROUPS:
        if name in classes:
            return gid
    if name.startswith("calc_"):
        return "logic"
    if name.startswith("monster_") or name.startswith("xen_"):
        return "monsters"
    if name.startswith("item_"):
        return "items"
    if name.startswith("weapon_"):
        return "weapons"
    if name.startswith("trigger_") and kind == "solidclass":
        return "triggers"
    if name.startswith("func_"):
        return "brush-entities"
    return None


# ---------------------------------------------------------------------------
# Parser: everything the docs need (labels, help texts, choice labels, comments)
# ---------------------------------------------------------------------------

def parse(path):
    with open(path, "rb") as fh:
        text = fh.read().decode("latin-1")
    lines = text.replace("\r\n", "\n").split("\n")
    p = fgd._Parser(fgd.tokenize(text))
    classes = collections.OrderedDict()
    while p.peek()[0] != "E":
        p.expect("@")
        kind = p.word("a class type")
        low = kind[1].lower()
        if low == "include":
            p.string()
            continue
        if low == "mapsize":
            p.expect("(")
            while not p.is_p(")"):
                p.next()
            p.next()
            continue
        cls = dict(kind=low, line=kind[2], bases=[], helpers=[], desc="", props=[], comment="")
        while not p.is_p("="):
            helper = p.word("a helper")
            args = []
            if p.is_p("("):
                p.next()
                while not p.is_p(")"):
                    tok = p.next()
                    if tok[0] != "P":
                        args.append(tok[1])
                p.next()
            if helper[1].lower() == "base":
                cls["bases"] += args
            else:
                cls["helpers"].append((helper[1].lower(), args))
        p.expect("=")
        name = p.word("a class name")[1]
        if p.is_p(":"):
            p.next()
            cls["desc"] = p.string()
        p.expect("[")
        while not p.is_p("]"):
            key = p.word("a key name")[1]
            p.expect("(")
            typ = p.word("a key type")[1].lower()
            p.expect(")")
            if p.peek()[0] == "W" and p.peek()[1].lower() == "readonly":
                p.next()
            fields = []
            while p.is_p(":"):
                p.next()
                tok = p.peek()
                if tok[0] == "S":
                    fields.append(p.string())
                elif tok[0] == "W" and not p.is_p("(", 1):
                    fields.append(p.next()[1])
                else:
                    fields.append(None)
            prop = dict(name=key, type=typ, label=fields[0] if fields else None,
                        default=fields[1] if len(fields) > 1 else None,
                        help=fields[2] if len(fields) > 2 else None, choices=None)
            if p.is_p("="):
                p.next()
                p.expect("[")
                choices = []
                while not p.is_p("]"):
                    value = p.next()[1]
                    p.expect(":")
                    label = p.string()
                    flag_default = None
                    if p.is_p(":"):
                        p.next()
                        flag_default = p.next()[1]
                    choices.append((value, label, flag_default))
                p.next()
                prop["choices"] = choices
            cls["props"].append(prop)
        p.next()
        # The // block right above the class line (no blank line between).
        comment = []
        i = cls["line"] - 2
        while i >= 0 and lines[i].strip().startswith("//"):
            comment.insert(0, lines[i].strip()[2:].strip())
            i -= 1
        cls["comment"] = " ".join(c for c in comment if c)
        classes[name] = cls
    return classes


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def esc(s):
    """Escape FGD text for Markdown (inline)."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("*", "\\*").replace("_", "\\_").replace("[", "\\[").replace("]", "\\]")
    return s


_DOCREF = re.compile(r'docs/([A-Z_0-9]+\.md)(?:,?\s*"[^"]*")?')


def text(s, prefix="../../", own=None, link=True):
    """FGD text to Markdown: \\n to paragraphs, escapes, docs/X.md references to links to the site's pages, and
    (with link) entity class names and target keywords to links (autolink)."""
    s = s.replace("\\n", "\n").strip()
    links = []

    def repl(m):
        page = DOC_PAGES.get(m.group(1))
        if not page:
            return "the developer docs"
        links.append("[%s](%s%s)" % (page[1], prefix, page[0]))
        return "\x00%d\x00" % (len(links) - 1)
    s = _DOCREF.sub(repl, s)
    if link:
        def lrepl(m):
            t = _target(m.group(1), own, "")
            if not t:
                return m.group(1)
            links.append("[`%s`](%s)" % (m.group(1), t))
            return "\x00%d\x00" % (len(links) - 1)
        s = _BARE.sub(lrepl, s)
    s = esc(s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: links[int(m.group(1))], s)
    s = re.sub(r"[ \t]*\n[ \t]*", "\n\n", s)
    return s.strip()


def cell(s, own=None, link=True):
    return text(s, own=own, link=link).replace("\n\n", "<br>").replace("|", "\\|")


def code(v):
    if v is None or v == "":
        return ""
    return "`%s`" % v.replace("`", "'").replace("|", "\\|")


# ---------------------------------------------------------------------------
# Key collection
# ---------------------------------------------------------------------------

def collect(classes, name, own=True, seen=None):
    """(keys, flags, common bases) of a class: bases first, own keys last; common bases are not expanded, except
    INLINE_COMMON (Name, Target, Delay, KillTarget and Master, rows of the entity's own table unless they repeat
    common-keys.md: page, inline_repeats)."""
    seen = set() if seen is None else seen
    keys = collections.OrderedDict()
    flags = collections.OrderedDict()
    common = []
    cls = classes[name]
    for base in cls["bases"]:
        if base in seen or base not in classes:
            continue
        seen.add(base)
        if base in COMMON_NAMES and own and base not in INLINE_COMMON:
            if base not in common:
                common.append(base)
            # Spawnflags of common bases are still shown with the entity.
            _k, f, _ = collect(classes, base, own=False, seen=set())
            flags.update(f)
            continue
        k, f, c = collect(classes, base, own, seen)
        keys.update(k)
        flags.update(f)
        for b in c:
            if b not in common:
                common.append(b)
    for prop in cls["props"]:
        if prop["name"].lower() == "spawnflags":
            for value, label, dflt in prop["choices"] or []:
                flags[value] = (label, dflt)
        elif own and prop["name"].lower() not in HIDDEN_KEYS.get(name, ()):
            keys[prop["name"].lower()] = prop
    return keys, flags, common


def expanded_bases(classes, name, seen=None):
    """The base classes whose keys or flags the page of a class shows (every base, common bases too for their
    flags), nearest first."""
    seen = set() if seen is None else seen
    out = []
    for base in classes[name]["bases"]:
        if base in seen or base not in classes:
            continue
        seen.add(base)
        out.append(base)
        out += expanded_bases(classes, base, seen)
    return out


def check_provenance(classes, prov, problems):
    """Every keys/flags entry of provenance.yml names a key or flag that its class (or base class) has."""
    for n, entries in prov["keys"].items():
        if n not in classes:
            problems.append("provenance.yml: keys/%s is no class of the FGD" % n)
            continue
        keys, _f, _c = collect(classes, n, own=True, seen=set())
        allk = set(keys) | {p["name"].lower() for p in classes[n]["props"]}
        for k in entries or {}:
            if str(k).lower() not in allk:
                problems.append("provenance.yml: keys/%s/%s is no key of the class" % (n, k))
    for n, entries in prov["flags"].items():
        if n not in classes:
            problems.append("provenance.yml: flags/%s is no class of the FGD" % n)
            continue
        _k, flags, _c = collect(classes, n, own=True, seen=set())
        for f in entries or {}:
            if str(f) not in flags:
                problems.append("provenance.yml: flags/%s/%s is no flag of the class" % (n, f))


# ---------------------------------------------------------------------------
# provenance.yml
# ---------------------------------------------------------------------------

def load_provenance(path, problems):
    try:
        import yaml
    except ImportError:
        sys.stderr.write("gen_entity_docs: PyYAML is missing (pip install pyyaml, or the python3-yaml package)\n")
        sys.exit(2)
    if not os.path.exists(path):
        return {"projects": {}, "entities": {}, "keys": {}, "flags": {}}
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    prov = {
        "projects": data.get("projects") or {},
        "entities": data.get("entities") or {},
        "keys": data.get("keys") or {},
        "flags": data.get("flags") or {},
    }
    for pid, proj in prov["projects"].items():
        for field in ("name", "url"):
            if not (proj or {}).get(field):
                problems.append("provenance.yml: project %s has no %s" % (pid, field))
        icon = (proj or {}).get("icon")
        if icon and not os.path.isfile(os.path.join(ICON_DIR, icon)):
            problems.append("provenance.yml: the icon %s of project %s is missing in %s" % (icon, pid, ICON_DIR))
    return prov


def _sources(value):
    """A provenance value (a project id, or a list of them) as a list."""
    if value is None:
        return []
    return [value] if isinstance(value, str) else list(value)


def ported_icons(prov, value, problems, where):
    """The "Ported from" icons of a provenance value: a [[ported:<id> ...]] marker, which the site hook
    docs-site/plugins/remark-sbo.mjs turns into one icon per project ("" for no value)."""
    ids = []
    for pid in _sources(value):
        if pid not in prov["projects"]:
            problems.append("provenance.yml: %s names the unknown project %s" % (where, pid))
            continue
        ids.append(pid)
    return "[[ported:%s]]" % " ".join(ids) if ids else ""


# ---------------------------------------------------------------------------
# Plain key names: the FGD labels without value hints (docs-site/key-help/names.yml for the rest)
# ---------------------------------------------------------------------------

NAMES_FILE = "names.yml"  # in KEY_HELP_DIR: {"FGD label": "plain name"}, for labels the rules below can't clean
NAMES = {}
_HINT_TAIL = re.compile(r"\s*(\[[^\[\]]*\]|\((?:[^()]|\([^()]*\))*\)|,\s*\[[^\[\]]*\])\s*$")
_RANGE_TAIL = re.compile(r"\s+-?\d+(?:\.\d+)?\s*-\s*-?\d+(?:\.\d+)?\s*$")
_TAG_TAIL = re.compile(r"\s*\[L[PVRE](?:\s+L[PVRE])*\](?:\s*/\s*(?:\[L[PVRE]\]|color))*\s*$")


def plain_name(label):
    """The editor name of a key or flag without value hints: "Volume (10 = loudest)" -> "Volume"."""
    if label is None:
        return ""
    label = label.replace("\\n", " ").strip()
    if label in NAMES:
        return NAMES[label]
    s = label
    while True:
        t = _RANGE_TAIL.sub("", _HINT_TAIL.sub("", s)).strip()
        if t == s or not t:
            break
        s = t
    return s or label


def plain_choice(label):
    """A choice label without its locus tag ("Calc Position of the entity [LP]"); other words stay."""
    label = (label or "").replace("\\n", " ").strip()
    if label in NAMES:
        return NAMES[label]
    return _TAG_TAIL.sub("", label).strip() or label


def name_ok(text_name, label, plain):
    """A name written in entity-text must be the editor name, or the start of it without the hints."""
    label = (label or "").replace("\\n", " ").strip()
    return text_name in (plain, label) or label.startswith(text_name)


# ---------------------------------------------------------------------------
# Links: entity class names and the target keywords
# ---------------------------------------------------------------------------

KEYWORD_LINKS = {
    "!activator": "../guide/entity-triggering.md#target-selectors",
    "!caller": "../guide/entity-triggering.md#target-selectors",
    "*locus": "../guide/locus.md#entity-names-in-a-locus-key",
    "*player": "../guide/locus.md#entity-names-in-a-locus-key",
}
CLASS_NAMES = set()  # every documented class (filled in main)
_LINK_OR_CODE = re.compile(r"(\[(?:[^\[\]]|\[[^\[\]]*\])*\]\([^)]*\)|`[^`]*`|<[^>]+>|https?://\S+)")
_BARE = re.compile(r"(?<![\w/.\\-])([A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]*[A-Za-z0-9]|!activator|!caller|\*locus|\*player)"
                   r"(?![\w/\\-]|\.\w)")


def _target(word, own, prefix):
    if word in KEYWORD_LINKS:
        return KEYWORD_LINKS[word]
    if word in CLASS_NAMES and word != own:
        return prefix + word + ".md"
    return None


def autolink(s, own=None, prefix=""):
    """Links every entity class name and target keyword (`!activator`, `*locus`, ...) that is not already in a
    link, as a code span: `env_fade` and env_fade both become [`env_fade`](env_fade.md). The page's own class
    stays plain. Headings, tables and fenced code are left alone by the callers."""
    out = []
    for part in _LINK_OR_CODE.split(s):
        if not part:
            continue
        if part.startswith("[") or part.startswith("<") or part.startswith("http"):
            out.append(part)
        elif part.startswith("`"):
            t = _target(part[1:-1], own, prefix)
            out.append("[%s](%s)" % (part, t) if t else part)
        else:
            out.append(_BARE.sub(lambda m: "[`%s`](%s)" % (m.group(1), _target(m.group(1), own, prefix))
                                 if _target(m.group(1), own, prefix) else m.group(1), part))
    return "".join(out)


def autolink_block(text_block, own, prefix=""):
    """autolink() on the prose lines of a Markdown block (not headings, tables or fenced code)."""
    out = []
    fence = False
    for line in text_block.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line)
        elif fence or line.startswith("#") or line.lstrip().startswith("|"):
            out.append(line)
        else:
            out.append(autolink(line, own, prefix))
    return "\n".join(out)


_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def list_items(lines):
    """(first line, last line) of each list item of a Markdown block (continuation lines are indented)."""
    spans = []
    start = None
    fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        if fence:
            if start is not None:
                spans.append((start, i - 1))
                start = None
            continue
        if _ITEM.match(line):
            if start is not None:
                spans.append((start, i - 1))
            start = i
        elif start is not None and (not line.strip() or not line.startswith((" ", "\t"))):
            spans.append((start, i - 1))
            start = None
    if start is not None:
        spans.append((start, len(lines) - 1))
    return spans


def strip_list_stops(block):
    """List lines end without a full stop (the style rules): the stop at the end of each list item goes."""
    lines = block.split("\n")
    for _a, b in list_items(lines):
        if lines[b].endswith(".") and not lines[b].endswith(".."):
            lines[b] = lines[b][:-1]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# entity-text/<class>.md
# ---------------------------------------------------------------------------

_BULLET = re.compile(r"^- `([^`]+)`:\s*(.*)$")  # old format: "- `key`: text" / "- `8`: text"
_ICONS = r"((?: \[\[ported:[a-z0-9 _-]+\]\])?)"
_ATTR = re.compile(r"^- \*\*(.+?)\*\* \(`([^`]+)`\)" + _ICONS + r"(?: - (.*))?$")
_FLAG = re.compile(r"^- \*\*(.+?)\*\* \((\d+)\)" + _ICONS + r"(?: - (.*))?$")
_DEFAULT = re.compile(r"\.?\s*Default (`[^`]*`|\S+)$")
EMPTY_LINE = "If you leave this key empty"


def _entry(name=None, desc="", icons=""):
    return {"name": name, "desc": desc, "items": [], "empty": "", "icons": icons.strip(), "old": name is None}


def _notes(lines, flags=False):
    """A Keys or Flags section: ({key or flag value: entry}, the other text). An entry has the name written in
    the text (None in the old "- `key`: text" format), the description, the sub-items (choices and other list
    lines), the "If you leave this key empty" line and the "Ported from" marker written after the name."""
    notes = collections.OrderedDict()
    other = []
    cur = None
    sub = None
    for line in lines:
        m = (_FLAG if flags else _ATTR).match(line)
        o = _BULLET.match(line)
        if m:
            cur = notes[m.group(2) if flags else m.group(2).lower()] = _entry(m.group(1), (m.group(4) or "").strip(),
                                                                                m.group(3))
            sub = "desc"
        elif o:
            cur = notes[o.group(1) if flags else o.group(1).lower()] = _entry(None, o.group(2).strip())
            sub = "desc"
        elif cur is not None and line.startswith("    - ") and not flags:
            item = line[6:].strip()
            if item.startswith(EMPTY_LINE):
                cur["empty"] = item
                sub = "empty"
            else:
                cur["items"].append(item)
                sub = "items"
        elif cur is not None and line.startswith((" ", "\t")) and line.strip():
            t = " " + line.strip()
            if sub == "items":
                cur["items"][-1] += t
            elif sub == "empty":
                cur["empty"] += t
            else:
                cur["desc"] = (cur["desc"] + t).strip()
        else:
            cur = None
            other.append(line)
    return notes, "\n".join(other).strip()


def load_text(path):
    """A text file split into summary, Attributes entries, Flags entries and the other sections (see the
    docstring)."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read().replace("\r\n", "\n")
    description = None
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        import yaml  # checked by load_provenance
        description = (yaml.safe_load(m.group(1)) or {}).get("description")
        text = text[m.end():]
    lines = text.split("\n")
    parts = [("", [])]
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            parts.append((line[3:].strip(), [line]))
        else:
            parts[-1][1].append(line)
    out = dict(summary="\n".join(parts[0][1]).strip(), keys={}, keys_intro="", flags={}, flags_intro="",
               rest=[], new=False, description=description)
    for heading, body in parts[1:]:
        if heading in ("Attributes", "Keys"):
            out["new"] = out["new"] or heading == "Attributes"
            out["keys"], out["keys_intro"] = _notes(body[1:])
        elif heading == "Flags":
            out["flags"], out["flags_intro"] = _notes(body[1:], flags=True)
        else:
            out["rest"].append("\n".join(body).strip())
    # A file in the new format: an "## Attributes" section, or a "## See also" section (the old one was "Related")
    out["new"] = out["new"] or any(h == "See also" for h, _b in parts[1:])
    return out


# Words and patterns a rewritten page (an entity-text file with "## Attributes") must not contain
STYLE_WORDS = re.compile(r"\b(he|his|him|himself|whatever)\b|Left out", re.I)
STYLE_PRONOUN = re.compile(r"\b(he|his|him|himself)\b", re.I)
STYLE_ORIGIN = re.compile(r"\bOrigin\s*:")


def style_problems(path, fn, problems):
    """The style rules that a script can check, on an entity-text file in the new format."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    for i, line in enumerate(lines, 1):
        bare = _CODE.sub("", line)
        m = STYLE_WORDS.search(bare)
        if m:
            problems.append("entity-text/%s:%d: '%s' breaks the style rules" % (fn, i, m.group(0)))
        if STYLE_ORIGIN.search(bare):
            problems.append("entity-text/%s:%d: write \"Ported from\" with the icons, not \"Origin\"" % (fn, i))
    for a, b in list_items(lines):
        if lines[b].endswith(".") and not lines[b].endswith(".."):
            problems.append("entity-text/%s:%d: a list line ends with a full stop" % (fn, b + 1))


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

PREFIX = "../../"  # from docs-site/docs/mapping/entities/ to docs-site/docs/


def tcell(s):
    """Hand-written Markdown in a table cell."""
    return s.replace("|", "\\|")


def _sentence(s):
    s = s.strip()
    return s + "." if s and not s.endswith((".", ":", "!", "?")) else s


def _choice_of(item, values):
    """(name, value, is_default, rest) of a sub-item written as "Name (value) - text" or "Name (value, default)
    - text", where value is one of values (None: any number); None if the item is no choice line."""
    for m in re.finditer(r" \(([^()]*)\)(?= - |$)", item):
        inner = m.group(1)
        dflt = inner.endswith(", default")
        v = inner[:-len(", default")] if dflt else inner
        v = v.strip().strip("`").strip('"')
        if (values is None and re.fullmatch(r"-?\d+(?:\.\d+)?", v)) or (values is not None and v in values):
            rest = item[m.end():]
            return item[:m.start()], v, dflt, rest[3:] if rest.startswith(" - ") else ""
    return None


def _value_label(v):
    return v if v != "" else "empty"


def key_row(name, k, prop, entry, help_entry, icons, problems, where):
    """One row of an Attributes table: (Key, Description, Default) cells."""
    entry = entry or _entry()
    help_entry = help_entry or {}
    label = prop["label"] or ""
    plain = plain_name(label) or prop["name"]
    shown = plain
    if entry["name"]:
        if not name_ok(entry["name"], label, plain):
            problems.append("%s: `%s` is called **%s** in the editor (\"%s\"), not **%s**"
                            % (where, k, plain, label, entry["name"]))
        shown = entry["name"]
    if entry["icons"] and entry["icons"] != icons:
        problems.append("%s: `%s` has %s in the text but %s in provenance.yml (provenance.yml decides)"
                        % (where, k, entry["icons"], icons or "nothing"))
    desc = entry["desc"]
    fgd_default = prop["default"]
    m = _DEFAULT.search(desc)
    if m:
        written = m.group(1).strip("`")
        if fgd_default is None or written != str(fgd_default):
            problems.append("%s: `%s` says Default %s, but the FGD default is %s"
                            % (where, k, written, "none" if fgd_default is None else fgd_default))
        desc = desc[:m.start()]
    if desc:
        desc = tcell(autolink(desc, name))
    elif help_entry.get("desc"):
        desc = tcell(autolink(help_entry["desc"], name))
    elif prop["help"]:
        desc = cell(prop["help"], name)
    default_cell = code(fgd_default)

    choices = prop["choices"] or []
    values = [v for v, _l, _d in choices]
    items = []
    if choices and entry["old"] and entry["desc"] and all(
            "(%s)" % v in entry["desc"] or "(`%s`)" % v in entry["desc"] for v in values):
        choices = []  # old format: the text already names every choice
    written = collections.OrderedDict()
    extra = []
    for it in entry["items"]:
        c = _choice_of(it, values if choices else None)
        if c:
            written[c[1]] = c
        else:
            extra.append(it)
    for v, lbl, _d in choices:
        if v in written:
            cname, _v, dflt, rest = written.pop(v)
            if not name_ok(cname, lbl, plain_choice(lbl)):
                problems.append("%s: `%s` choice %s is called \"%s\" in the editor, not \"%s\""
                                % (where, k, v, lbl, cname))
        else:
            cname, rest = plain_choice(lbl), (help_entry.get("choices") or {}).get(v, "")
        # a text value that is its own label ("button") is shown once
        line = cname if cname == v else "%s (%s)" % (cname, _value_label(v))
        if rest:
            line += " - " + rest
        items.append(autolink(line, name))
        if fgd_default is not None and str(fgd_default) == v:
            default_cell = cname if cname == v else "%s (%s)" % (cname, _value_label(v))
    for v, (cname, _v, dflt, rest) in written.items():
        if choices:
            problems.append("%s: `%s` has no choice %s in the FGD" % (where, k, v))
            continue
        items.append(autolink("%s (%s)%s" % (cname, v, " - " + rest if rest else ""), name))
        if dflt:
            if fgd_default is not None and str(fgd_default) != v:
                problems.append("%s: `%s` marks %s as the default, but the FGD default is %s"
                                % (where, k, v, fgd_default))
            default_cell = "%s (%s)" % (cname, v)
    items += [autolink(it, name) for it in extra + list(help_entry.get("items") or [])]
    empty = entry["empty"] or help_entry.get("empty") or ""

    parts = [_sentence(desc)] if desc else []
    if items:
        parts.append("<br>".join("&bull;&nbsp;" + tcell(i) for i in items))
    if empty:
        parts.append(tcell(_sentence(autolink(empty, name))))
    key_cell = "**%s**%s<br>`%s`" % (esc_name(shown), " " + icons if icons else "", prop["name"])
    return key_cell, "<br><br>".join(parts), default_cell


def esc_name(s):
    return s.replace("|", "\\|").replace("*", "\\*")


def key_table(name, keys, notes, help_owners, key_icons, problems, where):
    out = ["| Key | Description | Default |", "|---|---|---|"]
    seen = {}
    for k, prop in keys.items():
        help_entry = help_for(help_owners, "keys", k)
        kc, desc, dflt = key_row(name, k, prop, notes.get(k), help_entry, key_icons.get(k, ""), problems, where)
        shown = kc.split("**")[1]
        if shown in seen:
            problems.append("%s: `%s` and `%s` both show as **%s** (add plain names to key-help/%s)"
                            % (where, seen[shown], k, shown, NAMES_FILE))
        seen[shown] = k
        out.append("| %s | %s | %s |" % (kc, desc, dflt))
    return "\n".join(out)


def _flag_sort(kv):
    return int(kv[0]) if kv[0].isdigit() else 0


def flag_list(name, flags, notes, help_owners, flag_icons, problems, where):
    """The Flags section: "- **Name** (value) - what it does", in value order."""
    out = []
    seen = {}
    for value, (label, dflt) in sorted(flags.items(), key=_flag_sort):
        entry = notes.get(value) or _entry()
        plain = plain_name(label)
        if plain in seen:
            problems.append("%s: flags %s and %s both show as **%s** (add plain names to key-help/%s)"
                            % (where, seen[plain], value, plain, NAMES_FILE))
        seen[plain] = value
        shown = plain
        if entry["name"]:
            if not name_ok(entry["name"], label, plain):
                problems.append("%s: flag %s is called **%s** in the editor (\"%s\"), not **%s**"
                                % (where, value, plain, label, entry["name"]))
            shown = entry["name"]
        icons = flag_icons.get(value, "")
        if entry["icons"] and entry["icons"] != icons:
            problems.append("%s: flag %s has %s in the text but %s in provenance.yml (provenance.yml decides)"
                            % (where, value, entry["icons"], icons or "nothing"))
        desc = entry["desc"] or (help_for(help_owners, "flags", value) or {}).get("desc", "")
        desc = autolink(desc.strip(), name)
        if dflt == "1" and "by default" not in desc:
            desc = (desc.rstrip(".") + ". " if desc else "") + "This flag is set by default"
        desc = desc.rstrip(".") if not desc.endswith("..") else desc
        line = "- **%s** (%s)%s" % (esc_name(shown), value, " " + icons if icons else "")
        out.append(line + (" - " + desc if desc else ""))
    return "\n".join(out)


def _join(names):
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def _item_id(base, prop=None, flag=None):
    return "%s#%s" % (base, flag) if flag is not None else "%s.%s" % (base, prop["name"].lower())


def leaf_items(classes, base):
    """{item id: (base, prop or None, flag value or None, flag label)} of a base class and of every base it includes,
    with TOPIC_ALIASES mapped to their item."""
    out = collections.OrderedDict()
    for b in [base] + expanded_bases(classes, base):
        for prop in classes[b]["props"]:
            if prop["name"].lower() == "spawnflags":
                for value, label, _d in prop["choices"] or []:
                    out.setdefault(_item_id(b, flag=value), (b, None, value, label))
            else:
                iid = _item_id(b, prop)
                out.setdefault(TOPIC_ALIASES.get(iid, iid), (b, prop, None, None))
    return out


def topic_items(classes, problems):
    """{item id: (section anchor, link anchor, row anchors)} of TOPICS, checked against the FGD: every key and flag
    of the common bases is in exactly one section."""
    out = collections.OrderedDict()
    link = None
    for anchor, _lvl, _h, _intro, items, _old in TOPICS:
        if anchor in dict(TOPIC_LINKS):
            link = anchor
        for it in items:
            iid, _, anchors = it.partition(" ")
            if iid in out:
                problems.append("TOPICS: %s is in two sections" % iid)
            out[iid] = (anchor, link, anchors.split())
    known = collections.OrderedDict()
    for b in COMMON:
        if b in classes:
            for iid, info in leaf_items(classes, b).items():
                known.setdefault(iid, info)
    for iid in known:
        if iid not in out:
            problems.append("TOPICS: %s (a key or flag of a common base) is in no section of common-keys.md" % iid)
    for iid in out:
        if iid not in known:
            problems.append("TOPICS: %s is no key or flag of a common base" % iid)
    return out, known


def item_name(info):
    base, prop, flag, label = info
    return plain_name(label) if flag is not None else (plain_name(prop["label"] or "") or prop["name"])


def entity_common(classes, name, keys, flags, common):
    """{item id: info} of the common keys and flags of an entity: those of its common bases that are not rows of its
    own tables (its own key, or a flag it defines again)."""
    out = collections.OrderedDict()
    for b in common:
        for iid, info in leaf_items(classes, b).items():
            _b, prop, flag, label = info
            if flag is not None:
                if flags.get(flag, (None,))[0] != label:
                    continue  # the entity defines this flag value itself
            elif prop["name"].lower() in keys:
                continue
            out.setdefault(iid, info)
    return out


def common_links(classes, name, ent_items, keys, problems):
    """The list of the common-keys.md sections an entity has, each with the keys it has there (or the ones it
    doesn't have, if that list is shorter)."""
    topic, known = TOPIC_INFO
    lines = []
    for link, title in TOPIC_LINKS:
        group = [iid for iid, (_s, l, _a) in topic.items() if l == link]
        has = [iid for iid in group if iid in ent_items]
        if not has:
            continue
        present = set(has) | {iid for iid in group if "." in iid and iid.split(".", 1)[1] in keys}
        missing = [iid for iid in group if iid not in present]
        names = lambda ids: _join(["**%s**" % esc_name(item_name(known[i])) for i in ids])
        if link == "naming":
            what = names(has)  # the keys whose rows the page leaves out are named one by one
        elif not missing and len(has) > 2:
            what = "all of them"
        elif missing and len(missing) + 1 < len(has):
            what = "all except " + names(missing)  # only when clearly shorter than the list of what it has
        else:
            what = names(has)
        lines.append("- [%s](common-keys.md#%s): %s" % (title, link, what))
    return "The entity also has these [common keys](common-keys.md):\n\n" + "\n".join(lines)


TOPIC_INFO = ({}, {})  # (topic_items(), the items of the common bases), filled in main
# The rows of INLINE_ITEMS on common-keys.md: key -> (its description and each of its paragraphs, whitespace
# normalized; its default cell), filled in main (common_inline_rows)
COMMON_INLINE_ROWS = {}
# (class, key) of every INLINE_ITEMS row an entity page leaves out because it repeats common-keys.md
INLINE_DROPPED = []


def _norm(s):
    return " ".join(s.split())


def common_inline_rows(classes):
    """COMMON_INLINE_ROWS: the description of each INLINE_ITEMS row as common-keys.md shows it (common_page), and
    the paragraphs it is made of (a TOPIC_ALIASES paragraph, such as a monster's Target, is one of them)."""
    _topic, known = TOPIC_INFO
    for k, iid in INLINE_ITEMS.items():
        base, prop, _f, _l = known[iid]
        owners = [base] + expanded_bases(classes, base)
        _kc, desc, dflt = key_row(None, k, prop, None, help_for(owners, "keys", k), "", [], "")
        texts = {_norm(desc)} | {_norm(p) for p in desc.split("<br><br>")}
        for alias, target in TOPIC_ALIASES.items():
            a_base = alias.split(".")[0]
            if target == iid and a_base in classes:
                extra = help_for([a_base], "keys", k)
                if extra and extra.get("desc"):
                    texts.add(_norm(tcell(_sentence(autolink(extra["desc"])))))
        COMMON_INLINE_ROWS[k] = (texts, dflt)


def inline_repeats(name, k, prop, entry, owners, icon):
    """True when the entity's row of an INLINE_ITEMS key says only what its row on common-keys.md says: the same
    description (whitespace normalized, links as on common-keys.md), the same default and no icon of its own."""
    if k not in COMMON_INLINE_ROWS or icon:
        return False
    texts, dflt = COMMON_INLINE_ROWS[k]
    _kc, desc, own_dflt = key_row(None, k, prop, entry, help_for(owners, "keys", k), "", [], "")
    return _norm(desc) in texts and own_dflt == dflt


def fgd_title(cls):
    return cls["desc"].replace("\\n", "\n").strip().partition("\n")[0]


def load_key_help(problems):
    """docs-site/key-help/*.yml: descriptions for key and flag rows that have no entity-text bullet. Each file
    maps a class or base class to {keys: {key: text}, flags: {value: text}}; an entry of a base class fills that
    key or flag on every page that shows it. A key's text may also be a map: {desc: text, choices: {value: text},
    empty: "If you leave this key empty, ...", items: [list lines]}. A class may be in several files; each key or
    flag in one only. names.yml is the plain-name map instead (NAMES)."""
    import yaml
    out = {}
    if not os.path.isdir(KEY_HELP_DIR):
        return out
    for fn in sorted(os.listdir(KEY_HELP_DIR)):
        if not fn.endswith(".yml"):
            continue
        with open(os.path.join(KEY_HELP_DIR, fn), encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        if fn == NAMES_FILE:
            NAMES.update({str(k): str(v) for k, v in data.items()})
            continue
        with open(os.path.join(KEY_HELP_DIR, fn), encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                m = STYLE_PRONOUN.search(_CODE.sub("", line))
                if m:
                    problems.append("key-help/%s:%d: '%s' breaks the style rules (they / their / them)"
                                    % (fn, i, m.group(0)))
        for cls, entry in data.items():
            entry = entry or {}
            slot = out.setdefault(cls, {"keys": {}, "flags": {}, "file": fn})
            for kind in ("keys", "flags"):
                for k, v in (entry.get(kind) or {}).items():
                    k = str(k).lower() if kind == "keys" else str(k)
                    if k in slot[kind]:
                        problems.append("key-help/%s: %s %s %s is also in another key-help file" % (fn, cls, kind, k))
                        continue
                    if isinstance(v, dict):
                        v = {"desc": str(v.get("desc") or "").strip(),
                             "choices": {str(c): str(t).strip() for c, t in (v.get("choices") or {}).items()},
                             "empty": str(v.get("empty") or "").strip(), "items": list(v.get("items") or [])}
                    else:
                        v = {"desc": str(v).strip()}
                    slot[kind][k] = v
    return out


KEY_HELP = {}


def help_for(owners, kind, item):
    """The key-help entry of a key or flag, from the first of the owners (class, then its bases) that has one."""
    for owner in owners:
        entry = (KEY_HELP.get(owner) or {}).get(kind, {}).get(item)
        if entry:
            return entry
    return None


EMPTY_ROWS = []
FGD_HELP_ROWS = []  # rows whose description is the FGD's own help text (no entity-text bullet or key-help)


def _note_rows(name, keys, flags, key_notes, flag_notes, owners):
    for k, prop in keys.items():
        e = key_notes.get(k)
        h = help_for(owners, "keys", k)
        if not (e and e["desc"]) and not (h and h.get("desc")):
            if prop["help"]:
                FGD_HELP_ROWS.append((name, "key", k, prop["label"] or ""))
            else:
                # A choice list alone does not say what the key does: it needs a sentence too
                EMPTY_ROWS.append((name, "key", k, prop["label"] or ""))
    for f, (label, _d) in flags.items():
        e = flag_notes.get(f)
        if not (e and e["desc"]) and not help_for(owners, "flags", f):
            EMPTY_ROWS.append((name, "flag", f, label or ""))


def page(classes, name, text_part, prov, problems):
    cls = classes[name]
    keys, flags, common = collect(classes, name)
    where = "entity-text/%s.md" % name
    # The "Ported from" icons go in the page header (entity_mdx)
    head_icons = ported_icons(prov, prov["entities"].get(name), problems, "entities/" + name)
    out = [("# %s %s" % (name, head_icons)).rstrip(), ""]
    if text_part and text_part["summary"]:
        out += [autolink_block(text_part["summary"], name), ""]
    else:
        kind = "A brush entity" if cls["kind"] == "solidclass" else "A point entity"
        title = fgd_title(cls)
        out += ["%s%s" % (kind, ": " + esc(title) if title else ""), ""]

    # Icons of single keys and flags: entries of the class and of the bases its tables include.
    key_icons = {}
    flag_icons = {}
    for owner in [name] + expanded_bases(classes, name):
        for k, v in (prov["keys"].get(owner) or {}).items():
            key_icons.setdefault(str(k).lower(), ported_icons(prov, v, problems, "keys/%s/%s" % (owner, k)))
        for f, v in (prov["flags"].get(owner) or {}).items():
            flag_icons.setdefault(str(f), ported_icons(prov, v, problems, "flags/%s/%s" % (owner, f)))

    key_notes = {}
    flag_notes = {}
    if text_part:
        key_notes = dict(text_part["keys"])
        flag_notes = dict(text_part["flags"])
        for k in key_notes:
            if k not in keys:
                problems.append("%s: Attributes names `%s`, which is no key of the class" % (where, k))
        for f in flag_notes:
            if f not in flags:
                problems.append("%s: Flags names `%s`, which is no flag of the class" % (where, f))

    # Common flags are on common-keys.md; a page keeps one only if its text says what the flag does there
    ent_items = entity_common(classes, name, keys, flags, common)
    for iid, (_b, _p, flag, _l) in list(ent_items.items()):
        if flag is not None and (flag_notes.get(flag) or {}).get("desc"):
            del ent_items[iid]
    common_flags = {flag for _b, _p, flag, _l in ent_items.values() if flag is not None}
    flags = collections.OrderedDict((v, f) for v, f in flags.items() if v not in common_flags)

    owners = [name] + expanded_bases(classes, name)
    # Name, Target, Delay before trigger, KillTarget and Master: a row only where it says something of its own
    _topic, known = TOPIC_INFO
    for k in [k for k in keys if k in INLINE_ITEMS]:
        if inline_repeats(name, k, keys[k], key_notes.get(k), owners, key_icons.get(k, "")):
            if (key_notes.get(k) or {}).get("desc"):
                problems.append("%s: the bullet for `%s` says what common-keys.md says (remove it)" % (where, k))
            del keys[k]
            ent_items[INLINE_ITEMS[k]] = known[INLINE_ITEMS[k]]
            INLINE_DROPPED.append((name, k))
    _note_rows(name, keys, flags, key_notes, flag_notes, owners)
    if text_part and text_part["new"]:
        # A rewritten page has one source per row: its own key-help entries that the text replaces must go
        own_help = KEY_HELP.get(name) or {}
        for kind, notes in (("keys", key_notes), ("flags", flag_notes)):
            for item in own_help.get(kind, {}):
                if item in notes and notes[item]["desc"]:
                    problems.append("key-help/%s: %s %s %s is replaced by %s (remove it from key-help)"
                                    % (own_help["file"], name, kind, item, where))

    if keys or ent_items:
        out += ["## Attributes", ""]
        if text_part and text_part["keys_intro"]:
            out += [autolink_block(text_part["keys_intro"], name), ""]
        if keys:
            out += [key_table(name, keys, key_notes, owners, key_icons, problems, where), ""]
        if ent_items:
            out += [common_links(classes, name, ent_items, keys, problems), ""]
    if flags:
        out += ["## Flags", ""]
        if text_part and text_part["flags_intro"]:
            out += [autolink_block(text_part["flags_intro"], name), ""]
        out += [flag_list(name, flags, flag_notes, owners, flag_icons, problems, where), ""]
    if text_part:
        for section in text_part["rest"]:
            out += [strip_list_stops(autolink_block(section, name)), ""]
    return "\n".join(out).rstrip() + "\n"


COMMON_INTRO = ("Many entities share these keys and flags. Each entity page links to the sections here and names the "
                "keys it has.")


def common_page(classes, prov, problems):
    """common-keys.md: (the page as Markdown, for the checks; the page as MDX). Every key and flag of the common bases
    once, in the sections of TOPICS."""
    topic, known = TOPIC_INFO
    md = ["# Common keys", "", COMMON_INTRO, ""]
    mdx = [_front_matter([("title", "Common keys")]) + GENERATED, "# Common keys", "", mdx_block(COMMON_INTRO), ""]
    users = {}
    for n, c in classes.items():
        if c["kind"] in ("pointclass", "solidclass") and n not in HIDDEN_CLASSES:
            for b in collect(classes, n)[2]:
                users.setdefault(b, []).append(n)
    for anchor, level, heading, intro, items, old in TOPICS:
        for o in old:
            mdx += ['<Anchor id="%s" />' % o, ""]
        h = "%s %s {#%s}" % ("#" * level, heading, anchor)
        md += [h, ""]
        mdx += [h, ""]
        if intro:
            if "{users}" in intro:
                intro = intro.format(users=_join(sorted(users.get(anchor_base(items)) or ["No entity"])))
            block = autolink_block(intro, None)
            md += [block, ""]
            mdx += [mdx_block(block), ""]
        rows, flag_lines, row_anchors, flag_anchors = [], [], {}, {}
        for it in items:
            iid, _, _a = it.partition(" ")
            base, prop, flag, label = known[iid]
            owners = [base] + expanded_bases(classes, base)
            where = "common-keys.md (%s)" % iid
            if flag is None:
                k = prop["name"].lower()
                entry = {str(x).lower(): v for x, v in (prov["keys"].get(base) or {}).items()}.get(k)
                icons = ported_icons(prov, entry, problems, "keys/%s/%s" % (base, k))
                kc, desc, dflt = key_row(None, k, prop, None, help_for(owners, "keys", k), icons, problems, where)
                for alias, target in TOPIC_ALIASES.items():
                    a_base = alias.split(".")[0]
                    if target == iid and a_base in classes:
                        extra = help_for([a_base], "keys", k)
                        if extra and extra.get("desc") and extra["desc"] not in desc:
                            desc += "<br><br>" + tcell(_sentence(autolink(extra["desc"])))
                rows.append("| %s | %s | %s |" % (kc, desc, dflt))
                row_anchors[k] = topic[iid][2]
                _note_rows(base, {k: prop}, {}, {}, {}, owners)
            else:
                entry = {str(x): v for x, v in (prov["flags"].get(base) or {}).items()}.get(flag)
                icons = ported_icons(prov, entry, problems, "flags/%s/%s" % (base, flag))
                flag_lines.append(flag_list(None, {flag: (label, None)}, {}, owners, {flag: icons}, problems, where))
                flag_anchors[flag] = topic[iid][2]
                _note_rows(base, {}, {flag: (label, None)}, {}, {}, owners)
        if rows:
            table = "\n".join(["| Key | Description | Default |", "|---|---|---|"] + rows)
            md += [table, ""]
            mdx += [keyvalue_table(table, row_anchors), ""]
        if flag_lines:
            body = "\n".join(flag_lines)
            md += ["Flags:", "", body, ""]
            mdx += ["**Flags**", "", flag_components(body, flag_anchors), ""]
    return "\n".join(md).rstrip() + "\n", "\n".join(mdx).rstrip() + "\n"


def anchor_base(items):
    """The base class of the first item of a TOPICS section."""
    return items[0].split(".")[0].split("#")[0] if items else None


def index_page(classes, by_group, prov):
    parts = ["# Entities", "",
             "Every entity of `syndicate.fgd`, the editor file of the game, by group. Each page lists the "
             "entity's keys and flags as the editor shows them. Keys that many entities share are on "
             "[Common keys](common-keys.md).", ""]
    for gid, title, intro, _ in GROUPS:
        parts += ["## %s" % title, "", intro, "", "| Entity | Editor name | Ported from |", "|---|---|---|"]
        for n in by_group[gid]:
            src = ported_icons(prov, prov["entities"].get(n), [], "entities/" + n)
            parts.append("| [%s](%s.md) | %s | %s |" % (n, n, cell(fgd_title(classes[n]), link=False), src))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Docusaurus output: the Markdown pages above as MDX, the sidebar and the Entity List data
# ---------------------------------------------------------------------------

_PORTED = re.compile(r"\[\[ported:([a-z0-9_ -]+)\]\]")
_TAGS_OK = re.compile(r"<(?=/?(?:br|kbd|details|summary|sub|sup)\b)")
KINDS = {"pointclass": "Point", "solidclass": "Brush"}
# Classes that are neither: worldspawn, the one world entity of every map
SPECIAL = {"worldspawn"}


def kind_of(classes, name):
    """The type the docs show: Point, Brush or Special."""
    return "Special" if name in SPECIAL else KINDS[classes[name]["kind"]]


# Keys the player presses, written ++name++ in the text (as pymdownx.keys names them): shown as <kbd>
KEY_LABELS = {"enter": "Enter", "escape": "Esc", "tab": "Tab", "space": "Space", "page-up": "Page Up",
              "page-down": "Page Down", "shift": "Shift", "ctrl": "Ctrl", "alt": "Alt", "delete": "Del",
              "insert": "Ins", "end": "End", "home": "Home", "pause": "Pause", "arrow-up": "Up", "arrow-down": "Down",
              "arrow-left": "Left", "arrow-right": "Right"}


def _kbd(m):
    name = m.group(1)
    label = name[1:-1] if name.startswith('"') else KEY_LABELS.get(name, name.upper() if len(name) <= 3 else name)
    return "<kbd>%s</kbd>" % label


def mdx_escape(line):
    """One Markdown line, safe for MDX: braces escaped, <br> closed, a "<" that starts no known tag escaped, ++key++
    as <kbd>. Code spans are left alone. [[ported:...]] markers stay (portedPreprocessor in plugins/remark-sbo.mjs
    turns them into icons)."""
    parts = re.split(r"(`+[^`]*?`+)", line)
    for i in range(0, len(parts), 2):
        t = parts[i].replace("{", "\\{").replace("}", "\\}")
        t = re.sub(r"<br\s*/?>", "<br />", t)
        t = re.sub(r"<(?!/?(?:br|kbd|details|summary|sub|sup)\b|!--)", r"\\<", t)
        t = re.sub(r'\+\+("[^"]+"|[a-z0-9-]+)\+\+', _kbd, t)
        parts[i] = t
    return "".join(parts)


def mdx_block(block):
    """mdx_escape() on every line outside fenced code."""
    out, fence = [], False
    for line in block.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line)
        else:
            out.append(line if fence else mdx_escape(line))
    return "\n".join(out)


def _attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def _cell_blocks(cell):
    """A generated table cell (blocks split by <br><br>, bullets as &bull;&nbsp; lines) as Markdown blocks; a list
    of more than eight lines folds away."""
    blocks = []
    for block in cell.split("<br><br>"):
        lines = block.split("<br>")
        if all(l.startswith("&bull;") for l in lines):
            items = "\n".join("- " + l[len("&bull;&nbsp;"):] for l in lines)
            if len(lines) > 8:
                items = "<details>\n<summary>The %d choices</summary>\n\n%s\n\n</details>" % (len(lines), items)
            blocks.append(items)
        else:
            blocks.append("\n".join(lines))
    return "\n\n".join(mdx_block(b.replace("\\|", "|")) for b in blocks)


def _table_rows(body):
    """(pre text, [(name, ported ids, key, description, default)]) of an Attributes table section."""
    pre, rows = [], []
    for line in body.split("\n"):
        if line.startswith("| **"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            m = re.match(r"\*\*(.+?)\*\*(.*?)<br>`([^`]+)`", cells[0])
            ids = _PORTED.findall(m.group(2))
            rows.append((m.group(1).replace("\\*", "*"), ids[0] if ids else "", m.group(3), cells[1],
                         cells[2] if len(cells) > 2 else ""))
        elif not line.startswith("|"):
            pre.append(line)
    return "\n".join(pre).strip(), rows


def _default_attr(d):
    return d[1:-1] if d.startswith("`") and d.endswith("`") else d


def keyvalue_table(body, anchors=None):
    """An Attributes table as <KeyvalueTable>; anchors: {key (lower case): [row anchors]}."""
    pre, rows = _table_rows(body)
    out = []
    if pre:
        out += [mdx_block(pre), ""]
    if not rows:
        return "\n".join(out).rstrip()  # only the common-keys list: no table
    out.append("<KeyvalueTable>")
    out.append("")
    for name, ids, key, desc, default in rows:
        attrs = 'name="%s" keyname="%s"' % (_attr(name), _attr(key))
        if default:
            attrs += ' default="%s"' % _attr(_default_attr(default))
        if ids:
            attrs += ' ported="%s"' % ids
        if anchors and anchors.get(key.lower()):
            attrs += ' anchors="%s"' % " ".join(anchors[key.lower()])
        out += ["<Keyvalue %s>" % attrs, "", _cell_blocks(desc), "", "</Keyvalue>", ""]
    out.append("</KeyvalueTable>")
    return "\n".join(out)


def flag_components(body, anchors=None):
    """The Flags list ("- **Name** (value) [[ported:...]] - text") as <FlagList>; other lines stay text. anchors:
    {value: [anchors of the flag]}."""
    out, items, rest = [], [], []
    for item in re.split(r"\n(?=- )", body.strip()):
        m = re.match(r"- \*\*(.+?)\*\* \(([^)]+)\)(.*?)(?: - (.*))?$", item, re.S)
        if not m:
            rest.append(item)
            continue
        ids = _PORTED.findall(m.group(3))
        attrs = 'name="%s" value="%s"' % (_attr(m.group(1).replace("\\*", "*")), _attr(m.group(2)))
        if ids:
            attrs += ' ported="%s"' % ids[0]
        if anchors and anchors.get(m.group(2)):
            attrs += ' anchors="%s"' % " ".join(anchors[m.group(2)])
        desc = " ".join((m.group(4) or "").split())
        items += ["<Flag %s>" % attrs, "", mdx_block(desc), "", "</Flag>", ""]
    if items:
        out += ["<FlagList>", ""] + items + ["</FlagList>"]
    if rest:
        out += ["", mdx_block("\n".join(rest))]
    return "\n".join(out)


def _sections(content):
    """(title line, summary, [(heading, body)]) of a generated page."""
    head, _, rest = content.partition("\n")
    parts = re.split(r"^## (.+)$", rest, flags=re.M)
    return head, parts[0].strip(), [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def plain_summary(summary):
    first = summary.split("\n\n")[0]
    first = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first)
    first = _PORTED.sub("", first)
    first = re.sub(r'\+\+("[^"]+"|[a-z0-9-]+)\+\+', lambda m: _kbd(m)[5:-6], first)
    return " ".join(first.split())


def summary_html(summary):
    """The first paragraph of a summary as HTML, for the Entity List's description column."""
    s = plain_summary(summary).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("\\_", "_").replace("\\*", "*")
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def _front_matter(fields):
    out = ["---"]
    for k, v in fields:
        if v is not None:
            out.append("%s: %s" % (k, v if isinstance(v, int) else json.dumps(v)))
    return "\n".join(out + ["---", ""])


GENERATED = ("{/* Generated by scripts/gen_entity_docs.py from sdk/syndicate.fgd, docs-site/provenance.yml, "
             "docs-site/entity-text/ and docs-site/key-help/. Do not edit: change those. */}\n")


def entity_mdx(name, content, kind, icon, entity_ported, description=None):
    """An entity page: the header (editor icon, type, "Ported from"), the summary, the Attributes and Flags as
    components, the other sections as they are. The front matter description is the entity-text's own short
    description, else the summary's first paragraph."""
    _title, summary, sections = _sections(content)
    fm = _front_matter([("title", name), ("description", description or plain_summary(summary)), ("image", icon),
                        ("history_source", "docs-site/entity-text/%s.md" % name)])
    out = [fm + GENERATED]
    out.append('<EntityHeader name="%s" icon="%s" kind="%s"%s />' % (
        name, icon or "", kind, (' ported="%s"' % entity_ported) if entity_ported else ""))
    out += ["", mdx_block(summary), ""]
    for heading, body in sections:
        if heading == "Attributes":
            out += ["## Attributes", "", keyvalue_table(body), ""]
        elif heading == "Flags":
            pre, _, flags = body.partition("\n- ") if not body.startswith("- ") else ("", "", body[2:])
            out += ["## Flags", ""]
            if pre.strip():
                out += [mdx_block(pre.strip()), ""]
            out += [flag_components("- " + flags), ""]
        else:
            out += ["## %s" % mdx_escape(heading), "", mdx_block(body), ""]
    return "\n".join(out).rstrip() + "\n"


def index_mdx():
    return (_front_matter([("title", "Entity List"), ("sidebar_label", "Entity List"),
                           ("description", "Every entity of SBO with its editor icon and a short description"),
                           ("hide_table_of_contents", True)]) + GENERATED +
            "import EntityTable from '@site/src/components/EntityTable';\n"
            "import entities from './entity-index.json';\n\n"
            "# Entity List\n\n"
            "Every entity of `syndicate.fgd`, the editor file of the game, with its editor icon and a short "
            "description. Click an entity's name to open its page, which lists the entity's keys and flags as the "
            "editor shows them. Keys that many entities share are on [Common keys](common-keys.md).\n\n"
            "<EntityTable entities={entities} />\n")


def sidebar_items(by_group, icons):
    items = [{"type": "doc", "id": NAV_DIR + "/common-keys", "label": "Common keys"}]
    for gid, title, _intro, _ in GROUPS:
        group = []
        for n in by_group[gid]:
            item = {"type": "doc", "id": "%s/%s" % (NAV_DIR, n), "label": n}
            if icons.get(n):
                item["customProps"] = {"icon": icons[n]}
            group.append(item)
        items.append({"type": "category", "label": title, "collapsed": True, "items": group})
    return items


def entity_index(classes, by_group, pages, icons, prov):
    out = []
    for gid, title, _intro, _ in GROUPS:
        for n in by_group[gid]:
            _t, summary, _s = _sections(pages[n + ".md"])
            src = prov["entities"].get(n)
            out.append({"Classname": n, "Description": summary_html(summary), "Icon": icons.get(n) or "",
                        "Type": kind_of(classes, n), "Group": title,
                        "Ported": " ".join(_sources(src)) if src else ""})
    return sorted(out, key=lambda e: e["Classname"].lower())


# ---------------------------------------------------------------------------
# Entity icons (docs-site/static/img/entities/<class in lower case>.png, committed)
# ---------------------------------------------------------------------------

# Entities with no editor sprite or model (every brush entity and a few point entities) get a letter tile: the
# editor icons' disk and rim with the first letter of the name after its prefix (func_breakable -> B)
LETTER_COLORS = {"Brush": (95, 176, 79), "Point": (108, 117, 214), "Special": (230, 160, 50)}   # SBO green;
# the docs' info blue, darker; the warning amber for the world entity


def icon_letter(name):
    if name in SPECIAL:
        return name[0].upper()
    rest = name.split("_", 1)[1] if "_" in name.strip("_") else name
    return (rest.strip("_") or name)[0].upper()


def icon_source(classes, name):
    """(kind, detail) of a class's picture: ("sprite", path of the PNG source or .spr) for a point entity with an
    editor sprite, ("model", model path) for one the editor shows as a model, ("letter", None) for a brush entity
    and any other entity (a letter tile)."""
    cls = classes[name]
    if cls["kind"] == "solidclass":
        return "letter", None
    for helper, args in _helpers(classes, name):
        if helper == "iconsprite" and args:
            spr = args[0]
            base = os.path.splitext(os.path.basename(spr))[0]
            for cand in (os.path.join(REPO, "sdk", "spritesrc", "editor", base + ".png"),
                         os.path.join(REPO, "sdk", "spritesrc", "editor", name.lower() + ".png"),
                         os.path.join(REPO, "gamedir", "syndicate", spr)):
                if os.path.isfile(cand):
                    return "sprite", cand
            return "sprite", None
    for helper, args in _helpers(classes, name):
        if helper == "studio":
            return "model", args[0] if args else ""
    png = os.path.join(REPO, "sdk", "spritesrc", "editor", name.lower() + ".png")
    if os.path.isfile(png):
        return "sprite", png
    return "letter", None


def _helpers(classes, name, seen=None):
    """The class's own editor helpers, then those of its bases (the editor takes the first it finds)."""
    seen = set() if seen is None else seen
    out = list(classes[name]["helpers"])
    for base in classes[name]["bases"]:
        if base in classes and base not in seen:
            seen.add(base)
            out += _helpers(classes, base, seen)
    return out


def icon_file(name):
    """The picture's file name: the class name in lower case (Limitator -> limitator.png), as every file that ships
    is (scripts/check_lowercase.sh: the offline manual is part of the game's release zip)."""
    return name.lower() + ".png"


def entity_icons(classes, entities):
    """class -> the icon's site URL, for the classes whose icon file exists."""
    icons = {}
    for n in entities:
        kind, _detail = icon_source(classes, n)
        fn = icon_file(n)
        if kind and os.path.isfile(os.path.join(ENTITY_ICON_DIR, fn)):
            icons[n] = ENTITY_ICON_URL + fn
    return icons


def draw_letter_icon(letter, kind):
    """A letter tile in the editor icons' style (scripts/gen_editor_sprites.py): the 64x64 disk with its 1-pixel
    black rim, in the kind's color, and one capital of the pixel font, white with a black outline, at 5x."""
    import gen_editor_sprites as G
    c = G.Canvas(LETTER_COLORS[kind])
    scale = 5
    c.text_c(32, 32 - 7 * scale / 2.0, letter, (255, 255, 255), outline=(0, 0, 0), scale=scale)
    return [p + (255,) if p else (0, 0, 0, 0) for p in c.pixels()]


def write_icons(classes, entities):
    """Writes the sprite icons and the letter tiles; model pictures are rendered elsewhere (README) and kept."""
    import gen_editor_sprites as G
    os.makedirs(ENTITY_ICON_DIR, exist_ok=True)
    stale = os.path.join(ENTITY_ICON_DIR, "_brush.png")
    if os.path.isfile(stale):
        os.remove(stale)
    done = 0
    for n in entities:
        kind, src = icon_source(classes, n)
        if kind == "model" and not os.path.isfile(os.path.join(ENTITY_ICON_DIR, icon_file(n))):
            kind = "letter"   # a model entity with no default model to render (cycler)
        if kind == "letter":
            G.write_png(os.path.join(ENTITY_ICON_DIR, icon_file(n)), G.SIZE, G.SIZE,
                        draw_letter_icon(icon_letter(n), kind_of(classes, n)))
            done += 1
            continue
        if kind != "sprite" or not src:
            continue
        if src.endswith(".png"):
            w, h, px = G.read_png(src)
        else:
            w, h, px = G.spr_to_rgba(G.read_spr(src))
        if (w, h) == (G.SIZE * 4, G.SIZE * 4):
            px = [px[(y * 4) * w + x * 4] for y in range(G.SIZE) for x in range(G.SIZE)]
            w = h = G.SIZE
        G.write_png(os.path.join(ENTITY_ICON_DIR, icon_file(n)), w, h, px)
        done += 1
    return done


def write(path, content):

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--list-empty", action="store_true",
                    help="print every key and flag row without a description (class, key or flag, name, label)")
    ap.add_argument("--list-fgd-help", action="store_true",
                    help="print every key row that shows the FGD's own help text (no entity-text or key-help text)")
    ap.add_argument("--list-no-icon", action="store_true",
                    help="print every entity with no picture in static/img/entities/ (class, why)")
    ap.add_argument("--icons", action="store_true",
                    help="rewrite the editor-sprite icons and the letter tiles in static/img/entities/ (model "
                         "pictures are rendered separately and kept)")
    args = ap.parse_args()

    problems = []
    warnings = []
    classes = parse(FGD_PATH)
    entities = [n for n, c in classes.items()
                if c["kind"] in ("pointclass", "solidclass") and n not in HIDDEN_CLASSES]
    by_group = collections.OrderedDict((g[0], []) for g in GROUPS)
    for name in entities:
        g = group_of(name, classes[name]["kind"])
        if g is None:
            problems.append("no group for %s (add it to GROUPS)" % name)
        else:
            by_group[g].append(name)
    for g in by_group:
        by_group[g].sort(key=lambda n: (n != "worldspawn", n.lower()))

    CLASS_NAMES.update(entities)
    prov = load_provenance(PROVENANCE_PATH, problems)
    KEY_HELP.update(load_key_help(problems))
    for cls in KEY_HELP:
        if cls not in classes:
            problems.append("key-help/%s: %s is no class of the FGD" % (KEY_HELP[cls]["file"], cls))
    for n in prov["entities"]:
        if n not in entities:
            problems.append("provenance.yml: entities/%s is no class of the FGD" % n)
    check_provenance(classes, prov, problems)

    texts = {}
    if os.path.isdir(TEXT_DIR):
        for fn in sorted(os.listdir(TEXT_DIR)):
            if not fn.endswith(".md"):
                continue
            n = fn[:-3]
            if n not in entities:
                problems.append("entity-text/%s: no FGD class %s" % (fn, n))
                continue
            texts[n] = load_text(os.path.join(TEXT_DIR, fn))
            d = texts[n]["description"]
            if d is not None and not (isinstance(d, str) and d.strip() and len(d) <= DESCRIPTION_MAX):
                problems.append("entity-text/%s: the front matter description must be plain text of at most %d "
                                "characters" % (fn, DESCRIPTION_MAX))
            if texts[n]["new"]:
                style_problems(os.path.join(TEXT_DIR, fn), fn, problems)
    for n in entities:
        if n not in texts:
            warnings.append(n)

    for part, value in zip(TOPIC_INFO, topic_items(classes, problems)):
        part.update(value)
    common_inline_rows(classes)
    pages = collections.OrderedDict()
    for n in entities:
        pages[n + ".md"] = page(classes, n, texts.get(n), prov, problems)
    pages["common-keys.md"], common_mdx = common_page(classes, prov, problems)
    pages["index.md"] = index_page(classes, by_group, prov)
    monster_classes = gen_monster_classes.page(classes, problems)
    if args.check:
        gen_monster_classes.snapshot_problems(problems)
    if monster_classes:
        for i, line in enumerate(monster_classes.split("\n"), 1):
            bare = _CODE.sub("", line)
            m = FORBIDDEN.search(bare) or STYLE_PRONOUN.search(bare)
            if m:
                problems.append("templates/monster-classes.md: generated line %d: '%s' must not appear on the site"
                                % (i, m.group(0)))
    for cls, kind, item, _label in EMPTY_ROWS:
        problems.append("%s: %s %s has no description (entity-text bullet, FGD help or key-help)" % (cls, kind, item))
    if args.list_fgd_help:
        for row in dict.fromkeys(FGD_HELP_ROWS):
            print("%s\t%s\t%s\t%s" % row)
        return 0
    if args.list_empty:
        # One line per row without a description, under the class that defines the key or flag (a base class
        # once for all the pages that show it)
        done = set()
        for cls, kind, item, label in EMPTY_ROWS:
            owner = cls
            for o in [cls] + expanded_bases(classes, cls):
                props = classes[o]["props"]
                if kind == "key" and any(p["name"].lower() == item for p in props):
                    owner = o
                    break
                if kind == "flag" and any(p["name"].lower() == "spawnflags" and
                                          any(v == item for v, _l, _d in (p["choices"] or [])) for p in props):
                    owner = o
                    break
            if (owner, kind, item) in done:
                continue
            done.add((owner, kind, item))
            print("%s\t%s\t%s\t%s" % (owner, kind, item, label))
        return 0
    # Forbidden words: an error in the hand-written text, a warning in the generated pages (FGD text, which
    # this script does not own). Code spans (key names) are not checked.
    if os.path.isdir(TEXT_DIR):
        for fn in sorted(os.listdir(TEXT_DIR)):
            if fn.endswith(".md"):
                with open(os.path.join(TEXT_DIR, fn), encoding="utf-8") as fh:
                    for i, line in enumerate(fh, 1):
                        m = FORBIDDEN.search(_CODE.sub("", line))
                        if m:
                            problems.append("entity-text/%s:%d: '%s' must not appear on the site"
                                            % (fn, i, m.group(0)))
    fgd_words = []
    pronoun_warnings = []
    for fn, content in pages.items():
        rewritten = fn in ("index.md", "common-keys.md") or (texts.get(fn[:-3]) or {}).get("new")
        for i, line in enumerate(content.split("\n"), 1):
            bare = _CODE.sub("", line)
            m = FORBIDDEN.search(bare)
            if m:
                fgd_words.append("%s:%d '%s'" % (fn, i, m.group(0)))
            # he / his / him from any source (entity-text, key-help, FGD help): an error on a rewritten page, a
            # warning on a page in the old format
            m = STYLE_PRONOUN.search(bare)
            if m:
                where = "%s:%d '%s' (they / their / them)" % (fn, i, m.group(0))
                if rewritten:
                    problems.append("generated page " + where)
                else:
                    pronoun_warnings.append(where)
    if pronoun_warnings:
        sys.stderr.write("gen_entity_docs: warning: he / his / him on pages not rewritten yet: %s\n"
                         % ", ".join(pronoun_warnings))
    if fgd_words:
        sys.stderr.write("gen_entity_docs: warning: words from the FGD that must not appear on the site: %s\n"
                         % ", ".join(fgd_words))

    if args.icons:
        print("gen_entity_docs: %d sprite icons and letter tiles -> %s" % (write_icons(classes, entities),
                                                                                ENTITY_ICON_DIR))
    icons = entity_icons(classes, entities)
    no_icon = [(n, icon_source(classes, n)) for n in entities if n not in icons]
    if args.list_no_icon:
        for n, (kind, detail) in no_icon:
            why = {"model": "model %s not rendered" % (detail or "(none in the FGD)"),
                   "sprite": "sprite source missing", "letter": "letter tile missing"}.get(kind, "no editor sprite or model")
            print("%s\t%s" % (n, why))
        return 0

    if warnings:
        sys.stderr.write("gen_entity_docs: warning: no entity-text file (%d): %s\n"
                         % (len(warnings), ", ".join(warnings)))
    if problems:
        for p in dict.fromkeys(problems):
            sys.stderr.write("gen_entity_docs: %s\n" % p)
        return 1
    if args.check:
        print("gen_entity_docs: check OK (%d entities, %d text files)" % (len(entities), len(texts)))
        return 0

    out_dir = args.out or OUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    mdx = collections.OrderedDict()
    for n in entities:
        src = prov["entities"].get(n)
        mdx[n + ".md"] = entity_mdx(n, pages[n + ".md"], kind_of(classes, n), icons.get(n),
                                    " ".join(_sources(src)) if src else "",
                                    (texts.get(n) or {}).get("description"))
    mdx["common-keys.md"] = common_mdx
    mdx["index.md"] = index_mdx()
    keep = set(mdx) | {"sidebar.json", "entity-index.json"}
    for fn in os.listdir(out_dir) if out_dir == OUT_DIR else ():
        # The directory is build output: pages of classes that left the FGD are removed.
        if fn not in keep:
            os.remove(os.path.join(out_dir, fn))
    for fn, content in mdx.items():
        write(os.path.join(out_dir, fn), content)
    write(os.path.join(out_dir, "sidebar.json"), json.dumps(sidebar_items(by_group, icons), indent=1) + "\n")
    write(os.path.join(out_dir, "entity-index.json"),
          json.dumps(entity_index(classes, by_group, pages, icons, prov), indent=1) + "\n")
    write(MONSTER_CLASSES_PATH if out_dir == OUT_DIR else os.path.join(out_dir, "monster-classes.md"),
          monster_classes)
    if out_dir == OUT_DIR and gen_monster_classes.write_snapshot():
        print("gen_entity_docs: %s updated from src/dlls (commit it)" % os.path.relpath(gen_monster_classes.SNAPSHOT, REPO))
    if no_icon:
        sys.stderr.write("gen_entity_docs: warning: no picture (%d): %s\n"
                         % (len(no_icon), ", ".join(n for n, _ in no_icon)))
    print("gen_entity_docs: %d entity pages (%d with text) -> %s" % (len(entities), len(texts), out_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
