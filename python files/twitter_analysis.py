#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:16:48 2021

@author: taterosen

analyzing twitter data
"""

# load numpy and pandas for data manip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load statsmodels as alias 'sm'
import statsmodels.api as sm

# load the data downloaded from twitter
df = pd.read_csv('result2.csv', index_col=0)

# look at some correlations
print("correlation coefficient =", 
      np.corrcoef(df.followers, df.friends)[0,1])
print("correlation coefficient =", 
      np.corrcoef(df.followers, df.retwc)[0,1])

# create scatterplot of followers vs friends
plt.scatter(df.followers, df.friends)

# use regression analysis for predicting number of followers (y) using number of friends (x)
y = df.followers #response
x = df.friends #predictor
x = sm.add_constant(x) #adds a constant term to predictor

lr_model = sm.OLS(y,x).fit()
print(lr_model.summary())

# pick 100 pts equally spaced from min to max
x_prime = np.linspace(x.friends.min(), x.friends.max(), 100)
x_prime = sm.add_constant(x_prime) 

# calc predicted values
y_hat = lr_model.predict(x_prime)

plt.figure(1)

plt.subplot(211)
plt.scatter(df.followers, df.friends)

plt.subplot(212)
plt.scatter(x.friends, y) #plot raw data
plt.xlabel("friends")
plt.ylabel("followers")
plt.plot(x_prime[:,1], y_hat, 'blue') # add red regression line