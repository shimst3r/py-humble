import html

import pendulum
import requests
from feedgen.feed import FeedGenerator


def generate(category, products):
    fg = FeedGenerator()
    fg.id(f"https://shimst3r.xyz/py-humble/{category}")
    fg.title(f"Py Humble {category}".title())
    fg.author({"name": "Nils Müller", "email": "shimst3r+pyhumble@gmail.com"})
    fg.link(href=f"https://shimst3r.xyz/py-humble/{category}", rel="self")
    fg.subtitle(f"Awesome RSS Feeds about HumbleBundle {category.title()} bundles!")
    fg.language("en")
    fg.pubDate(pendulum.now("Europe/Berlin"))

    for product in products:
        fe = fg.add_entry()
        _set_image(fe, product)
        _set_metadata(fe, product)

    return fg.rss_str(pretty=True)


def _set_image(entry, product):
    r = requests.head(product["high_res_tile_image"])
    if r.status_code == 200:
        url = product["high_res_tile_image"]
        length = r.headers["content-length"]
        type = r.headers["content-type"]
        entry.enclosure(url=url, length=length, type=type)


def _set_metadata(entry, product) -> None:
    entry.title(product["tile_short_name"])
    entry.link(href=f"https://humblebundle.com{product['product_url']}")
    entry.content(html.unescape(product["detailed_marketing_blurb"]))
    entry.pubDate(f"{product['start_date|datetime']}Z")
    entry.description(html.unescape(product["short_marketing_blurb"]))
