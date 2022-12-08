import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk
import plotly.express as px 

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
st.markdown('Average Temperatures')

st.dataframe(data=df.sort_values('AVG_TEMP',
             ascending=False).reset_index(drop=True), use_container_width=True)


# Main - charts

st.markdown('Chart')

df.set_index(df['CITY'])
#df['CITY'] = df.index

#chart_data1=pd.DataFrame(df,rotation='horizontal')
#st.bar_chart(data=df['AVG_TEMP'])
df = df[df['MONTH'].isin(month_choice)]

fig1=px.bar(df,x='AVG_TEMP',y='CITY', orientation='h', width=650, height=500)
#st.write(fig1)

fig2=px.bar(df,x='PRCP',y='CITY', orientation='h', width=500, height=500)

col1,col2=st.columns(2)
with col1:
        st.header('AVG Temperature')
        st.write(fig1)
with col2:
        st.header('AVG Precipitation')
        st.write(fig2)


st.markdown('World Map')


tooltip = {
    'html': 'Durchschnittliche Temparatur in Grad Celsius:</b></b>',
    'style': {'background': 'grey', 'color': 'white', 'font-family': 'Helvetica Neue', 'z-index': '10000'}}


st.map(df)




