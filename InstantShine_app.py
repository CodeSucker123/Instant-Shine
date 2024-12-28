import streamlit as st

st.title("Instant Shine")

from PIL import image
import cv2

img = Image.open("Instant")
#img = cv2.imread("Instant")
st.image(
  img , 
  width = 800 , 
  channels = "RGB"
)

