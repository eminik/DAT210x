import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import os


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


fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel("area")
ax.set_ylabel("perimeter")
ax.set_zlabel("asymmetry")
ax.scatter(wheatData.area, wheatData.perimeter, wheatData.asymmetry, c = "red")
plt.show()


#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel("width")
ax.set_ylabel("groove")
ax.set_zlabel("length")
plt.scatter(wheatData.width, wheatData.groove, wheatData.length, c = "green")
plt.show()


