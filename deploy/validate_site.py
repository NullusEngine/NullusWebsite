#!/usr/bin/env python3
"""Check the static pages and the files required for a website release."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.nullusengine.com"
PAGES = {
    "index.html": ("zh-CN", f"{ORIGIN}/zh-cn/"),
    "zh-cn/index.html": ("zh-CN", f"{ORIGIN}/zh-cn/"),
    "en/index.html": ("en", f"{ORIGIN}/en/"),
}
ALTERNATES = {
    "zh-CN": f"{ORIGIN}/zh-cn/",
    "en": f"{ORIGIN}/en/",
    "x-default": f"{ORIGIN}/zh-cn/",
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.language = None
        self.canonical = None
        self.alternates = {}
        self.references = []
        self.ids = set()

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.language = attrs.get("lang")
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "link" and attrs.get("rel") == "alternate" and attrs.get("hreflang"):
            self.alternates[attrs["hreflang"]] = attrs.get("href")
        for attribute in ("src", "href"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])


def check_page(relative_path, expected_language, expected_canonical):
    page = ROOT / relative_path
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8-sig"))
    errors = []
    if parser.language != expected_language:
        errors.append(f"{relative_path}: unexpected HTML language {parser.language!r}")
    if parser.canonical != expected_canonical:
        errors.append(f"{relative_path}: unexpected canonical URL {parser.canonical!r}")
    if parser.alternates != ALTERNATES:
        errors.append(f"{relative_path}: language alternate links do not match the site URLs")

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
    for page, (language, canonical) in PAGES.items():
        errors.extend(check_page(page, language, canonical))

    sitemap = ET.parse(ROOT / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {node.text for node in sitemap.findall(".//s:loc", namespace)}
    if urls != {ALTERNATES["zh-CN"], ALTERNATES["en"]}:
        errors.append("sitemap.xml: expected the Chinese and English canonical URLs")
    if f"Sitemap: {ORIGIN}/sitemap.xml" not in (ROOT / "robots.txt").read_text(encoding="utf-8"):
        errors.append("robots.txt: sitemap URL is missing")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated static resources, language URLs, anchors, robots.txt, and sitemap.xml.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
