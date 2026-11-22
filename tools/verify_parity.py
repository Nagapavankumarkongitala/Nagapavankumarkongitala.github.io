"""Content-parity and structural checks for the portfolio redesign.

Compares all 17 portfolio project cards in the working index.html against the
untouched `main` branch, and reports structural/a11y regressions.

Usage:  python tools/verify_parity.py
"""
from __future__ import annotations

import subprocess
from collections import Counter
from pathlib import Path

from lxml import html

ROOT = Path(__file__).resolve().parents[1]
MIX_XPATH = '//*[contains(concat(" ", normalize-space(@class), " "), " mix ")]'

# Explicit, user-approved repairs that intentionally differ from `main`.
# key: (project number, field) -> approved replacement value
APPROVED_REPAIRS = {
    (17, "preview"): "https://github.com/Nagapavankumarkongitala/Netflix_strategy_analysis",
}


def _text(node) -> str:
    return " ".join(node.text_content().split()) if node is not None else ""


def extract_projects(source: str) -> list[dict[str, str]]:
    doc = html.fromstring(source)
    projects = []
    for card in doc.xpath(MIX_XPATH):
        paragraphs = card.xpath('.//div[contains(@class,"icons")]/p')
        image = card.xpath('.//img/@src')
        preview = card.xpath('.//a[contains(@class,"lightbox")]/@href')
        code = card.xpath('.//a[contains(@class,"link")]/@href')
        projects.append(
            {
                "title": _text(paragraphs[0]) if len(paragraphs) > 0 else "",
                "description": _text(paragraphs[1]) if len(paragraphs) > 1 else "",
                "image": image[0] if image else "",
                "preview": preview[0] if preview else "",
                "code": code[0] if code else "",
            }
        )
    return projects


def structural_report(source: str) -> list[str]:
    doc = html.fromstring(source)
    problems: list[str] = []

    ids = [node.get("id") for node in doc.xpath("//*[@id]")]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if duplicates:
        problems.append(f"duplicate IDs: {duplicates}")

    empty_alt = len(doc.xpath('//img[@alt=""]'))
    missing_alt = len(doc.xpath("//img[not(@alt)]"))
    if empty_alt or missing_alt:
        problems.append(f"images needing alt text: empty={empty_alt}, missing={missing_alt}")

    no_href = len(doc.xpath("//a[not(@href)]"))
    if no_href:
        problems.append(f"anchors without href: {no_href}")

    h1 = len(doc.xpath("//h1"))
    if h1 != 1:
        problems.append(f"h1 count should be 1, found {h1}")

    titles = doc.xpath("//title/text()")
    if len(titles) != 1:
        problems.append(f"title count should be 1, found {len(titles)}")

    cards = len(doc.xpath(MIX_XPATH))
    if cards != 17:
        problems.append(f"portfolio card count should be 17, found {cards}")

    return problems


def main() -> int:
    current = (ROOT / "index.html").read_text(encoding="utf-8")
    baseline = subprocess.check_output(
        ["git", "show", "main:index.html"], cwd=ROOT, text=True, encoding="utf-8"
    )

    base_projects = extract_projects(baseline)
    current_projects = extract_projects(current)

    print(f"Baseline projects: {len(base_projects)}")
    print(f"Current projects:  {len(current_projects)}")

    mismatches = []
    for index, (expected, actual) in enumerate(zip(base_projects, current_projects), 1):
        for field, value in expected.items():
            if value == actual.get(field):
                continue
            if APPROVED_REPAIRS.get((index, field)) == actual.get(field):
                print(f"Approved repair applied at #{index} {field}: {value!r} -> {actual.get(field)!r}")
                continue
            mismatches.append(
                    f"#{index} {field}:\n    expected: {value!r}\n    actual:   {actual.get(field)!r}"
                )

    if len(base_projects) != len(current_projects):
        mismatches.append("project count differs from baseline")

    if mismatches:
        print("\nCONTENT PARITY FAILED:")
        print("\n".join(mismatches))
        return 1

    print("CONTENT PARITY: 17/17 projects match main exactly.")

    problems = structural_report(current)
    if problems:
        print("\nSTRUCTURAL ISSUES:")
        print("\n".join(f"- {problem}" for problem in problems))
        return 1

    print("STRUCTURE: no duplicate IDs, all images have alt text, all anchors have href.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
