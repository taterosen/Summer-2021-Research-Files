#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:10:55 2021

@author: taterosen

nearest neighbor - rock music data
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
##from sklearn.cross_validation import train_test_split

df = pd.read_csv("rock_music_data.csv")

# Mark ~70% of data for training, use rest for testing
# we'll use 'density', 'sulfates', and 'residual_sugar' features for training a classifier on 'high_quality'
X_train, X_test, y_train, y_test = train_test_split(df[['loudness', 'energy', 'danceability']], df['mode'], test_size = .3)
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X_train, y_train)

# test classifier by giving it test instances
prediction = classifier.predict(X_test)

# count how many instances were correctly classified
correct = np.where(prediction == y_test, 1, 0).sum()
print(correct)

# calc accuracy of this classifier
accuracy = correct/len(y_test)
print(accuracy)

#start w array where results (k and corresponding accuracy) will be stored
results = []

for k in range(1, 51, 2):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    accuracy = np.where(prediction==y_test, 1, 0).sum() / (len(y_test))
    print("k =", k, "Accuracy =", accuracy)
    results.append([k,accuracy])    #storing the k, accuracy tuple in results array
    
    #convert that series of tuples in a dataframe for easy plotting
    results2 = pd.DataFrame(results, columns=["k","accuracy"])
    
    plt.plot(results2.k, results2.accuracy)
    plt.title("value of k and corresponding classification accuracy")
    plt.xlabel('k')
    plt.show()