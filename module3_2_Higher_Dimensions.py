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



## Andrew's Scale











































