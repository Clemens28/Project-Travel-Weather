import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

df20 = pd.read_csv('List_of_Weather_Data_Cleaned_Transposed_TAVG_v01.csv', sep=';')
print (df20)

print(df20.dtypes)

option = st.selectbox(
     'In welchem Monat möchtest du verreisen?',
     ('Januar', 'Februar', 'Maerz', 'April', 'Mai', 'Juni','Juli', 'August', 'September','Oktober', 'November', 'Dezember'))

st.write('You selected:', option)
tooltip = {
    'html': 'Durchschnittliche Temparatur in Grad Celsius:</b></b>',
    'style': {'background': 'grey', 'color': 'white', 'font-family': 'Helvetica Neue', 'z-index': '10000'}}
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=50.93,
         longitude=6.95,
         zoom=5,
         pitch=50,
     ),
     tooltip=tooltip,
     layers=[
         #pdk.Layer(
           # 'HexagonLayer',
           # data=df20,
           # get_position=[df20.columns[1], df20.columns[0]],
           # auto_highlight= True,
           # radius=10000,
           # elevation_scale=5000,
           # elevation_range=[0, 50],
           # pickable=True,
           # extruded=True,
        # ),
         #pdk.Layer(
           #'HeatmapLayer',
           #  data=df20,
           #  opacity=0.9,
           #  get_position='[lon, lat]',
           #  aggregation=pdk.types.String("MEAN"),
           # threshold=1,
           # get_weight="weight",
           # pickable=True,
         #),
         pdk.Layer(
             'ColumnLayer',
             data=df20,
             get_position=[df20.columns[1], df20.columns[0]],
             auto_highlight= True,
             get_elevation= option,
             elevation_scale=5000,
             radius=7000,
             get_fill_color=['April * 10', 30, 0, 160],
             pickable=True,
         

)
     ],
    ))