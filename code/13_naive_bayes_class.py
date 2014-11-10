'''
CLASS: Naive Bayes spam classifier using sklearn

Files used:
    ../data/ham/
    ../data/spam/

File source:
    http://spamassassin.apache.org/publiccorpus/
    300 ham emails from 20021010_easy_ham.tar.bz2
    300 spam emails from 20021010_spam.tar.bz2
'''

## READING FILES

# getting a list of filenames
import glob
ham_files = glob.glob("../data/ham/*")
spam_files = glob.glob("../data/spam/*")

# read the ham file contents into a list
ham_text = []
for filename in ham_files:
    with open(filename, 'rU') as f:
        ham_text.append(f.read())

# read the spam file contents into a list
spam_text = []
for filename in spam_files:
    with open(filename, 'rU') as f:
        spam_text.append(f.read())

# use the first 200 ham and first 200 spam as training data
train_text = ham_text[:200] + spam_text[:200]
train_labels = [0]*200 + [1]*200

# use the last 100 ham and last 100 spam as testing data
test_text = ham_text[200:] + spam_text[200:]
test_labels = [0]*100 + [1]*100


## COUNTVECTORIZER: 'convert text into a matrix of token counts'

# learn the 'vocabulary' of the training data
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(decode_error="ignore")
vect.fit(train_text)

# store feature names and examine it
train_features = vect.get_feature_names()
len(train_features)
train_features[:50]
train_features[10000:10002]

# transform documents to a 'document-term matrix'
train_dtm = vect.transform(train_text)
type(train_dtm)

# convert train to an array and examine it
train_arr = train_dtm.toarray()
train_arr.shape
train_arr[0]
sum(train_arr[0])


## SIMPLE SUMMARIES

# summarize the data
import numpy as np
tokens_per_email = np.sum(train_arr, axis=1)    # sum of each row
tokens_per_email
count_per_token = np.sum(train_arr, axis=0)     # sum of each column
count_per_token[:50]

# find the most frequent token
np.max(count_per_token)
np.argmax(count_per_token)
train_features[np.argmax(count_per_token)]


## MODEL BUILDING AND EVALUATION

# train a Naive Bayes model on the training data
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(train_dtm, train_labels)

# create document-term matrix of testing data
test_dtm = vect.transform(test_text)

# make predictions on test data and compare to true labels
preds = nb.predict(test_dtm)
from sklearn import metrics
print metrics.accuracy_score(test_labels, preds)
print metrics.confusion_matrix(test_labels, preds)
print metrics.classification_report(test_labels, preds)

# predict (poorly calibrated) probabilities and calculate AUC
probs = nb.predict_proba(test_dtm)[:, 1]
print metrics.roc_auc_score(test_labels, probs)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(test_labels, probs)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# pretend we didn't have test set and use cross-validation instead
from sklearn.cross_validation import cross_val_score
cross_val_score(MultinomialNB(), train_dtm, train_labels, cv=5, scoring="accuracy")
cross_val_score(MultinomialNB(), train_dtm, train_labels, cv=5, scoring="roc_auc")


## FIND THE HAMMIEST AND SPAMMIEST TOKENS

# split train_arr into ham and spam sections
ham_arr = train_arr[:200]
spam_arr = train_arr[200:]

# calculate count of each token
ham_count_per_token = np.sum(ham_arr, axis=0) + 1
spam_count_per_token = np.sum(spam_arr, axis=0) + 1

# alternative method for accessing counts
ham_count_per_token = nb.feature_count_[0] + 1
spam_count_per_token = nb.feature_count_[1] + 1

# calculate rate of each token
ham_token_rate = ham_count_per_token/float(200)
spam_token_rate = spam_count_per_token/float(200)

# for each token, calculate ratio of ham-to-spam
ham_to_spam_ratio = ham_token_rate/spam_token_rate
np.max(ham_to_spam_ratio)
ham_arr[:, np.argmax(ham_to_spam_ratio)]
spam_arr[:, np.argmax(ham_to_spam_ratio)]
train_features[np.argmax(ham_to_spam_ratio)]

# for each token, calculate ratio of spam-to-ham
spam_to_ham_ratio = spam_token_rate/ham_token_rate
np.max(spam_to_ham_ratio)
spam_arr[:, np.argmax(spam_to_ham_ratio)]
ham_arr[:, np.argmax(spam_to_ham_ratio)]
train_features[np.argmax(spam_to_ham_ratio)]
