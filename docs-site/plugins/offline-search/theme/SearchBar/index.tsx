import React, {useCallback, useEffect, useMemo, useRef, useState} from 'react';
import {useHistory} from '@docusaurus/router';

import styles from './styles.module.css';

// The offline manual's search box (plugins/offline-search): the index is search-index.js next to index.html, loaded
// with a <script> tag the first time the box gets the focus (fetch() is refused on file://), then searched here.
// Every word typed must start a word of the section (its page title, heading or text); hits in the title count most.

interface Entry { p: string; h: string; u: string; x: string }
interface Hit { entry: Entry; score: number; snippet: string }

declare global {
  interface Window { __SBO_SEARCH__?: Entry[] }
}

const LIMIT = 10;

function loadIndex(): Promise<Entry[]> {
  if (window.__SBO_SEARCH__) return Promise.resolve(window.__SBO_SEARCH__);
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    // next to index.html: the page's own address without its #/route
    script.src = new URL('search-index.js', document.baseURI).href;
    script.onload = () => (window.__SBO_SEARCH__ ? resolve(window.__SBO_SEARCH__) : reject(new Error('empty index')));
    script.onerror = () => reject(new Error('search-index.js not found'));
    document.head.appendChild(script);
  });
}

function fold(s: string): string {
  return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}

function wordStarts(text: string, word: string): number {
  const re = new RegExp(`(^|[^a-z0-9])${word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`);
  const m = re.exec(text);
  return m ? m.index + m[1].length : -1;
}

function search(index: Entry[], query: string): Hit[] {
  const words = fold(query).split(/[^a-z0-9_]+/).filter(Boolean);
  if (!words.length) return [];
  const hits: Hit[] = [];
  for (const entry of index) {
    const title = fold(entry.p), heading = fold(entry.h), text = fold(entry.x);
    let score = 0, first = -1, ok = true;
    for (const w of words) {
      const inTitle = wordStarts(title, w) >= 0, inHeading = wordStarts(heading, w) >= 0;
      const at = wordStarts(text, w);
      if (!inTitle && !inHeading && at < 0) { ok = false; break; }
      score += (inTitle ? 10 : 0) + (inHeading ? 5 : 0) + (at >= 0 ? 1 : 0);
      if (at >= 0 && (first < 0 || at < first)) first = at;
    }
    if (!ok) continue;
    if (!entry.h) score += 2;   // a page's top before its sections
    const start = Math.max(0, first - 40);
    const snippet = first < 0 ? entry.x.slice(0, 110)
      : (start ? '…' : '') + entry.x.slice(start, start + 110) + (start + 110 < entry.x.length ? '…' : '');
    hits.push({entry, score, snippet});
  }
  return hits.sort((a, b) => b.score - a.score).slice(0, LIMIT);
}

export default function SearchBar(): React.JSX.Element {
  const history = useHistory();
  const [index, setIndex] = useState<Entry[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState('');
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const box = useRef<HTMLDivElement>(null);

  const load = useCallback(() => {
    if (index || error) return;
    loadIndex().then(setIndex, (e: Error) => setError(e.message));
  }, [index, error]);

  const hits = useMemo(() => (index ? search(index, query) : []), [index, query]);
  useEffect(() => setActive(0), [query]);
  useEffect(() => {
    const close = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener('mousedown', close);
    return () => document.removeEventListener('mousedown', close);
  }, []);

  const go = (hit: Hit) => {
    setOpen(false);
    setQuery('');
    history.push(hit.entry.u);
  };

  const onKey = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(a => Math.min(a + 1, hits.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(a => Math.max(a - 1, 0)); }
    else if (e.key === 'Enter' && hits[active]) { e.preventDefault(); go(hits[active]); }
    else if (e.key === 'Escape') setOpen(false);
  };

  return (
    <div className={styles.search} ref={box}>
      <input
        type="search"
        className={styles.input}
        placeholder="Search"
        aria-label="Search"
        value={query}
        onFocus={() => { load(); setOpen(true); }}
        onChange={e => { setQuery(e.target.value); setOpen(true); }}
        onKeyDown={onKey}
      />
      {open && query.trim() && (
        <ul className={styles.results} role="listbox">
          {error && <li className={styles.empty}>The search index could not be loaded</li>}
          {!error && !index && <li className={styles.empty}>Loading…</li>}
          {index && !hits.length && <li className={styles.empty}>No results</li>}
          {hits.map((hit, i) => (
            <li key={hit.entry.u + i} role="option" aria-selected={i === active}>
              <a
                href={'#' + hit.entry.u}
                className={i === active ? styles.activeHit : styles.hit}
                onMouseEnter={() => setActive(i)}
                onClick={e => { e.preventDefault(); go(hit); }}>
                <span className={styles.title}>{hit.entry.p}{hit.entry.h ? ` › ${hit.entry.h}` : ''}</span>
                {hit.snippet && <span className={styles.snippet}>{hit.snippet}</span>}
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
