# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:11:05 2016

@author: Artemis Nika
"""

## K-Means
# Clustering groups samples that are similarn within the same cluster. The more similar the samples belonging to 
# a cluster group are (and conversely, the more dissimilar samples in separate groups), the better the clustering 
# algorithm has performed.
# K-means iteratively separates your samples into a user-specified number of K-cluster groups of roughly equal 
# variance. Cluster groups are defined by their geometric cluster center -  a single point called the centroid.
# Every sample in the dataset is assigned to the centroid nearest to it.
# In the case of continuous features, calculating the distance is straightforward, but when you have categorical
# features you'll have to come up with other methods.
#

## The K-means algorithm
#  K-means starts by placing a user-specified number of K cluster centers in your feature space. There are many 
# techniques fro choosing the first centroid placement and your results will vary depending on the one you select.
# The simples way is to use the position of some random samples as the centroids' starting sports.
#  Each cluster then takes ownership of the samples nearest to its centroid, and every sample can only be assigned
# to one cluster. The distance metric usually used  is the n-dimensional Euclidean distance between the sample and 
# the centroid. After all samples have been assigned to a cluster, the centroid location is updated to be the mean 
# value of all samples assigned to it. The mean value is calculated by feature, so the centroid position ends up 
# being a n-length vector within your feature space.
#  The assignment and update repeats until there are no more changes in either, at which point the algorithm has
# converged. K-means always converges but it does not always converge at the global minimum.
#   The technical explanation for what K-means does is minimizing the sum of squared errors between each sample and
# its respective centroid. As mentioned, the initial centroid assignment affects the results. Two runs of K-means
# might produce different outcomes, but the quality of their cluster assignments are ranked by looking at which run 
# has the smalles overall inertia.

## K-means use
#  K-Means clustering is best suited when you have a good idea of the number of distinct clusters your unlabeled dataset 
# should be segmented into. Generally, the output of K-Means is used in two ways. To separate your unlabeled data into K 
# groups, which is the clear use case, or to find and use the resulting centroids.
#  You can use the centroid to 'compress' your data. By referring to the centroid rather than the data sample, the number
# of unique values is reduced, which optimizes the execution speed of other algorithms. 
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans 
from sklearn import preprocessing

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
stand_df = preprocessing.scale(df)
kmeans = KMeans(n_clusters=5)
kmeans.fit(stand_df)

labels = kmeans.predict(stand_df)
centroids = kmeans.cluster_centers_


## K-means Gotchas
#  Considering how basic K-means is, it performs pretty well and its implementation is the basis of far more advanced
# clustering algorithms, such as learning vector quantization and Gaussian mixture. Having a solid understanding of 
# K-means will help you understand those better when you study them.
#  K-means is only really suitable when you have a good estimate of the number of clusters that exist in your data.
# Even if you do have the right number of clusters selected, the result produced by K-means can vary depending on the
# initial centroid placement. Due to cenrtroid seed placement having som much of an effect on your clustering outcome, 
# you have to be careful since it is possible to have centroid with only a single sample assigned to them, or even no
# samples assigned to them.
#  Two other key characteristics of K-means are that it assumes your samples are length normalized and as such is 
# sensitive to featire scaling. It also assumes that the cluster sizes are rougly spherical and similar; this way
# the nearest centroid is always the correct assignment.