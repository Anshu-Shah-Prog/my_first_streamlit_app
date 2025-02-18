import streamlit as st
import pandas as pd
st.header
df=pd.read_csv("Automobile.csv")
st.dataframe(df)
st.bar_chart(data=df,x='length',y='mileage',x_label='length', y_label="mileage", color="#ffaa0088")
