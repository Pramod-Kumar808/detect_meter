import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import cv2
import base64, os
import numpy as np
from pythonping import ping
import sys

st.set_page_config(page_title="Detection", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

@st.cache
def load_image(image):
    image = Image.open(image)
    return image

def save_uploadedfile(uploadedfile):
     with open(os.path.join("inputs",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{}".format(uploadedfile.name))

selected = option_menu(
        menu_title="Detection Choice",
        options=["Circle detect", "Using CV NN", "Using Yolo"],  
        icons=["house", "book", "envelope"],  
        menu_icon="cast",  
        default_index=0, 
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        },
    )

if selected == "Circle detect": 
    image_upload = st.file_uploader("Guage meter image", type=['png', 'jpg'])
    if image_upload is not None:
        image = Image.open(image_upload)
    #    save_uploadedfile(image_upload)
    #    data = "inputs/" + image_upload.name
    #    open_cv_read_image = cv2.imread(data)
    #    gray_image = cv2.cvtColor(open_cv_read_image, cv2.COLOR_BGR2GRAY)
    #    st.image(image)
        img_array = np.array(image)
        image_read = Image.fromarray(img_array.astype(np.uint8))
        open_cv_read_image = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
        st.image(open_cv_read_image)

text = st.text_input("Type the ip address here")
if text == "":
    st.error("Input the text")
else:
    scan = ping('127.0.0.1', timeout = 1,count = 1, out = sys.stdout)
    st.code(scan)