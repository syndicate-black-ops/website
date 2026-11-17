// Page history of every doc, from git log, shown in each page's footer (src/theme/DocItem/Footer).
//
// The docs plugin is wrapped: after it loads the docs, each doc gets the front matter field edit_history, the
// commits that changed its source file, newest first: {hash, date, message, author}. The source of a hand-written
// page is its own file (renames followed); a generated entity page names its source in the front matter field
// history_source (docs-site/entity-text/<class>.md).
//
// Names: git author names and emails never reach the site. authors.yml maps each git author email to the public
// GitHub username the page shows (with its GitHub avatar; the offline manual shows no avatars) or hides it; an
// author missing there stops the build.
//
// One git log over docs-site/ gives every page's history. CI needs the full history (GIT_DEPTH 0); in a shallow
// clone the pages show the commits the clone has.

import {execFileSync} from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';
import docsPluginModule from '@docusaurus/plugin-content-docs';

const docsPlugin = docsPluginModule.default ?? docsPluginModule;
const LIMIT = 30;
const PORTED = /\s*\[\[ported:[^\]]*\]\]/g;

// authors.yml keys: an email, or "sha256:<hex>" of the email in lower case (an address that must not be published
// in the repository)
function emailKey(email) {
  return 'sha256:' + crypto.createHash('sha256').update(email.toLowerCase()).digest('hex');
}

// email -> {login, avatar}, or null for a hidden author; get() / has() take a plain email
function readAuthors(file) {
  const data = yaml.load(fs.readFileSync(file, 'utf8')) || {};
  const map = new Map();
  for (const [email, entry] of Object.entries(data.authors || {})) {
    const login = entry && typeof entry.github === 'string' && entry.github.trim();
    if (!login && !(entry && entry.hidden === true)) {
      throw new Error(`authors.yml: ${email} needs a github username or hidden: true`);
    }
    // the offline manual makes no request to any other site: names without avatars
    const avatar = process.env.SBO_DOCS_MANUAL ? undefined : `https://github.com/${login}.png`;
    map.set(email.toLowerCase(), login ? {login, ...(avatar ? {avatar} : {})} : null);
  }
  const key = e => (map.has(e.toLowerCase()) ? e.toLowerCase() : emailKey(e));
  return {get: e => map.get(key(e)), has: e => map.has(key(e))};
}

// repo-relative path -> [{hash, date, message, email}], renames followed back to the oldest name
function gitHistory(repo, scope) {
  let out;
  try {
    out = execFileSync('git', ['-C', repo, 'log', '-M', '--name-status', '--format=%x01%H%x00%aI%x00%ae%x00%s', '--', scope],
      {encoding: 'utf8', maxBuffer: 256 * 1024 * 1024});
  } catch (e) {
    console.warn(`[page-history] git log failed (${e.message.split('\n')[0]}); pages get no history`);
    return {emails: new Set(), lookup: () => []};
  }
  const commits = out.split('\x01').filter(Boolean).map(block => {
    const [head, ...rest] = block.split('\n');
    const [hash, date, email, message] = head.split('\0');
    const changes = rest.filter(Boolean).map(l => l.split('\t'));
    return {hash, date, email, message, changes};
  });
  const history = new Map();
  return {
    emails: new Set(commits.map(c => c.email)),
    lookup(file) {
      if (history.has(file)) return history.get(file);
      // walk newest to oldest; a rename adds the older name
      const names = new Set([file]);
      const list = [];
      for (const c of commits) {
        let hit = false;
        for (const ch of c.changes) {
          const status = ch[0];
          if (status.startsWith('R') || status.startsWith('C')) {
            if (names.has(ch[2])) {
              hit = true;
              if (status.startsWith('R')) names.add(ch[1]);
            }
          } else if (names.has(ch[1])) {
            hit = true;
          }
        }
        if (hit) list.push({hash: c.hash, date: c.date, message: c.message, email: c.email});
      }
      history.set(file, list);
      return list;
    },
  };
}

export default async function pageHistoryDocs(context, options) {
  const plugin = await docsPlugin(context, options);
  const siteDir = context.siteDir;
  const repo = path.resolve(siteDir, '..');
  const scope = path.relative(repo, siteDir) || '.';
  return {
    ...plugin,
    async loadContent() {
      const content = await plugin.loadContent();
      const authors = readAuthors(path.join(siteDir, 'authors.yml'));
      const git = gitHistory(repo, scope);
      // every author of the history must be in authors.yml (mapped or hidden), so no git name can reach the site
      const unmapped = [...git.emails].filter(e => !authors.has(e.toLowerCase()));
      if (unmapped.length) {
        throw new Error(`[page-history] git authors missing in authors.yml (add a github username or hidden: true): ${unmapped.join(', ')}`);
      }
      for (const version of content.loadedVersions) {
        for (const doc of version.docs) {
          const fm = doc.frontMatter;
          const source = fm.history_source
            ? String(fm.history_source)
            : path.relative(repo, path.join(siteDir, doc.source.replace(/^@site\//, '')));
          fm.edit_history = git.lookup(source).slice(0, LIMIT).map(({hash, date, message, email}) => {
            const author = authors.get((email || '').toLowerCase()) || null;
            return author ? {hash, date, message, author} : {hash, date, message};
          });
          delete fm.history_source;
          // a "Ported from" marker on the page's first heading is no part of its title
          doc.title = doc.title.replace(PORTED, '');
          if (doc.description) doc.description = doc.description.replace(PORTED, '');
        }
      }
      return content;
    },
  };
}

pageHistoryDocs.validateOptions = docsPluginModule.validateOptions ?? docsPlugin.validateOptions;
