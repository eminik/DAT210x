# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:37:26 2016

@author: nikaa
"""

import pandas as pd
import os

# panda series are like R vectors - accept only one type of data
dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module2"

os.chdir(dataDirectory)


df = pd.read_csv("Datasets\direct_marketing.csv")


## Different Types of Column Indexing

# 1. Using Column Name - Readable code, a bit slower as the column name needs 
#    to be matched first
df.recency
df['recency']
df[['recency']]
# Once you are ready for the production environment Pandas documentation 
# recommends you use either .loc[], .iloc[], or .ix[] data access methods, 
# which are more optimized
df.loc[:, "recency"]
df.loc[:, ["recency"]]

# 2. Using Index - A bit faster
df[[0]]
df.iloc[:, 0]
df.iloc[:, [0]]
df.ix[:, 0]

# .loc[] method uses the column name
# .iloc[] method used the column index
# .ix[] method can be used whenever you want to use a hybrid approach of either

# You will notice that some of the methods take on a list as a parameter
# By passing a list of parameters you can select more than one column
# ATTENTION: if you use a list to select a single column the data type you get back
#            is a dataframe as opposed to a series.

# Produce a series object
type(df.recency).__name__
type(df[["recency"]]).__name__


## Row Indexing

# You can use any of the .loc[], .iloc[] or .ix[] methods to do selection be row
df[0:2]
df.iloc[0:2, :]

# ATTENTION: .loc[], .ix[] methods are inclusive of the range of values selected
#           where .iloc[] is non inclusive 

df.loc[0:1, :] # returns 2 rows
df.iloc[0:1, :] # returns 1 rows


## Boolean Indexing

# Create new boolean series
df.recency < 7
df[df.recency < 7]

#==============================================================================
# Can combine multible boolean indexing conditionals - round brackets are 
# compulsory
# Also inside pandas you use & and | instead of  or and and
# The reason regular Python boolean operators cannot be used to combine Pandas
# boolean conditionals is because doing so causes ambiguity. 
# There are two ways the following incorrect statement can be interpreted (df.recency<7) or (df.newbie==0):
# 1. If the evaluation the statement (df.recency<7) or the evaluation the 
#    statement (df.newbie==0) results in anything besides the False, 
#    then select all records in the dataset.
# 2. Select all columns belonging to rows in the dataset where
#    either of the following statements are true: (df.recency<7) or (df.newbie==0).
# Option 2 is the desired functionality, but to avoid this ambiguity entirely, 
# Pandas overloads bit-wise operators on its dataframe and series objects. 
# Be sure to encapsulate each conditional in parenthesis to make this work!!!
#==============================================================================
 
df[(df.recency < 7) & (df.newbie == 0)]
 
# Writing to a slice
df[df.recency < 7] = -100
df 
 
# In the above example, -100 is rendered as an integer in the recency column,
# a string in the history_segment column and a float in the history column
 







