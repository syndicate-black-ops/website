// Search for the offline manual (SBO_DOCS_MANUAL=1, docusaurus.config.ts). A page opened from disk (file://) can't
// fetch() a file or start a Web Worker, so the local search theme of the website doesn't work there. This plugin
// writes the index as a script file, search-index.js next to index.html, which sets window.__SBO_SEARCH__; the
// SearchBar of theme/ loads it with a <script> tag the first time the search box gets the focus, and searches it in
// the page.
//
// One index entry per section of a page: the text under the page's top (title) and under each ## / ### heading, and
// each key and flag row of an entity page (their anchors key-<name> / flag-<value>, or the row's own anchors).
// The text comes from the page sources (Markdown / MDX), made plain as the link-preview descriptions are
// (plugins/social-cards.mjs plainText); the Changelog page indexes CHANGELOG.md.
//
// Entry: {p: page title, h: section heading or "", u: route[#anchor], x: plain text}

import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createSlugger, parseMarkdownHeadingId} from '@docusaurus/utils';
import {plainText, templateVars} from '../social-cards.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const INDEX_FILE = 'search-index.js';
const TEXT_MAX = 2000;   // characters of text kept per section
const PORTED = /\s*\[\[ported:[^\]]*\]\]/g;
const ATTR = (tag, name) => (new RegExp(`\\b${name}="([^"]*)"`).exec(tag) || [])[1];

function stripFrontMatter(md) {
  return md.replace(/^---\n[\s\S]*?\n---\n/, '');
}

// The sections of one page source: [{heading, anchor, lines[]}], the first one the page top (heading '')
function sections(md, vars) {
  const slugger = createSlugger();
  const out = [{heading: '', anchor: '', lines: []}];
  let fence = false;
  for (const raw of stripFrontMatter(md).split('\n')) {
    const line = raw.replace(/\r$/, '');
    if (/^\s*(```|~~~)/.test(line)) { fence = !fence; continue; }
    if (fence) { out[out.length - 1].lines.push(line); continue; }
    if (/^(import|export)\s/.test(line)) continue;
    const h = /^(#{1,6})\s+(.*)$/.exec(line);
    if (h) {
      const level = h[1].length;
      const {text, id} = parseMarkdownHeadingId(h[2].replace(PORTED, '').trim());
      const title = plainText(text, vars);
      const anchor = id || slugger.slug(title);
      if (level === 1) continue;              // the page title
      if (level <= 3) { out.push({heading: title, anchor, lines: []}); continue; }
      out[out.length - 1].lines.push(title);
      continue;
    }
    const kv = /^<(Keyvalue|Flag)\b[^>]*>/.exec(line);
    if (kv) {
      const tag = kv[0];
      const name = ATTR(tag, 'name') || '';
      const anchors = (ATTR(tag, 'anchors') || '').split(/\s+/).filter(Boolean);
      const anchor = anchors[0] || (kv[1] === 'Keyvalue' ? `key-${ATTR(tag, 'keyname')}` : `flag-${ATTR(tag, 'value')}`);
      const detail = kv[1] === 'Keyvalue' ? ATTR(tag, 'keyname') : `flag ${ATTR(tag, 'value')}`;
      out.push({heading: `${name} (${detail})`, anchor, lines: []});
      continue;
    }
    out[out.length - 1].lines.push(line.replace(/^\s*\|/, '').replace(/\|/g, ' ').replace(/^\s*[-*]\s+/, ''));
  }
  return out;
}

function entries({title, permalink, source, vars}) {
  let md = fs.readFileSync(source, 'utf8');
  const list = [];
  const parts = sections(md, vars);
  if (/<Changelog\s*\/>/.test(md)) {
    const changelog = path.resolve(path.dirname(source), '..', '..', '..', 'CHANGELOG.md');
    if (fs.existsSync(changelog)) parts.push(...sections(fs.readFileSync(changelog, 'utf8'), vars).slice(1));
  }
  for (const s of parts) {
    const text = plainText(s.lines.join('\n'), vars).slice(0, TEXT_MAX);
    if (!text && !s.heading) continue;
    list.push({p: title, h: s.heading, u: permalink + (s.anchor ? `#${s.anchor}` : ''), x: text});
  }
  return list;
}

export default function offlineSearch(context) {
  let index = [];
  return {
    name: 'sbo-offline-search',
    getThemePath() {
      return path.join(HERE, 'theme');
    },
    async allContentLoaded({allContent}) {
      const vars = templateVars(context);
      const site = context.siteDir;
      index = [];
      for (const byId of Object.values(allContent)) {
        for (const content of Object.values(byId || {})) {
          for (const version of content?.loadedVersions || []) {
            for (const doc of version.docs) {
              const source = path.join(site, doc.source.replace(/^@site\//, ''));
              index.push(...entries({title: doc.title.replace(PORTED, ''), permalink: doc.permalink, source, vars}));
            }
          }
          for (const post of content?.blogPosts || []) {
            const {metadata} = post;
            const source = path.join(site, metadata.source.replace(/^@site\//, ''));
            index.push(...entries({title: metadata.title, permalink: metadata.permalink, source, vars}));
          }
        }
      }
    },
    async postBuild({outDir, routesPaths}) {
      const routes = new Set(routesPaths);
      // a folder's index page has the permalink /folder/ and the route /folder (trailingSlash: false)
      for (const e of index) {
        const [route, anchor] = e.u.split('#');
        const alt = route.replace(/(.)\/$/, '$1');
        if (!routes.has(route) && routes.has(alt)) e.u = alt + (anchor ? `#${anchor}` : '');
      }
      const missing = index.filter(e => !routes.has(e.u.split('#')[0]));
      if (missing.length) {
        throw new Error(`[offline-search] ${missing.length} index entries name no page, e.g. ${missing[0].u}`);
      }
      if (!index.length) throw new Error('[offline-search] the search index is empty');
      const js = `window.__SBO_SEARCH__=${JSON.stringify(index).replace(/</g, '\\u003c')};\n`;
      fs.writeFileSync(path.join(outDir, INDEX_FILE), js);
      console.log(`[offline-search] ${index.length} sections, ${INDEX_FILE} ${Math.round(js.length / 1024)} KB`);
    },
  };
}
