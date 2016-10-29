import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
dataDir = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module4"
os.chdir(dataDir)

samples = []
colours = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 


filesIn32 = os.listdir("Datasets/ALOI/32")
filesIn32i = os.listdir("Datasets/ALOI/32i")

for file in filesIn32:
    temp_img = misc.imread("Datasets/ALOI/32/" + file)
    temp_img = (temp_img[::2, ::2]/255.00).reshape(-1)
    samples.append(temp_img)
    colours.append("b")
    
for file in filesIn32i:
    temp_img = misc.imread("Datasets/ALOI/32i/" + file)
    temp_img = (temp_img[::2, ::2]/255.0).reshape(-1)
    samples.append(temp_img)
    colours.append("r")

# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn import manifold

iso = manifold.Isomap(n_neighbors = 6, n_components = 3)
iso.fit(df)

dfTrans = iso.transform(df)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("Component 0")
ax.set_ylabel("Component 1")
ax.scatter(dfTrans[:, 0], dfTrans[:, 1], marker = "o", c = colours)
plt.show()



#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 


fig = plt.figure(2)
ax = fig.add_subplot(1, 1, 1, projection = "3d")
ax.set_xlabel("Component 0")
ax.set_ylabel("Component 1")
ax.set_zlabel("Component 2")
ax.scatter(dfTrans[:, 0], dfTrans[:, 1], dfTrans[:, 2], marker = "o", c = colours)
plt.show()





# Trying different numbers for K


for K in np.arange(1, 6):    
    iso = manifold.Isomap(n_neighbors = K, n_components = 3)
    iso.fit(df)    
    dfTrans = iso.transform(df)    
    fig = plt.figure(K)
    ax = fig.add_subplot(1, 1, 1, projection = "3d")
    ax.set_xlabel("Component 0")
    ax.set_ylabel("Component 1")
    ax.set_zlabel("Component 2")
    ax.set_title("K = {0}".format(K))
    ax.scatter(dfTrans[:, 0], dfTrans[:, 1], dfTrans[:, 2], marker = "o", c = colours)
    plt.show()

    
    
    
    
    
    