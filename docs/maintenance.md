# Maintaining this index

How to sweep for entries that belong here but are missing, and how to catch
entries that have gone stale. Last run: **2026-07-25**.

## 1. Pull the full owned-repo list

`gh repo list` silently truncates at whatever `--limit` you pass, and quietly
returns exactly that many rows — so a run that returns 400 or 1000 has almost
certainly been cut off. Use the paginated API instead:

```bash
gh api 'user/repos?per_page=100&affiliation=owner' --paginate \
  --jq '.[] | {name:.name, visibility:.visibility, isFork:.fork, archived:.archived, pushed:.pushed_at, desc:.description}' \
  > repos.jsonl
```

As of 2026-07-25 that is 2,353 owned repos, 1,022 of them public.

## 2. Filter for Israel-focused candidates

Names and descriptions are descriptive enough that a keyword filter over
`name + description` catches nearly everything. Keywords that earned their
place:

```
israel hebrew jewish jerusalem jlm oref miklat knesset shelter zmanim shabbat
sefaria torah halach red-alert tzeva pikud aliyah yad2 ksp ivory green-invoice
paperless.tax iran bagrut hatzalah mda ivrit dicta tase ILS shekel
```

Avoid short tokens like `tase`, `nis`, `zim` or `idf` without word boundaries —
they match inside *database*, *primitives* and similar, and inflate the
candidate list several-fold.

## 3. Apply the scope test

From [SCOPE.md](../SCOPE.md): a project is in only if it is **both** AI-related
**and** meaningfully Israel-focused. In practice most of the filtering effort
goes on repos that are Israel-focused but not AI — Home Assistant Shabbat
dashboards, Red Alert notifiers and HA templates, alert-feed syntax notes,
shelter guideline translations, WiFi regulations, fonts, wallpapers, RSS feed
lists. These stay out even though they sit next to the AI work.

Data repos are in when they exist to ground or back an agent (Miklat MCP Data,
Israel Online Stores, the Form 6111 expense codes, the data.gov.il translation
mapping) and out when they are just data.

Only public repos may be listed — this index is public, and a private link is a
404 for every reader.

## 4. Check the existing links before adding new ones

Renames leave the old link working via GitHub's redirect, but the shields.io
star badge is fetched by the *old* name and breaks silently, so a stale entry
looks fine until you notice the missing badge. Deleted repos give a plain 404.

```bash
grep -oh 'github.com/danielrosehill/[A-Za-z0-9_.-]*' *.md \
  | sed 's|.*danielrosehill/||' | sort -u \
  | while read r; do
      res=$(gh api "repos/danielrosehill/$r" --jq '"\(.visibility) \(.name)"' 2>/dev/null)
      [ -z "$res" ] && { echo "MISSING: $r"; continue; }
      set -- $res
      [ "$1" = public ] || echo "NOT PUBLIC: $r ($1)"
      [ "$2" = "$r" ]   || echo "RENAMED: $r -> $2"
    done
```

The 2026-07-25 run found three: `Israel-Agent-Skills-Plugin` →
`Claude-Israel-Agent-Skills-Plugin`, `Geopol-Forecaster-POC` →
`Geopol-Forecaster`, and `Israeli-Tech-Shopping-MCP` gone with no redirect (its
successor is the Claude Israel Shopping Plugin, already listed).

## 5. Housekeeping

- New section in `mcps.md` → also add it to that file's Contents list *and* to
  the "By Domain" column of the README table.
- Bump both `*Last updated:*` stamps in the README (top of file and above the
  maintainer line) — they drift apart otherwise.
- A new `##` section needs nothing done for the [website](site.md): it is
  generated from these same markdown files on push, so the section becomes a
  category page by itself. A new **top-level `.md` file** is different — it has
  to be registered in `scripts/build_site.py` in three places (`PROJECT_PAGES`,
  `MD_TO_PAGE`, and the `links` list in `nav_html`) plus the README's Contents
  table and Projects list. Miss one and the build still succeeds; the page just
  never appears, or appears with no nav entry and cross-links pointing at
  github.com. Do check the entry-count and broken-link snippets in `site.md` after
  a large sweep — a malformed table row drops its entries from the site
  silently while still looking fine on github.com.
