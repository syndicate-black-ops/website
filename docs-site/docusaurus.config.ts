import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import type { PluginOptions as SearchOptions } from '@easyops-cn/docusaurus-search-local';
import { admonitions } from './src/admonitions';
import remarkSbo, { portedPreprocessor } from './plugins/remark-sbo.mjs';
import pageHistoryDocs from './plugins/page-history.mjs';
import blogPluginModule from '@docusaurus/plugin-content-blog';
import { withSocialCards, pluginOf, defaultCard } from './plugins/social-cards.mjs';
import offlineSearch from './plugins/offline-search/index.mjs';
import redirects from './plugins/redirects.mjs';

// The SBO docs (players, server operators, mappers), laid out like Source2Wiki (github.com/Source2Wiki/Source2Wiki)
// with one game. Built by GitHub Actions in the website repository for https://sbo.sbotnas.io (and by GitLab CI from
// develop); README.md says how to build it locally.
//
// SBO_DOCS_MANUAL=1 builds the offline manual that ships in the game's release zip (syndicate/manual/): one
// index.html opened from disk (file://), every page at index.html#/<route> (Docusaurus' hash router), no request to
// any other site, the search index in a script file (plugins/offline-search), the version it describes as its
// release, and no link-preview cards. scripts/docs_manual.sh checks and zips it.

const REPO = path.resolve(__dirname, '..');
const MANUAL = !!process.env.SBO_DOCS_MANUAL;

// The version the pages describe: project(VERSION) of the repository's CMakeLists.txt; the website repository has
// no CMakeLists.txt and takes the newest section of CHANGELOG.md, which CI keeps equal to project(VERSION)
function readDocsVersion(): string {
  const cmake = path.join(REPO, 'CMakeLists.txt');
  if (fs.existsSync(cmake)) {
    return /project\(\s*sbo\s+VERSION\s+(\d+\.\d+\.\d+)/.exec(fs.readFileSync(cmake, 'utf8'))![1];
  }
  const m = /^## \[(\d+\.\d+\.\d+)\]/m.exec(fs.readFileSync(path.join(REPO, 'CHANGELOG.md'), 'utf8'));
  if (!m) throw new Error('CHANGELOG.md has no "## [x.y.z]" section: the docs version is unknown');
  return m[1];
}
const docsVersion = readDocsVersion();

// The latest release, read from GitHub when the site is built. In GitHub Actions the request uses the workflow's
// GITHUB_TOKEN and a failure stops the build (a rerun is better than a wrong version); elsewhere, without a network
// or with SBO_DOCS_OFFLINE set, the build goes on with the fallback
const RELEASE_REPO = 'syndicate-black-ops/syndicate-black-ops';
const RELEASE_FALLBACK = '2.1.0';
async function latestRelease(): Promise<string> {
  const strict = process.env.GITHUB_ACTIONS === 'true';
  const token = process.env.GITHUB_TOKEN;
  if (strict && !token) throw new Error('[sbo] GITHUB_TOKEN is not set: the build cannot read the latest release');
  if (process.env.SBO_DOCS_OFFLINE && !strict) return RELEASE_FALLBACK;
  let why: string;
  try {
    const r = await fetch(`https://api.github.com/repos/${RELEASE_REPO}/releases/latest`, {
      headers: {
        Accept: 'application/vnd.github+json', 'User-Agent': 'sbo-docs',
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      signal: AbortSignal.timeout(15000),
    });
    const tag = r.ok ? ((await r.json()) as { tag_name?: string }).tag_name ?? '' : '';
    if (/^v?\d+\.\d+\.\d+$/.test(tag)) return tag.replace(/^v/, '');
    why = r.ok ? `tag "${tag}" is not vX.Y.Z` : `HTTP ${r.status}`;
  } catch (e) {
    why = (e as Error).name;
  }
  if (strict) throw new Error(`[sbo] the latest release of ${RELEASE_REPO} was not read (${why})`);
  console.warn(`[sbo] GitHub release not read (${why}); using ${RELEASE_FALLBACK}`);
  return RELEASE_FALLBACK;
}

// Old addresses of the site that still lead to their page (plugins/redirects.mjs; not in the manual)
const REDIRECTS: Record<string, string> = {
  // the Sprays page of the earlier two-page site (its Install page was the home page, which stays the home page)
  '/sprays': '/playing/sprays',
};

// The header's Discord and GitHub icons (simple-icons paths, 24x24)
const DISCORD_URL = 'https://discord.sbotnas.io';
// the docs site's source is published in this repository
const GITHUB_URL = 'https://github.com/syndicate-black-ops/website';
const DISCORD_PATH = 'M20.317 4.37a19.8 19.8 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.3 18.3 0 0 0-5.487 0 13 13 0 0 0-.617-1.25.08.08 0 0 0-.079-.037A19.7 19.7 0 0 0 3.677 4.37a.1.1 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.08.08 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.08.08 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13 13 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10 10 0 0 0 .372-.292.07.07 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.07.07 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.3 12.3 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.08.08 0 0 0 .084.028 19.8 19.8 0 0 0 6.002-3.03.08.08 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.06.06 0 0 0-.031-.03M8.02 15.33c-1.182 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418m7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418';
const GITHUB_PATH = 'M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12';
function iconLink(cls: string, url: string, label: string, d: string): string {
  return `<a href="${url}" class="${cls}-button" target="_blank" rel="noopener noreferrer" aria-label="${label}" title="${label}">`
    + `<svg class="${cls}-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="${d}"/></svg>`
    + `<span class="navbar-icon-label">${label}</span></a>`;
}

// Site address: GitLab CI passes CI_PAGES_URL, the website's workflow SBO_DOCS_URL; a local build serves from the root
function siteAddress(): { url: string; baseUrl: string } {
  if (MANUAL) return { url: 'https://sbo.sbotnas.io', baseUrl: '/' };
  const pages = process.env.CI_PAGES_URL;
  if (pages) {
    const u = new URL(pages);
    return { url: u.origin, baseUrl: u.pathname.replace(/\/?$/, '/') };
  }
  return { url: process.env.SBO_DOCS_URL || 'http://localhost:3210', baseUrl: '/' };
}

export default async function createConfig(): Promise<Config> {
  // the manual describes one release: its own version, linked to that release's page
  const release = MANUAL ? docsVersion : await latestRelease();
  const releaseUrl = MANUAL
    ? `https://github.com/${RELEASE_REPO}/releases/tag/v${docsVersion}`
    : `https://github.com/${RELEASE_REPO}/releases/latest`;
  const provenance = yaml.load(fs.readFileSync(path.join(__dirname, 'provenance.yml'), 'utf8')) as {
    projects: Record<string, { name: string; url: string; icon?: string }>;
  };
  for (const [id, p] of Object.entries(provenance.projects)) {
    if (p.icon && !fs.existsSync(path.join(__dirname, 'static', 'img', 'ported', p.icon))) {
      throw new Error(`provenance.yml: the icon ${p.icon} of project ${id} is missing in static/img/ported/`);
    }
  }
  const remark = [remarkSbo];
  const tagline = 'Player, server and mapping documentation for Syndicate Black Ops';
  const socialDefault = defaultCard(tagline);
  const { url, baseUrl } = siteAddress();

  return {
    title: 'Syndicate Black Ops Docs',
    tagline,
    favicon: 'img/favicon.png',
    future: { v4: true, faster: true, ...(MANUAL ? { experimental_router: 'hash' as const } : {}) },
    url,
    baseUrl,
    trailingSlash: false,
    onBrokenLinks: 'throw',
    onBrokenAnchors: 'throw',
    onDuplicateRoutes: 'throw',
    markdown: {
      format: 'mdx',
      preprocessor: portedPreprocessor(provenance.projects),
      // <!-- comments --> and ## Heading {#id} in the pages
      mdx1Compat: { comments: true, admonitions: true, headingIds: true },
      hooks: { onBrokenMarkdownLinks: 'throw', onBrokenMarkdownImages: 'throw' },
    },
    i18n: { defaultLocale: 'en', locales: ['en'] },
    customFields: {
      ported: provenance.projects,
      sbo: { docsVersion, release, releaseUrl, releaseRepo: RELEASE_REPO, manual: MANUAL },
    },
    // the local search needs a Web Worker and fetch(), which a page opened from disk can't use: the manual has its
    // own (plugins/offline-search)
    themes: MANUAL ? [] : [
      [
        require.resolve('@easyops-cn/docusaurus-search-local'),
        {
          hashed: true,
          language: ['en'],
          indexDocs: true,
          indexBlog: true,
          indexPages: false,
          docsRouteBasePath: '/',
          blogRouteBasePath: '/posts',
          searchResultLimits: 8,
          searchResultContextMaxLength: 50,
          highlightSearchTermsOnTargetPage: true,
        } satisfies SearchOptions,
      ],
    ],
    plugins: [
      require.resolve('docusaurus-plugin-image-zoom'),
      ...(MANUAL ? [offlineSearch] : [[redirects, { redirects: REDIRECTS }]]),
      [
        withSocialCards(pageHistoryDocs, 'docs', { draw: !MANUAL }),
        {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          admonitions,
          beforeDefaultRemarkPlugins: remark,
          // page history comes from plugins/page-history.mjs; Docusaurus' own last-update line would show git names
          showLastUpdateAuthor: false,
          showLastUpdateTime: false,
          exclude: ['**/_*.{md,mdx}', '**/_*/**', '**/*.test.{js,jsx,ts,tsx}', '**/__tests__/**', 'assets/**'],
        },
      ],
      // the blog is a plugin of its own (not the preset's) so its posts get social cards too
      [
        withSocialCards(pluginOf(blogPluginModule), 'blog', { draw: !MANUAL }),
        {
          path: 'blog',
          routeBasePath: 'posts',
          blogTitle: "What's New",
          blogDescription: 'News about SBO releases and the docs',
          blogSidebarTitle: "What's New",
          blogSidebarCount: 'ALL',
          showReadingTime: false,
          onUntruncatedBlogPosts: 'ignore',
          beforeDefaultRemarkPlugins: remark,
          // no feed files in the manual (only pages and their files ship there, scripts/docs_manual.sh)
          feedOptions: MANUAL ? { type: null } : { type: ['rss', 'atom'], title: "SBO: What's New" },
        },
      ],
    ],
    presets: [
      [
        'classic',
        {
          docs: false,
          blog: false,
          ...(MANUAL ? { sitemap: false as const } : {}),
          theme: { customCss: ['./src/css/custom.css', './src/css/sbo.css'] },
        } satisfies Preset.Options,
      ],
    ],
    themeConfig: {
      // the link-preview card and tags of pages without their own card (plugins/social-cards.mjs draws it)
      image: socialDefault.image,
      metadata: socialDefault.metadata,
      // the lightbox: a click on a picture in a page opens it large; icons and pictures with class no-zoom stay.
      // The whole picture fits the window with a 24 px margin (medium-zoom scales it to fit both ways); it opens over
      // the navbar through the z-index in custom.css ("Lightbox")
      zoom: {
        selector: '.markdown img:not(.no-zoom)',
        background: { light: 'rgb(255, 255, 255)', dark: 'rgb(27, 27, 31)' },
        config: { margin: 24 },
      },
      navbar: {
        title: 'Syndicate Black Ops',
        logo: { src: 'img/logo.png', alt: 'SBO' },
        // as Source2Wiki's header: latest version, What's New | Discord, GitHub | theme toggle, search (the logo goes home)
        items: [
          // the latest GitHub release, read when the site is built
          { href: releaseUrl, label: `v${release}`, position: 'right', className: 'release-link' },
          { to: '/posts', label: "What's New", position: 'right', className: 'whats-new-link' },
          { type: 'html', position: 'right', value: iconLink('discord', DISCORD_URL, 'Discord', DISCORD_PATH) },
          { type: 'html', position: 'right', value: iconLink('github', GITHUB_URL, 'GitHub', GITHUB_PATH) },
        ],
      },
      colorMode: { defaultMode: 'dark', respectPrefersColorScheme: false },
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    } satisfies Preset.ThemeConfig,
  };
}
