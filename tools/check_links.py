"""Check external HTTP(S) links used by index.html.

Usage: python tools/check_links.py
"""
from __future__ import annotations

import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "index.html").read_text(encoding="utf-8")

links = sorted(
    set(
        re.findall(
            r'href="(https?://[^"#]+)"',
            SOURCE,
        )
    )
)


def status(url: str) -> str:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            return str(response.status)
    except urllib.error.HTTPError as error:
        if error.code in (403, 405, 501):
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(request, timeout=12) as response:
                    return str(response.status)
            except Exception as exc:  # noqa: BLE001
                return f"error: {type(exc).__name__}"
        return str(error.code)
    except Exception as exc:  # noqa: BLE001
        return f"error: {type(exc).__name__}"


print(f"Checking {len(links)} unique external links...")
for link in links:
    print(f"{status(link):>12}  {link}")
