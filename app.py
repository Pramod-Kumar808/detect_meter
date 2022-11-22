import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import cv2

st.set_page_config(page_title="Detection", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

@st.cache
def load_image(image):
    image = Image.open(image)
    return image

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
        st.image(load_image(image_upload))
        cv_image_read = cv2.imread(image_upload)
        gray = cv2.cvtColor(cv_image_read, cv2.COLOR_BGR2GRAY)
        st.image(gray)