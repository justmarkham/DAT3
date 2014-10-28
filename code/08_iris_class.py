'''
CLASS: "Human Learning" with iris data
'''

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the famous iris data
iris = load_iris()

# what do you think these attributes represent?
iris.data
iris.data.shape
iris.feature_names
iris.target
iris.target_names

# intro to numpy
type(iris.data)


## PART 1: Read data into pandas and explore

# read iris.data into a pandas DataFrame (df), including column names

# clean up column names

# read into pandas again, with better column names

# create a list of species (150 elements) using iris.target and iris.target_names

# add the species list as a new DataFrame column

# explore data numerically, looking for differences between species

# explore data by sorting, looking for differences between species

# explore data visually, looking for differences between species


## PART 2: Write a function to predict the species for each observation

# create a dictionary so we can reference columns by name

# define function that takes in a row of data and returns a predicted species

# make predictions and store as numpy array

# calculate the accuracy of the predictions
