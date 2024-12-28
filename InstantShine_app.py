import streamlit as st
pip install opencv-python
from PIL import Image
import cv2

img = Image.open("Instant.jpeg")
#img = cv2.imread("Instant.jpeg")
st.image(
  img , 
  width = 800 , 
  channels = "RGB"
)

