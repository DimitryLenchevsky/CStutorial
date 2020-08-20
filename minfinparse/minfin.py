import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://minfin.com.ua/'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

html = get_html(URL)
print(html)