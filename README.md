# Syndicate Black Ops docs

The source of the Syndicate Black Ops documentation at https://sbo.sbotnas.io: how to install and play SBO, how to
run a server for it, and how to make maps for it. The same pages ship with every game release as an offline manual
(`syndicate/manual/index.html` in the release zip).

| Path | Holds |
|---|---|
| `docs-site/` | The site: pages, entity text, theme, build plugins (Docusaurus); `docs-site/README.md` explains it |
| `sdk/syndicate.fgd` | The entity definitions the entity pages are made from |
| `CHANGELOG.md` | The release notes, shown on the Changelog page |
| `scripts/` | The entity page generator and the checks the build runs |
| `.github/workflows/pages.yml` | Builds and publishes the site, and the offline manual as a release file of this repository |

The game itself is at https://github.com/syndicate-black-ops/syndicate-black-ops.

## Build

Python 3 with PyYAML, Node 22:

```sh
python3 scripts/gen_entity_docs.py              # the entity pages, from the FGD
cd docs-site && npm ci && npm run build         # the site, into docs-site/build
SBO_DOCS_MANUAL=1 npm run build -- --out-dir ../manual   # the offline manual
```
