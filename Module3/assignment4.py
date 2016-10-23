import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from pandas.tools.plotting import parallel_coordinates

dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module3"
os.chdir(dataDirectory)


# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheatData = pd.read_csv("Datasets/wheat.data")


#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..
w2 = wheatData.drop(labels = ["id", "area", "perimeter"], axis = 1)

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
parallel_coordinates(w2, "wheat_type", alpha = 0.4)  


plt.show()


# Andrews curves (assignment 5)

from pandas.tools.plotting import andrews_curves

andrews_curves(w2, "wheat_type", alpha = 0.4)

w3 = w2.copy()
w3["parameter"] = wheatData.perimeter
w3["area"] = wheatData.area

andrews_curves(w3, "wheat_type", alpha = 0.4)
















