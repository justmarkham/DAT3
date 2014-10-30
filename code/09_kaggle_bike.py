import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score

# read in files
train = pd.read_csv('../data/kaggle_bike_train.csv', index_col='datetime', parse_dates=True)
test = pd.read_csv('../data/kaggle_bike_test.csv', index_col='datetime', parse_dates=True)

# change weather=4 to weather=3
train.weather = np.where(train.weather==4, 3, train.weather)
test.weather = np.where(test.weather==4, 3, test.weather)

# add new features to train
train['hour'] = train.index.hour
train['daytime'] = np.where((train.hour > 6) & (train.hour < 21), 1, 0)
train['weather2'] = pd.get_dummies(train.weather).loc[:, 2]
train['weather3'] = pd.get_dummies(train.weather).loc[:, 3]

# add same features to test
test['hour'] = test.index.hour
test['daytime'] = np.where((test.hour > 6) & (test.hour < 21), 1, 0)
test['weather2'] = pd.get_dummies(test.weather).loc[:, 2]
test['weather3'] = pd.get_dummies(test.weather).loc[:, 3]

# choose my features
feature_cols = ['holiday', 'workingday', 'temp', 'humidity', 'daytime',
                'weather2', 'weather3']
X_train = train[feature_cols]
X_test = test[feature_cols]

# choose my response
y_train = train['count']

# try a linear model
lm = LinearRegression()
lm.fit(X_train, y_train)
lm.coef_                    # coefficients
lm.predict(X_train)         # predictions on training set
lm.score(X_train, y_train)  # R^2

# compute average RMSE for 5-fold CV
# note: sklearn returns MSE as negative, so negate scores
scores = cross_val_score(lm, X_train, y_train, cv=5, scoring='mean_squared_error')
np.mean(np.sqrt(-scores))

# train on training set, predict on test set
lm = LinearRegression()
lm.fit(X_train, y_train)
y_preds = lm.predict(X_test)

# adjust predictions: replace values less than 1 with 1
y_preds_fixed = np.where(y_preds >= 1, y_preds, 1)

# create submission file
out = pd.DataFrame(y_preds_fixed)
out.index = test.index
out.columns = ['count']
out.to_csv('../data/kaggle_bike_submission.csv')
