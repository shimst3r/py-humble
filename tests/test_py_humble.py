import pytest

from py_humble import feed_generator, parser, scraper


@pytest.mark.parametrize("category", ("books", "games", "software"))
def test_scraper(category):
    url = f"https://www.humblebundle.com/{category}"
    html = scraper.scrape(url)

    assert type(html) is str


@pytest.mark.parametrize("category", ("books", "games", "software"))
def test_parser(category):
    url = f"https://www.humblebundle.com/{category}"
    html = scraper.scrape(url)
    products = parser.parse(html, category)

    assert type(products) is list
    assert products is not []


@pytest.mark.parametrize("category", ("books", "games", "software"))
def test_generator(category):
    url = f"https://www.humblebundle.com/{category}"
    html = scraper.scrape(url)
    products = parser.parse(html, category)
    rss = feed_generator.generate(category, products)

    assert type(rss) is bytes
    assert rss != b""
