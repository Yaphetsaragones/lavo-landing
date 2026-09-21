"""Render the landing page to a static site in docs/ for GitHub Pages.

GitHub Pages cannot run Django. This renders the page once and writes plain
HTML plus the static files, which Pages can serve. Run it again after any
change to content.py, the template, the CSS or the images.

    python build_static.py

Then commit docs/ and push. In the repo: Settings > Pages > Source:
"Deploy from a branch", branch "main", folder "/docs".
"""

import os
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOCS = BASE / "docs"

# The URL the site will live at. Override before running, e.g.
# Default is the real published URL, so a plain `python build_static.py`
# is always correct. Override only when publishing somewhere else.
SITE_URL = os.environ.get("SITE_URL", "https://yaphetsaragones.github.io/lavo-landing")

os.environ["DJANGO_SETTINGS_MODULE"] = "lavo.settings"
os.environ["DJANGO_DEBUG"] = "False"          # hides the prototype ribbon
os.environ["DJANGO_SECRET_KEY"] = "build-only-key-not-used-at-runtime"
os.environ["DJANGO_ALLOWED_HOSTS"] = "testserver"
os.environ["SITE_URL"] = SITE_URL
# Static files sit next to index.html, so no hashed manifest
os.environ["DJANGO_STATIC_MANIFEST"] = "False"

import django  # noqa: E402

django.setup()

from django.test import Client  # noqa: E402


def main():
    client = Client()
    response = client.get("/", secure=True)
    if response.status_code != 200:
        sys.exit(f"Render failed: HTTP {response.status_code}")

    html = response.content.decode("utf-8")

    # Absolute /static/ paths break on a project page like user.github.io/repo/,
    # so make them relative to index.html.
    html = html.replace('src="/static/', 'src="static/')
    html = html.replace('href="/static/', 'href="static/')
    html = html.replace('content="https://testserver/static/', f'content="{SITE_URL}/static/')
    html = html.replace("https://testserver", SITE_URL)

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    (DOCS / "index.html").write_text(html, encoding="utf-8")
    # Stops Pages' Jekyll step from touching the files
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    shutil.copytree(BASE / "landing" / "static" / "landing", DOCS / "static" / "landing")

    robots = client.get("/robots.txt", secure=True)
    (DOCS / "robots.txt").write_bytes(robots.content)

    total = sum(f.stat().st_size for f in DOCS.rglob("*") if f.is_file())
    files = sum(1 for f in DOCS.rglob("*") if f.is_file())
    print(f"Built {DOCS}")
    print(f"  {files} files, {total / 1048576:.2f} MB")
    print(f"  site URL: {SITE_URL}")


if __name__ == "__main__":
    main()
