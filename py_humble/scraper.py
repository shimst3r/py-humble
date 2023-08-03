import requests


def scrape(url):
    r = requests.get(url)

    return r.text
