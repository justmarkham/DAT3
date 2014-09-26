# pandas tutorial

# adapted from:
#   http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

# files used:
#   ../data/u.user
#   ../data/u.data
#   ../data/u.item
# source:
#   main page - http://grouplens.org/datasets/movielens/
#   zip file - http://files.grouplens.org/datasets/movielens/ml-100k.zip
#   data dictionary - http://files.grouplens.org/datasets/movielens/ml-100k-README.txt


# imports
import pandas as pd
import numpy as np

# read 'u.user' into 'users'
u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('../data/u.user', header=None, names=u_cols, sep='|',
                      index_col='user_id')

# examine the users data
users
users.head(10)
users.tail()
users.describe()    # method
users.dtypes        # attribute

# DataFrame vs Series, selecting a column
type(users)
users['gender']
type(users['gender'])
users.gender

# selecting multiple columns
users[['age', 'gender']]
my_cols = ['age', 'gender']
users[my_cols]
type(users[my_cols])

# summarizing a non-numeric column
users.gender.describe()
users.gender.value_counts()

# filtering rows by index
users.ix[1]
users.ix[1:3]

# logical filtering
users[users.age < 20]
users.age[users.age < 20]
users[(users.age < 20) & (users.gender=='M')]

# sorting
users.age.order()
users.sort_index()
users.sort_index(by='age')
users.sort_index(by=['occupation','age'])

# split-apply-combine
# diagram: http://i.imgur.com/yjNkiwL.png

# for each occupation, calculate mean age
users.groupby('occupation').age.mean()

# for each occupation, count number of occurrences
users.groupby('occupation').occupation.count()
users.occupation.value_counts()

# for each occupation, calculate the min age, max age, and age range
users.groupby('occupation').age.min()
users.groupby('occupation').age.max()
users.groupby('occupation').age.apply(lambda x: x.max()-x.min())

# read 'u.data' into 'ratings'
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_table('../data/u.data', header=None, names=r_cols, sep='\t')

# read 'u.item' into 'movies'
m_cols = ['movie_id', 'title']
movies = pd.read_table('../data/u.item', header=None, names=m_cols, sep='|',
                       usecols=[0,1])

# merge 'movies' and 'ratings' (inner join on 'movie_id')
movie_ratings = pd.merge(movies, ratings)

# for each movie, count number of ratings
movie_ratings.title.value_counts()

# for each movie, calculate mean rating
movie_ratings.groupby('title').rating.mean().order(ascending=False)

# for each movie, count number of ratings and calculate mean rating
movie_stats = movie_ratings.groupby('title').agg({'rating': [np.size, np.mean]})

# limit results to movies with more than 100 ratings
movie_stats[movie_stats.rating.size > 100].sort_index(by=('rating', 'mean'))
