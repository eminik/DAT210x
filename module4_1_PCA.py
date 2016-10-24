# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:44:24 2016

@author: nikaa
"""

import os


dataDir = "C:/Users/NikaA/Desktop/Dat210x-master/Module4"
os.chdir(dataDir)


## Transformer: any algorithm that you apply to your dataset that changes either
#  the feature count or feature values, but does not alter the number of observations.
#  They can be used to clean up your data before it's fed to other algorithms
#  Dimensionality reduction is a popular transformer that reduces the number of features
#  to a subset of the original.


## PCA - Principal Component Analysis

#  PCA is a transformation that attempts to convert your possibly correlated features
#  into a set of linearly uncorrelated ones (dimensionality reduction algorithm).
#  If you have reason to believe your question has a simple answer, or that the
#  the features you've collected are actually many indirect observations of some
#  inherent source you either cannot or do not know how to measure, then dimensionality
#  reduction applies to your needs.
#  PCA's approach to dimensionality reduction is to derive a set of degrees of
#  freedom that can then be used to reproduce most of the variability in your data.

#  PCA models a linear subspace of your data by capturing its greatest variability.
#  It acceses your dataset's covariance structure directly using matrix calculations
#  and eigenvector to compute the best unique features that describe your samples.
#  An iterative approach to this would first find the center of your data, based off its 
#  numeric features and then it would search for the direction that has the most variance or 
#  widest spread of values. That direction is the principal compenent vector, so it is then 
#  added to the list. By searching for more directions of maximal variance that are orthogonal
#  to all previously computed vectors, more principal components can be added to the list. 
#  This set of vectors forms a new feature space that you can represent your samples with.

#  PCA orders the features by importance, assuming the the more variance expressed 
#  in a feature the more important it is. Dropping the least important features
#  in the list intelligently reduces the number of dimensions needed to represent
#  your dataset with minimal loss of information.

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

df = pd.DataFrame(np.array([[-1, -1, 4], 
                            [-2, -1, 0], 
                            [-3, -2, 12], 
                            [1, 1, 7],
                            [2, 1, 7],
                            [3, 2, 2]]))
pca = PCA(n_components = 2)

pca.fit(df)

# Once you've fit the model against your dataframe, you can use it to transform
# your dataset's observations into the newly computed, principal component feature
# space with the .transform() method. This transformation is bidirectional, so you 
# can recover you original feature values using the .inverse_transform() so long as
# you don't drop any components. If even one component was removed, the after performing
# the inverse transformation back to regular feature space, there will be some
# signs of information loss proportional to which component was dropped.

transDf = pd.DataFrame(pca.transform(df))
transDf.shape
df.shape

# Principal components vectors (linear combinations of your original features)
pca.components_

# Calculated amount of variance which exists in the newly computed principal components
pca.explained_variance_

# Nomralized version of explained variance 
pca.explained_variance_ratio_



## PCA Weaknesses

# 1. PCA is sensitive to the scaling of your features. If you have a feature with
#    large variance and others with small variances, the feature with the large 
#    variance can dominate your first principal component. 
#    Standardizing your variables ahead of time is the way to free your PCA results
#    of such scaling issues. The cases where you should not use standardization are
#    when you know your feature variables and thus their importance need to respect
#    the specific scaling you've set up. 
# 2. For very very large datasets PCA can be slow. You can use RandomizedPCA that applies
#    some approximation techniques to speed up large-scale matrix computation.
# 3. PCA is a linear transformation  only!  It can only capture the underlying 
#    linear shapes and variance within your data and cannot discern any complex,
#    nonlinear intricacies. For such cases you will have to make use of different
#    dimensionality reduction algorithms, such as isomap.


















