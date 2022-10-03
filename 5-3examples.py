#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:57:51 2021

@author: taterosen

Text ch 5 basic examples + statistical tools (numpy)
"""

import numpy as np
import matplotlib.pyplot as plt        #for histogram

print("Hello, World!")

year = 2020
if (year % 4 == 0):
    print("Leap year")
else: 
    print("Not leap year")

colYear = 3
if (colYear == 1):
    print("freshman")
elif(colYear == 2):
    print("sophomore")
elif(colYear == 3):
    print("junior")
else:
    print("senior")
    
a, b = 1, 5
while (a <= b):
    print(a)
    a += 1

for x in range(1, 6):
    print(x)

ans = 'A'
if ans == 'A' or ans == 'D':
    print ("yes")
else:
    print("no")
    
#ans = input("guess!")
#while (ans != 'A' and ans != 'D'):
#    print("no")
#    ans = input("guess again")
    
    
#ARRAY
data1 = [85, 62, 78, 64, 25, 12, 74, 96, 63, 45, 78, 20, 5, 30, 45, 78, 45, 96, 65, 45, 74, 12, 78, 23, 8]

#max
max = np.max(data1)
print("Max: {0:d}" .format(max))

#min (alt)
print("Min:" + str(min(data1)))

#mean
mean = np.mean(data1)
print("mean: {0:8.4f}" .format(mean))

#variance
variance = np.var(data1)
print("variance: {0:8.4f}" .format(variance))

#Standard deviation
sd = np.std(data1)
print("STD: {0:8.4f}" .format(sd))

#median
median = np.median(data1)
print("Median: {0:8.4f}" .format(median))

#histogram of distribution
plt.figure()
hist1, edges1 = np.histogram(data1)
plt.bar(edges1[:-1], hist1, width = edges1[1:] - edges1[:-1])

#random dataset
data2 = np.random.randn(1000)

max2 = np.max(data2)
print("Max: " + str(max2))

min2 = np.min(data2)
print("min: " + str(min2))

mean2 = np.mean(data2)
print("mean: " + str(mean))

sd2 = np.std(data2)
print("sd: " + str(sd2))

var2 = np.var(data2)
print("var: " + str(var2))

med2 = np.median(data2)
print("median: " + str(med2))

plt.figure()
hist2, edges2 = np.histogram(data2, bins = 100)     #bins = how many bars b
plt.bar(edges2[:-1], hist2, width = edges2[1:] - edges2[:-1])


















