import requests
from bs4 import BeautifulSoup
import pickle

r = requests.get('https://github.com/justmarkham/DAT3')
soup = BeautifulSoup(r.text)
links = [link.get('href') for link in soup.find_all('a')]

with open('links_list.pkl', 'wb') as f:
    pickle.dump(links, f)
