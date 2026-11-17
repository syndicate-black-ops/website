"""The Monster classes page of the docs site, read from the game code (called by scripts/gen_entity_docs.py).

    page(classes, problems) -> the page as MDX, or None after a problem
    snapshot_problems(problems), write_snapshot()   the code snapshot (below): stale? / refresh it

The page is docs-site/templates/monster-classes.md (hand-written) with two lines replaced:

    @@GRID@@        the relationship grid: CBaseMonster::IDefaultRelationship's table (src/dlls/monsters.cpp, the
                    rows and columns in CLASS_ order, cbase.h), one colored cell per pair
    @@DEFAULTS@@    the class of every monster_ entity of the FGD: its C++ class (LINK_ENTITY_TO_CLASS in src/dlls)
                    and the CLASS_ value its Classify() returns, looked up through the base classes

The class names are the choice names of trigger_sensor's "classify" key (0-13), and the other class keys of the FGD
must give the same values the same names. A Classify() that doesn't return one CLASS_ constant needs its text in
SPECIAL, and a problem is reported for one that has none, so the page can't drift from the code.

The code snapshot docs-site/templates/monster-classes-code.json (committed) holds the facts of src/dlls the page uses:
the CLASS_ values, the relationship table, the C++ class of each listed monster, the base classes and Classify() of
those classes, their IRelationship overrides, and the few code lines the checks read. Where src/dlls is missing (the
website repository, which gets the docs without the game code) the page is made from the snapshot. With src/dlls
the page is made from the code, and gen_entity_docs.py --check fails while the snapshot differs from it
(gen_entity_docs.py writes it), so a change to the code the page reads updates the snapshot in the same commit.
"""

import glob
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DLLS = os.path.join(REPO, "src", "dlls")
TEMPLATE = os.path.join(REPO, "docs-site", "templates", "monster-classes.md")
SNAPSHOT = os.path.join(REPO, "docs-site", "templates", "monster-classes-code.json")

# The relationship values (monsters.h R_*): the letter in the cell (the legend pairs it with the name, so both grids
# fit the content width of a desktop page), its name in the legend and the cell's tooltip, the CSS class that colors it
RELATIONS = {
    "R_NM": ("N", "Nemesis", "nm"),
    "R_HT": ("H", "Hate", "ht"),
    "R_DL": ("D", "Dislike", "dl"),
    "R_FR": ("F", "Fear", "fr"),
    "R_AL": ("A", "Ally", "al"),
    "R_NO": ("–", "Ignore", "no"),
}

# The class keys whose choice names must match trigger_sensor's for the same value (other values, such as -1 None
# or 0 Default, aren't classes)
NAME_KEYS = [("MonsterCore", "classify"), ("monster_target", "frags"), ("MonsterCore", "prisonerto"),
             ("MonsterCore", "ignoredby"), ("monstermaker", "classify")]

# C++ classes whose Classify() isn't one constant: the text for the Class column
SPECIAL = {
    "CSqueakGrenade": "Alien bioweapon, and Alien military while it chases a player or a monster of the classes "
                      "Human passive, Human military, Alien military, Alien monster or Alien predator",
    # its "frags" key (CMonsterTarget::Classify), with the FGD default
    "CMonsterTarget": lambda classes, names: "Its **Classification**, which is %s unless you pick another"
                      % names[int((_choices_default(classes, "monster_target", "frags")))],
}

# Left out of the list and the monster grid (checked in the code): corpses and props that never fight (every C++
# class whose name starts with CDead is a corpse too), and the rope drops, which only spawn a Fed. Things that are no
# monster that looks (grenades, mines, the target) stay in the list for their class but leave the grid.
NEVER_FIGHT = {
    "monster_furniture": "a prop that scripts animate: MonsterInit but no attack, Classify none",
    "monster_sitting_scientist": "no MonsterInit (its own SittingThink): no monster sees it, it never fights",
    "monster_grunt_repel": "a rope spot that spawns a Fed",
    "monster_grunt_hunter_repel": "a rope spot that spawns a Fed Hunter",
}
NOT_IN_GRID = {"monster_tripmine", "monster_satchel", "monster_target"}

# The rope drops and the monster each one creates (checked: Create( "<class>" ) in the rope drop's source). The note
# goes on the first one's monster, the Fed.
ROPE_DROPS = [("monster_grunt_repel", "monster_human_grunt"), ("monster_grunt_hunter_repel", "monster_grunt_hunter")]

# The grid's row and column for the player (CBasePlayer::Classify), with a render of SBO's male player model
# (models/player/agent/agent.mdl, made with the entity pictures' model renderer)
PLAYER = ("Player", "CBasePlayer", "monster-classes/player")

# IRelationship overrides whose extra rules depend on something a map sets per entity or that happens in play: the
# grid shows their default, and the page's notes describe them. Any other override must be a rule on a target class
# name (FClassnameIs ... return R_*), or only call its base class, or the check fails.
CONDITIONAL = {
    "CTalkMonster": "Cop and Scientist: a player who provoked them (Tolerance level) is hated, and Pre-provoked makes "
                    "a friendlier monster dislike players",
    "CDark": "spawnflag 64 (wait until provoked): ignores players until provoked",
    "CISlave": "spawnflag 64 (wait until provoked): ignores players until provoked",
    "Chunter": "spawnflag 64 (wait until provoked): ignores players until provoked",
    "Cwerewolf": "spawnflag 64 (wait until provoked): ignores players until provoked",
    "CWerewolf_hunter": "spawnflag 64 (wait until provoked): ignores players until provoked",
    "CHornet": "hornets of the same model ignore each other",
}

# Rules on a target class name that name a base monster but not its Hunter variant, and that the page states in its
# notes instead of keeping the Hunter in the grid: base monster -> the overriding classes
KNOWN_TARGET_RULES = {"monster_human_grunt": ("CMinotaure",)}

# The legend: what a monster does about what it sees (BestVisibleEnemy picks the highest relationship, the nearest
# among equals; R_FR and R_AL never become an enemy, and R_FR only sets bits_COND_SEE_FEAR, which interrupts idle
# schedules)
MEANINGS = {
    "R_NM": "attacks this first, even when something else is closer",
    "R_HT": "attacks this when no nemesis is in view",
    "R_DL": "attacks this only when nothing it hates or treats as a nemesis is in view",
    "R_FR": "never attacks this, and seeing it only interrupts what the monster is doing, without making it run away",
    "R_AL": "never attacks this",
    "R_NO": "pays this no attention",
}
NEAREST = ("Among targets of the same kind, a monster picks the nearest, and a Fed that sees a Gargantua and a player goes for "
           "the Gargantua, its nemesis, even when the player is closer.")

# The class the grid uses for a C++ class whose Classify() isn't one constant (SPECIAL): its last return, checked
GRID_CLASS = {"CSqueakGrenade": "CLASS_ALIEN_BIOWEAPON"}

CLASS_DEFINE = re.compile(r"#define\s+(CLASS_\w+)\s+(\d+)")
LINK = re.compile(r"LINK_ENTITY_TO_CLASS\(\s*(\w+)\s*,\s*(\w+)\s*\)")
INLINE = re.compile(r"\bClassify\s*\(\s*(?:void)?\s*\)\s*\{\s*return\s+([^;{}]+?)\s*;\s*\}\s*;?")
OUTLINE = re.compile(r"^int\s+(\w+)\s*::\s*Classify\s*\(\s*(?:void)?\s*\)\s*\n\{(.*?)\n\}", re.M | re.S)
RETURN_ONE = re.compile(r"^\s*return\s+(CLASS_\w+)\s*;\s*$")


def _sources():
    out = {}
    for path in sorted(glob.glob(os.path.join(DLLS, "*.cpp")) + glob.glob(os.path.join(DLLS, "*.h"))):
        with open(path, "rb") as fh:
            out[os.path.basename(path)] = fh.read().decode("latin-1").replace("\r\n", "\n")
    return out


def _class_bodies(text):
    """(name, base, body) of every class declaration with a body in text."""
    for m in re.finditer(r"\bclass\s+(\w+)\s*(?::\s*public\s+(\w+))?\s*\{", text):
        depth, i = 0, m.end() - 1
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        yield m.group(1), m.group(2), text[m.end():i]


def read_code(problems):
    """CLASS_ values, the relationship table, classname -> C++ class, C++ class -> base, C++ class -> Classify()."""
    src = _sources()
    values = {}
    for m in CLASS_DEFINE.finditer(src.get("cbase.h", "")):
        values[m.group(1)] = int(m.group(2))

    table = None
    m = re.search(r"static\s+int\s+iEnemy\s*\[\s*14\s*\]\s*\[\s*14\s*\]\s*=\s*\{(.*?)\n\s*\};",
                  src.get("monsters.cpp", ""), re.S)
    if not m:
        problems.append("monster classes: no iEnemy[14][14] table in src/dlls/monsters.cpp")
    else:
        rows = re.findall(r"\{([^{}]*)\}", m.group(1))
        table = [re.findall(r"R_[A-Z]{2}", r) for r in rows]
        if len(table) != 14 or any(len(r) != 14 for r in table):
            problems.append("monster classes: the iEnemy table in src/dlls/monsters.cpp is not 14 x 14")
            table = None
        elif any(v not in RELATIONS for r in table for v in r):
            problems.append("monster classes: a relationship value the page doesn't know (RELATIONS)")
            table = None

    links, bases, classify, src_of = {}, {}, {}, {}
    for fn, text in src.items():
        for m in LINK.finditer(text):
            links.setdefault(m.group(1), m.group(2))
        for name, base, body in _class_bodies(text):
            src_of.setdefault(name, text)
            if base:
                bases.setdefault(name, base)
            im = INLINE.search(body)
            if im:
                classify[name] = im.group(1).strip()
        for m in OUTLINE.finditer(text):
            body = m.group(2).strip("\n")
            lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("//")]
            one = RETURN_ONE.match(lines[0]) if len(lines) == 1 else None
            classify[m.group(1)] = one.group(1) if one else "(code)"
    overrides = read_overrides(src, problems)
    return values, table, links, bases, classify, src_of, overrides


OVERRIDE = re.compile(r"^int\s+(\w+)\s*::\s*IRelationship\s*\(\s*CBaseEntity\s*\*\s*\w+\s*\)\s*\n\{(.*?)\n\}",
                      re.M | re.S)
RULE = re.compile(r"if\s*\(\s*(?:pTarget\s*&&\s*)?FClassnameIs\(\s*pTarget->pev\s*,\s*\"(\w+)\"\s*\)\s*\)\s*"
                  r"\{?\s*return\s+(R_[A-Z]{2})\s*;\s*\}?")
DELEGATE = re.compile(r"^\s*return\s+\w+\s*::\s*IRelationship\s*\(\s*pTarget\s*\)\s*;\s*$")


def read_overrides(src, problems):
    """C++ class -> ("rules", {target classname: R_*}) or ("conditional", text) for every IRelationship override."""
    out = {}
    for fn, text in src.items():
        for m in OVERRIDE.finditer(text):
            cls, body = m.group(1), re.sub(r"//[^\n]*", "", m.group(2))
            if cls == "CBaseMonster":
                continue
            rules = {t: r for t, r in RULE.findall(body)}
            rest = RULE.sub("", body).strip()
            if DELEGATE.match(rest):
                out[cls] = ("rules", rules)
            elif cls in CONDITIONAL:
                out[cls] = ("conditional", re.sub(r"\s+", " ", rest))
            else:
                problems.append("monster classes: %s::IRelationship (%s) is neither a rule on a class name nor in "
                                "CONDITIONAL" % (cls, fn))
    for cls in CONDITIONAL:
        if cls not in out:
            problems.append("monster classes: CONDITIONAL has %s, which has no IRelationship override" % cls)
    return out


def class_of(cpp, bases, classify):
    """The Classify() of a C++ class, through its bases: a CLASS_ name, other code, or None (unknown chain)."""
    seen = set()
    while cpp and cpp not in seen:
        seen.add(cpp)
        if cpp in classify:
            return cpp, classify[cpp]
        if cpp == "CBaseEntity":
            return cpp, "CLASS_NONE"
        cpp = bases.get(cpp)
    return None, None


def _choices(classes, cls, key):
    for p in (classes.get(cls) or {}).get("props", []):
        if p["name"].lower() == key.lower() and p["choices"]:
            return {v: l for v, l, _d in p["choices"]}
    return None


def _choices_default(classes, cls, key):
    for p in (classes.get(cls) or {}).get("props", []):
        if p["name"].lower() == key.lower():
            return p["default"]
    return None


def class_names(classes, problems):
    names = _choices(classes, "trigger_sensor", "classify")
    if not names or any(str(i) not in names for i in range(14)):
        problems.append("monster classes: trigger_sensor's classify key has no choices 0-13 for the class names")
        return None
    names = [names[str(i)] for i in range(14)]
    for cls, key in NAME_KEYS:
        other = _choices(classes, cls, key)
        if other is None:
            problems.append("monster classes: %s has no choices for %s" % (cls, key))
            continue
        for v, label in other.items():
            if v.lstrip("-").isdigit() and 1 <= int(v) <= 13 and label != names[int(v)]:
                problems.append("monster classes: %s %s choice %s is \"%s\", trigger_sensor's is \"%s\""
                                % (cls, key, v, label, names[int(v)]))
    return names


def grid(names, table):
    e = html.escape
    out = [legend(), "", '<div className="monster-class-grid">', "<table>", "<thead>", "<tr>",
           '<th className="mc-corner" scope="col">Looking ↓ / seen →</th>']
    for n in names:
        out.append('<th scope="col"><span>%s</span></th>' % e(n))
    out += ["</tr>", "</thead>", "<tbody>"]
    for i, row in enumerate(table):
        out.append("<tr>")
        out.append('<th scope="row">%s</th>' % e(names[i]))
        for v in row:
            word, label, css = RELATIONS[v]
            out.append('<td className="mc-%s" title="%s">%s</td>' % (css, label, word))
        out.append("</tr>")
    out += ["</tbody>", "</table>", "</div>"]
    return "\n".join(out)


def _title(classes, name):
    """The SBO name: the FGD title up to its first colon."""
    return classes[name]["desc"].replace("\\n", "\n").strip().partition("\n")[0].partition(":")[0].strip()


def _chain(cpp, bases):
    seen = []
    while cpp and cpp not in seen:
        seen.append(cpp)
        cpp = bases.get(cpp)
    return seen


def _monster_rules(cpp, bases, overrides):
    """The target-class rules and the conditional notes of a C++ class's IRelationship, through its bases."""
    rules, notes = {}, []
    for c in _chain(cpp, bases):
        kind, what = overrides.get(c, (None, None))
        if kind == "rules":
            for t, r in what.items():
                rules.setdefault(t, r)
        elif kind == "conditional":
            notes.append(c)
    return rules, notes


def _fgd_bases(classes, name, seen=None):
    seen = set() if seen is None else seen
    for b in classes[name]["bases"]:
        if b in classes and b not in seen:
            seen.add(b)
            _fgd_bases(classes, b, seen)
    return seen


def monsters(classes, names, values, links, bases, classify, src_of, overrides, problems):
    """Every listed monster: dicts with name, title, cpp, class text, class value (None: special), rules, notes."""
    out, used = [], set()
    for name in classes:
        if classes[name]["kind"] not in ("pointclass", "solidclass"):
            continue
        if not name.startswith("monster_") and "MonsterCore" not in _fgd_bases(classes, name):
            continue
        cpp = links.get(name)
        if not cpp:
            problems.append("monster classes: no LINK_ENTITY_TO_CLASS for %s" % name)
            continue
        if name in NEVER_FIGHT or cpp.startswith("CDead"):
            continue
        owner, ret = class_of(cpp, bases, classify)
        value = values.get(ret) if ret in values and 0 <= values[ret] < 14 else None
        if owner in SPECIAL:
            text = SPECIAL[owner]
            if callable(text):
                text = text(classes, names)
            used.add(owner)
            if owner in GRID_CLASS:
                body = re.search(r"int\s+%s\s*::\s*Classify\s*\(.*?\n\}" % owner, src_of.get(owner, ""), re.S)
                last = re.findall(r"return\s+(CLASS_\w+)\s*;", body.group(0)) if body else []
                if not last or last[-1] != GRID_CLASS[owner]:
                    problems.append("monster classes: %s::Classify() no longer ends with %s (GRID_CLASS)"
                                    % (owner, GRID_CLASS[owner]))
                value = values.get(GRID_CLASS[owner])
        elif value is not None:
            text = names[value]
        elif ret is None:
            problems.append("monster classes: the base classes of %s (%s) don't lead to a Classify()" % (name, cpp))
            continue
        else:
            problems.append("monster classes: %s::Classify() returns %s; add its text to SPECIAL in %s"
                            % (owner, ret, os.path.basename(__file__)))
            continue
        rules, notes = _monster_rules(cpp, bases, overrides)
        out.append(dict(name=name, title=_title(classes, name), cpp=cpp, owner=owner, text=text, value=value,
                        rules=rules, notes=notes, grid=name not in NOT_IN_GRID))
    for owner in SPECIAL:
        if owner not in used:
            problems.append("monster classes: SPECIAL has %s, which no listed monster uses" % owner)
    for name in NEVER_FIGHT:
        if name not in classes:
            problems.append("monster classes: NEVER_FIGHT has %s, which is no FGD class" % name)
    # Hunter variants: "<title> Hunter" of a listed monster. Left out when they share the base monster's class and
    # IRelationship rules (the base monster gets an asterisk), kept when they differ.
    by_title = {m["title"]: m for m in out}
    keep = []
    for m in out:
        base = by_title.get(m["title"][:-len(" Hunter")]) if m["title"].endswith(" Hunter") else None
        if base and base["value"] == m["value"] and base["rules"] == m["rules"] \
                and [overrides[c] for c in base["notes"]] == [overrides[c] for c in m["notes"]] \
                and not any(len(set(what) & {base["name"], m["name"]}) == 1
                            for cls, (kind, what) in overrides.items()
                            if kind == "rules" and cls not in KNOWN_TARGET_RULES.get(base["name"], ())):
            base["hunter"] = True
            base["hunter_variant"] = m
            continue
        if base:
            m["hunter_differs"] = base["name"]
        keep.append(m)
    return keep


HUNTER_NOTE = "¹ The Hunter variant of this monster has the same class"


def rope_note(classes, mons, links, src_of, problems):
    """The note on the Fed: the rope drops create a normal Fed or Fed Hunter of the Fed's class."""
    by_name = {m["name"]: m for m in mons}
    made = []
    for drop, monster in ROPE_DROPS:
        cpp = links.get(drop)
        if not cpp or not re.search(r'Create\(\s*"%s"' % monster, src_of.get(cpp, "")):
            problems.append("monster classes: %s doesn't create a %s (ROPE_DROPS)" % (drop, monster))
            return None
        made.append(monster)
    for m in mons:
        if m.get("hunter_variant"):
            by_name.setdefault(m["hunter_variant"]["name"], m["hunter_variant"])
    fed, hunter = by_name.get(made[0]), by_name.get(made[1])
    if not fed or not hunter or fed["value"] != hunter["value"]:
        problems.append("monster classes: the rope drops' monsters are not of one class (ROPE_DROPS)")
        return None
    fed["marks"] = fed.get("marks", "") + "²"
    return ("² %ss and %ss are normal %ss and %ss, %s from the moment they appear, and they shoot at an enemy they "
            "can see on the way down the rope" % (_title(classes, ROPE_DROPS[0][0]), _title(classes, ROPE_DROPS[1][0]),
                                                  _title(classes, made[0]), _title(classes, made[1]), fed["text"]))


def _notes(mons, rope):
    out = []
    if any(m.get("hunter") for m in mons):
        out += ["", HUNTER_NOTE]
    if rope:
        out += ["", rope]
    return out


def _marks(m):
    return " ".join(x for x in ("¹" if m.get("hunter") else "", m.get("marks", "")) if x)


def defaults(mons, rope):
    rows = sorted(mons, key=lambda m: m["title"].lower())
    out = ['<div className="monster-class-list">', "", "| Monster | Entity | Class |", "|---|---|---|"]
    for m in rows:
        out.append("| [%s](../entities/%s.md)%s | `%s` | %s |" % (m["title"], m["name"], _marks(m), m["name"], m["text"]))
    out += ["", "</div>"] + _notes(mons, rope)
    return "\n".join(out)


def _icon(name, title):
    path = name if "/" in name else "entities/" + name
    return ('<img src={require("@site/static/img/%s.png").default} alt="%s" title="%s" width="24" '
            'height="24" />' % (path, html.escape(title, quote=True), html.escape(title, quote=True)))


def monster_grid(mons, table, values, classify, rope, problems):
    e = html.escape
    pv = values.get(classify.get(PLAYER[1], ""))
    if pv is None:
        problems.append("monster classes: %s::Classify() is not one CLASS_ constant" % PLAYER[1])
        return ""
    cols = [dict(name=PLAYER[2], title=PLAYER[0], value=pv, rules={}, star="")]
    cols += [dict(name=m["name"], title=m["title"], value=m["value"], rules=m["rules"],
                  star=_marks(m)) for m in sorted(mons, key=lambda m: m["title"].lower())
             if m["grid"]]
    out = [legend(meanings=True), "", '<div className="monster-class-grid monster-grid">', "<table>", "<thead>", "<tr>",
           '<th className="mc-corner" scope="col">Looking ↓ / seen →</th>']
    for c in cols:
        out.append('<th scope="col">%s</th>' % _icon(c["name"], c["title"]))
    out += ["</tr>", "</thead>", "<tbody>"]
    for r in cols:
        out.append("<tr>")
        out.append('<th scope="row"><span className="mc-who">%s<span>%s%s</span></span></th>'
                   % (_icon(r["name"], r["title"]), e(r["title"]), r["star"]))
        for c in cols:
            rel = r["rules"].get(c["name"]) or table[r["value"]][c["value"]]
            word, label, css = RELATIONS[rel]
            out.append('<td className="mc-%s" title="%s: %s %s">%s</td>'
                       % (css, e(r["title"], quote=True), label, e(c["title"], quote=True), word))
        out.append("</tr>")
    out += ["</tbody>", "</table>", "</div>"] + _notes(mons, rope)
    return "\n".join(out)


def legend(meanings=False):
    out = ['<p className="monster-class-legend">']
    for key, (word, label, css) in RELATIONS.items():
        out.append('<span className="mc-%s" title="%s: %s"><b>%s</b> %s</span>'
                   % (css, label, MEANINGS[key], word, label))
    out.append("</p>")
    if meanings:
        out += [""] + ["- **%s** (%s) - %s" % (label, word, MEANINGS[key]) for key, (word, label, css) in RELATIONS.items()]
        out += ["", NEAREST]
    return "\n".join(out)


def _listed(classes, name):
    return classes[name]["kind"] in ("pointclass", "solidclass") and \
        (name.startswith("monster_") or "MonsterCore" in _fgd_bases(classes, name))


def reduce_code(classes, values, table, links, bases, classify, src_of, overrides):
    """Only the facts the page reads, as plain JSON data: the links of the listed monsters and the rope drops, the
    base chains from their C++ classes (and the classes of PLAYER, SPECIAL, CONDITIONAL, GRID_CLASS and the
    overrides), Classify() of those classes, and of the code text only the Classify() bodies of GRID_CLASS and the
    Create( "..." ) calls of the rope drops."""
    names = sorted({n for n in classes if _listed(classes, n)} | {d for d, _m in ROPE_DROPS})
    links_r = {n: links[n] for n in names if n in links}
    todo = set(links_r.values()) | set(overrides) | set(SPECIAL) | set(CONDITIONAL) | set(GRID_CLASS) | {PLAYER[1]}
    chain = set()
    while todo:
        c = todo.pop()
        if c in chain:
            continue
        chain.add(c)
        if c in bases:
            todo.add(bases[c])
    src_r = {}
    for owner in GRID_CLASS:
        body = re.search(r"int\s+%s\s*::\s*Classify\s*\(.*?\n\}" % owner, src_of.get(owner, ""), re.S)
        if body:
            src_r[owner] = body.group(0)
    for drop, _monster in ROPE_DROPS:
        cpp = links.get(drop)
        if cpp:
            src_r[cpp] = "\n".join(re.findall(r'Create\(\s*"\w+"', src_of.get(cpp, "")))
    return {
        "values": values, "table": table, "links": links_r,
        "bases": {c: bases[c] for c in sorted(chain) if c in bases},
        "classify": {c: classify[c] for c in sorted(chain) if c in classify},
        "src_of": src_r,
        "overrides": {c: list(v) for c, v in sorted(overrides.items())},
    }


_SNAPSHOT_TEXT = None   # the snapshot made from src/dlls by page(), for write_snapshot() / snapshot_problems()


def _snapshot_text(facts):
    return json.dumps(facts, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def code_facts(classes, problems):
    """(values, table, links, bases, classify, src_of, overrides): from src/dlls when it is there, else from the
    snapshot."""
    global _SNAPSHOT_TEXT
    if os.path.isdir(DLLS):
        facts = reduce_code(classes, *read_code(problems))
        _SNAPSHOT_TEXT = _snapshot_text(facts)
    elif os.path.isfile(SNAPSHOT):
        with open(SNAPSHOT, encoding="utf-8") as fh:
            facts = json.load(fh)
    else:
        problems.append("monster classes: neither src/dlls nor %s" % os.path.relpath(SNAPSHOT, REPO))
        return None
    overrides = {c: (v[0], v[1]) for c, v in facts["overrides"].items()}
    return (facts["values"], facts["table"], facts["links"], facts["bases"], facts["classify"], facts["src_of"],
            overrides)


def snapshot_problems(problems):
    """A problem when the committed snapshot differs from src/dlls (after page())."""
    if _SNAPSHOT_TEXT is None:
        return
    old = open(SNAPSHOT, encoding="utf-8").read() if os.path.isfile(SNAPSHOT) else None
    if old != _SNAPSHOT_TEXT:
        problems.append("monster classes: %s is out of date with src/dlls: run scripts/gen_entity_docs.py and commit "
                        "it" % os.path.relpath(SNAPSHOT, REPO))


def write_snapshot():
    """Writes the snapshot made from src/dlls (after page()); True when it changed."""
    if _SNAPSHOT_TEXT is None:
        return False
    old = open(SNAPSHOT, encoding="utf-8").read() if os.path.isfile(SNAPSHOT) else None
    if old == _SNAPSHOT_TEXT:
        return False
    with open(SNAPSHOT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(_SNAPSHOT_TEXT)
    return True


def page(classes, problems):
    n = len(problems)
    names = class_names(classes, problems)
    facts = code_facts(classes, problems)
    if facts is None:
        return None
    values, table, links, bases, classify, src_of, overrides = facts
    if not os.path.isfile(TEMPLATE):
        problems.append("monster classes: %s is missing" % os.path.relpath(TEMPLATE, REPO))
        return None
    with open(TEMPLATE, encoding="utf-8") as fh:
        text = fh.read()
    for marker in ("@@MONSTERGRID@@", "@@GRID@@", "@@DEFAULTS@@"):
        if text.count(marker) != 1:
            problems.append("monster classes: the template needs one line %s" % marker)
    if len(problems) > n or names is None or table is None:
        return None
    mons = monsters(classes, names, values, links, bases, classify, src_of, overrides, problems)
    rope = rope_note(classes, mons, links, src_of, problems)
    text = text.replace("@@MONSTERGRID@@", monster_grid(mons, table, values, classify, rope, problems))
    text = text.replace("@@GRID@@", grid(names, table))
    text = text.replace("@@DEFAULTS@@", defaults(mons, rope))
    return text if len(problems) == n else None
