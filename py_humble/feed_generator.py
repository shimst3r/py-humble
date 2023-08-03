import html

import pendulum

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
        fe.title(product["tile_short_name"])
        fe.link(href=f"https://humblebundle.com{product['product_url']}")
        fe.content(html.unescape(product["detailed_marketing_blurb"]))
        fe.pubDate(f"{product['start_date|datetime']}Z")
        fe.description(html.unescape(product["short_marketing_blurb"]))

    return fg.rss_str(pretty=True)
