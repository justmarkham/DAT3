import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ticker')
args = parser.parse_args()

stock_ticker = args.ticker
base_url = 'http://www.marketwatch.com/investing/stock/'

try:
    r = requests.get(base_url + stock_ticker)
    soup = BeautifulSoup(r.text)
    price = float(soup.find(name='p', attrs={'class':'data bgLast'}).text)
    print price
except:
    print 'not found!'
