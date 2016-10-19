import pandas as pd
import numpy as np
dataDirectory = "C:\Users\NikaA\Desktop\DAT210x-master\Module2"
os.chdir(dataDirectory)

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
dat = pd.read_csv(filepath_or_buffer = "Datasets\servo.data",
                  names = ['motor', 'screw', 'pgain', 'vgain', 'class'])

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
np.sum(dat.vgain == 5)

# or

len(dat[dat.vgain == 5].index)

# or

dat[dat.vgain == 5].shape[0]

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..

len(dat[(dat.motor == 'E') & (dat.screw == 'E')].index)

sum((dat.motor == 'E') & (dat.screw == 'E'))

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

print np.mean(dat.loc[dat.pgain == 4, ["vgain"]])

print dat.loc[dat.pgain == 4, ["vgain"]].mean()

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



