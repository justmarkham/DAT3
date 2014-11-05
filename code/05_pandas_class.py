'''
CLASS: Pandas for Data Analysis in Python

Adapted from:
    http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/

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
import matplotlib.pyplot as plt


'''
Basics: Reading Files, Selecting, Filtering, Sorting, Summarizing
'''

# read 'u.user' into 'users'
u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('../data/u.user', header=None, names=u_cols, sep='|',
                      index_col='user_id')

# examine the users data
users
users.head(10)
users.tail()
users.describe()        # describe any numeric columns
users.index             # "the index" (aka "the labels")
users.columns           # column names (which is "an index")
users.dtypes            # data types of each column
users.values            # underlying numpy array
users.info()            # concise summary

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

# loc: filter rows by LABEL, and select columns by LABEL
users.loc[1]                        # row with label 1
users.loc[1:3]                      # rows with labels 1 through 3
users.loc[1:3, 'age':'occupation']  # rows 1-3, columns 'age' through 'occupation'
users.loc[:, 'age':'occupation']    # all rows, columns 'age' through 'occupation'
users.loc[[1,3], ['age','gender']]  # rows 1 and 3, columns 'age' and 'gender'

# iloc: filter rows by POSITION, and select columns by POSITION
users.iloc[0]                       # row with 0th position (first row)
users.iloc[0:3]                     # rows with positions 0 through 2 (not 3)
users.iloc[0:3, 0:3]                # rows and columns with positions 0 through 2
users.iloc[:, 0:3]                  # all rows, columns with positions 0 through 2
users.iloc[[0,2], [0,1]]            # 1st and 3rd row, 1st and 2nd column

# mixing: select columns by LABEL, then filter rows by POSITION
users.age[0:3]
users[['age', 'gender', 'occupation']][0:3]

# logical filtering
users[users.age < 20]
users.age[users.age < 20]
users[['age', 'occupation']][users.age < 20]
users[(users.age < 20) & (users.gender=='M')]
users[users.occupation.isin(['doctor','lawyer'])]

# sorting
users.age.order()                           # only works for a Series
users.sort_index()                          # sort rows by label
users.sort_index(ascending=False)
users.sort_index(by='age')                  # sort rows by specific column
users.sort_index(by=['occupation', 'age'])  # sort by multiple columns

# detecting duplicate rows
users.duplicated()                                  # Series of logicals
users.duplicated().sum()                            # count of duplicates
users[users.duplicated()]                           # only show duplicates
users[users.duplicated()==False]                    # only show unique rows
users.duplicated(['age','gender','zip_code']).sum() # columns for identifying duplicates


'''
Exercise: Variation of the 'drinks' exercise from last class, with Pandas!

- Read drinks.csv and store it in a DataFrame called 'drinks' (use the default index)
- Count the number of 'continent' values and make sure it looks correct
- Calculate the average 'beer_servings' for the entire dataset
- Calculate the average 'beer_servings' for Europe
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
Adding, Renaming, and Removing Columns
'''

# add a new column as a function of existing columns
drinks['total_servings'] = drinks.beer_servings + drinks.spirit_servings + drinks.wine_servings
drinks.head()

# alternative method: default is column sums, 'axis=1' does row sums
drinks['total_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].sum(axis=1)

# rename a column
drinks.rename(columns={'total_litres_of_pure_alcohol':'pure_alcohol'}, inplace=True)

# hide a column (temporarily)
drinks.drop(['total_servings'], axis=1)
drinks[drinks.columns[:-1]]

# delete a column (permanently)
del drinks['total_servings']


'''
Handling Missing Values
'''

# read in data with missing values
drinks = pd.read_csv('../data/drinks.csv')

# set more values to NaN
drinks.loc[192, 'beer_servings':'wine_servings'] = np.nan

# missing values are often just excluded
drinks.describe()                           # excludes missing values
drinks.continent.value_counts()             # excludes missing values
drinks.continent.value_counts(dropna=False) # includes missing values (new in pandas 0.14.1)

# find missing values in a Series
drinks.continent.isnull()       # True if NaN, False otherwise
drinks.continent.notnull()      # False if NaN, True otherwise
drinks.continent.isnull().sum() # count the missing values

# find missing values in a DataFrame
drinks.isnull()
drinks.isnull().sum()

# drop missing values
drinks.dropna()             # drop a row if ANY values are missing
drinks.dropna(how='all')    # drop a row only if ALL values are missing

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

# for each occupation, count number of occurrences (excluding NaN)
users.groupby('occupation').occupation.count()
users.occupation.value_counts()

# for each occupation, calculate the min age, max age, and age range
users.groupby('occupation').age.min()
users.groupby('occupation').age.max()
users.groupby('occupation').age.apply(lambda x: x.max() - x.min())

# for each occupation/gender combination, calculate mean age
users.groupby(['occupation','gender']).age.mean()
users.groupby(['gender','occupation']).age.mean()


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


'''
Plotting
'''

# bar plot of number of countries in each continent
drinks.continent.value_counts().plot(kind='bar', title='Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.show()

# bar plot of average number of beer servings (per adult per year) by continent
drinks.groupby('continent').beer_servings.mean().plot(kind='bar')

# histogram of beer servings
drinks.beer_servings.hist(bins=20)

# grouped histogram of beer servings
drinks.beer_servings.hist(by=drinks.continent, sharex=True)

# density plot of beer servings
drinks.beer_servings.plot(kind='density', xlim=(0,500))

# boxplot of beer servings by continent
drinks.boxplot(column='beer_servings', by='continent')

# scatterplot of beer servings versus wine servings
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', alpha=0.3)

# same scatterplot, except all European countries are colored red
colors = np.where(drinks.continent=='EU', 'r', 'b')
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', c=colors)
