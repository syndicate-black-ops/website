// The "On this page" list: Docusaurus' own TOCItems, with its highlight (useTOCHighlight) replaced by the one below.
//
// Docusaurus highlights the first heading in the top half of the window, or the one before it. The last headings of
// a page are often short sections that can't scroll up that far, so clicking one of them, or scrolling to the end,
// left an earlier heading highlighted. Here:
// - the entry you click stays highlighted until the page is scrolled again;
// - at the bottom of the page, the last heading in view is highlighted;
// - anywhere else, Docusaurus' rule as before.
// Docusaurus' own highlight is switched off (no linkActiveClassName passed on): it reads the heading from the link's
// address after the first '#', which never matches in the offline manual, where links read #/route#heading.

import React, {useEffect} from 'react';
import TOCItems from '@theme-original/TOCItems';
import type TOCItemsType from '@theme/TOCItems';
import type {WrapperProps} from '@docusaurus/types';
import {useThemeConfig} from '@docusaurus/theme-common';

type Props = WrapperProps<typeof TOCItemsType>;

// a heading with no height (a marker): measure its parent instead, as Docusaurus does
function rectOf(el: Element): DOMRect {
  const r = el.getBoundingClientRect();
  return r.top === r.bottom && el.parentElement ? rectOf(el.parentElement) : r;
}

// the heading id a TOC link points at: after the last '#' (the hash router puts the route before it)
function headingOf(link: HTMLAnchorElement): string {
  return decodeURIComponent(link.href.slice(link.href.lastIndexOf('#') + 1));
}

function useTOCHighlightToEnd(
  linkClassName: string | undefined,
  activeClassName: string | undefined,
  minLevel: number,
  maxLevel: number,
): void {
  useEffect(() => {
    if (!linkClassName || !activeClassName) {
      return undefined;
    }
    const selector = Array.from({length: maxLevel - minLevel + 1}, (_, i) => `h${minLevel + i}.anchor`).join();
    const links = () => Array.from(document.getElementsByClassName(linkClassName)) as HTMLAnchorElement[];
    const page = () => document.scrollingElement ?? document.documentElement;
    let clicked: string | null = null; // heading of the clicked entry, kept until the page is scrolled
    let clickedY: number | null = null; // where the jump to it ended
    let settle: ReturnType<typeof setTimeout> | undefined;

    function active(): string | null {
      const headings = Array.from(document.querySelectorAll<HTMLElement>(selector));
      if (clicked && headings.some((h) => h.id === clicked)) {
        return clicked;
      }
      if (!headings.length) {
        return null;
      }
      const {scrollTop, scrollHeight} = page();
      const scrolls = scrollHeight > window.innerHeight + 2;
      if (scrolls && scrollTop + window.innerHeight >= scrollHeight - 2) {
        const inView = headings.filter((h) => rectOf(h).top < window.innerHeight);
        return (inView[inView.length - 1] ?? headings[headings.length - 1]).id;
      }
      // Docusaurus' rule: the first heading under the navbar if it is in the top half of the window, else the one
      // before it (none before the first heading)
      const navbar = document.querySelector('.navbar')?.clientHeight ?? 0;
      const next = headings.find((h) => rectOf(h).top >= navbar);
      if (!next) {
        return headings[headings.length - 1].id;
      }
      const r = rectOf(next);
      if (r.top > 0 && r.bottom < window.innerHeight / 2) {
        return next.id;
      }
      return headings[headings.indexOf(next) - 1]?.id ?? null;
    }

    function update() {
      const id = active();
      for (const link of links()) {
        link.classList.toggle(activeClassName!, id !== null && headingOf(link) === id);
      }
    }

    // the jump to a clicked heading has ended once no scroll came for a moment
    function waitForJump() {
      clearTimeout(settle);
      settle = setTimeout(() => {
        if (clicked) {
          clickedY = page().scrollTop;
        }
      }, 200);
    }

    function onScroll() {
      if (clicked) {
        if (clickedY === null) {
          waitForJump();
        } else if (Math.abs(page().scrollTop - clickedY) > 1) {
          clicked = null;
        }
      }
      update();
    }

    function onClick(e: MouseEvent) {
      const link = (e.target as Element | null)?.closest?.('a');
      if (link && links().includes(link as HTMLAnchorElement)) {
        clicked = headingOf(link as HTMLAnchorElement);
        clickedY = null;
        waitForJump();
        update();
      }
    }

    document.addEventListener('scroll', onScroll, {passive: true});
    document.addEventListener('click', onClick);
    window.addEventListener('resize', update);
    update();
    return () => {
      clearTimeout(settle);
      document.removeEventListener('scroll', onScroll);
      document.removeEventListener('click', onClick);
      window.removeEventListener('resize', update);
    };
  }, [linkClassName, activeClassName, minLevel, maxLevel]);
}

export default function TOCItemsWrapper(props: Props): React.JSX.Element {
  const {tableOfContents} = useThemeConfig();
  useTOCHighlightToEnd(
    props.linkClassName ?? undefined,
    props.linkActiveClassName,
    props.minHeadingLevel ?? tableOfContents.minHeadingLevel,
    props.maxHeadingLevel ?? tableOfContents.maxHeadingLevel,
  );
  return <TOCItems {...props} linkActiveClassName={undefined} />;
}
