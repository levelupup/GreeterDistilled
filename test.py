import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
df = pd.read_csv('india_telecom_performance_indicators.csv')
category_a = st.selectbox('Select major classification',df['Category_A'].unique())


df = df[df['Category_A'].eq(category_a)]
df = df.sort_values(by='Date')
df = pd.pivot_table(df,index=['Category_A','Date'],columns=['Category_B'],values='value')

fig, ax = plt.subplots()
ax = sns.lineplot(data=df,x='Date',y=df.columns)
plt.xticks(rotation='vertical')
st.pyplot(fig)
