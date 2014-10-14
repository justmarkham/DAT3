'''
CLASS: Pandas for Data Analysis in Python

Adapted from:
    http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

Files used:
    ../data/u.user
    ../data/u.data
    ../data/u.item

File source:
    main page - http://grouplens.org/datasets/movielens/
    zip file - http://files.grouplens.org/datasets/movielens/ml-100k.zip
    data dictionary - http://files.grouplens.org/datasets/movielens/ml-100k-README.txt
'''

# imports
import pandas as pd
import numpy as np


'''
Basics: reading files, selecting, filtering, sorting, summarizing
'''

# read 'u.user' into 'users'
u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('../data/u.user', header=None, names=u_cols, sep='|',
                      index_col='user_id')

# examine the users data
users
users.head(10)
users.tail()
users.describe()        # method
users.index             # attribute
users.columns
users.dtypes

# DataFrame vs Series, selecting a column
type(users)
users['gender']
users.gender            # equivalent
type(users.gender)

# summarizing a non-numeric column
users.gender.describe()
users.gender.value_counts()

# selecting multiple columns
users[['age', 'gender']]
my_cols = ['age', 'gender']
users[my_cols]
type(users[my_cols])

# loc: filter rows by label, and select columns by label
users.loc[1]                        # row with label 1
users.loc[1:3]                      # rows with labels 1 through 3
users.loc[1:3, 'age':'occupation']  # rows 1-3, columns 'age' through 'occupation'
users.loc['age':'occupation']       # does not work
users.loc[:, 'age':'occupation']    # all rows, columns 'age' through 'occupation'

# iloc: filter rows by position, and select columns by position
users.iloc[0]                       # row with 0th position (first row)
users.iloc[0:3]                     # rows with positions 0 through 2 (not 3)
users.iloc[0:3, 0:3]                # rows and columns with positions 0 through 2
users.iloc[:, 0:3]                  # all rows, columns with positions 0 through 2

# ix: for mixing label selection and position selection
users.ix[0:3, 'age':'occupation']   # filter rows by position, select columns by label
users.ix[1, 'age':'occupation']     # danger! '1' is interpreted as a label

# logical filtering
users[users.age < 20]
users.age[users.age < 20]
users[['age', 'occupation']][users.age < 20]
users[(users.age < 20) & (users.gender=='M')]

# sorting
users.age.order()                           # only works for a Series
users.sort_index()                          # sort rows by label
users.sort_index(ascending=False)
users.sort_index(by='age')                  # sort rows by specific column
users.sort_index(by=['occupation', 'age'])  # sort by multiple columns


'''
Exercise: Variation of the 'drinks' exercise from last class, with Pandas!

- Read drinks.csv and store it in a DataFrame called 'drinks' (use the default index)
- Count the number of 'continent' values and make sure it looks correct
- Calculate the average 'beer_servings' for the entire dataset
- Calculate the average 'beer servings' for Europe
- Determine which country has the maximum value for 'beer_servings'
- Determine which 10 countries have the highest 'total_litres_of_pure_alcohol'
'''

drinks = pd.read_csv('../data/drinks.csv', na_filter=False)
drinks.continent.value_counts()
drinks.beer_servings.mean()
drinks.beer_servings[drinks.continent=='EU'].mean()
drinks.country[drinks.beer_servings==drinks.beer_servings.max()]
drinks.sort_index(by='total_litres_of_pure_alcohol').tail(10)


'''
Adding and Removing Columns
'''

# adding a new column as a function of existing columns
drinks['total_servings'] = drinks.beer_servings + drinks.spirit_servings + drinks.wine_servings
drinks['total_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].sum(axis=1)

# deleting a column
del drinks['total_servings']


'''
Handling Missing Values
'''

# read in data with missing values
drinks = pd.read_csv('../data/drinks.csv')

# set more values to NaN
drinks.loc[192, 'beer_servings':'wine_servings'] = np.nan

# look for missing values
drinks.describe()                           # excludes missing values
drinks.continent.value_counts()             # excludes missing values
drinks.continent.value_counts(dropna=False) # includes missing values (new in pandas 0.14.1)

# create a Series of logicals
drinks.continent.isnull()   # True if NaN, False otherwise
drinks.continent.notnull()  # False if NaN, True otherwise

# drop missing values
drinks.dropna()             # drop a row if it is missing any values
drinks.dropna(how='all')    # drop a row only if all values are missing

# fill in missing values
drinks.continent.fillna(value='NA', inplace=True)
drinks.fillna(drinks.mean())


'''
More File Reading and File Writing
'''

# read a CSV into a list of lists, then convert it to a DataFrame
import csv
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]
drinks = pd.DataFrame(data, columns=header)     # no automatic handling of missing values

# write a DataFrame out to a CSV
drinks.to_csv('../data/drinks_updated.csv')     # index is created as first column
drinks.to_csv('../data/drinks_updated.csv', index=False)


'''
Split-Apply-Combine
'''

# for each occupation, calculate mean age
users.groupby('occupation').age.mean()

# for each occupation, count number of occurrences
users.groupby('occupation').occupation.count()
users.occupation.value_counts()

# for each occupation, calculate the min age, max age, and age range
users.groupby('occupation').age.min()
users.groupby('occupation').age.max()
users.groupby('occupation').age.apply(lambda x: x.max()-x.min())


'''
Joining Data
'''

# read 'u.data' into 'ratings'
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_table('../data/u.data', header=None, names=r_cols, sep='\t')

# read 'u.item' into 'movies'
m_cols = ['movie_id', 'title']
movies = pd.read_table('../data/u.item', header=None, names=m_cols, sep='|',
                       usecols=[0,1])

# merge 'movies' and 'ratings' (inner join on 'movie_id')
movies.head()
ratings.head()
movie_ratings = pd.merge(movies, ratings)
movie_ratings.head()


'''
Further Exploration
'''

# for each movie, count number of ratings
movie_ratings.title.value_counts()

# for each movie, calculate mean rating
movie_ratings.groupby('title').rating.mean().order(ascending=False)

# for each movie, count number of ratings and calculate mean rating
movie_ratings.groupby('title').rating.count()
movie_ratings.groupby('title').rating.mean()
movie_stats = movie_ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()  # hierarchical index

# limit results to movies with more than 100 ratings
movie_stats[movie_stats.rating.size > 100].sort_index(by=('rating', 'mean'))
