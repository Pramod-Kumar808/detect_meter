import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Detecttion", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

selected = option_menu(
        menu_title="Detection Choice",
        options=["Circle_Detection", "Using CV NN", "Using Yolo"],  
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
