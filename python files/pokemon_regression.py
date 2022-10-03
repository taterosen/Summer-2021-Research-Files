#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:43:18 2021

@author: taterosen

regression analysis on pokemon stats
"""

# load numpy and pandas for data manip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load statsmodels as alias 'sm'
import statsmodels.api as sm

# load the data downloaded from twitter
df = pd.read_csv('Pokemon.csv', index_col=0)

# look at some correlations
print("correlation coefficient =", 
      np.corrcoef(df.Attack, df.Defense)[0,1])
print("correlation coefficient =", 
      np.corrcoef(df.Attack, df.HP)[0,1])

# create scatterplot of Attack stat vs Defense stat
plt.scatter(df.Attack, df.Defense)

# use regression analysis for predicting number of Attack (y) using number of Defense (x)
y = df.Attack #response
x = df.Defense #predictor
x = sm.add_constant(x) #adds a constant term to predictor

lr_model = sm.OLS(y,x).fit()
print(lr_model.summary())

# pick 100 pts equally spaced from min to max
x_prime = np.linspace(x.Defense.min(), x.Defense.max(), 100)
x_prime = sm.add_constant(x_prime) 

# calc predicted values
y_hat = lr_model.predict(x_prime)

plt.figure(1)

plt.subplot(211)
plt.scatter(df.Attack, df.Defense)

plt.subplot(212)
plt.scatter(x.Defense, y) #plot raw data
plt.xlabel("defense")
plt.ylabel("attack")
plt.plot(x_prime[:,1], y_hat, 'blue') # add red regression line