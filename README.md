# LAVO Laundry — landing site

Django 5/6 project serving the LAVO Laundry landing page for Muntinlupa and San Pedro.

## Run it locally

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

copy .env.example .env          # macOS/Linux: cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000.

Generate a real secret key for `.env`:

```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

## Where things live

| Path | What it is |
|---|---|
| `landing/content.py` | **All page copy** — services, prices, branches, coverage areas, reviews, FAQs, phone numbers |
| `landing/views.py` | Builds the page context and the LocalBusiness structured data |
| `landing/templates/landing/index.html` | The page; loops over everything in `content.py` |
| `landing/templates/landing/_map_svg.html` | Coverage map drawing |
| `landing/templates/landing/_icons.html` | Inline icon set |
| `landing/static/landing/css/site.css` | All styles |
| `landing/static/landing/js/site.js` | Menu, dropdown, coverage checker, map zoom |
| `landing/static/landing/img/` | Hero, four branch photos, four service posters |

**To change a price, a branch address or an FAQ, edit `landing/content.py` only.** The
template and the structured data both read from it, so they can't drift apart.

The coverage checker's area list is serialised into the page with `json_script`, so the
browser and the server share one definition of where LAVO delivers.

## Analytics

Set `GOOGLE_ANALYTICS_ID` and `META_PIXEL_ID` in `.env`. Left blank, neither snippet is
rendered at all — no empty tags, no requests. Create both properties under **LAVO's own**
Google and Meta accounts, then add us as users, so ownership stays with LAVO.

## Deploying

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
gunicorn lavo.wsgi              # or the platform's own start command
```

Set in the production environment:

```
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=<a real key>
DJANGO_ALLOWED_HOSTS=lavolaundry.ph,www.lavolaundry.ph
DJANGO_CSRF_TRUSTED_ORIGINS=https://lavolaundry.ph,https://www.lavolaundry.ph
SITE_URL=https://lavolaundry.ph
```

With `DJANGO_DEBUG=False` the project turns on HTTPS redirect, one-year HSTS, secure
cookies and the proxy SSL header. Static files are served by WhiteNoise with hashed
filenames, so no separate web server config is needed.

`DEBUG` also controls the "Prototype" ribbon at the top of the page — it disappears in
production automatically.

## Not built yet

- **Booking form.** The brief calls for name, number, address, estimated loads and
  preferred schedule, with an instant notification to LAVO and a reference number per
  request. Nothing on the page captures a lead today; every path ends at a phone number.
  This is the main reason to be on Django rather than static HTML.
- **Sitemap.** `robots.txt` already points at `/sitemap.xml`; add `django.contrib.sitemaps`
  when there is more than one page.
- **Real photography.** All nine images are AI-generated. The branch shots are not the
  actual storefronts and the service posters advertise shoes, stuffed toys and bags that
  are not in the price list. Replace before launch — Google Business Profile requires
  photos to represent the real premises.
- **Branch coordinates.** Only Parkhomes has latitude/longitude, so only it emits `geo`
  in the structured data. Add the other three to `content.py` for better local ranking.
