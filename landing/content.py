"""Site content for the LAVO landing page.

Everything the page says lives here rather than in the template, so copy,
prices, branches and coverage can be changed without touching markup.
When LAVO wants to edit these themselves, move them into models and the
Django admin — the template loops stay the same.
"""

CONTACT = {
    "phone_display": "0993 921 6705",
    "phone_e164": "+639939216705",
    "phone_alt_display": "0992 827 8815",
    "phone_alt_e164": "+639928278815",
    "hours": "Mon – Sun · 8:00 AM – 8:00 PM",
    "messenger": "https://m.me/Lavoph",
    "facebook": "https://www.facebook.com/Lavoph",
    "instagram": "https://instagram.com/",
    "tiktok": "https://tiktok.com/",
    "reviews_url": "https://www.facebook.com/Lavoph",
}

REASONS = [
    {
        "title": "Separate washing",
        "body": "Your load never shares a machine with anyone else's. Better care, better hygiene.",
        "icon": "basket",
        "image": "landing/img/why-separate-sm.jpg",
        "w": 600,
        "h": 400,
        # full-resolution original, kept for print and social
        "banner": "landing/img/why-separate.png",
        "alt": "Separate washing — your load never shares a machine with anyone else's",
    },
    {
        "title": "Blue Card tracking",
        "body": "Every pickup carries a Blue Card number, so you can check where your laundry is at any time.",
        "icon": "card",
        "image": "landing/img/why-bluecard-sm.jpg",
        "w": 600,
        "h": 450,
        # full-resolution original, kept for print and social
        "banner": "landing/img/why-bluecard.png",
        "alt": "Blue Card tracking — check where your laundry is at any time",
    },
    {
        "title": "Weighing upon request",
        "body": "Ask us to weigh in front of you at pickup or drop-off. No guessing, no surprises.",
        "icon": "scales",
        "image": "landing/img/why-weighing-sm.jpg",
        "w": 600,
        "h": 400,
        # full-resolution original, kept for print and social
        "banner": "landing/img/why-weighing.png",
        "alt": "Weighing upon request — we weigh in front of you at pickup or drop-off",
    },
    {
        "title": "Four branches",
        "body": "Two in Muntinlupa, two in San Pedro — so pickups reach you faster.",
        "icon": "store",
        "image": "landing/img/why-branches-sm.jpg",
        "w": 600,
        "h": 337,
        # full-resolution original, kept for print and social
        "banner": "landing/img/why-branches.png",
        "alt": "Four branches — two in Muntinlupa, two in San Pedro",
    },
]

SERVICES = [
    {
        "name": "Wash & Fold",
        "body": "Everyday clothes, washed separately and folded fresh.",
        "price": "70",
        "unit": "per kg",
        "prefix": "",
        "image": "landing/img/svc-wash-fold.jpg",
        "alt": "LAVO Wash & Fold service — clean clothes, no hassle",
    },
    {
        "name": "Wash, Dry & Fold",
        "body": "The full service — washed, dried, folded, delivered.",
        "price": "80",
        "unit": "per kg",
        "prefix": "",
        "image": "landing/img/svc-wash-dry-fold.jpg",
        "alt": "LAVO Wash, Dry & Fold service — washed, dried, folded, ready",
    },
    {
        "name": "Premium Care",
        "body": "Delicate fabrics and garments that need extra attention.",
        "price": "100",
        "unit": "per kg",
        "prefix": "",
        "image": "landing/img/svc-premium-care.jpg",
        "alt": "LAVO Premium Care service — special attention for your favourite outfits",
    },
    {
        "name": "Special Items",
        "body": "Comforters, beddings, curtains and other bulky pieces.",
        "price": "150",
        "unit": "per piece",
        "prefix": "From",
        "image": "landing/img/svc-special-items.jpg",
        "alt": "LAVO Special Items service — extra care for comforters, shoes, stuffed toys and bags",
    },
]

PICKUP_CONDITIONS = [
    "Minimum 5 kg per pickup",
    "Within our coverage area only",
    "Pickup and delivery are scheduled, not on-demand",
    "Prices may vary for special or heavily soiled items",
]

STEPS = [
    ("Book a pickup", "Call or message us your address and pickup time. That is the whole booking."),
    ("We pick it up", "Our rider collects your laundry at your chosen time window."),
    ("We wash & care", "Washed separately, handled with care, tracked on your Blue Card."),
    ("We deliver", "Folded and fresh, back at your door on the scheduled day."),
]

# Coverage stops, in north-to-south order along the National Road.
# `cx`/`cy` are positions inside the 600x400 map viewBox; `keys` drive the checker.
AREAS = [
    {
        "id": "alabang", "label": "Alabang", "query": "Alabang, Muntinlupa City",
        "cx": 257, "cy": 76,
        "keys": ["alabang", "ayala alabang", "alabang hills", "new alabang",
                 "susana heights", "cupang", "buli"],
    },
    {
        "id": "putatan", "label": "Putatan", "query": "Putatan, Muntinlupa City",
        "cx": 257, "cy": 124,
        "keys": ["putatan", "bayanan"],
    },
    {
        "id": "muntinlupa", "label": "Muntinlupa", "query": "Muntinlupa City",
        "cx": 257, "cy": 172,
        "keys": ["muntinlupa", "poblacion", "sucat"],
    },
    {
        "id": "parkhomes", "label": "Parkhomes Tunasan", "query": "Parkhomes Tunasan, Muntinlupa City",
        "cx": 257, "cy": 220,
        "keys": ["parkhomes", "park homes", "golden gate"],
    },
    {
        "id": "villacarolina", "label": "Villa Carolina 1", "query": "Villa Carolina, Tunasan, Muntinlupa City",
        "cx": 257, "cy": 268,
        "keys": ["villa carolina", "carolina"],
    },
    {
        "id": "tunasan", "label": "Tunasan", "query": "Tunasan, Muntinlupa City",
        "cx": 257, "cy": 316,
        "keys": ["tunasan"],
    },
    {
        "id": "sanpedro", "label": "San Pedro", "query": "San Pedro, Laguna",
        "cx": 257, "cy": 364,
        "keys": ["san pedro", "cuyab", "amante", "santo nino", "sto nino",
                 "pacita", "landayan", "nueva", "riverside", "magsaysay"],
    },
]

BRANCHES = [
    {
        "name": "Parkhomes Branch",
        "street": "Golden Gate Park Ave",
        "locality": "Tunasan, Muntinlupa",
        "region": "Metro Manila",
        "postal_code": "1773",
        "address": "Golden Gate Park Ave, Tunasan, Muntinlupa, 1773 Metro Manila",
        "lat": 14.3753656,
        "lng": 121.0469753,
        # Google Business Profile CID — stable even if the listing name changes
        "maps_url": "https://www.google.com/maps?cid=3599832990173072245",
        "image": "landing/img/parkhomes.jpg",
    },
    {
        "name": "Poblacion Branch",
        "street": "San Guillermo St.",
        "locality": "Poblacion, Muntinlupa",
        "region": "Metro Manila",
        "postal_code": "",
        "address": "San Guillermo St., Poblacion, Muntinlupa",
        "lat": None,
        "lng": None,
        "maps_url": "https://www.google.com/maps/search/?api=1&query=LAVO+Laundry+-+San+Guillermo",
        "image": "landing/img/poblacion.jpg",
    },
    {
        "name": "Cuyab Branch",
        "street": "Amante St.",
        "locality": "Cuyab, San Pedro",
        "region": "Laguna",
        "postal_code": "",
        "address": "Amante St., Cuyab, San Pedro, Laguna",
        "lat": None,
        "lng": None,
        "maps_url": "https://www.google.com/maps/search/?api=1&query=LAVO+Laundry+-+Cuyab",
        "image": "landing/img/cuyab.jpg",
    },
    {
        "name": "Santo Niño Branch",
        "street": "Santo Niño St.",
        "locality": "Poblacion, San Pedro",
        "region": "Laguna",
        "postal_code": "",
        "address": "Santo Niño St., Poblacion, San Pedro, Laguna",
        "lat": None,
        "lng": None,
        "maps_url": "https://www.google.com/maps/search/?api=1&query=LAVO+Laundry+-+Cuyab",
        "image": "landing/img/santonino.jpg",
    },
]

# Verbatim Facebook recommendations. Facebook has no star rating, so these are
# rendered as "Recommends" rather than as a score.
REVIEWS = [
    {
        "initials": "MB",
        "name": "Myka Barcena",
        "date": "14 August",
        "paragraphs": [
            "Very smooth transaction. Mabilis and professional mag reply sa Messenger. "
            "I also appreciate the timely updates. Will definitely avail their service "
            "again in the future. \U0001F44D\U0001F60A",
        ],
    },
    {
        "initials": "KT",
        "name": "Kylie Tejada",
        "date": "24 June",
        "paragraphs": [
            "It’s our first time having our clothes washed at LAVO. We were looking for an "
            "affordable and fast laundry service for quite some time and LAVO is definitely the one.",
            "They replied to us quickly and courteously. They picked it up the same day and kept me "
            "updated on the status of delivery. The clothes were folded neatly and smelled fresh.",
            "Thank you for the great service. We will definitely avail of your services again.",
        ],
    },
    {
        "initials": "W",
        "name": "Wewel",
        "date": "24 April",
        "paragraphs": ["Thankyou sa good service at sa papromo \U0001F929"],
    },
]

FAQS = [
    (
        "What areas do you cover?",
        "Alabang, Putatan, Muntinlupa, Parkhomes Tunasan, Villa Carolina 1, Tunasan and San Pedro. "
        "We cater to other areas as well — use the coverage checker above, or send us your "
        "complete address and we'll confirm.",
    ),
    (
        "What is the minimum load?",
        "5 kg per pickup. Below that we can still take your items, but the 5 kg minimum rate applies.",
    ),
    (
        "How do I track my laundry?",
        "Every pickup gets a Blue Card number, handed to you when our rider collects. Send it to us on "
        "Messenger or by call and we'll tell you exactly which stage your load is in.",
    ),
    (
        "How long is the turnaround time?",
        "Standard wash, dry and fold is returned within 24 to 48 hours of pickup. Premium Care and "
        "special items such as comforters may take up to 72 hours.",
    ),
    (
        "Do you weigh in front of me?",
        "Yes, on request. Just tell the rider at pickup and we'll weigh your load in front of you.",
    ),
    (
        "What payment methods do you accept?",
        "Cash on delivery, GCash and Maya. Payment is settled when your laundry comes back.",
    ),
]
