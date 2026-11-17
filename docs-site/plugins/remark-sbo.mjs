// Markdown additions of the SBO docs:
//
// - "Ported from" icons (portedPreprocessor, markdown.preprocessor in docusaurus.config.ts): [[ported:<id> ...]]
//   becomes <Ported ids="..." />, one small icon per project of provenance.yml (src/components/Entity). A marker at
//   the end of a heading puts the icons on the heading's line; the heading's text, its anchor and its table of
//   contents entry stay free of them. An unknown project id stops the build.
// - The Changelog page: <Changelog /> is replaced by the release sections of the repository's CHANGELOG.md
//   ("## [x.y.z] - date" becomes "## SBO x.y.z" with "Released on <date>." under it; "Unreleased" and a version
//   without a date keep their heading; an empty section is left out; link reference lines are dropped).

import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {visit, SKIP} from 'unist-util-visit';

const MARKER = /\[\[ported:([a-z0-9_ -]+)\]\]/g;
const SECTION = /^## \[([^\]]+)\](?:\s*-\s*(\d{4}-\d{2}-\d{2}))?\s*$/;
const LINKREF = /^\[[^\]]+\]:\s*\S+\s*$/;
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
  'November', 'December'];

// [[ported:<id> ...]] -> <Ported ids="..." />, on the raw text before it is parsed (a marker would otherwise be split
// by the directive syntax, ":name" is a text directive). On a heading the space before the marker goes, so the
// heading's anchor and table of contents entry are its text alone.
export function portedPreprocessor(projects) {
  return ({filePath, fileContent}) => {
    if (!fileContent.includes('[[ported:')) return fileContent;
    let fence = false;
    const out = fileContent.split('\n').map(line => {
      if (/^\s*(```|~~~)/.test(line)) fence = !fence;
      if (fence) return line;
      const head = /^#{1,6}\s/.test(line);
      return line.split(/(`+[^`]*?`+)/).map((part, i) => i % 2 ? part : part.replace(
        head ? /\s*\[\[ported:([a-z0-9_ -]+)\]\]/g : MARKER, (_m, ids) => {
          const list = ids.trim().split(/\s+/);
          for (const id of list) {
            if (!projects[id]) throw new Error(`${filePath}: [[ported:${ids}]]: ${id} is no project of provenance.yml`);
          }
          return `<Ported ids="${list.join(' ')}"${head ? ' head' : ''} />`;
        })).join('');
    });
    const text = out.join('\n');
    const left = /\[\[ported:[^\]]*\]\]/.exec(text.replace(/`+[^`]*?`+/g, ''));
    if (left) throw new Error(`${filePath}: a [[ported:...]] marker was not converted: ${left[0]}`);
    return text;
  };
}

export function changelogMarkdown(path) {
  if (!fs.existsSync(path)) return null;
  const lines = fs.readFileSync(path, 'utf8').split(/\r?\n/);
  const start = lines.findIndex(l => SECTION.test(l));
  if (start < 0) return null;
  const out = [];
  for (const line of lines.slice(start)) {
    const m = SECTION.exec(line);
    if (m) {
      const [, version, date] = m;
      out.push(/^\d+\.\d+\.\d+$/.test(version) ? `## SBO ${version}` : `## ${version}`, '');
      if (date) {
        const [y, mo, d] = date.split('-').map(Number);
        out.push(`Released on ${MONTHS[mo - 1]} ${d}, ${y}.`, '');
      }
      continue;
    }
    if (LINKREF.test(line)) continue;
    out.push(line);
  }
  const text = out.join('\n').trim() + '\n';
  // a section with nothing in it (an empty "Unreleased") is left out
  return text.replace(/^## [^\n]*\n\s*(?=^## |(?![\s\S]))/gm, '');
}

function mdxSafe(text) {
  // CHANGELOG.md is plain Markdown: braces and a "<" outside code would start JSX in MDX
  return text.split('\n').map(line => line.split(/(`+[^`]*?`+)/).map((part, i) =>
    i % 2 ? part : part.replace(/[{}<]/g, c => '\\' + c)).join('')).join('\n');
}

// the repository's CHANGELOG.md (docs-site/plugins/ -> the repository root)
const CHANGELOG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', 'CHANGELOG.md');

export default function remarkSbo() {
  const changelogPath = CHANGELOG;
  const processor = this;
  return (tree, vfile) => {
    const file = vfile.path || '(page)';
    visit(tree, 'mdxJsxFlowElement', (node, index, parent) => {
      if (node.name !== 'Changelog' || !parent) return;
      const md = changelogMarkdown(changelogPath);
      if (md === null) {
        throw new Error(`${file}: <Changelog />: no "## [x.y.z]" section in ${changelogPath}`);
      }
      const sub = processor.parse(mdxSafe(md));
      parent.children.splice(index, 1, ...sub.children);
      return [SKIP, index + sub.children.length];
    });
  };
}
