



'''

# Import the libraries that will assist in computation
# Pysal contains functions that perform Spatial Autocorrelation computation.
# numpy assists pysal with matrix handling functions and operations.
import pysal
import numpy as np

# Load the St. Louis homicide data set from pysal's examples.
f = pysal.open(pysal.examples.get_path("stl_hom.txt"))

# Select the single column of interest from the dataset.
y = np.array(f.by_col['HR8893'])

# Load the Rook continuity matrix for use in Moran's I computation.
w = pysal.open(pysal.examples.get_path('stl.gal')).read()

# Compute Moran's I for the data.
mi = pysal.Moran(y, w,two_tailed=False)

# Report that value of Moran's I
print (mi.I)

'''