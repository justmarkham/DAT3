'''
CLASS: Model evaluation with scikit-learn
'''

import numpy as np
import matplotlib.pyplot as plt

# read in the iris data
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target


## TRAIN AND TEST ON THE SAME DATA (OVERFITTING)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
knn.score(X, y)


## TEST SET APPROACH

# split data into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.3, random_state=1)

# check test set error for K=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)

# check test set error for K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)

# verify that a different train/test split can result in a different accuracy
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.3, random_state=2)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)


## CROSS-VALIDATION

from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV

# check CV score for K=1
knn = KNeighborsClassifier(n_neighbors=1)
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
scores
np.mean(scores)

# check CV score for K=5
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
scores
np.mean(scores)

# search for an optimal value of K
k_range = range(1, 31)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores.append(np.mean(cross_val_score(knn, X, y, cv=5, scoring='accuracy')))

# plot the K values (x-axis) versus the 5-fold CV score (y-axis)
plt.figure()
plt.plot(k_range, scores)

# automatic grid search for an optimal value of K
knn = KNeighborsClassifier()
k_range = range(1, 31)
param_grid = dict(n_neighbors=k_range)
grid = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)

# check the results of the grid search
grid.grid_scores_
grid_mean_scores = [result[1] for result in grid.grid_scores_]
plt.figure()
plt.plot(k_range, grid_mean_scores)
grid.best_score_
grid.best_params_
grid.best_estimator_


## CONFUSION MATRIX

# generate data from the slides
actual = [1]*100 + [1]*5 + [0]*10 + [0]*50
predicted = [1]*100 + [0]*5 + [1]*10 + [0]*50

# confusion matrix from sklearn
from sklearn import metrics
print metrics.confusion_matrix(actual, predicted)
print metrics.confusion_matrix(actual, predicted, labels=[1, 0]).T

# nicer confusion matrix from nltk
import nltk
print nltk.ConfusionMatrix(actual, predicted)

# try both on KNN predictions
knn = KNeighborsClassifier(n_neighbors=25)
knn.fit(X_train, y_train)
y_preds = knn.predict(X_test)
print metrics.confusion_matrix(y_test, y_preds)
print nltk.metrics.ConfusionMatrix(list(y_test), list(y_preds))

# generate metrics
print metrics.accuracy_score(y_test, y_preds)
print metrics.classification_report(y_test, y_preds)


## ROC CURVE AND AUC

# change iris to a binary classification problem
# setosa=0, versicolor=0, virginica=1
y_binary = np.where(y==2, 1, 0)
y_train_binary = np.where(y_train==2, 1, 0)
y_test_binary = np.where(y_test==2, 1, 0)

# make the problem harder by changing every 5th element to a 1
y_train_binary = [1 if index % 5 == 0 else response for index, response in enumerate(y_train_binary)]
y_test_binary = [1 if index % 5 == 0 else response for index, response in enumerate(y_test_binary)]

# use KNN for binary classification
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train_binary)

# get predictions
y_preds_binary = knn.predict(X_test)
print metrics.confusion_matrix(y_test_binary, y_preds_binary)

# get predicted probabilities
y_probs_binary = knn.predict_proba(X_test)[:, 1]
print metrics.roc_auc_score(y_test_binary, y_probs_binary)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(y_test_binary, y_probs_binary)
plt.figure()
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# redo CV using AUC as the scoring metric
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y_binary, cv=5, scoring='roc_auc')
scores
np.mean(scores)

# redo grid search for optimal K using AUC as the scoring metric
grid = GridSearchCV(knn, param_grid, cv=5, scoring='roc_auc')
grid.fit(X, y_binary)
grid_mean_scores = [result[1] for result in grid.grid_scores_]
plt.figure()
plt.plot(k_range, grid_mean_scores)
grid.best_score_
grid.best_params_
