// Social cards: the picture and short text a link preview shows (Discord, Steam, forums), for every page.
//
// withSocialCards() wraps a docs or blog plugin. After the plugin loads its pages, each page gets the front matter
// field social: {image, description, alt}. src/theme/DocItem/Metadata and src/theme/BlogPostPage/Metadata put it in
// the page's Open Graph and Twitter tags. After the build, each page's card is drawn into the build folder at
// img/social/<page path>.png (1200x630): the page title, its short description, its section in the sidebar
// ("Mapping · Entities"), the site name, and the page's icon (an entity page's picture) or the SBO logo. The docs
// plugin also draws img/social/default.png, the card of pages without their own (themeConfig.image).
//
// Short description: the front matter description, else the page's first paragraph, without Markdown, cut after the
// last whole sentence that fits in 155 characters. SBO_SOCIAL_REPORT=1 lists the pages where that cut falls inside a
// sentence, leaves only a short first sentence or finds no paragraph; give those pages a description in their front
// matter (entity pages: a "description:" line in the front matter of entity-text/<class>.md).
//
// Drawing: satori (layout and text to SVG), resvg (SVG to pixels) and UPNG (a 256-color PNG), no browser. The cards
// are cached by the hash of what they show in .social-cache/ (CI caches the folder), so a build draws only the cards
// that changed.

import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);

export const CARD = {width: 1200, height: 630};
const DESCRIPTION_MAX = 155;
const SITE_NAME = 'Syndicate Black Ops Docs';
// raise when the drawing changes, so cached cards are drawn again
const DESIGN = 2;

// The site's dark theme (src/css/sbo.css)
const COLORS = {
  bg: '#1b1b1f',
  panel: '#202127',
  raised: '#2b2c33',
  line: '#3c3f44',
  text: '#dfdfd6',
  muted: '#98989f',
  accent: '#8bd47a',
  theme: '#5fb04f',
  // behind the icon: light enough for the dark-grey model renders
  iconPanel: '#3a3c44',
};

// ---------------------------------------------------------------------------------------------------------------
// Short description

const PORTED = /\s*\[\[ported:[^\]]*\]\]/g;

// Markdown / MDX of one paragraph -> plain text
export function plainText(md, vars = {}) {
  return md
    .replace(PORTED, '')
    .replace(/\{\/\*[\s\S]*?\*\/\}/g, '')
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<([A-Z]\w*)\s*\/>/g, (m, name) => (name in vars ? vars[name] : ''))
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\[([^\]]*)\]\[[^\]]*\]/g, '$1')
    .replace(/<\/?[a-zA-Z][^>]*>/g, '')
    .replace(/\+\+([^+]+)\+\+/g, '$1')
    .replace(/`([^`]*)`/g, '$1')
    .replace(/(\*\*|__)(.+?)\1/g, '$2')
    .replace(/(^|[^\w*])\*([^*\s][^*]*?)\*(?!\w)/g, '$1$2')
    .replace(/(^|\W)_([^_\s][^_]*?)_(?!\w)/g, '$1$2')
    .replace(/\\([\\`*_{}\[\]()<>#+\-.!|])/g, '$1')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

// The first paragraph of a page body (front matter removed): {text, kind}, kind 'paragraph', or what came first
// when no paragraph comes before the first "## " heading ('none')
export function firstParagraph(body) {
  const lines = body.split('\n');
  let inFence = false;
  let inComment = false;
  let inAdmonition = 0;
  let inDetails = 0;
  const para = [];
  for (const raw of lines) {
    const line = raw.trim();
    if (inComment) {
      if (line.includes('*/}') || line.includes('-->')) inComment = false;
      continue;
    }
    if (/^(```|~~~)/.test(line)) {
      inFence = !inFence;
      if (para.length) break;
      continue;
    }
    if (inFence) continue;
    if (/^:::\w/.test(line)) { inAdmonition++; if (para.length) break; continue; }
    if (/^:::\s*$/.test(line)) { inAdmonition = Math.max(0, inAdmonition - 1); continue; }
    if (inAdmonition) continue;
    if (/^<details/.test(line)) { inDetails++; if (para.length) break; continue; }
    if (/^<\/details>/.test(line)) { inDetails = Math.max(0, inDetails - 1); continue; }
    if (inDetails) continue;
    if (line === '') {
      if (para.length) break;
      continue;
    }
    if ((line.startsWith('{/*') && !line.includes('*/}')) || (line.startsWith('<!--') && !line.includes('-->'))) {
      inComment = true;
      continue;
    }
    if (/^\{\/\*.*\*\/\}$/.test(line) || /^<!--.*-->$/.test(line)) continue;
    if (/^(import|export)\s/.test(line)) continue;
    if (/^##\s/.test(line)) break;            // the first section: no lead paragraph
    if (/^#\s/.test(line)) continue;          // the page title
    if (/^<[A-Za-z][^>]*\/>$/.test(line) || /^<\/?[A-Za-z][^>]*>$/.test(line)) {
      if (para.length) break;
      continue;                               // a component or tag on its own line (EntityHeader, a picture)
    }
    if (/^!\[/.test(line)) { if (para.length) break; continue; }
    if (/^(\||[-*+]\s|\d+\.\s|>)/.test(line)) {
      if (para.length) break;
      return {text: '', kind: line.startsWith('|') ? 'table' : 'list'};
    }
    para.push(line);
  }
  return {text: para.join(' '), kind: para.length ? 'paragraph' : 'none'};
}

// Plain text -> at most DESCRIPTION_MAX characters, cut after a whole sentence: {text, cut, thin}. cut: no whole
// sentence fits and the text ends inside one; thin: sentences were left out and what is left is under 70 characters.
// A last sentence that ends in ":" (it leads into a list) is left out.
export function shortDescription(full) {
  const ends = [];
  const re = /[.!?:](?=\s+["'(\[A-Z0-9])|[.!?:]$/g;
  let m;
  while ((m = re.exec(full))) {
    const before = full.slice(Math.max(0, m.index - 4), m.index + 1);
    if (/\b(e\.g|i\.e|etc|vs)\.$/i.test(before)) continue;
    if (full[m.index] === ':' && m.index + 1 < full.length) continue;   // a colon inside a sentence
    ends.push(m.index + 1);
  }
  let text = full;
  if (text.endsWith(':')) {
    const earlier = ends.filter(i => i < text.length);
    text = earlier.length ? text.slice(0, earlier[earlier.length - 1]).trim() : `${text.slice(0, -1)}.`;
  }
  if (text.length <= DESCRIPTION_MAX) return {text, cut: false, thin: text.length < full.length && text.length < 70};
  const fit = ends.filter(i => i <= DESCRIPTION_MAX);
  if (fit.length) {
    const short = text.slice(0, fit[fit.length - 1]).trim();
    return {text: short, cut: false, thin: short.length < 70};
  }
  const words = text.slice(0, DESCRIPTION_MAX - 1).replace(/\s+\S*$/, '').replace(/[,;:\s]+$/, '');
  return {text: `${words}…`, cut: true, thin: false};
}

// ---------------------------------------------------------------------------------------------------------------
// Sidebar sections and icons

// docId -> {section: ['Mapping', 'Entities'], icon}
function sidebarIndex(sidebars) {
  const index = new Map();
  const walk = (items, trail) => {
    for (const item of items || []) {
      if (item.type === 'category') {
        const here = [...trail, item.label];
        const linkId = item.link && item.link.type === 'doc' ? item.link.id : null;
        if (linkId && !index.has(linkId)) index.set(linkId, {section: here, icon: item.customProps?.icon});
        walk(item.items, here);
      } else if ((item.type === 'doc' || item.type === 'ref') && item.id) {
        if (!index.has(item.id) || item.type === 'doc') {
          const prev = index.get(item.id);
          if (!prev || prev.section.length < trail.length) index.set(item.id, {section: trail, icon: item.customProps?.icon});
        }
      }
    }
  };
  for (const items of Object.values(sidebars || {})) walk(items, []);
  return index;
}

// an icon path of the site (/img/...) -> its file in static/, if it is a picture that exists
function staticFile(siteDir, p) {
  if (typeof p !== 'string' || !/^\/img\/.+\.png$/i.test(p)) return null;
  const file = path.join(siteDir, 'static', p);
  return fs.existsSync(file) ? file : null;
}

function cardPath(permalink, baseUrl) {
  let rel = permalink.startsWith(baseUrl) ? permalink.slice(baseUrl.length) : permalink.replace(/^\//, '');
  rel = rel.replace(/\/+$/, '');
  return `img/social/${rel || 'index'}.png`;
}

function readBody(siteDir, source) {
  const file = path.join(siteDir, source.replace(/^@site\//, ''));
  const text = fs.readFileSync(file, 'utf8');
  return text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');
}

function describe({siteDir, source, frontMatter, vars, where, report}) {
  const own = typeof frontMatter.description === 'string' && frontMatter.description.trim();
  let plain;
  let kind = 'description';
  if (own) {
    plain = plainText(own, vars);
  } else {
    const first = firstParagraph(readBody(siteDir, source));
    kind = first.kind;
    plain = plainText(first.text, vars);
  }
  const short = shortDescription(plain);
  if (!short.text || short.cut || short.thin) {
    const problem = !short.text ? `no paragraph (${kind} first)` : short.cut ? 'cut inside a sentence' : 'only a short first sentence fits';
    report.push({where, kind, problem, text: short.text});
  }
  return short.text;
}

function socialFields(card, title, section, description) {
  const alt = [title, section.join(' · '), SITE_NAME].filter(Boolean).join(' · ');
  return {image: `/${card.file}`, description: description || undefined, alt};
}

// ---------------------------------------------------------------------------------------------------------------
// Drawing

let renderer = null;
async function loadRenderer(siteDir) {
  if (renderer) return renderer;
  const {default: satori} = await import('satori');
  const {Resvg} = await import('@resvg/resvg-js');
  const fontDir = path.join(path.dirname(require.resolve('@fontsource/inter/package.json')), 'files');
  const font = (weight) => ({
    name: 'Inter',
    weight,
    style: 'normal',
    data: fs.readFileSync(path.join(fontDir, `inter-latin-${weight}-normal.woff`)),
  });
  const fonts = [font(400), font(600), font(700)];
  const UPNG = require('upng-js');
  const logo = fs.readFileSync(path.join(siteDir, 'static', 'img', 'logo.png'));
  renderer = {satori, Resvg, UPNG, fonts, logo};
  return renderer;
}

const dataUri = (png) => `data:image/png;base64,${png.toString('base64')}`;

// a small picture scaled up without blurring its pixels (the editor icons are pixel art)
function upscale(Resvg, png, size) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${size}" height="${size}">`
    + `<image width="${size}" height="${size}" image-rendering="optimizeSpeed" xlink:href="${dataUri(png)}"/></svg>`;
  return new Resvg(svg, {fitTo: {mode: 'original'}}).render().asPng();
}

const h = (type, style, children) => ({type, props: {style, children}});

// The title's font size: as large as 76 px, but the longest word must fit on one line of the text column (about 740
// px; an Inter Bold letter is about 0.62 of the size wide), and a long title gets a smaller size
function titleSize(title) {
  const longest = Math.max(...title.split(/\s+/).map(w => w.length));
  const fit = Math.floor(740 / (0.62 * longest));
  const byLength = title.length <= 22 ? 76 : title.length <= 40 ? 64 : 54;
  return Math.max(36, Math.min(byLength, fit));
}

function cardTree({title, description, section, icon, logo}) {
  const {width, height} = CARD;
  const iconBox = h('div', {
      display: 'flex', alignItems: 'center', justifyContent: 'center', width: 264, height: 264, flexShrink: 0,
      marginLeft: 48, borderRadius: 32, backgroundColor: COLORS.iconPanel, border: `2px solid ${COLORS.line}`,
    }, [{type: 'img', props: {src: icon || logo, width: icon ? 192 : 168, height: icon ? 192 : 168}}]);
  return h('div', {
    display: 'flex', flexDirection: 'column', width, height, padding: '56px 72px 0 72px',
    backgroundColor: COLORS.bg,
    fontFamily: 'Inter', color: COLORS.text,
  }, [
    // the site: logo and name
    h('div', {display: 'flex', alignItems: 'center'}, [
      {type: 'img', props: {src: logo, width: 56, height: 56}},
      h('div', {marginLeft: 20, fontSize: 30, fontWeight: 600, color: COLORS.text}, SITE_NAME),
    ]),
    // the page
    h('div', {display: 'flex', flexGrow: 1, alignItems: 'center'}, [
      h('div', {display: 'flex', flexDirection: 'column', flexGrow: 1, flexShrink: 1, minWidth: 0}, [
        section ? h('div', {fontSize: 28, fontWeight: 600, color: COLORS.accent, marginBottom: 14}, section) : null,
        h('div', {
          fontSize: titleSize(title), fontWeight: 700, lineHeight: 1.12, color: '#ffffff', wordBreak: 'break-word',
          display: 'block', lineClamp: 3,
        }, title),
        description ? h('div', {
          fontSize: 30, fontWeight: 400, lineHeight: 1.4, color: COLORS.muted, marginTop: 22,
          display: 'block', lineClamp: 3,
        }, description) : null,
      ].filter(Boolean)),
      iconBox,
    ].filter(Boolean)),
    // the green line along the bottom
    h('div', {display: 'flex', width: width, height: 10, marginLeft: -72, backgroundColor: COLORS.theme}, []),
  ]);
}

async function drawCard(r, card) {
  const icon = card.iconFile ? dataUri(upscale(r.Resvg, fs.readFileSync(card.iconFile), 192)) : null;
  const svg = await r.satori(cardTree({...card, icon, logo: dataUri(r.logo)}), {...CARD, fonts: r.fonts});
  const image = new r.Resvg(svg, {fitTo: {mode: 'original'}, font: {loadSystemFonts: false}}).render();
  // a palette of 256 colors keeps the file small (about a third of the full-color PNG)
  const pixels = image.pixels;
  const rgba = pixels.buffer.slice(pixels.byteOffset, pixels.byteOffset + pixels.byteLength);
  return Buffer.from(r.UPNG.encode([rgba], image.width, image.height, 256));
}

function cardHash(card) {
  const icon = card.iconFile ? crypto.createHash('sha256').update(fs.readFileSync(card.iconFile)).digest('hex') : '';
  return crypto.createHash('sha256')
    .update(JSON.stringify([DESIGN, card.title, card.description, card.section, icon]))
    .digest('hex').slice(0, 32);
}

// Draw (or take from the cache) every card into the build folder; cards this build doesn't use leave the cache
export async function writeCards({siteDir, outDir, cards, label}) {
  const cacheDir = path.join(siteDir, '.social-cache', label);
  fs.mkdirSync(cacheDir, {recursive: true});
  const start = Date.now();
  const used = new Set();
  let drawn = 0;
  let r = null;
  for (const card of cards) {
    const name = `${cardHash(card)}.png`;
    used.add(name);
    const cached = path.join(cacheDir, name);
    if (!fs.existsSync(cached)) {
      r = r || await loadRenderer(siteDir);
      const png = await drawCard(r, card);
      fs.writeFileSync(`${cached}.tmp`, png);
      fs.renameSync(`${cached}.tmp`, cached);
      drawn++;
    }
    const target = path.join(outDir, card.file);
    fs.mkdirSync(path.dirname(target), {recursive: true});
    fs.copyFileSync(cached, target);
  }
  for (const name of fs.readdirSync(cacheDir)) {
    if (!used.has(name)) fs.rmSync(path.join(cacheDir, name), {force: true});
  }
  console.log(`[social-cards] ${label}: ${cards.length} cards (${drawn} drawn, ${cards.length - drawn} cached) in ${((Date.now() - start) / 1000).toFixed(1)} s`);
}

function printReport(label, report) {
  if (!process.env.SBO_SOCIAL_REPORT || !report.length) return;
  console.log(`[social-cards] ${label}: ${report.length} pages need a description in their front matter:`);
  for (const r of report) console.log(`  ${r.where}: ${r.problem}${r.text ? `: ${r.text}` : ''}`);
}

// ---------------------------------------------------------------------------------------------------------------
// Plugin wrappers

export function templateVars(context) {
  const sbo = context.siteConfig.customFields?.sbo || {};
  return {SboVersion: `SBO ${sbo.docsVersion}`, DocsVersion: sbo.docsVersion, LatestRelease: sbo.release};
}

// A plugin module's factory with its validateOptions (as Docusaurus finds it on a plugin given by name)
export function pluginOf(module) {
  const factory = module.default ?? module;
  const plugin = (context, options) => factory(context, options);
  plugin.validateOptions = module.validateOptions ?? factory.validateOptions;
  return plugin;
}

// kind: 'docs' (also draws the default card) or 'blog'; draw: false keeps the tags but draws no card (the offline
// manual, which no link preview ever reads)
export function withSocialCards(factory, kind, {draw = true} = {}) {
  async function wrapped(context, options) {
    const plugin = await factory(context, options);
    const {siteDir, baseUrl} = context;
    const vars = templateVars(context);
    let cards = [];
    return {
      ...plugin,
      async loadContent() {
        const content = await plugin.loadContent();
        const report = [];
        cards = [];
        if (kind === 'docs') {
          for (const version of content.loadedVersions) {
            const sidebar = sidebarIndex(version.sidebars);
            for (const doc of version.docs) {
              const fm = doc.frontMatter;
              const where = doc.source.replace(/^@site\//, '');
              const nav = sidebar.get(doc.id) || {section: []};
              const section = nav.section.slice(0, 2);
              const description = describe({siteDir, source: doc.source, frontMatter: fm, vars, where, report});
              const iconFile = staticFile(siteDir, nav.icon) || staticFile(siteDir, fm.image) || staticFile(siteDir, fm.icon);
              const card = {file: cardPath(doc.permalink, baseUrl), title: doc.title, description,
                section: section.join(' · '), iconFile};
              cards.push(card);
              fm.social = socialFields(card, doc.title, section, description);
            }
          }
          const tagline = context.siteConfig.tagline;
          cards.push({file: 'img/social/default.png', title: 'Syndicate Black Ops', description: tagline, section: '', iconFile: null});
        } else {
          for (const post of content.blogPosts) {
            const {metadata} = post;
            const fm = metadata.frontMatter;
            const where = metadata.source.replace(/^@site\//, '');
            const description = describe({siteDir, source: metadata.source, frontMatter: fm, vars, where, report});
            const section = [options.blogTitle || 'Blog'];
            const card = {file: cardPath(metadata.permalink, baseUrl), title: metadata.title, description,
              section: section.join(' · '), iconFile: staticFile(siteDir, fm.image)};
            cards.push(card);
            fm.social = socialFields(card, metadata.title, section, description);
          }
        }
        printReport(kind, report);
        return content;
      },
      async postBuild(props) {
        if (plugin.postBuild) await plugin.postBuild(props);
        if (draw) await writeCards({siteDir, outDir: props.outDir, cards, label: kind});
      },
    };
  }
  wrapped.validateOptions = factory.validateOptions;
  return wrapped;
}

// The tags of pages without their own card (the What's New list, search, 404); a page's own tags replace them
export function defaultCard(description) {
  return {
    image: 'img/social/default.png',
    metadata: [
      {name: 'description', content: description},
      {property: 'og:description', content: description},
      {property: 'og:type', content: 'website'},
      {property: 'og:site_name', content: SITE_NAME},
      {property: 'og:image:width', content: String(CARD.width)},
      {property: 'og:image:height', content: String(CARD.height)},
      {property: 'og:image:type', content: 'image/png'},
      {property: 'og:image:alt', content: SITE_NAME},
      {name: 'twitter:image:alt', content: SITE_NAME},
    ],
  };
}
