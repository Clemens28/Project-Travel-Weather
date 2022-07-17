import pandas as pd


df21 = pd.read_csv('List_of_Weather_Data_Cleaned_Tryout1.csv', sep=';')
print (df21)

print(df21.dtypes)

df22=df21['tavg'].transpose()

print(df22)

df22.to_csv('List_of_Weather_Data_Cleaned_Tryout1_Transposed.csv', mode='a', index=True, header=False)