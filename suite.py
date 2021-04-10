import streamlit as st
import pandas as pd
from PIL import Image
from os import path
from wordcloud import WordCloud
import numpy as np

#user inputs
st.title("Welcome to our wordCloud")
'please input the needed info in the sidebar and we will do the rest !'

bc = st.sidebar.color_picker("Pick a color for the background of your wordcloud",value='#FFFFFF')
text_color = st.sidebar.radio("Do you want for the words in your cloud to have a specific color ?", ["yes", "No"])
if text_color == "yes":
    c = st.sidebar.color_picker("Pick a color for your text")
    val = True
else:
    val = False



# color palette for contour

wid = st.sidebar.slider("choose the width in px", 0, 400, 1000)
hei = st.sidebar.slider("choose the height in px", 0, 400, 1000)
#mask or no mask
l = pd.DataFrame({'l': ['Simple', 'Shaped']})
logo = st.sidebar.selectbox("How do you want your wordcloud?", l)
if logo == 'Shaped':
    contour = st.sidebar.radio("Do you want your word cloud to have a contour?", ["Yes", "No"])
    if contour == "Yes":
        z = pd.DataFrame({'z': ['Cloud', 'Circle', 'Mickey-Mouse','Heart']})
        ma = st.sidebar.selectbox("Choose a shape for your wordcloud", z)
        if ma == 'Cloud':
            ma = np.array(Image.open(path.join("cloud.png")))
        elif ma == 'Circle':
            ma = np.array(Image.open(path.join("cercle.png")))
        elif ma == 'Mickey-Mouse':
            ma = np.array(Image.open(path.join("mickey-mouse.png")))
        else :
            ma = np.array(Image.open(path.join("coeur.png")))
        cd = 0.5
        cd_c = st.sidebar.color_picker("Pick a color for your contour")
    else:
        cd = 0
        cd_c = None

t=pd.DataFrame({'s':['enter a text','upload a file']})
#text input
Place_holder=st.sidebar.selectbox("how do you want to submit the text ?",t)
if Place_holder=='enter a text':
    txt=st.sidebar.text_area("enter your text here")
else:
    #fichier=st.sidebar.file_uploader('test',type='txt',accept_multiple_files=False)
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    try:
        txt=uploaded_file.getvalue().decode("utf-8")
    except AttributeError:
        txt=''
        'please upload a text file'
    except UnicodeDecodeError:
        'Wrong file format, we only accept .txt extension !'
        txt=''
try:
    if len(txt) == 0:
        raise ValueError("Empty text")
except ValueError:
    ''
else:
    if val == True and logo== 'Shaped' :
        word = WordCloud(width=wid, height=hei, margin=0, background_color=bc, mask=ma, contour_width=0.5,
                         color_func=lambda *args, **kwargs: c,contour_color=cd_c).generate(txt)
    elif val == False and logo == 'Shaped' :
         word = WordCloud(width=wid, height=hei, margin=0, background_color=bc, mask=ma, contour_width=cd,contour_color=cd_c).generate(txt)
    elif val == False and logo == 'Simple' :
         word = WordCloud(width=wid, height=hei, margin=0, background_color=bc).generate(txt)
    else:
         word =WordCloud(width=wid, height=hei, margin=0, background_color=bc,color_func=lambda *args, **kwargs: c).generate(txt)
    word.to_file('wordcld.png')
    st.subheader("\nHere is your wordcloud :")
    image = Image.open('wordcld.png')
    st.image(image, caption='wordcloud')
