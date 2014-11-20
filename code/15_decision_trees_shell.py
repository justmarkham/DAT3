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
d= pd.read_csv('titanic.csv')

# Take a  selection of the variables
d = d[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch']]

# Check variable types

# Convert all variables to numeric

# Split data into training and test sets

# There is an error. Why?

# Determine the missing values per column of data

# Fill missing values with the mean value

# Now, split the data into training and test sets

# Create a decision tree classifier instance called "clf"

# Fit the decision tree classider

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


# Predict what will happen for 1st class female, age 5 with 3 siblings/parents

# Predict what will happen for 3rd class man, age 50 with 3 siblings/parents/children

# Which features are the most important?

# Make class predictions

# Calculate accuracy for test and train sets


# Make predictions on the test set using predict_proba

# Calculate the AUC metric


'''
FINE-TUNING THE TREE
'''
# Modified from Kevin's lecture on model evaluation
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV

y = d['survived'].values
X = d[['pclass', 'sex', 'age', 'sibsp', 'parch']].values

# check CV score for max depth= 3 (use the roc_auc metric)

# check CV score for max depth= 10

# Conduct a grid search for the best tree depth

# Check out the scores of the grid search



# Plot the results of the grid search


# Now let's plot the best tree (best)

with open("titanic_best_2.dot", 'w') as f:
    f = tree.export_graphviz(best, out_file=f, feature_names=features, close=True)