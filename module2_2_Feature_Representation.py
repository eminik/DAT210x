# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:42:51 2016

@author: nikaa
"""
import os
import pandas as pd

dataDirectory = "C:\Users\Pavlos-Dell\Desktop\Further Learning\edX\Programming with Python for Data Science\DAT210x\Module2"
os.chdir(dataDirectory)


## Textual Categorical Features

# Ordinal Features - (Ordered Categories)
#  For ordinal features, map the order as increasing integers in a single numeric
#  feature. Any entries not found in your designated categories list will be mapped to -1
ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']

df = pd.DataFrame({'satisfaction': ['Mad', 'Happy', 'Unhappy', 'Neutral']})

df.satisfaction = df.satisfaction.astype('category', ordered = True,
                                         categories = ordered_satisfaction).cat.codes
                                         
print df.satisfaction                   


# Nominal Features - (Unordered Categories)
#  Method 1 -  Can encode it similar as for ordinal features. This would be a
#  fast and dirty approach you can use while you are getting accustomed to your
#  dataset and taking it for its first run through your data analysis pipeline

df = pd.DataFrame({'vertebrates': ['Bird', 'Bird', 'Mammal', 'Fish', 
                                  'Amphibian', 'Reptile', 'Mammal']})

df['vertebrates'] = df.vertebrates.astype("category").cat.codes

print df

# ordered = Trued was not passed in, nor was a specific ordering listed. Because
# of this Pandas encodes your nominal entries in alhabetical order. The issue here
# is thatit introduces an ordering to a categorical list of items that inherently
# has none. This may cause problems.

# Method 2 -  A more precise approach would be to separate the distinct values 
# out into individual boolean features
df = pd.DataFrame({'vertebrates': ['Bird', 'Bird', 'Mammal', 'Fish', 
                                  'Amphibian', 'Reptile', 'Mammal']})

print df.vertebrates.unique()                                  
                                  
df = pd.get_dummies(df, columns = ['vertebrates'])

print df


## Pure Textual Features

#  If you are trying to featurize a body of text such as a webpage, a tweet, a
#  passage from a newspaper, an entire book, or a PDF document, creating a corpus
#  of words and counting their frequency is an extremely powerful encoding tool.
#  This is also know as the Bag of Words model, implemented with the CountVectorizer()
#  method in SciKit-Learn.

from sklearn.feature_extraction.text import CountVectorizer

corpus = ["Authman ran faster than Harry because he is an athlete.",
          "Authman and Harry ran faster and faster."]

bow = CountVectorizer()

X = bow.fit_transform(corpus) # Sparse Matrix

# X is a SciPy compressed, sparse, row matrix

bow.get_feature_names()

X.toarray()

# SciPy implements their sparse matrices like Python implements its dictionaries:
# only the keys that have a value get stored and everything else is assumed to be
# empty. You can always convert it to a regular Python list by using the .toarray()
# method, but this converts it to a dense array, which might not be desirable due to 
# memory reasons. To use your compressed sparse row matrix in Pandas, you are going to 
# want to convert it to a  Pandas SpareDataFrame



## Graphical Features
# One way to represent images as features is to resize the picture to a fixed
# size, convert it to grayscale, then encode every pixel as an element in a uni-
# dimensional feature array.

# Uses the Image module (PIL)
from scipy import misc

# Load the image up
img = misc.imread('Datasets\puzzle.png')
print img.shape, img.dtype

# Is the image too big? Resample it down by an order of magnitude
img = img[::2, ::2]
print img.shape, img.dtype

# Scale the colours from (0-255) to (0-1), then reshape to 1D array per pixel
img = (img/255.0).reshape(-1, 3)

red = img[:, 0]
green = img[:, 1]
blue = img[:, 2]

gray = 0.299 * red + 0.587 * green + 0.114 * blue

print img.shape, gray.shape


## Audio Features





















                      