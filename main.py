#python script
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Monthly, Point
import pandas as pd

# Set time period
start = datetime(1991, 1, 1)
end = datetime(2021, 12, 31)
location_lat=9.512
location_lon=100.013
location=Point(location_lat,location_lon)



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

avg_tmin_01=df3.loc[df3['month'] == '01', 'tmin'].mean()
avg_tmin_02=df3.loc[df3['month'] == '02', 'tmin'].mean()
avg_tmin_03=df3.loc[df3['month'] == '03', 'tmin'].mean()
avg_tmin_04=df3.loc[df3['month'] == '04', 'tmin'].mean()
avg_tmin_05=df3.loc[df3['month'] == '05', 'tmin'].mean()
avg_tmin_06=df3.loc[df3['month'] == '06', 'tmin'].mean()
avg_tmin_07=df3.loc[df3['month'] == '07', 'tmin'].mean()
avg_tmin_08=df3.loc[df3['month'] == '08', 'tmin'].mean()
avg_tmin_09=df3.loc[df3['month'] == '09', 'tmin'].mean()
avg_tmin_10=df3.loc[df3['month'] == '10', 'tmin'].mean()
avg_tmin_11=df3.loc[df3['month'] == '11', 'tmin'].mean()
avg_tmin_12=df3.loc[df3['month'] == '12', 'tmin'].mean()

print(avg_tmin_01)
print(avg_tmin_02)
print(avg_tmin_07)

avg_tmax_01=df3.loc[df3['month'] == '01', 'tmax'].mean()
avg_tmax_02=df3.loc[df3['month'] == '02', 'tmax'].mean()
avg_tmax_03=df3.loc[df3['month'] == '03', 'tmax'].mean()
avg_tmax_04=df3.loc[df3['month'] == '04', 'tmax'].mean()
avg_tmax_05=df3.loc[df3['month'] == '05', 'tmax'].mean()
avg_tmax_06=df3.loc[df3['month'] == '06', 'tmax'].mean()
avg_tmax_07=df3.loc[df3['month'] == '07', 'tmax'].mean()
avg_tmax_08=df3.loc[df3['month'] == '08', 'tmax'].mean()
avg_tmax_09=df3.loc[df3['month'] == '09', 'tmax'].mean()
avg_tmax_10=df3.loc[df3['month'] == '10', 'tmax'].mean()
avg_tmax_11=df3.loc[df3['month'] == '11', 'tmax'].mean()
avg_tmax_12=df3.loc[df3['month'] == '12', 'tmax'].mean()

print(avg_tmax_01)
print(avg_tmax_02)
print(avg_tmax_07)

avg_prcp_01=df3.loc[df3['month'] == '01', 'prcp'].mean()
avg_prcp_02=df3.loc[df3['month'] == '02', 'prcp'].mean()
avg_prcp_03=df3.loc[df3['month'] == '03', 'prcp'].mean()
avg_prcp_04=df3.loc[df3['month'] == '04', 'prcp'].mean()
avg_prcp_05=df3.loc[df3['month'] == '05', 'prcp'].mean()
avg_prcp_06=df3.loc[df3['month'] == '06', 'prcp'].mean()
avg_prcp_07=df3.loc[df3['month'] == '07', 'prcp'].mean()
avg_prcp_08=df3.loc[df3['month'] == '08', 'prcp'].mean()
avg_prcp_09=df3.loc[df3['month'] == '09', 'prcp'].mean()
avg_prcp_10=df3.loc[df3['month'] == '10', 'prcp'].mean()
avg_prcp_11=df3.loc[df3['month'] == '11', 'prcp'].mean()
avg_prcp_12=df3.loc[df3['month'] == '12', 'prcp'].mean()

avg_wspd_01=df3.loc[df3['month'] == '01', 'wspd'].mean()
avg_wspd_02=df3.loc[df3['month'] == '02', 'wspd'].mean()
avg_wspd_03=df3.loc[df3['month'] == '03', 'wspd'].mean()
avg_wspd_04=df3.loc[df3['month'] == '04', 'wspd'].mean()
avg_wspd_05=df3.loc[df3['month'] == '05', 'wspd'].mean()
avg_wspd_06=df3.loc[df3['month'] == '06', 'wspd'].mean()
avg_wspd_07=df3.loc[df3['month'] == '07', 'wspd'].mean()
avg_wspd_08=df3.loc[df3['month'] == '08', 'wspd'].mean()
avg_wspd_09=df3.loc[df3['month'] == '09', 'wspd'].mean()
avg_wspd_10=df3.loc[df3['month'] == '10', 'wspd'].mean()
avg_wspd_11=df3.loc[df3['month'] == '11', 'wspd'].mean()
avg_wspd_12=df3.loc[df3['month'] == '12', 'wspd'].mean()

avg_pres_01=df3.loc[df3['month'] == '01', 'pres'].mean()
avg_pres_02=df3.loc[df3['month'] == '02', 'pres'].mean()
avg_pres_03=df3.loc[df3['month'] == '03', 'pres'].mean()
avg_pres_04=df3.loc[df3['month'] == '04', 'pres'].mean()
avg_pres_05=df3.loc[df3['month'] == '05', 'pres'].mean()
avg_pres_06=df3.loc[df3['month'] == '06', 'pres'].mean()
avg_pres_07=df3.loc[df3['month'] == '07', 'pres'].mean()
avg_pres_08=df3.loc[df3['month'] == '08', 'pres'].mean()
avg_pres_09=df3.loc[df3['month'] == '09', 'pres'].mean()
avg_pres_10=df3.loc[df3['month'] == '10', 'pres'].mean()
avg_pres_11=df3.loc[df3['month'] == '11', 'pres'].mean()
avg_pres_12=df3.loc[df3['month'] == '12', 'pres'].mean()

avg_tsun_01=df3.loc[df3['month'] == '01', 'tsun'].mean()
avg_tsun_02=df3.loc[df3['month'] == '02', 'tsun'].mean()
avg_tsun_03=df3.loc[df3['month'] == '03', 'tsun'].mean()
avg_tsun_04=df3.loc[df3['month'] == '04', 'tsun'].mean()
avg_tsun_05=df3.loc[df3['month'] == '05', 'tsun'].mean()
avg_tsun_06=df3.loc[df3['month'] == '06', 'tsun'].mean()
avg_tsun_07=df3.loc[df3['month'] == '07', 'tsun'].mean()
avg_tsun_08=df3.loc[df3['month'] == '08', 'tsun'].mean()
avg_tsun_09=df3.loc[df3['month'] == '09', 'tsun'].mean()
avg_tsun_10=df3.loc[df3['month'] == '10', 'tsun'].mean()
avg_tsun_11=df3.loc[df3['month'] == '11', 'tsun'].mean()
avg_tsun_12=df3.loc[df3['month'] == '12', 'tsun'].mean()


d={'lat':[location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat, location_lat], 
'lon':[location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon, location_lon], 
'month':['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'], 
'tavg':[avg_tavg_01, avg_tavg_02, avg_tavg_03, avg_tavg_04, avg_tavg_05, avg_tavg_06, avg_tavg_07, avg_tavg_08, avg_tavg_09, avg_tavg_10, avg_tavg_11, avg_tavg_12],
'tmin':[avg_tmin_01, avg_tmin_02, avg_tmin_03, avg_tmin_04, avg_tmin_05, avg_tmin_06, avg_tmin_07, avg_tmin_08, avg_tmin_09, avg_tmin_10, avg_tmin_11, avg_tmin_12],
'tmax':[avg_tmax_01, avg_tmax_02, avg_tmax_03, avg_tmax_04, avg_tmax_05, avg_tmax_06, avg_tmax_07, avg_tmax_08, avg_tmax_09, avg_tmax_10, avg_tmax_11, avg_tmax_12],
'prcp':[avg_prcp_01, avg_prcp_02, avg_prcp_03, avg_prcp_04, avg_prcp_05, avg_prcp_06, avg_prcp_07, avg_prcp_08, avg_prcp_09, avg_prcp_10, avg_prcp_11, avg_prcp_12],
'wspd':[avg_wspd_01, avg_wspd_02, avg_wspd_03, avg_wspd_04, avg_wspd_05, avg_wspd_06, avg_wspd_07, avg_wspd_08, avg_wspd_09, avg_wspd_10, avg_wspd_11, avg_wspd_12],
'pres':[avg_pres_01, avg_pres_02, avg_pres_03, avg_pres_04, avg_pres_05, avg_pres_06, avg_pres_07, avg_pres_08, avg_pres_09, avg_pres_10, avg_pres_11, avg_pres_12],
'tsun':[avg_tsun_01, avg_tsun_02, avg_tsun_03, avg_tsun_04, avg_tsun_05, avg_tsun_06, avg_tsun_07, avg_tsun_08, avg_tsun_09, avg_tsun_10, avg_tsun_11, avg_tsun_12],
}

df4=pd.DataFrame(data=d)

print(df4)

## This creates a csv to write all the data in. Only run once to initially create the csv file

#df4.to_csv("List_of_Weather_Data.csv")

##This writes the weather data of the input coordinates into the csv every time the script runs

df4.to_csv('List_of_Weather_Data.csv', mode='a', index=True, header=False)

