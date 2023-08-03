import sys

from py_humble.feed_generator import generate
from py_humble.parser import parse
from py_humble.scraper import scrape


def main():
    for category in ("books", "games", "software"):
        html = scrape(f"https://www.humblebundle.com/{category}")
        products = parse(html, category)
        rss = generate(category, products)

        with open(f"./docs/{category}.rss", "w", encoding="utf8") as file:
            file.write(rss.decode("utf8"))


if __name__ == "__main__":
    sys.exit(main())
