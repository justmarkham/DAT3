'''
CLASS: Web Scraping in Python
'''


import requests
from bs4 import BeautifulSoup

# read in a page and convert requests text into 'soup' object
r = requests.get('http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228')
soup = BeautifulSoup(r.text)

# find the section of relevant links and then parse into iterable rows
links_section = soup.find(name='dl', attrs={'class':'boccat'})
link_rows = links_section.find_all(name='dd')

# create a list of category links
category_links = ['http://chicagoreader.com' + row.a['href'] for row in link_rows]

# function that takes a link and returns a dictionary of info about that page
def get_category_winners(category_link):
    r = requests.get(category_link)
    soup = BeautifulSoup(r.text)
    return {"category":     soup.find(name='h1', attrs={'class':'headline'}).string,
            "url":          category_link,
            "winners":      [h2.string for h2 in soup.find_all(name='h2', attrs={'class':'boc1'})],
            "runners_up":   [h2.string for h2 in soup.find_all(name='h2', attrs={'class':'boc2'})]
            }

# test function by passing in first link
get_category_winners(category_links[0])

# create list of dictionaries for the first five links
from time import sleep
winners = []
for category_link in category_links[0:5]:
    winner = get_category_winners(category_link)
    winners.append(winner)
    sleep(1)

from pprint import pprint
pprint(winners)
