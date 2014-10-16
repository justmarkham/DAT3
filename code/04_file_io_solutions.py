'''
SOLUTIONS: Reading and Writing Files in Python
'''

'''
Exercise 2:
Learn csv.DictReader() and redo all of Exercise 1 using csv.DictReader()

Part 1:
    Read in drinks.csv
    Store the header in a list called 'header'
    Store the data in a list of lists called 'data'
Part 2:
    Isolate the beer_servings column in a list of integers called 'beers'
    Hint: use a list comprehension to do this in one line
Part 3:
    Create separate lists of NA and EU beer servings ('NA_beers', 'EU_beers')
    Hint: use list comprehensions
Part 4:
    Calculate the average NA and EU beer servings ('NA_avg', 'EU_avg') to 2 decimals
'''

import csv

# Part 1 with READER:
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

# Part 1 with DICTREADER:
with open('../data/drinks.csv', 'rU') as f:
    data2 = [row for row in csv.DictReader(f)]

header = data2[0].keys()    # don't rely on the ordering


# Part 2 with READER:
assert(header[1] == 'beer_servings')
beers = [int(row[1]) for row in data]

# Part 2 with DICTREADER:
beers = [int(row['beer_servings']) for row in data2]


# Part 3 with READER:
assert(header[5] == 'continent')
NA_beers = [int(row[1]) for row in data if row[5]=='NA']
EU_beers = [int(row[1]) for row in data if row[5]=='EU']

# Part 3 with DICTREADER:
NA_beers = [int(row['beer_servings']) for row in data2 if row['continent']=='NA']
EU_beers = [int(row['beer_servings']) for row in data2 if row['continent']=='EU']


# Part 4:
NA_avg = round(sum(NA_beers) / float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers) / float(len(EU_beers)), 2)



'''
Exercise 3:
Learn zip() and write some 'nicer code' for Exercise 1 with zip() and csv.reader()
'''

### OPTION A ###

# read with csv.reader()
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

# create a dictionary: headers are keys, positions are values
header_dict = dict(zip(header, range(len(header))))

# isolate beers in a list
beer_col = header_dict['beer_servings']
beers = [int(row[beer_col]) for row in data]

# isolate continents in a list
continent_col = header_dict['continent']
continents = [row[continent_col] for row in data]

# iterate through two lists at once
NA_beers = [beer for beer, continent in zip(beers, continents) if continent=='NA']
EU_beers = [beer for beer, continent in zip(beers, continents) if continent=='EU']


### OPTION B ###

# use zip() to "convert" csv.reader() into csv.DictReader()
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data2 = [dict(zip(header, row)) for row in csv.reader(f)] 
