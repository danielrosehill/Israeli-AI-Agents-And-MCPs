#!/usr/bin/env python3
"""Build the GitHub Pages site from the markdown index files.

The markdown files at the repo root stay the single source of truth — this
script parses them and renders a static site into `_site/`. Nothing is
committed: the GitHub Actions workflow runs this on push and publishes the
output. Standard library only, so the workflow needs no dependency install.

Usage: python3 scripts/build_site.py [--out _site]
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"

SITE_TITLE = "Israeli AI Ecosystem"
SITE_TAGLINE = (
    "A curated map of the Israeli AI ecosystem — agents, agent skills, MCP "
    "servers, Hebrew language resources, and the communities around them."
)
REPO_URL = "https://github.com/danielrosehill/Israeli-AI"
CONTACT_EMAIL = "public@danielrosehill.com"

# Source pages that carry project listings. `split` means each `##` section
# becomes its own category page rather than a heading on one long page.
PROJECT_PAGES = [
    {"src": "agents.md", "slug": "agents", "title": "AI Agents", "icon": "🤖", "split": False},
    {"src": "agent-skills.md", "slug": "agent-skills", "title": "Agent Skills", "icon": "🧩", "split": False},
    {"src": "mcps.md", "slug": "mcps", "title": "MCP Servers", "icon": "🔌", "split": True},
    {"src": "ideation.md", "slug": "ideation", "title": "AI Ideation", "icon": "💡", "split": False},
    {"src": "hebrew.md", "slug": "hebrew", "title": "Hebrew & Language", "icon": "🇮🇱", "split": True},
]

# Level-1 README sections that become ecosystem pages, in site order.
ECOSYSTEM_SECTIONS = [
    ("Curated Lists", "curated-lists", "📚"),
    ("Communities & Organizations", "communities", "👥"),
    ("Government Bodies", "government-bodies", "🏛️"),
    ("Centers of Excellence", "centers-of-excellence", "🎓"),
    ("Conferences & Events", "conferences", "📅"),
    ("Inference Providers & Local Clouds", "inference-providers", "☁️"),
    ("Startup Ecosystem", "startups", "🚀"),
    ("Related Indexes", "related-indexes", "🔗"),
]

# README sections the site renders elsewhere (nav, footer, /scope/) or drops.
README_SKIP = {"Contents", "Projects", "Hebrew Language Resources"}


# --------------------------------------------------------------------------
# Markdown parsing
# --------------------------------------------------------------------------


@dataclass
class Block:
    kind: str  # "p" | "table" | "list" | "quote" | "hr"
    lines: list[str] = field(default_factory=list)
    rows: list[list[str]] = field(default_factory=list)
    headers: list[str] = field(default_factory=list)


@dataclass
class Section:
    level: int
    title: str
    blocks: list[Block] = field(default_factory=list)
    children: list["Section"] = field(default_factory=list)


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text.strip().lower())
    return re.sub(r"-{2,}", "-", text).strip("-")


def split_row(line: str) -> list[str]:
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def parse_markdown(path: Path) -> list[Section]:
    """Flat list of sections in document order; blocks are grouped by type."""
    sections: list[Section] = []
    current = Section(level=0, title="")
    sections.append(current)
    block: Block | None = None
    in_html = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()

        # The README's Contents block is hand-written HTML; the site builds its
        # own navigation, so skip over it wholesale.
        if line.lstrip().startswith("<table"):
            in_html = True
        if in_html:
            if line.lstrip().startswith("</table"):
                in_html = False
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            block = None
            current = Section(level=len(heading.group(1)), title=heading.group(2).strip())
            sections.append(current)
            continue

        if not line.strip():
            block = None
            continue

        if re.match(r"^-{3,}$|^\*{3,}$", line.strip()):
            block = None
            current.blocks.append(Block(kind="hr"))
            continue

        if line.lstrip().startswith("|"):
            cells = split_row(line)
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue  # table separator row
            if block is None or block.kind != "table":
                block = Block(kind="table", headers=cells)
                current.blocks.append(block)
            else:
                block.rows.append(cells)
            continue

        if re.match(r"^\s*[-*+]\s+", line):
            item = re.sub(r"^\s*[-*+]\s+", "", line)
            if block is None or block.kind != "list":
                block = Block(kind="list")
                current.blocks.append(block)
            block.lines.append(item)
            continue

        if line.lstrip().startswith(">"):
            item = line.lstrip().lstrip(">").strip()
            if block is None or block.kind != "quote":
                block = Block(kind="quote")
                current.blocks.append(block)
            block.lines.append(item)
            continue

        if block is None or block.kind != "p":
            block = Block(kind="p")
            current.blocks.append(block)
        block.lines.append(line.strip())

    return [s for s in sections if s.title or s.blocks]


def nest(sections: list[Section], top_level: int) -> list[Section]:
    """Attach deeper sections to the preceding section at `top_level`."""
    out: list[Section] = []
    for sec in sections:
        if sec.level <= top_level or not out:
            out.append(sec)
        else:
            out[-1].children.append(sec)
    return out


# --------------------------------------------------------------------------
# Inline rendering
# --------------------------------------------------------------------------

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")


def esc(text: str) -> str:
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"&(?![a-zA-Z#][a-zA-Z0-9]*;)", "&amp;", text)


def inline(text: str) -> str:
    out = esc(text)
    out = IMAGE_RE.sub(
        lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">', out
    )
    out = LINK_RE.sub(
        lambda m: f'<a href="{m.group(2)}"{_target(m.group(2))}>{m.group(1)}</a>', out
    )
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def _target(href: str) -> str:
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""


# Cross-links in the markdown point at sibling files in the repo; on the site
# they have to point at the corresponding page. Split pages fold their `##`
# anchors into per-category directories.
MD_TO_PAGE = {
    "README.md": ("", False),
    "agents.md": ("agents/", False),
    "agent-skills.md": ("agent-skills/", False),
    "mcps.md": ("mcps/", True),
    "ideation.md": ("ideation/", False),
    "hebrew.md": ("hebrew/", True),
    "SCOPE.md": ("scope/", False),
}


def rewrite_internal_links(body: str, up: str) -> str:
    def repl(m: re.Match) -> str:
        href = m.group(1)
        file, _, anchor = href.partition("#")
        if file not in MD_TO_PAGE:
            # Anything else in the repo (pending.md, docs/) has no site page.
            return f'href="{REPO_URL}/blob/main/{href}" target="_blank" rel="noopener"'
        path, split = MD_TO_PAGE[file]
        if anchor and split:
            return f'href="{up}{path}{re.sub("-{2,}", "-", anchor)}/"'
        suffix = f"#{anchor}" if anchor else ""
        return f'href="{up}{path}{suffix}"'

    return re.sub(r'href="((?!https?:|mailto:|#|\.)[^"]+\.md(?:#[^"]*)?)"', repl, body)


def strip_md(text: str) -> str:
    text = IMAGE_RE.sub("", text)
    text = LINK_RE.sub(r"\1", text)
    return re.sub(r"[*`_]", "", text).strip()


# --------------------------------------------------------------------------
# Entries (the card model behind both rendering and search)
# --------------------------------------------------------------------------


@dataclass
class Entry:
    title: str
    href: str
    description: str
    badge: str = ""

    @property
    def host_label(self) -> str:
        m = re.match(r"https?://(?:www\.)?github\.com/([^/]+)/?", self.href)
        if m:
            return m.group(1)
        m = re.match(r"https?://(?:www\.)?([^/]+)", self.href)
        return m.group(1) if m else ""


def table_entries(block: Block) -> list[Entry]:
    entries = []
    for row in block.rows:
        if not row or not row[0]:
            continue
        link = LINK_RE.search(row[0])
        title = link.group(1) if link else strip_md(row[0])
        href = link.group(2) if link else ""
        badge = ""
        desc_cells = []
        for cell in row[1:]:
            if IMAGE_RE.search(cell):
                img = IMAGE_RE.search(cell)
                badge = img.group(2)
            elif cell:
                desc_cells.append(cell)
        entries.append(Entry(title, href, " · ".join(desc_cells), badge))
    return entries


def list_entries(block: Block) -> list[Entry]:
    """Bullets shaped `- [Name](url) — description` become cards too."""
    entries = []
    for item in block.lines:
        link = LINK_RE.search(item)
        if not link or not item.strip().startswith("["):
            return []
        rest = item[link.end():].strip()
        rest = re.sub(r"^[—–-]\s*", "", rest)
        entries.append(Entry(link.group(1), link.group(2), rest))
    return entries


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------


def render_entry(e: Entry) -> str:
    title = f'<a href="{e.href}"{_target(e.href)}>{esc(e.title)}</a>' if e.href else esc(e.title)
    parts = [f'    <h3 class="card-title">{title}</h3>']
    if e.description:
        parts.append(f'    <p class="card-desc">{inline(e.description)}</p>')
    meta = []
    if e.host_label:
        meta.append(f'<span class="card-host">{esc(e.host_label)}</span>')
    if e.badge:
        meta.append(f'<img class="card-badge" src="{e.badge}" alt="stars" loading="lazy">')
    if meta:
        parts.append(f'    <div class="card-meta">{"".join(meta)}</div>')
    body = "\n".join(parts)
    return f'  <article class="card" data-entry>\n{body}\n  </article>'


def render_blocks(blocks: list[Block]) -> tuple[str, list[Entry]]:
    out: list[str] = []
    entries: list[Entry] = []
    for block in blocks:
        if block.kind == "p":
            out.append(f'<p>{inline(" ".join(block.lines))}</p>')
        elif block.kind == "quote":
            out.append(f'<blockquote>{inline(" ".join(block.lines))}</blockquote>')
        elif block.kind == "hr":
            continue  # section boundaries are structural on the site
        elif block.kind == "table":
            found = table_entries(block)
            entries.extend(found)
            cards = "\n".join(render_entry(e) for e in found)
            out.append(f'<div class="card-grid">\n{cards}\n</div>')
        elif block.kind == "list":
            found = list_entries(block)
            if found:
                entries.extend(found)
                cards = "\n".join(render_entry(e) for e in found)
                out.append(f'<div class="card-grid">\n{cards}\n</div>')
            else:
                items = "\n".join(f"  <li>{inline(i)}</li>" for i in block.lines)
                out.append(f'<ul class="prose-list">\n{items}\n</ul>')
    return "\n".join(out), entries


def render_section(sec: Section, heading_level: int = 2) -> tuple[str, list[Entry]]:
    body, entries = render_blocks(sec.blocks)
    anchor = slugify(sec.title)
    head = (
        f'<h{heading_level} id="{anchor}" class="section-heading">'
        f'<a href="#{anchor}">{inline(sec.title)}</a></h{heading_level}>'
        if sec.title
        else ""
    )
    parts = [head, body]
    for child in sec.children:
        child_html, child_entries = render_section(child, min(heading_level + 1, 6))
        parts.append(child_html)
        entries.extend(child_entries)
    return "\n".join(p for p in parts if p), entries


# --------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------


def nav_html(depth: int, active: str) -> str:
    up = "../" * depth if depth else "./"
    links = [
        ("", "Home", "home"),
        ("agents/", "Agents", "agents"),
        ("agent-skills/", "Skills", "agent-skills"),
        ("mcps/", "MCP Servers", "mcps"),
        ("ideation/", "Ideation", "ideation"),
        ("hebrew/", "Hebrew", "hebrew"),
        ("ecosystem/", "Ecosystem", "ecosystem"),
        ("scope/", "Scope", "scope"),
    ]
    items = "".join(
        f'<a href="{up}{href}" class="{"active" if key == active else ""}">{label}</a>'
        for href, label, key in links
    )
    return items


def page(
    *,
    out_dir: Path,
    rel_path: str,
    title: str,
    description: str,
    body: str,
    active: str,
    breadcrumb: list[tuple[str, str]] | None = None,
    depth: int,
) -> None:
    # Relative links throughout, so the site works under the /Israeli-AI/
    # project-pages subpath and from a plain `file://` open.
    up = "../" * depth if depth else "./"
    body = rewrite_internal_links(body, up)
    crumbs = ""
    if breadcrumb:
        links = " <span>/</span> ".join(
            f'<a href="{up}{href}">{esc(label)}</a>' if href is not None else f"<span>{esc(label)}</span>"
            for label, href in breadcrumb
        )
        crumbs = f'<nav class="breadcrumb">{links}</nav>'

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{up}">
      <span class="brand-mark">🇮🇱</span>
      <span class="brand-text">Israeli AI<span class="brand-sub">Ecosystem index</span></span>
    </a>
    <nav class="site-nav">{nav_html(depth, active)}</nav>
    <div class="header-tools">
      <input type="search" id="site-search" class="search-input" placeholder="Filter this page…" aria-label="Filter entries on this page" autocomplete="off">
      <a class="gh-link" href="{REPO_URL}" target="_blank" rel="noopener" aria-label="View on GitHub">GitHub</a>
    </div>
  </div>
</header>
<main id="main" class="wrap">
{crumbs}
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <p>Maintained by <a href="https://github.com/danielrosehill" target="_blank" rel="noopener">Daniel Rosehill</a>.
       Additions welcome — open a PR or email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
    <p class="muted">Inclusion is not an endorsement; evaluate each project independently.
       Built from the markdown in the <a href="{REPO_URL}" target="_blank" rel="noopener">source repo</a>.
       Last built {date.today().isoformat()}.</p>
  </div>
</footer>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""
    target = out_dir / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding="utf-8")


def card_link(href: str, title: str, desc: str, count: int | None, icon: str = "") -> str:
    badge = f'<span class="count">{count}</span>' if count is not None else ""
    mark = f'<span class="nav-icon">{icon}</span>' if icon else ""
    return f"""  <a class="nav-card" href="{href}">
    <span class="nav-card-head">{mark}<span class="nav-card-title">{esc(title)}</span>{badge}</span>
    <span class="nav-card-desc">{esc(desc)}</span>
  </a>"""


def intro_text(sec: Section) -> str:
    for block in sec.blocks:
        if block.kind == "p":
            return strip_md(" ".join(block.lines))
    return ""


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------


def build(out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    search_index: list[dict] = []
    nav_cards: dict[str, list[str]] = {"projects": [], "ecosystem": []}
    totals = {"entries": 0, "categories": 0}

    def record(entries: list[Entry], category: str, page_url: str) -> None:
        for e in entries:
            search_index.append(
                {
                    "t": e.title,
                    "d": strip_md(e.description)[:220],
                    "u": e.href,
                    "c": category,
                    "p": page_url,
                }
            )

    # ---- project pages -----------------------------------------------------
    for spec in PROJECT_PAGES:
        sections = nest(parse_markdown(ROOT / spec["src"]), top_level=1)
        root_sec = next((s for s in sections if s.level <= 1), sections[0])
        children = [c for c in root_sec.children if c.title.lower() != "contents"]
        lede = intro_text(root_sec)

        if not spec["split"]:
            body_parts, entries = render_blocks(root_sec.blocks)
            html_parts = [
                f'<h1 class="page-title">{spec["icon"]} {esc(spec["title"])}</h1>',
                f'<p class="lede">{inline(lede)}</p>' if lede else "",
                body_parts,
            ]
            for child in children:
                child_html, child_entries = render_section(child, 2)
                html_parts.append(child_html)
                entries.extend(child_entries)
            page(
                out_dir=out_dir,
                rel_path=f"{spec['slug']}/index.html",
                title=f"{spec['title']} — {SITE_TITLE}",
                description=lede or SITE_TAGLINE,
                body="\n".join(p for p in html_parts if p),
                active=spec["slug"],
                breadcrumb=[("Home", ""), (spec["title"], None)],
                depth=1,
            )
            record(entries, spec["title"], f"{spec['slug']}/")
            totals["entries"] += len(entries)
            totals["categories"] += 1
            nav_cards["projects"].append(
                card_link(f"{spec['slug']}/", spec["title"], lede, len(entries), spec["icon"])
            )
            continue

        # split: one page per category, plus a hub
        hub_cards = []
        page_entries = 0
        for child in children:
            child_slug = slugify(child.title)
            child_html, entries = render_section(child, 1)
            child_html = child_html.replace(
                f'class="section-heading"', 'class="page-title"', 1
            )
            page(
                out_dir=out_dir,
                rel_path=f"{spec['slug']}/{child_slug}/index.html",
                title=f"{strip_md(child.title)} — {spec['title']} — {SITE_TITLE}",
                description=intro_text(child) or f"{strip_md(child.title)} — {spec['title']}.",
                body=child_html,
                active=spec["slug"],
                breadcrumb=[("Home", ""), (spec["title"], f"{spec['slug']}/"), (strip_md(child.title), None)],
                depth=2,
            )
            record(entries, strip_md(child.title), f"{spec['slug']}/{child_slug}/")
            page_entries += len(entries)
            totals["categories"] += 1
            hub_cards.append(
                card_link(
                    f"{child_slug}/",
                    strip_md(child.title),
                    intro_text(child),
                    len(entries) or None,
                )
            )

        hub_body = "\n".join(
            [
                f'<h1 class="page-title">{spec["icon"]} {esc(spec["title"])}</h1>',
                f'<p class="lede">{inline(lede)}</p>' if lede else "",
                f'<p class="stat-line">{page_entries} entries across {len(hub_cards)} categories</p>',
                '<div class="nav-grid">',
                "\n".join(hub_cards),
                "</div>",
            ]
        )
        page(
            out_dir=out_dir,
            rel_path=f"{spec['slug']}/index.html",
            title=f"{spec['title']} — {SITE_TITLE}",
            description=lede or SITE_TAGLINE,
            body=hub_body,
            active=spec["slug"],
            breadcrumb=[("Home", ""), (spec["title"], None)],
            depth=1,
        )
        totals["entries"] += page_entries
        nav_cards["projects"].append(
            card_link(f"{spec['slug']}/", spec["title"], lede, page_entries, spec["icon"])
        )

    # ---- ecosystem pages from the README ------------------------------------
    readme = nest(parse_markdown(ROOT / "README.md"), top_level=1)
    readme_by_title = {s.title: s for s in readme}
    ecosystem_cards = []      # hub-relative, for /ecosystem/
    ecosystem_cards_home = []  # root-relative, for /
    for title, slug, icon in ECOSYSTEM_SECTIONS:
        sec = readme_by_title.get(title)
        if sec is None:
            continue
        body_html, entries = render_section(sec, 1)
        body_html = body_html.replace('class="section-heading"', 'class="page-title"', 1)
        page(
            out_dir=out_dir,
            rel_path=f"ecosystem/{slug}/index.html",
            title=f"{title} — {SITE_TITLE}",
            description=intro_text(sec) or f"{title} in the Israeli AI ecosystem.",
            body=body_html,
            active="ecosystem",
            breadcrumb=[("Home", ""), ("Ecosystem", "ecosystem/"), (title, None)],
            depth=2,
        )
        record(entries, title, f"ecosystem/{slug}/")
        totals["entries"] += len(entries)
        totals["categories"] += 1
        ecosystem_cards.append(
            card_link(f"{slug}/", title, intro_text(sec), len(entries) or None, icon)
        )
        ecosystem_cards_home.append(
            card_link(f"ecosystem/{slug}/", title, intro_text(sec), len(entries) or None, icon)
        )

    page(
        out_dir=out_dir,
        rel_path="ecosystem/index.html",
        title=f"Ecosystem — {SITE_TITLE}",
        description="Israeli AI communities, meetups, government bodies, conferences and startup resources.",
        body="\n".join(
            [
                '<h1 class="page-title">🌐 Ecosystem</h1>',
                '<p class="lede">Communities, meetups, government bodies, academic centres, '
                "conferences and the directories that track the Israeli AI scene.</p>",
                '<div class="nav-grid">',
                "\n".join(ecosystem_cards),
                "</div>",
            ]
        ),
        active="ecosystem",
        breadcrumb=[("Home", ""), ("Ecosystem", None)],
        depth=1,
    )
    nav_cards["ecosystem"] = ecosystem_cards_home

    # ---- scope / about ------------------------------------------------------
    scope_sections = nest(parse_markdown(ROOT / "SCOPE.md"), top_level=1)
    scope_root = scope_sections[0]
    scope_html, _ = render_section(scope_root, 1)
    scope_html = scope_html.replace('class="section-heading"', 'class="page-title"', 1)
    extras = []
    for extra in ("Contributing", "Disclaimer"):
        sec = readme_by_title.get(extra)
        if sec:
            extra_html, _ = render_section(sec, 2)
            extras.append(extra_html)
    page(
        out_dir=out_dir,
        rel_path="scope/index.html",
        title=f"Scope & Contributing — {SITE_TITLE}",
        description="Inclusion criteria for the Israeli AI ecosystem index, and how to contribute.",
        body="\n".join([scope_html, *extras]),
        active="scope",
        breadcrumb=[("Home", ""), ("Scope", None)],
        depth=1,
    )

    # ---- home ---------------------------------------------------------------
    home_body = "\n".join(
        [
            '<section class="hero">',
            f'  <h1>{esc(SITE_TITLE)}</h1>',
            f'  <p class="lede">{esc(SITE_TAGLINE)}</p>',
            '  <p class="hero-note">Not a directory of every AI company in Israel — a curated set of '
            "directions for people working in AI here: community, organisations, and practical tools.</p>",
            f'  <p class="stat-line"><strong>{totals["entries"]}</strong> entries · '
            f'<strong>{totals["categories"]}</strong> categories · updated {date.today().isoformat()}</p>',
            "</section>",
            '<h2 class="section-heading">Projects</h2>',
            '<div class="nav-grid">',
            "\n".join(nav_cards["projects"]),
            "</div>",
            '<h2 class="section-heading">Ecosystem</h2>',
            '<div class="nav-grid">',
            "\n".join(nav_cards["ecosystem"]),
            "</div>",
        ]
    )
    page(
        out_dir=out_dir,
        rel_path="index.html",
        title=SITE_TITLE,
        description=SITE_TAGLINE,
        body=home_body,
        active="home",
        depth=0,
    )

    # ---- assets & data ------------------------------------------------------
    assets = out_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for asset in WEB.iterdir():
        if asset.is_file():
            shutil.copy2(asset, assets / asset.name)
    banner = ROOT / "images" / "banner.png"
    if banner.exists():
        shutil.copy2(banner, assets / "banner.png")

    (out_dir / "search.json").write_text(
        json.dumps(search_index, ensure_ascii=False), encoding="utf-8"
    )
    # Jekyll would otherwise ignore nothing here, but keep it explicit.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    print(
        f"Built {len(list(out_dir.rglob('*.html')))} pages, "
        f"{totals['entries']} entries, {totals['categories']} categories → {out_dir}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(ROOT / "_site"), help="output directory")
    args = ap.parse_args()
    build(Path(args.out).resolve())


if __name__ == "__main__":
    main()
