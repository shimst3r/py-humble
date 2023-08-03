import json

import pendulum
from bs4 import BeautifulSoup as bs


def parse(html, category):
    parser = bs(html, "html.parser")
    node = parser.find("script", {"id": "landingPage-json-data"})
    data = json.loads(list(node.children)[0])["data"]
    products = sorted(
        data[category]["mosaic"][0]["products"],
        key=lambda p: pendulum.parse(p["start_date|datetime"]),
    )

    return products
