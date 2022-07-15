import pandas as pd

df10 = pd.read_csv('GlobalAirportDatabase_Updated_v0.1.csv', sep=';')
print (df10)

location_lat=df10.iat[0,3]
location_lon=df10.iat[0,4]

print(location_lat)
print(location_lon)

#df10.astype({'LAT':float,'LON':float},errors='raise')

print(df10.dtypes)


for 'LAT' in df10:
  print('LAT')