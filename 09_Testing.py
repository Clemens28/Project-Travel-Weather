import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(
    np.random.rand(9, 4),
    index=["air","coffee","orange","whitebread","potato","wine","beer","wheatbread","carrot"],
)

print(chart_data)

df23 = pd.read_csv('List_of_Weather_Data_Cleaned_Transposed_TAVG_withLocation_v03_short.csv', sep=';')
print (df23.dtypes)



# Vertical stacked bar chart
#st.bar_chart(chart_data)

# Convert wide-form data to long-form
# See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
data = pd.melt(df23.reset_index(), id_vars=["index"])

# Horizontal stacked bar chart
chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("value", type="quantitative", title=""),
        y=alt.Y("index", type="nominal", title=""),
        color=alt.Color("variable", type="nominal", title=""),
        order=alt.Order("variable", sort="descending"),
    )
)

#st.altair_chart(chart, use_container_width=True)