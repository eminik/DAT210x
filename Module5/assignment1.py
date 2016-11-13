#
# TOOD: Import whatever needs to be imported to make this work
#
# .. your code here ..
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn.cluster import KMeans

## Changed to Python 3 from here on ##
plt.style.use('ggplot') # Look Pretty


# Change directory
dataDirectory = "C:/Users/Pavlos-Dell/Desktop/Further Learning/edX/Programming with Python for Data Science/DAT210x/Module5"
os.chdir(dataDirectory)
#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'



def doKMeans(df):
  #
  # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

  #
  # TODO: Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  # .. your code here ..
  df = df[["Longitude", "Latitude"]]
  #
  # TODO: Use K-Means to try and find seven cluster centers in this df.
  #
  # .. your code here ..
  kmeans_model = KMeans(n_clusters=7)
  kmeans_model.fit(df)
  #
  # INFO: Print and plot the centroids...
  centroids = kmeans_model.cluster_centers_
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  print(centroids)



#
# TODO: Load your dataset after importing Pandas
#
# .. your code here ..

gamblingData = pd.read_csv("Datasets/gambling_crimes.csv")
print(gamblingData.describe())

#
# TODO: Drop any ROWs with nans in them
#
# .. your code here ..

gamblingData = gamblingData.dropna()
#
# TODO: Print out the dtypes of your dset
#
# .. your code here ..

print(gamblingData.dtypes)
#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
# .. your code here ..
gamblingData["Date"] = pd.to_datetime(gamblingData["Date"], format="%m/%d/%Y %I:%M:%S %p")
print(gamblingData.dtypes)
print(gamblingData.head())

# INFO: Print & Plot your data
doKMeans(gamblingData)



#
# TODO: Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
# .. your code here ..
gamblingDataFiltered = gamblingData.loc[gamblingData.Date > '2011-01-01', :]
print(gamblingData.shape)
print(gamblingDataFiltered.shape)

# INFO: Print & Plot your data
doKMeans(gamblingDataFiltered)
plt.show()


