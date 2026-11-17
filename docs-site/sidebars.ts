import fs from 'node:fs';
import path from 'node:path';
import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

// The site's navigation. The Entities part is written by scripts/gen_entity_docs.py with the entity pages
// (docs/mapping/entities/sidebar.json, build output like the pages).
const ENTITY_SIDEBAR = path.join(__dirname, 'docs', 'mapping', 'entities', 'sidebar.json');
if (!fs.existsSync(ENTITY_SIDEBAR)) {
  throw new Error('docs/mapping/entities/ is missing: run python3 scripts/gen_entity_docs.py first');
}
const entities = JSON.parse(fs.readFileSync(ENTITY_SIDEBAR, 'utf8'));

const doc = (id: string, label: string) => ({ type: 'doc' as const, id, label });
const category = (label: string, items: unknown[], link?: string) => ({
  type: 'category' as const,
  label,
  collapsed: true,
  ...(link ? { link: { type: 'doc' as const, id: link } } : {}),
  items,
});

const sidebars: SidebarsConfig = {
  docs: [
    doc('index', 'Welcome'),
    category('Playing', [
      doc('playing/installing', 'Downloading & Installing'),
      doc('playing/controls', 'Controls'),
      doc('playing/loadout', 'Loadout'),
      doc('playing/weapons-and-items', 'Weapons and items'),
      doc('playing/hud-and-scoreboard', 'HUD and scoreboard'),
      doc('playing/chat-and-console', 'Chat and console'),
      doc('playing/spectating', 'Spectating'),
      doc('playing/menus', 'Menus'),
      doc('playing/options', 'Options'),
      doc('playing/sprays', 'Sprays'),
      doc('playing/discord', 'Discord'),
    ]),
    category('Game modes', [
      doc('game-modes/coop', 'Co-op'),
      doc('game-modes/battle-royale', 'Battle Royale'),
      doc('game-modes/bounty-killer', 'Bounty Killer'),
    ], 'game-modes/index'),
    category('Server setup', [
      doc('server/settings', 'Settings'),
      doc('server/files', 'Files'),
      doc('server/logs', 'Logs'),
    ], 'server/index'),
    category('Mapping', [
      category('Getting started', [
        doc('mapping/getting-started/editor-setup', 'Editor setup'),
        doc('mapping/getting-started/compiling', 'Compiling'),
        doc('mapping/getting-started/testing', 'Testing a map'),
        doc('mapping/getting-started/cheat-commands', 'Cheat commands'),
        doc('mapping/getting-started/useful-tools', 'Useful tools'),
        doc('mapping/basics/map-names-and-spawns', 'Map names and spawns'),
        doc('mapping/basics/briefing', 'Briefing'),
        doc('mapping/basics/custom-content', 'Custom content'),
        doc('mapping/basics/overviews', 'Overviews'),
        doc('mapping/basics/map-picture', 'Map picture'),
        doc('mapping/basics/compiler-notes', 'Compiler notes'),
        doc('mapping/basics/old-maps', 'Old maps'),
      ]),
      category('Logic and triggering', [
        doc('mapping/guide/entity-keyvalues', 'Entity keyvalues'),
        doc('mapping/guide/entity-triggering', 'Entity triggering'),
        doc('mapping/guide/trigger-modes', 'Trigger modes'),
        doc('mapping/guide/locus', 'Locus system'),
        doc('guides/locus', 'Locus tutorial'),
        doc('mapping/guide/masters-and-states', 'Masters and states'),
        doc('guides/masters', 'Masters tutorial'),
        doc('guides/value-triggers', 'Changing values'),
        doc('guides/calc-entities', 'calc_ entities'),
        doc('mapping/guide/changing-keys', 'Changing keys'),
        doc('mapping/guide/round-hooks', 'Round hooks'),
        doc('mapping/guide/monster-classes', 'Monster classes'),
      ]),
      category('Features', [
        doc('mapping/features/weather', 'Weather and fog'),
        doc('mapping/features/color-correction', 'Color correction'),
        doc('mapping/features/sky', '3D sky'),
        doc('mapping/features/mirrors', 'Mirrors'),
        doc('mapping/features/entity-glow', 'Entity glow'),
        doc('mapping/features/waypoints', 'Waypoints'),
        doc('mapping/features/world-text', 'World text'),
        doc('mapping/features/world-screens', 'World screens'),
        doc('mapping/features/moving-objects', 'Moving objects'),
        doc('mapping/features/model-scale', 'Model scale'),
        doc('mapping/features/particles', 'Particles'),
        doc('mapping/features/props-and-fades', 'Props, models and fades'),
        doc('mapping/features/materials', 'Materials'),
        doc('mapping/features/light-styles', 'Light styles'),
        doc('mapping/features/model-lights', 'Lights on models'),
        doc('mapping/features/music', 'Music and sound'),
        doc('mapping/features/sequences', 'Sequence files'),
        doc('mapping/features/tutor', 'Tutor messages'),
        doc('mapping/features/message-boxes', 'Message boxes'),
        doc('mapping/features/game-timer', 'HUD timer'),
        doc('mapping/features/teleports-and-jump-pads', 'Teleports and jump pads'),
        doc('mapping/features/video', 'Video'),
      ]),
      category('Entities', entities, 'mapping/entities/index'),
    ]),
    category('Changelog', [
      doc('changes', 'Changes since 1.38'),
    ], 'changelog/index'),
    doc('credits', 'Credits'),
  ],
};

export default sidebars;
