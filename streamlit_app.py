import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🤖 Machine Learning App")
st.info("This app builds a machine learning model")


with st.expander("Data Preview"):
  st.write("**Raw data**")
  df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df
  
  st.write("**X**")
  X=df.drop('species',axis=1)
  X
  
  st.write("**y**")
  y=df['species']
  y

with st.expander("Data Visualization"):
  st.markdown("**Penguin Bill Length vs. Bill Depth by Species**")
  st.scatter_chart(df,x="bill_length_mm",y="bill_depth_mm",color="species")
  fig=px.strip(df,x="island",y="body_mass_g", color="island",title="Body Mass Distributions by Island")
  st.plotly_chart(fig, use_container_width=True)
  fig=px.histogram(df,x="bill_length_mm",color="species",barmode="overlay",title="Distribution of Bill Length by Species")
  st.plotly_chart(fig)

with st.sidebar:
  st.header("Input Features")
  island=st.selectbox("Island",("Biscoe","Dream","Torgersen"))
  gender= st.selectbox("Gender",("Male","Female"))
  bill_length=st.slider('Bill Length (mm)',32.1, 59.6, 43.9)
  
      

