# Deployment Guide

This site is a plain static site published with GitHub Pages. There is no build step, no `package.json`, and no backend.

## Local preview

```bash
git clone https://github.com/Nagapavankumarkongitala/Nagapavankumarkongitala.github.io.git
cd Nagapavankumarkongitala.github.io
python -m http.server 8765
```

Then open `http://localhost:8765/`.

## Verify before publishing

```bash
python tools/verify_parity.py
python tools/check_links.py
```

`verify_parity.py` confirms that all 17 portfolio projects still match `main` exactly and that the document has no duplicate IDs, empty image alt text, or anchors without `href`. `check_links.py` reports the HTTP status of every external link.

Check in the browser that:

- all 17 project cards are visible
- each portfolio filter shows the expected count (All 17, SQL 3, Python 5, Power BI 6, Excel 3, ML 2)
- the contact email, phone and resume links work
- there are no console errors or failed local asset requests

## Publishing

1. Commit changes on a feature branch.
2. Merge into `main` only after review approval.
3. Push `main` to `origin`.

GitHub Pages serves the repository root automatically. `.nojekyll` is present so asset paths are never rewritten by Jekyll. Do not deploy from a build folder and do not use FTP.

## Known external issue

`https://github.com/Nagapavankumarkongitala/Cognorise_infotech_internship` currently returns HTTP 404. The link is retained verbatim at the owner's explicit instruction.
