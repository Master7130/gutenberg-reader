import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


def scrape(url):
    req = requests.get(
        f'https://www.gutenberg.org/cache/epub/{url}/pg{url}-images.html', headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    for s in soup.select("section"):
        s.extract()

    return soup.find("body")
