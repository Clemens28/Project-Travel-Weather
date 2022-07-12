#python script
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Monthly, Point
import pandas as pd

# Set time period
start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)
location=Point(50.866,7.143),

# Get Monthly data
data = Monthly(location, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()



df1=pd.DataFrame(data)

df1_transposed=df1.T

print(df1_transposed)

df1_transposed.to_csv('Cologne_Location.csv')
