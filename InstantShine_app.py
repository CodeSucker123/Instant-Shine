import streamlit as st
from PIL import Image
import cv2

img=Image.open("Instant.jpeg")
#img = cv2.imread("Instant.jpeg")
st.image(img)
