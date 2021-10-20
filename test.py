import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
df = pd.read_csv('india_telecom_performance_indicators.csv')
category_a = st.selectbox('Select major classification',df['Category_A'].unique())
category_b = st.selectbox('Select minor classification',df['Category_B'].unique())

df = df[df['Category_A'].eq(category_a) & df['Category_B'].eq(category_b)]
df = df.sort_values(by='Date')

fig, ax = plt.subplots()
ax = sns.lineplot(data=df,x='Date',y='value')
plt.xticks(rotation='vertical')
st.pyplot(fig)
