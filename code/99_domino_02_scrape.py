import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/justmarkham/DAT3')
soup = BeautifulSoup(r.text)
links = [link.get('href') for link in soup.find_all('a')]
print links
