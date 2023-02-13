import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Import and filter the world map dataset as above.
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")]

# Re-read the data file as a separate variable to perform transformations for proportional symbol mapping.
data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
data = data[(data.pop_est > 0) & (data.name != 'Antarctica')]

# Compute the centroid of each country from its shape file.
data['centroid_column'] = data.centroid

# Compute the gdp per capita as above.
data['gdp_per_cap'] =data.gdp_md_est / data.pop_est

# Construct a second dataframe with the XY coordinates of each centroid and the gpd per capita data.
centroids = list(data['centroid_column'])
df = pd.DataFrame({'y':[centroids[i].y for i in range(len(centroids))],'x':[centroids[i].x for i in range(len(centroids))],'data':list(data['gdp_per_cap'])})

print(df)

# Create a base plot showing the outlines of each country on the map.
base = world.plot(color='white',edgecolor='black')

# Annotate the base plot with circles scaled to the size of the data.
df.plot(kind='scatter', x='x', y='y',s=df['data']*1000,ax=base)

# Show the plot in the notebook.
plt.show()

pass
