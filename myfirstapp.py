import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Streamlit App")
option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C'])
if option=='line chart':
    chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [3.1242, 101.6861],
    columns=['lat', 'lon'])
    st.map(map_data) 
elif option=='T n C':
    st.write("test")


