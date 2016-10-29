# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:05:26 2016

@author: Pavlos-Dell
"""

## Data Cleansing
#  In Data Wrangling, irrelevant, incomplete and missing data is either defaulted to
#  a specific value or removed entirely. NaN's are stripped out, typographical errors
#  are patched and perhaps even some data normalization occurs. 
#  The goal of Data Cleansing is to take wrangling a step further by rectifying
#  innacurate and inconsistent data to standardize it. Inconsistent data can lead 
#  to false intelligence being produced by your machine learning algorithms or not
#  no intelligence at all.
#
#  An example of when cleansing is necessary is when data comes from multiple sources.
#  If on average, a specific source consistently reports figures offset from others,
#  identifying the source of the error (be it faulty sensor or bad reporting etc.)
#  and the making calculated adjustments is a way to improve you overall data accuracy.
#  But without carefully balancing keeping your data as close as possible to its raw form
#  and making these error corrections, you might get accused of cooking your data. After all,
#  it's possible that there is no error at all. 