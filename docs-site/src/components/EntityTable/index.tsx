import React, { useState, useMemo, useEffect } from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import useIsBrowser from '@docusaurus/useIsBrowser';
import styles from './styles.module.css';

// One row of the Entity List (docs/mapping/entities/entity-index.json, written by scripts/gen_entity_docs.py)
export interface Entity {
  Classname: string;
  Description: string;
  Icon: string;
  Type: string;
  Group: string;
  Ported: string;
}

function Icon({ src }: { src: string }): React.JSX.Element {
  const url = useBaseUrl(src);
  return (
    <img src={url} alt="" className="no-zoom" loading="lazy" decoding="async" width={42} height={42}
      style={{ width: '42px', height: '42px' }} />
  );
}

// a long class name (color_correction_volume) wraps inside its cell after an underscore
function BreakAtUnderscores({ name }: { name: string }): React.JSX.Element {
  const parts = name.split('_');
  return <>{parts.map((p, i) => <React.Fragment key={i}>{p}{i < parts.length - 1 ? <>_<wbr /></> : null}</React.Fragment>)}</>;
}

// Source2Wiki's Entity List with one game: no game column and no game filter; a search box, a type filter and a
// group filter (the groups of the sidebar). ?search=<text> fills the search box.
export default function EntityTable({ entities }: { entities: Entity[] }): React.JSX.Element {
  const [searchTerm, setSearchTerm] = useState('');
  const [type, setType] = useState('');
  const [group, setGroup] = useState('');
  const isBrowser = useIsBrowser();
  const groups = useMemo(() => [...new Set(entities.map(e => e.Group))], [entities]);

  useEffect(() => {
    const q = new URLSearchParams(window.location.search).get('search');
    if (q) setSearchTerm(q);
  }, []);

  const filtered = useMemo(() => {
    const s = searchTerm.trim().toLowerCase();
    return entities.filter(e =>
      (!s || e.Classname.toLowerCase().includes(s) || e.Description.toLowerCase().includes(s)) &&
      (!type || e.Type === type) && (!group || e.Group === group));
  }, [entities, searchTerm, type, group]);

  return (
    <div className={styles.entityTableContainer}>
      <div className={styles.filterBar}>
        <div className={styles.searchBox}>
          <input className="navbar__search-input" placeholder="Search names and descriptions" value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)} />
        </div>
        <select className={styles.typeSelect} value={group} onChange={(e) => setGroup(e.target.value)}>
          <option value="">All groups</option>
          {groups.map(g => <option key={g} value={g}>{g}</option>)}
        </select>
        <select className={styles.typeSelect} value={type} onChange={(e) => setType(e.target.value)}>
          <option value="">All types</option>
          <option value="Point">Point entities</option>
          <option value="Brush">Brush entities</option>
          <option value="Special">Special entities</option>
        </select>
      </div>
      <div className={styles.resultsCount} style={{ visibility: isBrowser ? 'visible' : 'hidden' }}>
        Showing {filtered.length} of {entities.length} entities
      </div>
      {filtered.length === 0 ? (
        <div className={styles.noResults}>No entities found</div>
      ) : (
        <table className={styles.table}>
          <thead>
            <tr>
              <th>Classname</th>
              <th className={styles.description}>Description</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((entity) => (
              <tr key={entity.Classname} className={styles.row}>
                <td>
                  <Link to={`/mapping/entities/${entity.Classname}`} className={styles.entityLink}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      {entity.Icon ? <Icon src={entity.Icon} /> : <span className={styles.noIcon} />}
                      <code className={styles.code}><BreakAtUnderscores name={entity.Classname} /></code>
                    </div>
                  </Link>
                </td>
                <td className={styles.description} dangerouslySetInnerHTML={{ __html: entity.Description }} />
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
