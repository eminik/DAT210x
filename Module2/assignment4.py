import pandas as pd
import numpy as np

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
dat = pd.read_html("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2",
                   header = 1, match = "PLAYER")
# dat is a list of a single dataframe, therefore we need to extract it
dat = dat[0]
dat.head(100)

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
dat2 = dat.loc[~dat.apply(lambda x: sum(x.isnull()) >= 4, axis = 1), :]


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..

dat3 = dat2.loc[~(dat2.RK == 'RK'), :]

# TODO: Get rid of the 'RK' column
#
# .. your code here ..

dat3 = dat3.drop(axis = 1, labels = ["RK"])

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

dat3 = dat3.reset_index(drop = True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

dat3.dtypes
#dat3.ix[:, 2] = pd.to_numeric(dat3.iloc[:, 2], errors = "coerce")
dat3 = dat3.apply(lambda x: pd.to_numeric(x, errors = "ignore"), axis = 0)

dat3.dtypes

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

