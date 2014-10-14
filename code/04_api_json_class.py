'''
CLASS: Getting data from APIs into Python
'''


'''
Option 1: curl to file, read into Python with json.load()

curl 'http://developer.echonest.com/api/v4/artist/top_hottt?api_key=YOUR_API_KEY&format=json' > echo_nest_top.txt
'''

import json
with open('../data/echo_nest_top.txt', 'rU') as f:
    top = json.load(f)  # dictionary


'''
Option 2: use requests, read into Python with json() method
'''

import requests
r = requests.get('http://developer.echonest.com/api/v4/artist/top_hottt?api_key=YOUR_API_KEY&format=json')
top = r.text    # unicode text string
top = r.json()  # dictionary

# pretty print
from pprint import pprint
pprint(top)

# pull out the artist data
artists = top['response']['artists']    # list of 15 dictionaries

# reformat data into a table structure
artists_header = artists[0].keys()                      # list of 2 strings
artists_data = [artist.values() for artist in artists]  # list of 15 lists


'''
Option 3: use Pyechonest (API wrapper)
'''

from pyechonest import config
config.ECHO_NEST_API_KEY='YOUR_API_KEY'

# get top hottt artists
from pyechonest import artist
for hottt_artist in artist.top_hottt():
    print hottt_artist.name, hottt_artist.hotttnesss

# get blogs about weezer    
weezer_results = artist.search(name='weezer')
weezer = weezer_results[0]
weezer_blogs = weezer.blogs
[blog.get('url') for blog in weezer_blogs]
