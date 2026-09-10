#!/usr/bin/env python3
"""Build a single print-friendly HTML file from MkDocs nav order."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

try:
    import markdown
    import yaml
except ImportError as exc:
    mkdocs_path = shutil.which("mkdocs")
    if mkdocs_path and os.environ.get("BUILD_BOOK_HTML_REEXECED") != "1":
        first_line = Path(mkdocs_path).read_text(encoding="utf-8").splitlines()[0]
        if first_line.startswith("#!") and "python" in first_line.lower():
            interpreter = first_line[2:].strip().split()
            os.environ["BUILD_BOOK_HTML_REEXECED"] = "1"
            os.execvpe(
                interpreter[0],
                [*interpreter, str(Path(__file__).resolve()), *sys.argv[1:]],
                os.environ,
            )

    raise SystemExit(
        "Missing dependency. Install MkDocs first: python -m pip install mkdocs"
    ) from exc


@dataclass(frozen=True)
class Page:
    title: str
    source: str
    breadcrumbs: tuple[str, ...]
    page_id: str


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug or "page"


def is_external_target(target: str) -> bool:
    parsed = urlsplit(target)
    return bool(parsed.scheme or parsed.netloc) or target.startswith("#")


def normalize_nav_path(path: str) -> str:
    return Path(path).as_posix().lstrip("./")


def read_config(config_path: Path) -> dict[str, Any]:
    with config_path.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file) or {}

    if "nav" not in config:
        raise ValueError(f"{config_path} does not contain a 'nav' section.")

    return config


def nav_for_section(nav: list[Any], section_name: str | None) -> list[Any]:
    if section_name is None:
        return nav

    for item in nav:
        if isinstance(item, dict):
            for label, value in item.items():
                if label == section_name:
                    if not isinstance(value, list):
                        raise ValueError(f"Section '{section_name}' is not a nav group.")
                    return value

    raise ValueError(f"Section '{section_name}' was not found in mkdocs.yml nav.")


def collect_pages(nav_items: list[Any], breadcrumbs: tuple[str, ...] = ()) -> list[Page]:
    pages: list[Page] = []

    def walk(items: list[Any], crumbs: tuple[str, ...]) -> None:
        for item in items:
            if isinstance(item, str):
                source = normalize_nav_path(item)
                if source.endswith(".md"):
                    title = Path(source).stem.replace("-", " ").title()
                    page_number = len(pages) + 1
                    pages.append(
                        Page(
                            title,
                            source,
                            crumbs,
                            f"page-{page_number:03d}-{slugify(source)}",
                        )
                    )
                continue

            if not isinstance(item, dict):
                continue

            for label, value in item.items():
                if isinstance(value, str):
                    source = normalize_nav_path(value)
                    if source.endswith(".md") and not is_external_target(source):
                        page_number = len(pages) + 1
                        pages.append(
                            Page(
                                label,
                                source,
                                crumbs + (label,),
                                f"page-{page_number:03d}-{slugify(source)}",
                            )
                        )
                elif isinstance(value, list):
                    walk(value, crumbs + (label,))

    walk(nav_items, breadcrumbs)
    return pages


def html_attr_path(path: Path) -> str:
    return path.as_posix()


def rewrite_asset_and_page_links(
    rendered_html: str,
    *,
    page: Page,
    docs_dir: Path,
    output_path: Path,
    page_id_by_source: dict[str, str],
) -> str:
    page_dir = docs_dir / Path(page.source).parent
    output_dir = output_path.parent

    def replace(match: re.Match[str]) -> str:
        attr = match.group(1)
        raw_target = html.unescape(match.group(2))

        if is_external_target(raw_target):
            return match.group(0)

        parsed = urlsplit(raw_target)
        target_path = parsed.path

        if not target_path:
            return match.group(0)

        resolved_source = normalize_nav_path(
            (Path(page.source).parent / target_path).as_posix()
        )

        if attr == "href" and resolved_source.endswith(".md"):
            target_id = page_id_by_source.get(resolved_source)
            if target_id:
                return f'{attr}="#{target_id}"'

        resolved_file = (page_dir / target_path).resolve()
        if resolved_file.exists():
            relative = Path(os.path.relpath(resolved_file, output_dir.resolve()))
            return f'{attr}="{html.escape(html_attr_path(relative))}"'

        return match.group(0)

    return re.sub(r'(href|src)="([^"]+)"', replace, rendered_html)


def render_page(
    page: Page,
    *,
    docs_dir: Path,
    output_path: Path,
    page_id_by_source: dict[str, str],
) -> str:
    source_path = docs_dir / page.source

    if not source_path.exists():
        raise FileNotFoundError(f"Nav page not found: {source_path}")

    markdown_text = source_path.read_text(encoding="utf-8")
    md = markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "toc",
        ],
        output_format="html5",
    )
    body = md.convert(markdown_text)
    body = rewrite_asset_and_page_links(
        body,
        page=page,
        docs_dir=docs_dir,
        output_path=output_path,
        page_id_by_source=page_id_by_source,
    )

    source_label = html.escape(page.source)
    breadcrumb = " / ".join(html.escape(part) for part in page.breadcrumbs)

    return f"""
<article class="book-page" id="{html.escape(page.page_id)}">
  <header class="page-header">
    <p class="page-source">{source_label}</p>
    <p class="page-breadcrumb">{breadcrumb}</p>
  </header>
  {body}
</article>
"""


def render_table_of_contents(pages: list[Page]) -> str:
    items = []
    for index, page in enumerate(pages, start=1):
        title = html.escape(page.title)
        path = html.escape(page.source)
        crumbs = " / ".join(html.escape(part) for part in page.breadcrumbs[:-1])
        crumb_html = f'<span class="toc-crumbs">{crumbs}</span>' if crumbs else ""
        items.append(
            f'<li><a href="#{html.escape(page.page_id)}">{index}. {title}</a>'
            f'{crumb_html}<span class="toc-path">{path}</span></li>'
        )

    return "\n".join(items)


def render_book(
    *,
    site_name: str,
    pages: list[Page],
    docs_dir: Path,
    output_path: Path,
) -> str:
    page_id_by_source = {page.source: page.page_id for page in pages}
    rendered_pages = [
        render_page(
            page,
            docs_dir=docs_dir,
            output_path=output_path,
            page_id_by_source=page_id_by_source,
        )
        for page in pages
    ]
    title = html.escape(site_name)
    toc = render_table_of_contents(pages)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} Book</title>
  <style>
    :root {{
      color-scheme: light;
      --text: #1f2933;
      --muted: #66788a;
      --border: #d9e2ec;
      --code-bg: #f5f7fa;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      color: var(--text);
      font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #ffffff;
    }}

    main {{
      max-width: 900px;
      margin: 0 auto;
      padding: 40px 28px;
    }}

    h1, h2, h3, h4, h5, h6 {{
      line-height: 1.25;
      margin: 1.6em 0 0.5em;
    }}

    h1 {{
      border-bottom: 2px solid var(--border);
      padding-bottom: 0.25em;
    }}

    a {{
      color: #155eef;
      text-decoration: none;
    }}

    code, pre {{
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      font-size: 0.92em;
    }}

    code {{
      background: var(--code-bg);
      border-radius: 4px;
      padding: 0.1em 0.3em;
    }}

    pre {{
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow-x: auto;
      padding: 14px 16px;
      white-space: pre-wrap;
    }}

    pre code {{
      background: transparent;
      padding: 0;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }}

    th, td {{
      border: 1px solid var(--border);
      padding: 8px 10px;
      vertical-align: top;
    }}

    img {{
      max-width: 100%;
    }}

    .cover {{
      min-height: 70vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-bottom: 2px solid var(--border);
      margin-bottom: 40px;
    }}

    .cover h1 {{
      border-bottom: 0;
      font-size: 3rem;
      margin: 0 0 0.5rem;
    }}

    .cover p, .page-source, .page-breadcrumb, .toc-path, .toc-crumbs {{
      color: var(--muted);
    }}

    .toc {{
      page-break-after: always;
    }}

    .toc ol {{
      padding-left: 1.5rem;
    }}

    .toc li {{
      margin: 0.35rem 0;
    }}

    .toc-path, .toc-crumbs {{
      display: block;
      font-size: 0.85rem;
    }}

    .book-page {{
      page-break-before: always;
    }}

    .page-header {{
      border-bottom: 1px solid var(--border);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
    }}

    .page-source, .page-breadcrumb {{
      font-size: 0.85rem;
      margin: 0;
    }}

    @media print {{
      @page {{
        margin: 18mm 14mm;
      }}

      body {{
        font-size: 11pt;
      }}

      main {{
        max-width: none;
        padding: 0;
      }}

      a {{
        color: inherit;
      }}

      pre, blockquote, table, img {{
        page-break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <section class="cover">
      <h1>{title}</h1>
      <p>Single-file book generated from MkDocs navigation order.</p>
      <p>Total pages: {len(pages)}</p>
    </section>
    <section class="toc">
      <h1>Table of Contents</h1>
      <ol>
        {toc}
      </ol>
    </section>
    {"".join(rendered_pages)}
  </main>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create one print-friendly HTML file from MkDocs nav order."
    )
    parser.add_argument(
        "--config",
        default="mkdocs.yml",
        type=Path,
        help="Path to mkdocs.yml. Default: mkdocs.yml",
    )
    parser.add_argument(
        "--output",
        default="site/book.html",
        type=Path,
        help="Output HTML path. Default: site/book.html",
    )
    parser.add_argument(
        "--section",
        help="Optional top-level nav section to export, for example: Python",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    project_dir = config_path.parent

    config = read_config(config_path)
    docs_dir = (project_dir / config.get("docs_dir", "docs")).resolve()
    output_path = (project_dir / args.output).resolve()

    nav = nav_for_section(config["nav"], args.section)
    pages = collect_pages(nav)

    if not pages:
        raise ValueError("No Markdown pages were found in the selected MkDocs nav.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    book_html = render_book(
        site_name=config.get("site_name", "MkDocs Notes"),
        pages=pages,
        docs_dir=docs_dir,
        output_path=output_path,
    )
    output_path.write_text(book_html, encoding="utf-8")

    section_label = f" section '{args.section}'" if args.section else ""
    print(f"Wrote {len(pages)} pages from{section_label} nav to {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
