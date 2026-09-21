import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from . import content


def _coverage_payload():
    """The subset of AREAS the browser needs for the coverage checker."""
    return [
        {
            "id": a["id"],
            "label": a["label"],
            "query": a["query"],
            "cx": a["cx"],
            "cy": a["cy"],
            "keys": a["keys"],
        }
        for a in content.AREAS
    ]


def _local_business_schema(request):
    """LocalBusiness structured data, one entry per branch.

    This is what puts the branches into Google's local results, so it is
    generated from the same BRANCHES list the page renders.
    """
    site = settings.SITE_URL.rstrip("/")
    items = []
    for index, branch in enumerate(content.BRANCHES, start=1):
        entry = {
            "@type": "DryCleaningOrLaundry",
            "@id": f"{site}/#branch-{index}",
            "name": f"LAVO Laundry — {branch['name']}",
            "url": site,
            "telephone": content.CONTACT["phone_e164"],
            "image": request.build_absolute_uri(
                f"{settings.STATIC_URL}{branch['image']}"
            ),
            "address": {
                "@type": "PostalAddress",
                "streetAddress": branch["street"],
                "addressLocality": branch["locality"],
                "addressRegion": branch["region"],
                "addressCountry": "PH",
            },
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": [
                        "Monday", "Tuesday", "Wednesday", "Thursday",
                        "Friday", "Saturday", "Sunday",
                    ],
                    "opens": "08:00",
                    "closes": "20:00",
                }
            ],
            "areaServed": [a["label"] for a in content.AREAS],
            "hasMap": branch["maps_url"],
        }
        if branch["postal_code"]:
            entry["address"]["postalCode"] = branch["postal_code"]
        if branch["lat"] is not None and branch["lng"] is not None:
            entry["geo"] = {
                "@type": "GeoCoordinates",
                "latitude": branch["lat"],
                "longitude": branch["lng"],
            }
        items.append(entry)
    return {"@context": "https://schema.org", "@graph": items}


@require_GET
def index(request):
    context = {
        "contact": content.CONTACT,
        "reasons": content.REASONS,
        "services": content.SERVICES,
        "pickup_conditions": content.PICKUP_CONDITIONS,
        "steps": content.STEPS,
        "areas": content.AREAS,
        "branches": content.BRANCHES,
        "reviews": content.REVIEWS,
        "faqs": content.FAQS,
        # json_script escapes this safely for the browser
        "coverage": _coverage_payload(),
        # "<" is escaped so the JSON-LD block cannot break out of its script tag
        "schema_json": json.dumps(
            _local_business_schema(request), ensure_ascii=False
        ).replace("<", "\\u003c"),
        "ga_id": settings.GOOGLE_ANALYTICS_ID,
        "pixel_id": settings.META_PIXEL_ID,
        "show_prototype_notice": settings.DEBUG,
    }
    return render(request, "landing/index.html", context)


@require_GET
def robots_txt(request):
    site = settings.SITE_URL.rstrip("/")
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        f"Sitemap: {site}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")
