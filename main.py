import streamlit as st
import pandas as pd
from PIL import Image
from os import path
from wordcloud import WordCloud
import numpy as np

#user inputs
st.title("Welcome to our wordCloud")
'please input the needed info in the sidebar and we will do the rest !'
c = pd.DataFrame({'c':['white', 'pink', 'black', 'blue', 'green', 'purple']})
color = st.sidebar.selectbox("please choose a background color", c)
wid = st.sidebar.slider("choose the width in px", 0, 400, 1000)
hei = st.sidebar.slider("choose the height in px", 0, 400, 1000)

#text input
txt = st.sidebar.text_area("enter your text here")
try:
    if len(txt) == 0:
        raise ValueError("Empty text")
except ValueError:
    'Please enter your text! We can not generate your WordCloud with no words'
else:
    ma = np.array(Image.open(path.join("C:\\Users\\lenovo\\Desktop\\WORDCLOUD-MASK\\cloud.png")))
    word = WordCloud(width=wid, height=hei, margin=0, background_color=color, mask=ma, contour_width=0.5).generate(txt)
    word.to_file('wordcld.png')
    image = Image.open('wordcld.png')
    st.image(image, caption='wordcloud')