// Old addresses that lead to their page on this site: after the build, each old path gets <path>.html and
// <path>/index.html (a static host serves one or the other, with or without the trailing slash), a small page that
// sends the browser on at once and names the new address as canonical for search engines.
//
//   [redirects, {redirects: {'/old': '/new/page'}}]   (paths from the site root, without a trailing slash)

import fs from 'node:fs';
import path from 'node:path';

function page(to) {
  const esc = to.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="${esc}">
<meta http-equiv="refresh" content="0; url=${esc}">
<meta name="robots" content="noindex">
</head>
<body><p>This page moved to <a href="${esc}">${esc}</a>.</p></body>
</html>
`;
}

export default function redirectsPlugin(context, options) {
  const list = Object.entries(options.redirects || {});
  return {
    name: 'sbo-redirects',
    async postBuild({outDir, routesPaths}) {
      const base = context.baseUrl.replace(/\/$/, '');
      const routes = new Set(routesPaths);
      for (const [from, to] of list) {
        const target = base + to;
        if (!routes.has(target)) throw new Error(`[redirects] ${from} -> ${to}: no page ${target} in the build`);
        if (routes.has(base + from)) throw new Error(`[redirects] ${from} is a page of the site: no redirect needed`);
        const rel = from.replace(/^\/+/, '');
        for (const file of [`${rel}.html`, path.join(rel, 'index.html')]) {
          const dest = path.join(outDir, file);
          fs.mkdirSync(path.dirname(dest), {recursive: true});
          fs.writeFileSync(dest, page(target));
        }
      }
      if (list.length) console.log(`[redirects] ${list.length} old addresses`);
    },
  };
}
