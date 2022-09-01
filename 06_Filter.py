import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

df21 = pd.read_csv('List_of_Weather_Data_Cleaned_Transposed_TAVG_withLocation_v02.csv', sep=';')
print (df21)

print(df21.dtypes)

option = st.selectbox(
     'In welchem Monat möchtest du verreisen?',
     ('Januar', 'Februar', 'Maerz', 'April', 'Mai', 'Juni','Juli', 'August', 'September','Oktober', 'November', 'Dezember'))
