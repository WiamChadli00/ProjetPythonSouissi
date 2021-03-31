import streamlit as st
import pandas as pd
from PIL import Image
from os import path
from wordcloud import WordCloud
import numpy as np

# Header section
st.title("Welcome to our wordCloud")
st.markdown("_please input the needed information in the sidebar and we will do the rest !_")
st.markdown("____")


# User input
# color palette for background and text
bc = st.sidebar.color_picker("Pick a color for the background of your wordcloud")
c = st.sidebar.color_picker("Pick a color for your text")

# color palette for contour
contour = st.sidebar.radio("Do you want your word cloud to have a contour?", ["Yes", "No"])
if contour == "Yes":
    cd = 0.5
    cd_c = st.sidebar.color_picker("Pick a color for your contour")
else:
    cd = 0
    cd_c = None

# Width and height and contour
st.sidebar.markdown("----")
wid = st.sidebar.slider("choose the width in px", 0, 400, 1000)
hei = st.sidebar.slider("choose the height in px", 0, 400, 1000)

t = pd.DataFrame({'s': ['enter a text', "download a text file"]})

# empty slot to use later for the wordcloud
empty_place = st.empty()

information = st.beta_expander("Who are we?", False)
information.text("We are INPT first year students...")

# text input
st.sidebar.markdown("----")
Place_holder = st.sidebar.selectbox("how do you want to submit the text ?", t)
if Place_holder == 'enter a text':
    txt = st.sidebar.text_area("enter your text here")
else:
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    try:
        txt = uploaded_file.getvalue().decode("utf-8")
    except AttributeError:
        txt = ''
        'please upload a text file'
    except UnicodeDecodeError:
        'Wrong file format, we only accept .txt extension !'
        txt = ''
try:
    if len(txt) == 0:
        raise ValueError("Empty text")
except ValueError:
    ''
else:
    ma = np.array(Image.open(path.join("ppWhite.png")))
    word = WordCloud(width=wid, height=hei, margin=0, color_func=lambda *args, **kwargs: c, background_color=bc,
                     mask=ma, contour_width=cd, contour_color=cd_c).generate(txt)
    word.to_file('wordcloud.png')
    image = Image.open('wordcloud.png')
    empty_place.image(image, caption="Your customized Word cloud")
    # Putting the word cloud image in the empty slot we reserved before