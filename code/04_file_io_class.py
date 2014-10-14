'''
CLASS: Reading and Writing Files in Python
'''


'''
Reading generic text files
Note: 'rU' mode (read universal) converts different line endings into '\n'
'''

# read the whole file at once, return a single string
f = open('../data/drinks.csv', 'rU')
f.read()        # one big string including newlines
f.read()        # empty string
f.close()

# read the whole file at once, return a list of lines
f = open('../data/drinks.csv', 'rU')
f.readlines()   # one list, each line is one string
f.readlines()   # empty list
f.close()

# read one line at a time (entire file does not have to fit into memory)
f = open('../data/drinks.csv', 'rU')
f.readline()    # one string per line (including newlines)
f.readline()    # next line
f.close()

# reminder on list comprehensions
my_list = []
for letter in 'word':
    my_list.append(letter)

[letter for letter in 'word']

# use list comprehension to duplicate readlines without reading entire file at once
f = open('../data/drinks.csv', 'rU')
[row for row in f]
f.close()


'''
Reading CSV files with csv module
'''

import csv

# csv.reader returns a list and splits into elements by comma
f = open('../data/drinks.csv', 'rU')
for row in csv.reader(f):
    print row
f.close()

# use list comprehension to create a list of lists instead
f = open('../data/drinks.csv', 'rU')
[row for row in csv.reader(f)]
f.close()

# use a context manager to automatically close your file
with open('../data/drinks.csv', 'rU') as f:
    [row for row in csv.reader(f)]

# use next to grab the next row
with open('../data/drinks.csv', 'rU') as f:
    csv.reader(f).next()
    [row for row in csv.reader(f)]


'''
Exercise 1:

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

# Part 1:
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

# Part 2:
assert(header[1] == 'beer_servings')
beers = [int(row[1]) for row in data]

# Part 3:
assert(header[5] == 'continent')
NA_beers = [int(row[1]) for row in data if row[5]=='NA']
EU_beers = [int(row[1]) for row in data if row[5]=='EU']

# Part 4:
NA_avg = round(sum(NA_beers) / float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers) / float(len(EU_beers)), 2)


'''
Writing generic text files
Note: 'wb' mode (write binary) seems to be the recommended option
'''

# write a string to a file
with open('nums.txt', 'wb') as f:
    for num in range(5):
        f.write(str(num) + '\n')

# append an existing file
with open('nums.txt', 'ab') as f:
    for num in range(5, 10):
        f.write(str(num) + '\n')


'''
Writing CSV files
'''

# write a CSV file with two columns ('continent' and 'avg_beer') and two rows with the values
output = [['continent', 'avg_beer'], ['NA', NA_avg], ['EU', EU_avg]]
with open('avg_beer.csv', 'wb') as f:
    w = csv.writer(f)
    for row in output:
        w.writerow(row)

# use writerows to do this in one line
with open('avg_beer.csv', 'wb') as f:
    csv.writer(f).writerows(output)


'''
Exercise 2 (homework):
Learn csv.DictReader() and redo all of Exercise 1 using csv.DictReader()

Exercise 3 (optional homework):
Learn zip() and write some 'nicer code' for Exercise 1 with zip() and csv.reader()
'''
