import streamlit as st
from process import Process
from PIL import Image

st.title("Background Image Styler")

img_uploaded_file = st.file_uploader('Upload Image File')
back_uploaded_file = st.file_uploader('Upload Background Image File')
if (img_uploaded_file is not None) and (back_uploaded_file is not None):
    h = st.slider('Lower and Higher Values of H', 0, 255, (35, 85))
    s = st.slider('Lower and Higher Values of S', 0, 255, (0, 255))
    v = st.slider('Lower and Higher Values of V', 0, 255, (0, 255))

    col1, col2 = st.columns(2)
    with col1:
        img = Image.open(img_uploaded_file)
        st.image(img, channels="RGB", width=300)
    with col2:
        back_img = Image.open(back_uploaded_file)
        st.image(back_img, channels="RGB", width=300)

    im = Process(img, back_img, h[0], h[1], s[0], s[1], v[0], v[1]).join_image()

    st.image(im, channels="RGB", width=700)
else:
    st.write(f'Please upload a file')
