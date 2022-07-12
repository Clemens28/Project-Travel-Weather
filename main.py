#python script
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Monthly, Point
import pandas as pd

# Set time period
start = datetime(1991, 1, 1)
end = datetime(2021, 12, 31)
location=Point(50.866,7.143)

# Get Monthly data
data = Monthly(location, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
#data.plot(y=['tavg', 'tmin', 'tmax'])
#plt.show()



df1=pd.DataFrame(data)

print(df1)

#df1_transposed=df1.T

#print(df1_transposed)

#df1_transposed.to_csv('Cologne_Location.csv')

# Build the avg. values per month of the last 30 years

### convert timestamp into string

df1['time'] = df1.index

df1['time']=df1['time'].dt.strftime('%Y-%m-%d')

print(df1.dtypes)

## cut the year and the day from the timestamp

mid=df1['time'].str[5:7]

#mid.columns=['month']

#mid= mid.rename(columns={'time': 'month'})

#print(mid)

#print(mid.dtypes)

df2= pd.concat([df1, mid], axis=1, join="inner")

print(df2.columns)
df2= df2.rename(columns={df2.columns[8]: 'month'})

print(df2)
print (df2.dtypes)
#df2 = df2.drop(df2.columns[(8)], axis=1)
print(df2)
#print(df3)