import React from 'react';
import styles from './styles.module.css';

// Value-flow diagrams for the guides: boxes for entities, arrows for what passes between them.
//
//   <Flow caption="...">
//     <FlowNode cls="trigger_multiple" name="pad">Target: boom</FlowNode>
//     <FlowArrow label="triggers" />
//     <FlowNode cls="env_explosion" name="boom">Position: eyes</FlowNode>
//     <FlowArrow label="asks for a position" />
//     <FlowNode cls="calc_position" name="eyes" />
//   </Flow>
//
// Up to three entities stand in one row; a longer chain, and every chain on a narrow screen, stacks top to bottom
// with the arrows turned down. <FlowArrow back /> points the other way: the value that goes back to the entity that
// asked for it.

interface FlowProps {
  caption?: React.ReactNode;
  children?: React.ReactNode;
}

const ROW_MAX = 3;

export function Flow({ caption, children }: FlowProps) {
  const nodes = React.Children.toArray(children).filter(
    (c) => React.isValidElement(c) && c.type === FlowNode,
  ).length;
  return (
    <figure className={`${styles.flow} ${nodes > ROW_MAX ? styles.vertical : ''}`}>
      <div className={styles.row}>{children}</div>
      {caption ? <figcaption className={styles.caption}>{caption}</figcaption> : null}
    </figure>
  );
}

interface FlowNodeProps {
  cls?: string;
  name?: string;
  kind?: 'entity' | 'player' | 'value';
  children?: React.ReactNode;
}

export function FlowNode({ cls, name, kind = 'entity', children }: FlowNodeProps) {
  return (
    <div className={`${styles.node} ${styles[kind] ?? ''}`}>
      {cls ? <code className={styles.cls}>{cls}</code> : null}
      {name ? <span className={styles.name}>{name}</span> : null}
      {children ? <div className={styles.body}>{children}</div> : null}
    </div>
  );
}

interface FlowArrowProps {
  label?: React.ReactNode;
  back?: boolean;
}

export function FlowArrow({ label, back = false }: FlowArrowProps) {
  return (
    <div className={`${styles.arrow} ${back ? styles.back : ''}`} role="presentation">
      {label ? <span className={styles.label}>{label}</span> : null}
      <span className={styles.line} aria-hidden="true" />
    </div>
  );
}

export default Flow;
