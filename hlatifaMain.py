import os
from wordcloud import WordCloud
import streamlit as st
import pandas as pd
from PIL import Image
from os import path
import numpy as np

# user inputs
st.title("Welcome to our wordCloud")
st.header('Please input the needed info in the sidebar and we will do the rest, Configure until you are satisfied !')
c = pd.DataFrame({'c': ['white', 'pink', 'black', 'blue', 'green', 'gray', 'purple']})
st.sidebar.title("Customize your wordcloud :")
color = st.sidebar.selectbox("please choose a background color", c)
wid = st.sidebar.slider("choose the width in px", 0, 700)
hei = st.sidebar.slider("choose the height in px", 0, 700)
l = pd.DataFrame({'l': ['Simple', 'Shaped']})
logo = st.sidebar.selectbox("How do you want your wordcloud?", l)

# text input
txt = st.sidebar.text_area("enter your text here")
try:
    if len(txt) == 0:
        raise ValueError("Empty text")
except ValueError:
    'Please enter your text! We can not generate your WordCloud with no words'
else:
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # read the mask image
    mpt_mask = np.array(Image.open(path.join(d, "mpt.png")))
    # ma = np.array(Image.open(path.join("C:\\Users\\lenovo\\Desktop\\WORDCLOUD-MASK\\cloud.png")))
    # Generate the wordcloud :
    if logo == 'Shaped':
        word = WordCloud(width=wid, height=hei, margin=0, background_color=color, mask=mpt_mask, contour_width=0.1,
                         contour_color='#006994').generate(txt)
    else:
        word = WordCloud(width=wid, height=hei, margin=0, background_color=color).generate(txt)
    # Store to file :
    word.to_file(path.join(d, 'wordcld.png'))
    st.subheader("\nHere is your wordcloud :")
    image = Image.open('wordcld.png')
    st.image(image, caption='wordcloud')

if st.sidebar.button("About (this can change your wordcloud!)"):
    st.sidebar.title("Who are we?")
    st.sidebar.text("We are first year Innovation and\nAMOA engineering students :")
    st.sidebar.text("Chadli Wiam\nAllam Laila\nZoufir Zineb\nLaaqira Chaima\nHammani Latifa")
    st.sidebar.title("What is this project about?")
    st.sidebar.text("Bghina gha nvalidiw hh")
