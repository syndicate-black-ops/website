import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBrokenLinks from '@docusaurus/useBrokenLinks';
import styles from './styles.module.css';

type Project = { name: string; url: string; icon?: string };

function PortedIcon({ project }: { project: Project }): React.JSX.Element {
  const src = useBaseUrl(`/img/ported/${project.icon}`);
  return <img className="no-zoom" src={src} alt={project.name} />;
}

// "Ported from" icons (docs-site/provenance.yml, [[ported:...]] markers): one per project, a link to its repository
// with "Ported from <name>" as the tooltip; a project without an icon shows its name as a small text link. On a
// heading (head) the icons are a little larger and sit on the heading's line.
export function Ported({ ids, head }: { ids: string; head?: boolean }): React.JSX.Element {
  const projects = useDocusaurusContext().siteConfig.customFields?.ported as Record<string, Project>;
  return (
    <span className={head ? `${styles.ported} ${styles.portedHead}` : styles.ported}>
      {ids.split(/\s+/).filter(Boolean).map(id => {
        const p = projects[id];
        if (!p) return null;
        return (
          <a key={id} href={p.url} title={`Ported from ${p.name}`} target="_blank" rel="noopener noreferrer">
            {p.icon ? <PortedIcon project={p} /> : <span className={styles.portedText}>{p.name}</span>}
          </a>
        );
      })}
    </span>
  );
}

// The editor icon, the entity type and the "Ported from" icons above the summary
export function EntityHeader({ name, icon, kind, ported }: { name: string; icon?: string; kind: string; ported?: string }): React.JSX.Element {
  return (
    <div className={styles.header}>
      {icon ? <img className={`no-zoom ${styles.icon}`} src={useBaseUrl(icon)} alt={`${name} icon`} /> : null}
      <div className={styles.meta}>
        <span className={styles.kind}>{kind} entity</span>
        {ported ? <span className={styles.portedLine}>Ported from <Ported ids={ported} /></span> : null}
      </div>
    </div>
  );
}

export function KeyvalueTable({ children }: { children: React.ReactNode }): React.JSX.Element {
  return (
    <div className={styles.kvTable} role="table">
      <div className={styles.kvHead} role="row">
        <span role="columnheader">Key</span>
        <span role="columnheader">Description</span>
        <span role="columnheader">Default</span>
      </div>
      {children}
    </div>
  );
}

// Link targets of a row: the first id names the row, the others are extra anchors in it (anchors="a b c"). Each is
// registered, so the build's anchor check knows them.
function useAnchors(anchors: string | undefined, fallback: string): [string, React.ReactNode] {
  const brokenLinks = useBrokenLinks();
  const ids = (anchors ?? '').split(/\s+/).filter(Boolean);
  ids.forEach(id => brokenLinks.collectAnchor(id));
  return [ids[0] ?? fallback, ids.slice(1).map(id => <span key={id} id={id} className={styles.anchor} />)];
}

// An extra link target, e.g. a second id for a heading: <Anchor id="name" />
export function Anchor({ id }: { id: string }): React.JSX.Element {
  useBrokenLinks().collectAnchor(id);
  return <span id={id} className={styles.anchor} />;
}

export function Keyvalue({ name, keyname, default: def, ported, anchors, children }:
  { name: string; keyname: string; default?: string; ported?: string; anchors?: string; children: React.ReactNode }): React.JSX.Element {
  const [id, extra] = useAnchors(anchors, `key-${keyname}`);
  return (
    <div className={styles.kvRow} role="row" id={id}>
      <div className={styles.kvKey} role="cell">
        {extra}
        <strong>{name}</strong>{ported ? <Ported ids={ported} /> : null}
        <code>{keyname}</code>
      </div>
      <div className={styles.kvDesc} role="cell">{children}</div>
      <div className={styles.kvDefault} role="cell">
        {def ? <><span className={styles.kvDefaultLabel}>Default </span><code>{def}</code></> : null}
      </div>
    </div>
  );
}

export function FlagList({ children }: { children: React.ReactNode }): React.JSX.Element {
  return <div className={styles.flags}>{children}</div>;
}

export function Flag({ name, value, ported, anchors, children }:
  { name: string; value: string; ported?: string; anchors?: string; children: React.ReactNode }): React.JSX.Element {
  const [id, extra] = useAnchors(anchors, `flag-${value}`);
  return (
    <div className={styles.flag} id={id}>
      <div className={styles.flagHead}>
        {extra}
        <code className={styles.flagValue}>{value}</code>
        <strong>{name}</strong>
        {ported ? <Ported ids={ported} /> : null}
      </div>
      <div className={styles.flagDesc}>{children}</div>
    </div>
  );
}
