# The GitHub Pages site

<https://danielrosehill.github.io/Israeli-AI/> — a browsable version of this
index with a page per category. Added 2026-07-25.

## The one rule

**The markdown files at the repo root are the only source of truth.** The site
is generated from them by `scripts/build_site.py`; there is no second copy of
the content to keep in sync. Add an entry to `mcps.md` and the matching category
page updates on the next push. Never hand-edit HTML — there is none to edit.

## Why a generator rather than Jekyll

GitHub Pages' built-in Jekyll only processes markdown files that carry YAML
front matter, and GitHub renders front matter as an ugly table at the top of a
file when you view it on github.com. Since these files are read directly on
GitHub at least as often as on the site, adding front matter to them was not
acceptable, and `defaults:` in `_config.yml` does not substitute for it. A ~500
line stdlib-only Python generator avoids the tradeoff entirely and gives full
control over the per-category page split.

## Structure it produces

| Source | Site |
| --- | --- |
| `README.md` intro | `/` — landing page with entry counts and cards for every category |
| `agents.md` | `/agents/` |
| `agent-skills.md` | `/agent-skills/` |
| `mcps.md` | `/mcps/` hub + one page per `##` section, e.g. `/mcps/finance-banking/` |
| `ideation.md` | `/ideation/` |
| `hebrew.md` | `/hebrew/` hub + one page per `##` section |
| `README.md` level-1 ecosystem sections | `/ecosystem/` hub + `/ecosystem/communities/` etc. |
| `SCOPE.md` + README Contributing/Disclaimer | `/scope/` |

`mcps.md` and `hebrew.md` are the "split" pages — this is set by the `split`
flag in `PROJECT_PAGES` at the top of the script. Which README sections become
ecosystem pages is set by `ECOSYSTEM_SECTIONS` in the same block; a level-1
README section not listed there is silently left off the site, which is how
`Contents` and `Projects` (navigation-only sections) are dropped.

Every markdown table with a linked first column is rendered as a grid of cards
rather than a table: first column becomes the title and link, image cells become
the star badge, everything else becomes the description. Bullet lists shaped
`- [Name](url) — description` get the same treatment; other lists stay lists.

## Cross-links

Links between the markdown files (`[Israeli AI Ecosystem](README.md)`,
`[Finance & Banking](mcps.md#finance--banking)`) work on GitHub *and* on the
site: `rewrite_internal_links()` maps `*.md` hrefs onto site paths, folding the
`##` anchors of split pages into their per-category directories (GitHub's
`#finance--banking` → `/mcps/finance-banking/`). A link to a repo file with no
site page — `pending.md`, anything under `docs/` — is rewritten to the file on
github.com instead. So keep writing cross-links the normal markdown way.

## Building locally

```bash
python3 scripts/build_site.py          # → _site/
python3 -m http.server -d _site 8777   # → http://localhost:8777/
```

No dependencies, no virtualenv; Python 3.10+ for the `X | Y` type syntax.
`_site/` is gitignored — CI builds it, the repo never carries it.

Links are all relative, so the output works under the `/Israeli-AI/`
project-pages subpath and equally from a `file://` open of `_site/index.html`.

## Deployment

`.github/workflows/pages.yml` runs on push to `main` (when a `.md`, the script,
`web/`, or `images/` changes) and on manual dispatch, then publishes with
`actions/deploy-pages`. The repo's Pages source must be set to **GitHub
Actions**, not "deploy from a branch" — if it is on branch mode the workflow
succeeds and nothing changes on the live site, which is a confusing failure.

## Checks worth running after a content change

Both catch real breakage and neither needs the site to be deployed:

```bash
# 1. No entry silently dropped by a malformed table row
grep -h '^|' *.md | grep -vE '^\| *(Project|Organization|Meetup|Index) *\|' | grep -vc '^|---'
grep -ro 'data-entry' _site --include=*.html | wc -l   # ≥ the above (bullet lists add more)

# 2. No broken internal link
python3 - <<'EOF'
import re
from pathlib import Path
bad = []
for p in Path('_site').rglob('*.html'):
    for href in re.findall(r'(?:href|src)="([^"]+)"', p.read_text()):
        if href.startswith(('http', 'mailto:', '#', 'data:')): continue
        t = (p.parent / href.split('#')[0]).resolve()
        t = t / 'index.html' if t.is_dir() else t
        if not t.exists(): bad.append((str(p), href))
print('broken:', len(bad), bad[:5])
EOF
```

## Known limits

- The header search box filters **the current page only** (`web/site.js`). A
  `search.json` covering all 171 entries is emitted at the site root and is
  ready for a cross-site search UI; nothing consumes it yet.
- The markdown parser handles what these files actually contain — headings,
  tables, bullet lists, paragraphs, blockquotes, `---`. It has no support for
  code fences, nested lists, or reference-style links, and will pass them
  through as plain paragraphs. Raw HTML blocks are skipped entirely, which is
  how the README's hand-written `<table>` Contents block is ignored.
- Entries that appear in two source sections (e.g. Hebrew AI Models, in both
  `hebrew.md` and the README's Related Indexes) appear on both pages, and twice
  in `search.json`. That mirrors the source and is intentional.
