import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning App")
st.info("This app builds a machine learning model")


with st.expander("Data Preview"):
  st.write("**Raw data**")
  df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")

st.write("**X**")
X=df.drop('species',axis=1)
X

st.write("**y**")
y=df['species']
y
          
