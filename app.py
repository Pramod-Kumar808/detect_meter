import streamlit as st
from streamlit_option_menu import option_menu
import cv2
import numpy as np
import os

st.set_page_config(page_title="Detection", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# @st.cache
# def load_image(image):
#     image = Image.open(image)
#     return image

# def save_uploadedfile(uploadedfile):
#      with open(os.path.join("inputs",uploadedfile.name),"wb") as f:
#          f.write(uploadedfile.getbuffer())
#      return st.success("Saved File:{}".format(uploadedfile.name))

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
        file_bytes = np.asarray(bytearray(image_upload.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image_gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        st.image(opencv_image_gray)