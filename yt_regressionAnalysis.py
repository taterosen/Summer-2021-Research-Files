#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:54:37 2021

@author: taterosen

twitter regression analysis code (p333) but w youtube data
"""

# load numpy and pandas for data manip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load statsmodels as alias 'sm'
import statsmodels.api as sm

# load the data downloaded from twitter
df = pd.read_csv('youtube_results4.csv', index_col=0)

# look at some correlations
print("correlation coefficient =", 
      np.corrcoef(df.viewCount, df.likeCount)[0,1])
print("correlation coefficient =", 
      np.corrcoef(df.likeCount, df.commentCount)[0,1])

# create scatterplot of views vs likes
plt.scatter(df.viewCount, df.likeCount)

# use regression analysis for predicting number of views (y) using number of likes (x)
y = df.viewCount #response
x = df.likeCount #predictor
x = sm.add_constant(x) #adds a constant term to predictor

lr_model = sm.OLS(y,x).fit()
print(lr_model.summary())

# pick 100 pts equally spaced from min to max
x_prime = np.linspace(x.likeCount.min(), x.likeCount.max(), 100)
x_prime = sm.add_constant(x_prime) 

# calc predicted values
y_hat = lr_model.predict(x_prime)

plt.figure(1)

plt.subplot(211)
plt.scatter(df.viewCount, df.likeCount)

plt.subplot(212)
plt.scatter(x.likeCount, y) #plot raw data
plt.xlabel("likes")
plt.ylabel("views")
plt.plot(x_prime[:,1], y_hat, 'blue') # add red regression line