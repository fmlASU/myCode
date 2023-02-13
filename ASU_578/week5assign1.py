import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


us_income= pd.read_csv('D:\myCode\ASU_578\\usjoin.csv')

#print(us_income)

us_income_shape = gpd.read_file('D:\myCode\ASU_578\myshape.shp')

for indexs in us_income_shape.index:
    STATE_FIPS = int(us_income_shape.loc[indexs].values[5])
    Income = us_income.loc[us_income['STATE_FIPS'] == STATE_FIPS]['2009'].values[0]
    us_income_shape.loc[indexs, 'Income'] = Income

us_income_shape.plot(column='Income', legend = True, legend_kwds={'label': "Income",'orientation': "horizontal"})
plt.title('Income of each US state in 2009', fontsize = 20)
plt.show()

pass


'''
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pysal



us_income = pd.read_csv(pysal.examples.get_path('usjoin.csv'))
us_income_shape = gpd.read_file(pysal.examples.get_path('us48.shp'))

us_income_2009 = us_income[['STATE_FIPS', '2009']]
us_income_2009 

state_shape = us_income_shape[['geometry', 'STATE_FIPS']]
state_shape['STATE_FIPS'] = state_shape['STATE_FIPS'].astype(int)

'''