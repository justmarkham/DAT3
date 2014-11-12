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

# read the ham file contents into a list (each element is one email)
ham_text = []
for filename in ham_files:
    with open(filename, 'rU') as f:
        ham_text.append(f.read())

# read the spam file contents into a list (each element is one email)
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

# store feature names and examine them
train_features = vect.get_feature_names()
len(train_features)
train_features[:50]
train_features[10000:10002]

# transform training data into a 'document-term matrix'
train_dtm = vect.transform(train_text)
type(train_dtm)

# convert train_dtm to a regular array and examine it
train_arr = train_dtm.toarray()
train_arr.shape
train_arr
sum(train_arr[0])


## SIMPLE SUMMARIES OF THE DATA

# sum the rows and columns
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

# transform testing data into a document-term matrix
test_dtm = vect.transform(test_text)
test_dtm

# make predictions on test data and compare to true labels
preds = nb.predict(test_dtm)
preds
from sklearn import metrics
print metrics.accuracy_score(test_labels, preds)
print metrics.confusion_matrix(test_labels, preds)

# predict (poorly calibrated) probabilities and calculate AUC
probs = nb.predict_proba(test_dtm)[:, 1]
probs
print metrics.roc_auc_score(test_labels, probs)

# plot ROC curve
fpr, tpr, thresholds = metrics.roc_curve(test_labels, probs)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

# pretend we didn't have test set and use cross-validation instead
from sklearn.cross_validation import cross_val_score
cross_val_score(MultinomialNB(), train_dtm, train_labels, cv=5, scoring="accuracy")
cross_val_score(MultinomialNB(), train_dtm, train_labels, cv=5, scoring="roc_auc")


## FIND THE 'HAMMIEST' AND 'SPAMMIEST' TOKENS

# split train_arr into ham and spam sections
ham_arr = train_arr[:200]
spam_arr = train_arr[200:]
ham_arr
spam_arr

# calculate count of each token
ham_count_per_token = np.sum(ham_arr, axis=0) + 1
spam_count_per_token = np.sum(spam_arr, axis=0) + 1

# alternative method for accessing counts
ham_count_per_token = nb.feature_count_[0] + 1
spam_count_per_token = nb.feature_count_[1] + 1

# calculate rate of each token
ham_token_rate = ham_count_per_token/float(200)
spam_token_rate = spam_count_per_token/float(200)
ham_token_rate
spam_token_rate

# for each token, calculate ratio of ham-to-spam
ham_to_spam_ratio = ham_token_rate/spam_token_rate
np.max(ham_to_spam_ratio)
ham_arr[:, np.argmax(ham_to_spam_ratio)]        # count of that token in ham emails
spam_arr[:, np.argmax(ham_to_spam_ratio)]       # count of that token in spam emails
train_features[np.argmax(ham_to_spam_ratio)]    # hammiest token

# for each token, calculate ratio of spam-to-ham
spam_to_ham_ratio = spam_token_rate/ham_token_rate
np.max(spam_to_ham_ratio)
spam_arr[:, np.argmax(spam_to_ham_ratio)]       # count of that token in spam emails
ham_arr[:, np.argmax(spam_to_ham_ratio)]        # count of that token in ham emails
train_features[np.argmax(spam_to_ham_ratio)]    # spammiest token
