# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:45:05 2016

@author: nikaa
"""

import os


dataDir = "C:/Users/NikaA/Desktop/Dat210x-master/Module4"
os.chdir(dataDir)


## ISOMAP
# Isomap is an unsupervised dimensionality reduction tehnique that reduces the
# dimensionality of your dataset.
# PCA is faster than Isomap and works well in most situations, but its limitation
# is that it assumes a linear relationship exists between your features. You should
# transform your high dimensionality datasets with Isomap when they do not exhibit
# the behaviour you want, haveing been passed through PCA. 

# In order to address non-linear situations, Isomap uses an entirely different
# approach to the dimensionality reduction problem, one that is highly efficient
# albeit more processor intensive than PCA. Nonetheless, for non-linear relatioships
# it is a must. Its goal: to uncover the instrinsic, geometric nature of your dataset 
# as opposed to simply capturing your datasets most variant directions.

# Isomap operates by first computing each record's nearest neighbours. This is done
# by comparing each sample to tevery other sample in the dataset. Only a samples
# K-nearest samples qualify for being included in its nearest neighbourhood samples list.
# A neighbourhood graph is then constructed by linking each sample to its K- nearest 
# neighbours. The result is similar to a map of roads that is traversed in order to move
# from point to point. Isomap travels from sample to sample  taking the shortest 
# neighbourhood paths between any two distant samples in your dataset. The straighforward
# direct Euclidean distance between any two records fails to properly account for any
# nonlinear geometry present within your dataset's features. Isomap is able to 
# intelligently recover and estimate a  lower dimensional embedding, also know as
# a MANIFOLD, by traversing the shortest distances between samples, hopping along
# through the calculated neighbourhood map. It is with this map thatIsomap calculates
# a projection or a reduced dimensional embedding that represent your dataset through
# MULTI-DIMENSIONAL scaling.

# Multi-dimensional scaling is a process of taking samples in N-dimensional space
# and representing them on some other M-dimensional space while attempting to preserve
# inter-sample distances as much as possible. If you are going from lower to higher
# dimensionality then the distances can be preserved perfectly, but when you reduce
# dimensions some information is lost.

import numpy as np
from sklearn import manifold
import pandas as pd
import string
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iso = manifold.Isomap(n_neighbors = 4, n_components = 2)

df = pd.DataFrame(np.random.rand(100, 15), columns = list(string.ascii_lowercase[0:15]))

df.o = 3 * df.a ** 3 + 6 * df.b ** 2

iso.fit(df)

# The largest your n_neighbors value is, the longer it will take to calculate the
# node neighbourhood map. You will have to experimentwith the neighbourhood connectivity
# in order to get better results.
# You also need to reflect on how many samples need to be collected in order to 
# properly capture the your lower dimensional manifold. A rule of thumb is the curvier
# your dataset is (sharpness of the edges) the more dense your samples must be in order
# to capture its latent relationships. 

df_manifold = iso.transform(df)

print df.shape
print df_manifold.shape

df_manifold = pd.DataFrame(df_manifold, columns = ["t1", "t2"])



fig = plt.figure(1)
ax = fig.add_subplot(111, projection = "3d")
ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel("o")
ax.scatter(df.a, df.b, df.o, c = df.o, marker = "o", s = 30)
plt.show()

fig = plt.figure(2)
plt.scatter(df_manifold.t1, df_manifold.t2, c = df.o)
plt.xlabel("t1")
plt.ylabel("t2")
plt.show()


# Unlike PCA, ISOMAP transformations are undirectional so you will not be able to 
# .inverse_transform() your projected data back into your original feature space,
# even if it has the same number of dimensions as your original datasets.

# Isomap is more sensitive to noise than PCA. Noisy data can actually act as a 
# conduit to short-circuit the nearest neighbourhood map, because isomap prefers the
# 'noisy' shorter path between samples that lie on the real geodesic surface of 
# your data that would otherwise be well separated.

# When using unsupervised dimensionality reduction techniques, be sure to use the 
# feature scaling on all of your features because the nearest-neighbours search that
# isomap bases your manifold on will do poorly if you don't and PCA will prefer
# features with largest variances.
# You can use SciKit-Learn's StandardScaler 



