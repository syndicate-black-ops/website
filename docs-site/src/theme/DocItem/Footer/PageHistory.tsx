import React from 'react';
import clsx from 'clsx';
import {ThemeClassNames} from '@docusaurus/theme-common';
import {useDateTimeFormat} from '@docusaurus/theme-common/internal';

import styles from './styles.module.css';

// One commit that changed the page (plugins/page-history.mjs). author is only there for a git author that
// authors.yml maps to a public GitHub username; nobody else's name reaches the page.
export interface PageEdit {
  hash: string;
  date: string;
  message: string;
  author?: {login: string; avatar?: string};
}

// no avatar in the offline manual (plugins/page-history.mjs leaves it out there: no request to github.com)
function Avatar({src}: {src?: string}): React.JSX.Element | null {
  return src ? <img className={styles.avatar} src={src} alt="" loading="lazy" /> : null;
}

// same format as Docusaurus' own last updated line, UTC so the server and browser render the same day
function useDateFormat(): Intl.DateTimeFormat {
  return useDateTimeFormat({day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC'});
}

function plural(count: number, word: string): string {
  return `${count} ${word}${count === 1 ? '' : 's'}`;
}

// everyone with a public name and an edit to the page, whoever made the most first; nothing when nobody has one
export function Contributors({history}: {history: PageEdit[]}): React.JSX.Element | null {
  const edits = new Map<string, {author: NonNullable<PageEdit['author']>; count: number}>();
  for (const edit of history) {
    if (!edit.author) continue;
    const entry = edits.get(edit.author.login) ?? {author: edit.author, count: 0};
    entry.count++;
    edits.set(edit.author.login, entry);
  }
  if (edits.size === 0) return null;
  const list = [...edits.values()].sort((a, b) => b.count - a.count);
  return (
    <div className={styles.contributors}>
      <div className={styles.contributorsTitle}>Contributors</div>
      <ul className={styles.chips}>
        {list.map(({author, count}) => (
          <li key={author.login}>
            <a className={styles.chip} href={`https://github.com/${author.login}`} target="_blank"
              rel="noopener noreferrer" title={`${plural(count, 'edit')} to this page`}>
              <Avatar src={author.avatar} />
              {author.login}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

// when the page changed last, which is also the toggle for the list of every commit to it, newest first
export function PageHistory({history}: {history: PageEdit[]}): React.JSX.Element {
  const dateFormat = useDateFormat();
  const lastUpdated = new Date(history[0].date);

  return (
    <details className={styles.history}>
      <summary className={styles.summary}>
        <span className={clsx(ThemeClassNames.common.lastUpdated, styles.lastUpdated)}>
          Last updated
          <time dateTime={lastUpdated.toISOString()} itemProp="dateModified">
            {dateFormat.format(lastUpdated)}
          </time>
        </span>
        <span className={styles.separator} aria-hidden="true">·</span>
        <span className={styles.historyToggle}>See page history</span>
      </summary>
      <ol className={styles.edits}>
        {history.map(edit => {
          const date = new Date(edit.date);
          return (
            <li key={edit.hash} className={styles.edit}>
              <time className={styles.date} dateTime={date.toISOString()}>
                {dateFormat.format(date)}
              </time>
              <span className={clsx(styles.person, styles.author)}>
                {edit.author && (
                  <>
                    <Avatar src={edit.author.avatar} />
                    {edit.author.login}
                  </>
                )}
              </span>
              <span className={styles.message} title={edit.hash.slice(0, 8)}>
                {edit.message}
              </span>
            </li>
          );
        })}
      </ol>
    </details>
  );
}
