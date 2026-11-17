import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

// The SBO version the docs describe (docsVersion: project(VERSION) of the repository's CMakeLists.txt) and the latest
// release on GitHub, read when the site is built (docusaurus.config.ts)
interface Versions { docsVersion: string; release: string; releaseUrl: string; releaseRepo: string; manual: boolean }

function useVersions(): Versions {
  return useDocusaurusContext().siteConfig.customFields?.sbo as Versions;
}

function newer(a: string, b: string): boolean {
  const pa = a.split('.').map(Number);
  const pb = b.split('.').map(Number);
  for (let i = 0; i < 3; i++) {
    if ((pa[i] ?? 0) !== (pb[i] ?? 0)) return (pa[i] ?? 0) > (pb[i] ?? 0);
  }
  return false;
}

export function VersionBadge({ next }: { next: boolean }): React.JSX.Element {
  return next ? <span className="sbo-badge sbo-badge--next">upcoming</span> : <span className="sbo-badge">latest</span>;
}

export function DocsVersion(): React.JSX.Element {
  return <>{useVersions().docsVersion}</>;
}

export function LatestRelease(): React.JSX.Element {
  return <>{useVersions().release}</>;
}

// The download address of a zip of the latest release (the manual: of its own release): name "sbo-sdk" is
// sbo-sdk-v<version>.zip, the file the release workflow publishes (.github/workflows/release.yml)
function useReleaseFile(name: string): { file: string; url: string } {
  const { release, releaseRepo } = useVersions();
  const file = `${name}-v${release}.zip`;
  return { file, url: `https://github.com/${releaseRepo}/releases/download/v${release}/${file}` };
}

// A file of the latest release, linked by its name: <ReleaseFile name="sbo-sdk" /> is sbo-sdk-v<version>.zip
export function ReleaseFile({ name }: { name: string }): React.JSX.Element {
  const { file, url } = useReleaseFile(name);
  return <Link to={url}>{file}</Link>;
}

// A file or folder of the SDK, shown as code and linked to the SDK zip that holds it:
// <SdkFile path="sdk/examples/maps/co_example_calc/" />
export function SdkFile({ path }: { path: string }): React.JSX.Element {
  const { url } = useReleaseFile('sbo-sdk');
  return <Link to={url}><code>{path}</code></Link>;
}

// The line on the home page that says which version the pages describe (the manual describes its own release only,
// with no latest / upcoming badge: a copy on disk can't know of later releases)
export function SboVersion(): React.JSX.Element {
  const { docsVersion, release, releaseUrl, manual } = useVersions();
  if (manual) {
    return (
      <p>
        These pages describe <Link to={releaseUrl}>SBO {docsVersion}</Link>, the version this manual came with. The
        latest docs are at <Link to="https://sbo.sbotnas.io">sbo.sbotnas.io</Link>.
      </p>
    );
  }
  if (newer(docsVersion, release)) {
    return (
      <p>
        These pages describe <strong>SBO {docsVersion}</strong> <VersionBadge next />, the next release. The latest
        release is <Link to={releaseUrl}>SBO {release}</Link> <VersionBadge next={false} />; what changes
        in {docsVersion} is marked on each page and in the <Link to="/changelog">changelog</Link>.
      </p>
    );
  }
  return (
    <p>
      These pages describe <Link to={releaseUrl}>SBO {docsVersion}</Link> <VersionBadge next={false} />.
    </p>
  );
}
