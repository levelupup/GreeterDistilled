import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
df = pd.read_csv('world_fdi.csv')

economy = st.sidebar.multiselect('Select economies',df['Economy Label'].unique())
mode = st.sidebar.multiselect('Select modes',df['Mode Label'].unique())
direction = st.sidebar.multiselect('Select directions',df['Direction Label'].unique())
year = st.sidebar.multiselect('Select years',df['Year'].unique())
item = st.selectbox('select items',['US dollars at current prices in millions',
                                     'US dollars at current prices per capita',	
                                     'Percentage of total world',
                                     'Percentage of Gross Domestic Product'])

df = df[df['Economy Label'].eq(economy) & df['Mode Label'].eq(mode) & df['Direction Label'].eq(direction) & df['Year'].eq(year)]


fig, ax = plt.subplots()
ax = sns.lineplot(data=df,x='Year',y=item)
plt.xticks(rotation='vertical')
st.pyplot(fig)
