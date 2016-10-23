# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:55:56 2016

@author: Pavlos-Dell
"""
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates

# ggplot style

matplotlib.style.use("ggplot")

dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module3"
os.chdir(dataDirectory)

## Parallel Coordinates
#  Parallel coordinates plots are similar to scatter plots in that each axis maps
#  to the ordered, numeric domain of a feature. But, instead of having axes aligned
#  in an orthogonal manner, parallel coordinates get their name due to their axes 
#  being arranged vertically and in parallel.

#  Each graphed observation is plotted as a polyline, a series of connected line 
#  segments. The joines of the polyline fall on each axis. Since each axis maps
#  to the domain of a numeric feature, the resulting polyline fully describes the 
#  value of each of the observation's features.

# Parallel coordinates works well for <= 10 features.

# Load iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]

# Parallel Coordinates
plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()

# Parallel coordinates support onle a single scale for ALL your axis. If you have 
# some features that are on a small scale and others on a large scale, you'll
# have to deal with a compressed plot. Solutions:
# 1. Normalize your features before charting them
# 2. Chane the scale to log scale
# 3. Create a separate, multiple parallel coordinate charts. Each one only
#    plotting features with similar domain scales plotted.



## Andrew's Curve
#  An Andrew's curve helps you visualize higher dimensionality, multivariate data
#  by plotting each observation as a curve. The feature values of the observation
#  act as the coefficients of the curve, so observations with similar characteristics
#  tend to group closer to each other. Due to this, Andrews curves have some use
#  in outlier detection.
#  
# Similar to Parallel coordinates, every plotted feature must be numeric since the
# curve equation is essentially the product of the observation's features vector
# (transposed) and the vector (1/sqrt(2), sin(t), sin(2t), cos(2t), sin(3t), cos(3t))
# to create a Fourier Series.

from pandas.tools.plotting import andrews_curves

plt.figure()
andrews_curves(df, "target_names")
plt.show()

# One of the current weaknesses with the Pandas implementation is that every
# single observation is charted. In the MATLAB version, you can specify a quantile
# or probability distribution cutoff. This way, only the mean feature values for a 
# specific group are plotted, with a transparent boundary around the cutoffs.


## Imshow
#  Matplotlib's .imshow() method generates an image based off of the normalized
#  values stored in a matrix, or rectangular array of float64s. The properties
#  of the generated image will depend on the dimensions and contents of the array
#  passed in:
#   - An [X, Y] shaped array will result in a grayscale image being generated
#   - An [X, Y, 3] array results in full color image (1 channel for red, 1 channel
#    for green and 1 for blue)
#   - An [X, Y, 4] shaped array results in a full color image as before with an 
#     an extra channel for alpha

# Besides being a straightforward way to display .png and other images, the .imshow
# method has quite a few other uses. When you use the .corr() method on your
# dataset, Pandas calculates a correlation matrix for you that measures how close
# to being linear the relatioship between any two features in your dataset are.
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 5), columns = ['a', 'b', 'c', 'd', 'e'])
df.corr()
plt.imshow(df.corr(), cmap = plt.cm.Blues, interpolation = "nearest")
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation = 'vertical')
plt.yticks(tick_marks, df.columns)
plt.show()









































