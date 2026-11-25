#!/usr/bin/env python3
"""Check the static pages and the files required for a website release."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.nullusengine.com"
ROUTES = ("", "rendering/", "getting-started/")
PAGES = {"index.html": ("zh-CN", "", f"{ORIGIN}/")}
for route in ROUTES:
    for locale, language in (("zh-cn", "zh-CN"), ("en", "en")):
        PAGES[f"{locale}/{route}index.html"] = (language, route, f"{ORIGIN}/{locale}/{route}")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.language = None
        self.canonical = None
        self.alternates = {}
        self.references = []
        self.ids = set()
        self.robots = ""
        self.description = ""
        self.title = ""
        self.open_graph = {}
        self.twitter = {}
        self.language_links = []
        self.h1_count = 0
        self.invalid_links = []
        self.json_ld_blocks = []
        self._in_json_ld = False
        self._in_title = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self._in_title = True
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots = attrs.get("content", "")
        if tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content", "")
        if tag == "meta" and attrs.get("property", "").startswith("og:"):
            self.open_graph[attrs["property"]] = attrs.get("content", "")
        if tag == "meta" and attrs.get("name", "").startswith("twitter:"):
            self.twitter[attrs["name"]] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "link" and attrs.get("rel") == "alternate" and attrs.get("hreflang"):
            self.alternates[attrs["hreflang"]] = attrs.get("href")
        if tag == "a" and attrs.get("hreflang"):
            self.language_links.append((attrs["hreflang"], attrs.get("href", "")))
        if "card-link" in attrs.get("class", "").split() and tag != "a":
            self.invalid_links.append("a feature detail link is not an anchor")
        if tag == "img" and "alt" not in attrs:
            self.invalid_links.append(f"image missing alt text: {attrs.get('src', '')}")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_json_ld = True
            self.json_ld_blocks.append("")
        for attribute in ("src", "href"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])

    def handle_data(self, data):
        if self._in_json_ld:
            self.json_ld_blocks[-1] += data
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_json_ld = False
        if tag == "title":
            self._in_title = False


def check_page(relative_path, expected_language, route, public_url):
    page = ROOT / relative_path
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8-sig"))
    errors = []
    expected_canonical = f"{ORIGIN}/{'en' if expected_language == 'en' else 'zh-cn'}/{route}"
    alternates = {
        "zh-CN": f"{ORIGIN}/zh-cn/{route}",
        "en": f"{ORIGIN}/en/{route}",
        "x-default": f"{ORIGIN}/zh-cn/{route}",
    }
    if parser.language != expected_language:
        errors.append(f"{relative_path}: unexpected HTML language {parser.language!r}")
    if parser.canonical != expected_canonical:
        errors.append(f"{relative_path}: unexpected canonical URL {parser.canonical!r}")
    if parser.alternates != alternates:
        errors.append(f"{relative_path}: language alternate links do not match the site URLs")
    if parser.h1_count != 1 or not parser.title.strip() or not parser.description.strip():
        errors.append(f"{relative_path}: a title, a single H1, and a meta description are required")
    if parser.open_graph.get("og:url") != expected_canonical:
        errors.append(f"{relative_path}: Open Graph URL does not match the canonical URL")
    if parser.open_graph.get("og:image") != f"{ORIGIN}/assets/og-cover.jpg":
        errors.append(f"{relative_path}: the shared social image is missing")
    if (parser.open_graph.get("og:image:width"), parser.open_graph.get("og:image:height")) != ("1200", "630"):
        errors.append(f"{relative_path}: unexpected social image dimensions")
    if parser.twitter.get("twitter:card") != "summary_large_image" or parser.twitter.get("twitter:image") != f"{ORIGIN}/assets/og-cover.jpg":
        errors.append(f"{relative_path}: Twitter card metadata is incomplete")
    if relative_path == "index.html" and "noindex" not in parser.robots:
        errors.append("index.html: the duplicate root page must remain noindex")
    if relative_path != "index.html" and "noindex" in parser.robots:
        errors.append(f"{relative_path}: an indexable page is marked noindex")
    expected_other = "zh-CN" if expected_language == "en" else "en"
    if not any(lang == expected_other and urljoin(public_url, href) == alternates[expected_other]
               for lang, href in parser.language_links):
        errors.append(f"{relative_path}: a crawlable link to the other language is missing")
    errors.extend(f"{relative_path}: {problem}" for problem in parser.invalid_links)
    for block in parser.json_ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as error:
            errors.append(f"{relative_path}: invalid JSON-LD: {error}")
    if not parser.json_ld_blocks:
        errors.append(f"{relative_path}: JSON-LD is missing")

    for reference in parser.references:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        if not url.path:
            if url.fragment and unquote(url.fragment) not in parser.ids:
                errors.append(f"{relative_path}: missing anchor {reference}")
            continue
        target = (ROOT / url.path.lstrip("/")) if url.path.startswith("/") else (page.parent / unquote(url.path))
        target = target.resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"{relative_path}: missing local resource {reference}")
    return errors


def main():
    errors = []
    for asset in ("assets/editor-1920.jpg", "assets/og-cover.jpg", "assets/favicon.png"):
        if not (ROOT / asset).is_file():
            errors.append(f"Required image is missing: {asset}")
    for page, (language, route, public_url) in PAGES.items():
        errors.extend(check_page(page, language, route, public_url))

    sitemap = ET.parse(ROOT / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {node.text for node in sitemap.findall(".//s:loc", namespace)}
    expected_urls = {f"{ORIGIN}/{locale}/{route}" for route in ROUTES for locale in ("zh-cn", "en")}
    if urls != expected_urls:
        errors.append("sitemap.xml: expected the canonical URLs for both languages")
    if f"Sitemap: {ORIGIN}/sitemap.xml" not in (ROOT / "robots.txt").read_text(encoding="utf-8"):
        errors.append("robots.txt: sitemap URL is missing")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated static resources, metadata, JSON-LD, language links, anchors, robots.txt, and sitemap.xml.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
