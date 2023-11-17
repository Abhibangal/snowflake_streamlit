import streamlit as st
import pandas as pd
st.set_page_config(layout='wide', page_title='SNOWFLAKE_DATA_APP')
st.title('Ordershorder')
st.header("Healthy Food Deliver's")
st.subheader('🥑Veg/🐔Non-Veg')
st.text('🥦Kith n Kin')
st.text('Modern Cafe')
st.text('Shalu')
st.text('G2')

fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.mulitselect("Pick Some Fruits:",list(fruit_list.index))
st.dataframe(fruit_list)
