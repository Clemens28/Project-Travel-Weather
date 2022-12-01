import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

df = pd.read_csv('List_of_Weather_Data_Cleaned_ALL_withLocation_v01.csv', sep=';')
#print (df21)

print(df.dtypes)

pd.to_numeric(df['PRCP'])
pd.to_numeric(df['TSUN'])


# Data import & columns


Month = list(df['MONTH'].drop_duplicates())


# App

# Sidebar - title & filters
st.sidebar.markdown('### Data Filters')
month_choice = st.sidebar.multiselect(
    'Choose Month:', Month, default=Month)
tavg_choice = st.sidebar.slider(
    'Choose Minumum Average Temperature:', min_value=0.0, max_value=50.0, step=0.1)
prcp_choice = st.sidebar.slider(
    'Choose Maximum Average Precipitation:', min_value=0.0, max_value=500.0, step=0.1)
#tsun_choice = st.sidebar.slider(
    #'Choose Minumum Average Hours of Sun:', min_value=0.0, max_value=11000.0, step=0.1)

df = df[df['MONTH'].isin(month_choice)]
df = df[df['AVG_TEMP'] > tavg_choice]
df = df[df['PRCP'] < prcp_choice]
#df = df[df['TSUN'] > tsun_choice]
# Main
st.title(f"Where to travel next?")

# Main - dataframes
st.markdown('Averange Temperatures')

st.dataframe(df.sort_values('AVG_TEMP',
             ascending=False).reset_index(drop=True))


# Main - charts
st.markdown('World Map')


tooltip = {
    'html': 'Durchschnittliche Temparatur in Grad Celsius:</b></b>',
    'style': {'background': 'grey', 'color': 'white', 'font-family': 'Helvetica Neue', 'z-index': '10000'}}

st.map(df)




