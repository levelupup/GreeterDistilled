import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

df = pd.read_csv('world_fdi.csv')
df['Economy Label'] = df['Economy Label'].replace({'Korea, Republic of':'South Korea','China, Taiwan Province of':'Taiwan'})

asia_economies = ['China','South Korea','Malaysia','Philippines',
                  'Singapore','Thailand','Viet Nam','India',
                  'Indonesia','Taiwan']
economy = st.sidebar.multiselect('Select economies',asia_economies)
mode = st.sidebar.selectbox('Select flow or stock',df['Mode Label'].unique())
direction = st.sidebar.selectbox('Select inward or outward',df['Direction Label'].unique())
year_values = st.sidebar.slider('Select years to watch',1970,2020,(2010,2020))

item = st.selectbox('select items',['US dollars at current prices in millions',
                                     'US dollars at current prices per capita',	
                                     'Percentage of total world',
                                     'Percentage of Gross Domestic Product'])

df = df[df['Year'].ge(year_values[0]) & df['Year'].le(year_values[1])]
df = df[df['Economy Label'].isin(economy) & df['Mode Label'].eq(mode) & df['Direction Label'].eq(direction)]
df = pd.pivot_table(df,index='Year',columns=['Economy Label'],values=item)
fig, ax = plt.subplots()

st.title('World FDI Watch')
st.header(item)
for eco in economy:
    plt.plot(df[eco])
plt.legend(economy,edgecolor='white')
st.pyplot(fig)
st.subheader('source: UNCTAD')
