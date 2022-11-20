from flask import Flask, jsonify
from scraper import scrape

app = Flask(__name__)


@app.route('/<url>')
def scrapeUrl(url):
    html = scrape(url)
    # return f'{html}'
    response = jsonify({'html': str(html)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
