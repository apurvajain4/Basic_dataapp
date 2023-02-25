import streamlit as st
from matplotlib import image
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "Cars.jfif")
st.title("CARS")

img = image.imread(IMAGE_PATH)
st.image(img)

st.subheader('THIS IS A CAR')