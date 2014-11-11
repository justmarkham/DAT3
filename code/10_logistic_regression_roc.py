'''
CLASS: Logistic Regression, ROC, AUC
'''

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# Read in Default.csv and convert all data to numeric
d = pd.read_csv('../data/Default.csv')
d.student = np.where(d.student == 'Yes', 1, 0)

# Split the data into train and test sets
train, test = train_test_split(d, test_size=0.3, random_state=1)

# Convert them back into dataframes
train = pd.DataFrame(data=train, columns=d.columns)
test = pd.DataFrame(data=test, columns=d.columns)

# Run a logistic regression on the balance variable
balance = smf.logit('default ~ balance', data=train).fit()

# Create predictions using the balance model on the test set
test['pred'] = balance.predict(test)
test['pred_class'] = np.where(test['pred'] >= 0.5, 1, 0)

# Accuracy
sum(test.pred_class == test.default) / float(len(test))

# Specificity: For those who didn't default, how many did it predict correctly?
test_nd = test[test.default == 0]
sum(test_nd.pred_class == 0) / float(len(test_nd))

# Sensitivity: For those who did default, how many did it predict correctly? 
test_d = test[test.default == 1]
sum(test_d.pred_class == 1) / float(len(test_d))

# Null accuracy (by predicting majority class)
1 - sum(d.default) / float(len(d))


# generate metrics
from sklearn import metrics
print metrics.accuracy_score(test.default, test.pred_class)
print metrics.confusion_matrix(test.default, test.pred_class)
print metrics.roc_auc_score(test.default, test.pred)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(test.default, test.pred)
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# FYI: you can use AUC as your scoring parameter with sklearn
# scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
# grid = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')
