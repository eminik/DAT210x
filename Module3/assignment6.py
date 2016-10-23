import pandas as pd
import matplotlib.pyplot as plt
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

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..

wheatData = wheatData.drop(["id"], axis = 1)
#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..

cor = wheatData.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
tick_marks = [i for i in range(len(cor.columns))]
plt.imshow(cor, cmap = plt.cm.Blues, interpolation = "nearest")
plt.xticks(tick_marks, cor.columns, rotation = 'vertical')
plt.yticks(tick_marks, cor.columns)
plt.show()


# min value in dataframe
minVal = wheatData.corr().abs().min(axis = 0).min()

wheatData.corr()[wheatData.corr().abs().iloc[:,:] == minVal]


