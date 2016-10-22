# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:18:36 2016

@author: nikaa
"""

import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.style.use("ggplot")


dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module3"
os.chdir(dataDirectory)

# Load data 
student_dataset = pd.read_csv("Datasets/students.data", index_col = 0)

## HISTOGRAMS
# To render a histogram with matplotlib through Pandas, call the .plot.hist()
# method on either a dataframe or a series.

# frequencies
student_dataset.G3.plot.hist(alpha = 0.5)
student_dataset.loc[:, ["G3", "G2", "G1"]].plot.hist(alpha = 0.5)

# probabilities

student_dataset.G3.plot.hist(alpha = 0.5, normed = True)
student_dataset.loc[:, ["G3", "G2", "G1"]].plot.hist(alpha = 0.5, normed = True)


# 2D - SCATTER PLOTS

student_dataset.plot.scatter(x = 'G1', y = 'G3')
# or
matplotlib.pyplot.scatter(x = student_dataset.G1, y = student_dataset.G3)


# 3D - SCATTER PLOTS
# Unfortunately the pyplot member of Pandas dataframes don't natively support the
# ability to generate 3D plots, so we are going to it directly with matplotlib
 
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.set_xlabel("Final Grade")
ax.set_ylabel("First Grade")
ax.set_zlabel("Daily Alcohol")
ax.scatter(student_dataset.G1, student_dataset.G2,student_dataset.Dalc, c = "r", marker = ".")
plt.show()






