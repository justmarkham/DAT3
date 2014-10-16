'''
Pandas Reference Guide

Source:
    http://fonnesbeck.github.io/Bios366/lectures.html

Files used:
    ../data/microbiome.csv
    ../data/microbiome_missing.csv
    ../data/baseball.csv
'''

import pandas as pd
import numpy as np


### SERIES ###

# create Series with default index (0, 1, 2, 3)
counts = pd.Series([632, 1638, 569, 115])
counts.values   # numpy array
counts.index    # index object

# create Series and specify index
bacteria = pd.Series([632, 1638, 569, 115], 
    index=['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes'])

# filter a Series
bacteria['Actinobacteria']  # by label
bacteria[2]                 # by position
bacteria[[name.endswith('bacteria') for name in bacteria.index]]
bacteria[bacteria > 1000]

# give name to index and to values
bacteria.index.name = 'phylum'
bacteria.name = 'counts'

# vectorized operations on a Series
np.log(bacteria)            # return a Series
np.log(bacteria.values)     # return an array

# create Series from a dict (creates in key-sorted order)
bacteria_dict = {'Firmicutes': 632, 'Proteobacteria': 1638,
                 'Actinobacteria': 569, 'Bacteroidetes': 115}
pd.Series(bacteria_dict)

# pass a custom index to Series
# indices without values will be treated as missing (NaN)
bacteria2 = pd.Series(bacteria_dict,
    index=['Cyanobacteria','Firmicutes','Proteobacteria','Actinobacteria'])
bacteria2.isnull()

# labels are used to align data when used in operations with other Series
# note that result is NaN if either Series has NaN for that index
bacteria + bacteria2


### DATAFRAME ###

# create DataFrame from dictionary of lists
data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
    'patient':[1, 1, 1, 1, 2, 2, 2, 2],
    'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes',
              'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})

# DataFrame has second index representing the columns
data.columns
data.dtypes

# select column from DataFrame
data.value
data['value']       # returns a Series
data[['value']]     # returns a DataFrame

# select column, then filter by index (or "label")
data.value[3]
data.loc[3, 'value']    # less ambiguous

# select column, then filter by position
data.value[0:2]
data.iloc[0:2, 2]       # less ambiguous, but requires column position

# filter rows by boolean
data[data.value>1000]

# Series returned when selecting columns is a view by default, not a copy
vals = data.value           # view
vals = data.value.copy()    # copy

# create DataFrame columns by assignment
data['year'] = 2013
data['month'] = ['Jan'] * len(data)

# remove DataFrame columns
del data['month']

# extract data as ndarray
# dtype of array is "object" due to mixed data types
data.values


### IMPORTING DATA ###

# read from CSV
mb = pd.read_csv('../data/microbiome.csv')

# use header=0 to overwrite column names, or header=None to add column names
mb = pd.read_csv('../data/microbiome.csv', header=0, names = ['a','b','c','d','e'])

# limit which rows are read in
pd.read_csv('../data/microbiome.csv', skiprows=[3,4,6])
pd.read_csv('../data/microbiome.csv', nrows=4)

# read_table is a more general function
# can use regular expression to define variable amount of whitespace
mb = pd.read_table('../data/microbiome.csv', sep='\s+')

# use chunksize to return iterable object 
data_chunks = pd.read_csv('../data/microbiome.csv', chunksize=15)
mean_tissue = {chunk.Taxon[0]: chunk.Tissue.mean() for chunk in data_chunks}

# missing data, NA, and NULL will automatically be replaced with NaN
# specify additional symbols with na_values
pd.read_csv('../data/microbiome_missing.csv')
pd.isnull(pd.read_csv('../data/microbiome_missing.csv'))
mb2 = pd.read_csv('../data/microbiome_missing.csv', na_values=['?', -99999])


### MISSING VALUES ###

# drop any rows with missing values
mb2.dropna()

# only drop a row if every field is a missing value
mb2.dropna(how='all')

# fill missing values with specific values
mb2.fillna({'Tissue':500, 'Stool':1000})


### INDEXING ###

# specify which column contains an index
baseball = pd.read_csv('../data/baseball.csv', index_col='id')

# can also set index after reading it in
baseball = pd.read_csv('../data/baseball.csv')
baseball.set_index('id', inplace=True)

# create our own index 
player_id = baseball.player + baseball.year.astype(str)
baseball_new = baseball.copy()
baseball_new.index = player_id

# our new index is not unique (which is not illegal)
# indexing by label will return multiple values for some labels
baseball_new.index.is_unique
pd.Series(baseball_new.index).value_counts()
baseball_new.ix['wickmbo012007']

# reindex to maniulpate the data indices in a DataFrame
baseball.reindex(baseball.index[::-1])


### SLICING ###

# select columns
baseball_new[['h','ab']]
baseball_new[baseball_new.ab>500]

# select column, then filter rows by index
baseball_new.h['womacto012006']
baseball_new.h[['womacto012006', 'schilcu012006']]
baseball_new.h['womacto012006':'myersmi012006']

# select column, then filter rows by position (works because index is not an integer)
baseball_new.h[0]
baseball_new.h[0:3]

# alternatively: filter rows then select columns
baseball_new.ix['womacto012006', 'h']
baseball_new.ix['gonzalu012006', ['h','X2b', 'X3b', 'hr']]
baseball_new.ix[['gonzalu012006','finlest012006'], 5:8]

# remove rows or columns
baseball.drop([89525, 89526])
baseball.drop(['ibb', 'hbp'], axis=1)


### APPLYING FUNCTIONS ###

# apply
stats = baseball[['h','X2b', 'X3b', 'hr']]
stats.apply(np.median)      # median of each column
stats.apply(np.sum, axis=1) # sum of each row
stats.apply(lambda x: x.max() - x.min())

# built-in functions
baseball.mean()         # ignores NaN by defalut
mb2.mean(skipna=False)
baseball.describe()
baseball.player.describe()  # works on non-numeric data also
baseball.head()
baseball.tail()


### SORTING AND ORDERING ###

# sorting by index
baseball_new.sort_index()
baseball_new.sort_index(ascending=False)
baseball_new.sort_index(axis=1)

# sorting by value
baseball.hr.order(ascending=False)
baseball.sort_index(ascending=[False,True], by=['sb','cs'])

# rank each value relative to others in the Series
# high rank means high value
baseball.hr.rank()
baseball.rank()


### HIERARCHICAL INDEXING ###

# specify multiple columns to create hierarchical index
mb = pd.read_csv('../data/microbiome.csv', index_col=['Taxon','Patient'])

# use tuple to subset
mb.ix[('Other',1)]

# subset based on partial index
mb.ix['Other']


### WRITING TO FILES ###

# write to CSV, useful arguments are sep, na_rep, index, header
mb.to_csv('mb.csv')

# write to disk in binary format
baseball.to_pickle('baseball_pickle')
pd.read_pickle('baseball_pickle')
