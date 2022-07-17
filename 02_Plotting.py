import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

df20 = pd.read_csv('List_of_Weather_Data_Cleaned.csv', sep=';')
print (df20)

print(df20.dtypes)

option = st.selectbox(
     'In welchem Monat möchtest du verreisen?',
     ('Januar', 'Februar', 'Maerz', 'April', 'Mai', 'Juni','Juli', 'August', 'September','Oktober', 'November', 'Dezember'))

st.write('You selected:', option)
tooltip = {
    'html': '</b> {option} </b> Durchschnittliche Temparatur in Grad Celsius',
    'style': {'background': 'grey', 'color': 'white', 'font-family': 'Helvetica Neue', 'z-index': '10000'}}
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=50.93,
         longitude=6.95,
         zoom=11,
         pitch=50,
     ),
     tooltip=tooltip,
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df20,
            get_position=[df20.columns[1], df20.columns[0]],
            radius=10000,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
        # pdk.Layer(
         #  'ScatterplotLayer',
           #  data=df,
           #  get_position='[lon, lat]',
            # get_color='[200, 30, 0, 160]',
            # get_radius=200,
         #),
         pdk.Layer(
             'ColumnLayer',
             data=df20,
             get_position=[df20.columns[1], df20.columns[0]],
             get_elevation= option,
             elevation_scale=500,
             radius=10000,
             get_fill_color=[200, 30, 0, 160],
             pickable=True,
             auto_highlight=True,
)
     ],
    ))