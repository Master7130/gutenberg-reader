from flask import Flask, jsonify
from scraper import scrape

app = Flask(__name__)


@app.route('/<code>')
def scrapeUrl(code):
    html = scrape(code)
    response = jsonify({'html': str(html)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
