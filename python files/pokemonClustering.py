#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:30 2021

@author: taterosen

pokemon clustering example
"""

import numpy as np
import matplotlib.pyplot as plt

# import style class from matplotlib and use to apply ggplot styling
from matplotlib import style
style.use("ggplot")

# get KMeans class from clustering lib avail within scikit-learn
from sklearn.cluster import KMeans

# define data points on 2D plane using cartesian coordinates
X = np.loadtxt("Pokemon.csv", delimiter=",", usecols = (6,7))



# perform clustering using k-means alg
kmeans = KMeans (n_clusters = 4)
kmeans.fit(X)

# 'kmeans' holds the model; extract info abt clusters as rep by their centroids, along w their labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# define colors array
colors = ["g.", "r.", "c.", "y."]

# loop to go through each data pt, plotting it on the plane w/ color from above list(1 color per cluster)
for i in range (len(X)):
    print("coordinate:", X[i], "Label:", labels[i])
    plt.plot (X[i][0], X[i][1], colors[labels[i]], markersize = 10)
    
# plot the centroids using "x"
plt.scatter(centroids[:,0], centroids[:,1], marker = "x", s = 150, linewidths = 2, zorder = 10)
plt.xlabel('attack')
plt.ylabel('defense')
plt.show()