import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

df21 = pd.read_csv('List_of_Weather_Data_Cleaned_Transposed_TAVG_withLocation_v02.csv', sep=';')
print (df21)

print(df21.dtypes)

#df_Januar=df21[['Januar', 'CITY','COUNTRY']].copy()
#df_Februar=df21[['Februar', 'CITY','COUNTRY']].copy()
#df_Maerz=df21[['Maerz', 'CITY','COUNTRY']].copy()
#df_April=df21[['April', 'CITY','COUNTRY']].copy()
#df_Mai=df21[['Mai', 'CITY','COUNTRY']].copy()
#df_Juni=df21[['Juni', 'CITY','COUNTRY']].copy()
#df_Juli=df21[['Juli', 'CITY','COUNTRY']].copy()
#df_August=df21[['August', 'CITY','COUNTRY']].copy()
#df_September=df21[['September', 'CITY','COUNTRY']].copy()
#df_Oktober=df21[['Oktober', 'CITY','COUNTRY']].copy()
#df_November=df21[['November', 'CITY','COUNTRY']].copy()
#df_Dezember=df21[['Dezember', 'CITY','COUNTRY']].copy()

#print(df_Januar)

option = st.selectbox(
     'In welchem Monat möchtest du verreisen?',
     ('Januar', 'Februar', 'Maerz', 'April', 'Mai', 'Juni','Juli', 'August', 'September','Oktober', 'November', 'Dezember'))

st.write('Du verreist im:', option)

n_rows=1000

sliders = {
    "Januar": st.sidebar.slider(
        "Wie warm soll es im Januar sein?", min_value=0.0, max_value=50.0, value=(0.0, 1.0), step=0.01
    ),
    "Februar": st.sidebar.slider(
        "Wie warm soll es im Februar sein?", min_value=0.0, max_value=50.0, value=(0.0, 1.0), step=0.01
    ),
}
filter = df21  

for feature_name, slider in sliders.items():
    
    filter = (
         (df21[feature_name] >= slider[0])
        & (df21[feature_name] <= slider[1])
    )
    

st.write(df21[filter])

