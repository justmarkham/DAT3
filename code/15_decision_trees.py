'''
CART
'''
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Read in the data
titanic = pd.read_csv('titanic.csv')

# Takea  selection of the variables
d = titanic[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch']]

# Check variable types
d.dtypes

# Convert all variables to numeric
d.sex = np.where(d.sex == 'male', 1, 0)

# Split data into training and test sets
train, test = train_test_split(d,test_size=0.3, random_state=1)

# There is an error. Why?

# Determine the missing values per column of data
d.isnull().sum()

# Fill missing values with the mean value
d.age = d.age.fillna(d.age.mean())

# Now, split the data into training and test sets
train, test = train_test_split(d,test_size=0.3, random_state=1)

# Create a decision tree classifier instance
clf = tree.DecisionTreeClassifier(random_state=1)

# Fit the decision tree classider
clf.fit(train[:,1:], train[:,0])

# Create a feature vector
features = d.columns.values[1:]

# Create a dot file
with open("titanic.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f, feature_names=features, close=True)

'''
INSTRUCTIONS FOR USING GRAPHVIZ TO VISUALIZE THE TREE DIAGRAM
1) download graphviz
    http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-2.38.msi

2) add the file location to your environment variables

    For PC users: 
    Right click on Computer -> Advanced system settings -> Environment 
    Variables -> Under system variable, edit Path -> Copy and paste the folder
    location where \Graphviz is stored with no spaces: 
    'C:\Program Files (x86)\Graphviz2.30\bin;'

3) You might need to restart your computer

4) convert the dot file to a pdf 
    
    run the following from the command line interface in the same 
    directory as your dot file
    dot -Tpdf titanic.dot -o titanic.pdf
'''

# How to interpret the diagram?
clf.classes_ # First means survived, second means died

# Predict what will happen for 1st class woman
features
clf.predict([1, 0, 5, 3, 3])

# Predict what will happen for a 3rd class man
clf.predict([3, 1, 50, 3, 3])

# Which features are the most important?
imp = pd.DataFrame(clf.feature_importances_.reshape(1,5), columns=features)

# Make predictions
preds_train = clf.predict(train[:,1:])
preds = clf.predict(test[:,1:])

# Calculate accuracy
metrics.accuracy_score(train[:,0], preds_train)
metrics.accuracy_score(test[:,0], preds)

# Confusion matrix
pd.crosstab(test[:,0], preds, rownames=['actual'], colnames=['predicted'])

# Make predictions on the test set using predict_proba
probs = clf.predict_proba(test[:,1:])[:,1]

# Calculate the AUC metric
metrics.roc_auc_score(test[:,0], probs)


'''
FINE-TUNING THE TREE
'''
# Modified from Kevin's lecture on model evaluation
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV

y = d['survived'].values
X = d[['pclass', 'sex', 'age', 'sibsp', 'parch']].values

# check CV score for max depth= 3
clf = tree.DecisionTreeClassifier(max_depth=3)
scores = cross_val_score(clf, X, y, cv=5, scoring='roc_auc')
scores
np.mean(scores)

# check CV score for max depth= 10
clf = tree.DecisionTreeClassifier(max_depth=10)
scores = cross_val_score(clf, X, y, cv=5, scoring='roc_auc')
scores
np.mean(scores)

# Conduct a grid search for the best tree depth
clf = tree.DecisionTreeClassifier(random_state=1, min_samples_leaf=20)
depth_range = range(1, 20)
param_grid = dict(max_depth=depth_range)
grid = GridSearchCV(clf, param_grid, cv=5, scoring='roc_auc')
grid.fit(X, y)

# Check out the scores of the grid search
grid_mean_scores = [result[1] for result in grid.grid_scores_]

# Plot the results of the grid search
plt.figure()
plt.plot(depth_range, grid_mean_scores)
plt.hold(True)
plt.plot(grid.best_params_['max_depth'], grid.best_score_, 'ro', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')
plt.grid(True)
# Now let's plot the best tree

best = grid.best_estimator_

with open("titanic_best.dot", 'w') as f:
    f = tree.export_graphviz(best, out_file=f, feature_names=features, close=True)