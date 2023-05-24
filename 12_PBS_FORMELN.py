from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Monthly, Point
import pandas as pd

df001 = pd.read_csv('pe-prognosen-2023-05-19.csv', sep=',')




# Umsetzungsquote > 85% checken

df001.astype({'Umsetzungsquote IST PE': 'float64'}).dtypes

df001.loc[df001['Umsetzungsquote IST PE'] <= 0.85, 'Umsetzungsquote > 85 %'] = 'False' 
df001.loc[df001['Umsetzungsquote IST PE'] > 0.85, 'Umsetzungsquote > 85 %'] = 'True'

print (df001.dtypes)

print(df001['Umsetzungsquote > 85 %'])




# Bester Increase eines Marktes checken

max_increase_per_store = df001.groupby('ma_id')['ZUSÄTZLICHER Jahresumsatz nach Anpassung'].max()

df002 = df001.merge(max_increase_per_store, left_on='ma_id', right_index=True, suffixes=('', '_max_per_store'))

print(df002.dtypes)

print(max_increase_per_store)

#df002.to_csv('EMPFEHLUNGSLISTE_MIT_FILTER.csv')



# Bester Decrease eines Marktes checken

decreases = df002[df002['ZUSÄTZLICHER Jahresumsatz nach Anpassung'] < 0]

best_decrease_per_store = decreases.groupby('ma_id')['ZUSÄTZLICHER Jahresumsatz nach Anpassung'].max()

df003 = df002.merge(best_decrease_per_store, left_on='ma_id', right_index=True, suffixes=('', '_best_neg_per_store'))


df003.to_csv('EMPFEHLUNGSLISTE_MIT_FILTER.csv')