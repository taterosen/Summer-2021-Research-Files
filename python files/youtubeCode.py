#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:37:03 2021

@author: taterosen

youtube code
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split

df = pd.read_csv("youtube_results4.csv")

# Mark ~70% of data for training, use rest for testing
X_train, X_test, y_train, y_test = train_test_split(df[['likeCount', 'dislikeCount', 'commentCount']], df['viewCount'], test_size = .3)
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X_train, y_train)

# test classifier by giving it test instances
prediction = classifier.predict(X_test)

# count how many were correctly classified
correct = np.where(prediction == y_test, 1, 0).sum()
print(correct)

# calc accuracy of this classifier
accuracy = correct/len(y_test)
print(accuracy)

#start w array where results (k and corresponding accuracy) will be stored
results = []

for k in range(1, 16, 2):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    accuracy = np.where(prediction==y_test, 1, 0).sum() / (len(y_test))
    print("k =", k, "Accuracy =", accuracy)
    results.append([k,accuracy])    #storing the k, accuracy tuple in results array
    
    #convert that series of tuples in a dataframe for easy plotting
    results = pd.DataFrame(results, columns=["k","accuracy"])
    
    plt.plot(results.k, results.accuracy)
    plt.title("value of k and corresponding classification accuracy")
    plt.show()