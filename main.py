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

df2= pd.concat([df1, mid], axis=1, join="inner")

print(df2.columns)
df2= df2.rename(columns={df2.columns[8]: 'month'})

print(df2)
print (df2.dtypes)

print(df2)

df3 = df2.iloc[: , [0, 1, 2, 3, 4, 5, 6, 8]].copy()

print(df3)

avg_tavg_01=df3.loc[df3['month'] == '01', 'tavg'].mean()
avg_tavg_02=df3.loc[df3['month'] == '02', 'tavg'].mean()
avg_tavg_03=df3.loc[df3['month'] == '03', 'tavg'].mean()
avg_tavg_04=df3.loc[df3['month'] == '04', 'tavg'].mean()
avg_tavg_05=df3.loc[df3['month'] == '05', 'tavg'].mean()
avg_tavg_06=df3.loc[df3['month'] == '06', 'tavg'].mean()
avg_tavg_07=df3.loc[df3['month'] == '07', 'tavg'].mean()
avg_tavg_08=df3.loc[df3['month'] == '08', 'tavg'].mean()
avg_tavg_09=df3.loc[df3['month'] == '09', 'tavg'].mean()
avg_tavg_10=df3.loc[df3['month'] == '10', 'tavg'].mean()
avg_tavg_11=df3.loc[df3['month'] == '11', 'tavg'].mean()
avg_tavg_12=df3.loc[df3['month'] == '12', 'tavg'].mean()

print(avg_tavg_01)
print(avg_tavg_02)
print(avg_tavg_07)