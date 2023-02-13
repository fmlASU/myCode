import os
os.environ['USE_PYGEOS'] = '0'

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

us_income= pd.read_csv('D:\myCode\ASU_578\\usjoin.csv')

#print(us_income)

us_income_shape = gpd.read_file('D:\myCode\ASU_578\myshape.shp')

for indexs in us_income_shape.index:
    STATE_FIPS = int(us_income_shape.loc[indexs].values[5])
    #Income = us_income.loc[us_income['STATE_FIPS'] == STATE_FIPS]['1929'].values[-1]
    Income = us_income.loc[us_income['STATE_FIPS'] == STATE_FIPS]['2009'].values[-1]
    us_income_shape.loc[indexs, 'Income'] = Income

us_income_shape['centroid_column'] = us_income_shape.centroid
centroids = list(us_income_shape['centroid_column'])
df = pd.DataFrame({'y':[centroids[i].y for i in range(len(centroids))],'x':[centroids[i].x for i in range(len(centroids))],'data':list(us_income_shape['Income'])})

#print(df)

base = us_income_shape.plot(color='white',edgecolor='black')

df.plot(kind='scatter', x='x', y='y',s=df['data']*0.001,ax=base)
plt.title('proportional symbol map of the per capita income of each US state in 2009')
plt.show()

pass


