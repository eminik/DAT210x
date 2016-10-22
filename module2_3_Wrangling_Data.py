# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:55:19 2016

@author: nikaa
"""

import os
import pandas as pd
import numpy as np


dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module2"
os.chdir(dataDirectory)


## Missing Data
#  Pandas represents missing data internally using Numpy's np.nan. Had Python's
#  None been used, there would be ambiguous collision cases when you actually
#  wished to store None and could no longer differentiate that and a missing
#  record.


df = pd.DataFrame({'satisfaction': ['Sad', 'Mad', 'Happy', 
                                    'Unhappy', 'Neutral', 'Unhappy',
                                    'Neutral', "Mad"],
                  'age': [18, np.nan, np.nan, 9, 10, 9, 5, np.nan]})


# Detect NaN values - missing
df.isnull()
df.age.notnull()

# Fill NAN's with a scalar
df.age.fillna(df.age.mean())


# Replace with immediate previous non-nan value
df.fillna(method = "ffill") # fill the values forward
df.fillna(method = "bfill") # fill the values in reverse
df.fillna(method = "ffill", limit = 1)

# You can fill out NANs by interpolating over them with the non-NAN values that
# come immediately before and after. You can select the interpolation method you'd
# like to use, such as nearest, cubic, spline and more. If your NANs occur at the
# start or end of your list, interpolation will not help you.

df.interpolate(method = "polynomial", order = 2)


## Dropping Data
#  You should always first try to fill in missing data rather than deleting it.
#  If all else fails and you've given up rectifying your NANs, you can always
#  remove the sample or column completely so that it no longer negatively impacts
#  your analysis.

# Remove any row with NANs
df.dropna(axis = 0)
df.loc[df.age.notnull(), :]

# Remove columns with NANs
df.dropna(axis = 1)

# Remove any columns
df.drop(labels = ["satisfaction"], axis = 1)

# You might also want to prune duplicat records if samples cannot have identical
# properties. Be careful though! In order to get rid of duplicate records, you
# should tell Pandas which features are to be examined, because Pandas generates
# indices for you automatically when you load a dataframe without specifying an 
# index column. With each column having a unique index, Pandas won't find any 
# duplicates unless you limit your search to a subset of your dataframe's features.

df
df.drop_duplicates(subset = ["age", "satisfaction"])

# Removing duplicate samples will cause gaps to occur in your index count. You 
# can interpolate to fill those holes where appropriate, or alternatively you can
# reindex your dataframe.
df.index.values
df = df.drop_duplicates(subset = ["age", "satisfaction"])
df.index.values

df.reset_index(drop = True).index.values

# The drop = True parameter tells Pandas not to keep a backup copy of the original
# index.

# Most of the above methods return a copy of your dataframe. This is useful
# because you can chain methods

# drop rows that contain less than "thresh" observations
df.dropna(axis = 0, thresh = 2).drop(labels = ["satisfaction"], axis = 1).drop_duplicates(subset = ["age"]).reset_index(drop = True)
 

# If you want these operations to work in place on the dataframe calling them, 
# rather than returning a new dataframe, pass inplace = True as a parameters to any
# of the above methods to get that working.



## More wrangling
# Pandas will automatically attempt to figure out the best data type to use for
# each series in your dataset. Most of the time this works OK, but other times not.
# Particularly the .read_html() method is notorious for defaulting all series 
# data types to Python objects. You should check and double check the actual type
# of each column in your dataset to avoid unwanted surprises.

df.dtypes

# If your data types are wrong you can explicitly convert them to the desired 
# type using .to_datetime(), .to_numeric(), and to .timedelta() methods.

df.satisfaction = df.satisfaction.apply(str)
df
df.dtypes

df.age = pd.to_numeric(df.age, errors = "coerce")
df.dtypes

# to_numeric converts to decimal or integer depending on the data it finds
# The errors  = "coerce" parameter instructs Pandas to enter NaN at any field 
# where conversion fails.

# Unique values
df.age.unique()

# Count for every unique
df.satisfaction.value_counts()

























