# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import csv


from PIL import Image
st.title("                   Google Trends ")
st.write("""###             For Keyword Analysis""")
st.write("""###             Developed by Marwan Zamkah""")
st.write("""###             """)
st.write("""###             """)
st.write("1- Video Tutorial For  Google Trends ")
st.video('http://www.youtube.com/watch?v=8xbvJdw4xBk')
r = st.slider('Select Number Of Keywords need to search in Google Trends last 5 Years in KSA  (Max 10) ', min_value=1, max_value=10)
try:
 keyword=[]
 for i in range(r):
     k=st.text_input("Enter The Keyword No "+str(i+1))
     keyword.append(k)

 submit = st.button('Search Google Trends .... 🔎')
 pytrends = TrendReq(hl='en-SA', tz=360)

 pytrends.build_payload(kw_list = keyword, cat=0, timeframe='today 5-y', geo='', gprop='')
 data=pytrends.interest_over_time()
 data2 = data.drop(labels=['isPartial'],axis='columns')

 image = data2.plot(title = 'Last 5 years on Google Trends')
 fig = image.get_figure()
 fig.savefig('figure.jpg')

 data2.to_csv('googletrends2.csv', encoding='utf_8_sig')
 df = pd.read_csv("googletrends2.csv",index_col=None)
 st.header("Number of Appearance in Google Trends Last Five Years for Keywords")
 st.table(df)
 img = Image.open("figure.jpg")
 st.image(img, width=800)
except:
    st.write("select the keywords")