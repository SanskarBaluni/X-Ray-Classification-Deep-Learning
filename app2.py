import tensorflow as tf
import streamlit as st

# st.markdown("""
#     <style>
#         .stApp {
#         background: url("https://assets.technologynetworks.com/production/dynamic/images/content/default/default-960x540.jpg?cb=4928198");
#         background-size: cover;
#         }
#     </style>""", unsafe_allow_html=True)
#
st.cache_data()

@st.cache_resource


def load_model():
    model = tf.keras.models.load_model('CNN_Model.h5')
    return model


with st.spinner('Model is being loaded..'):
    model = load_model()

#
# st.markdown("""
# <style>
# .big-font {
#     font-size:60px ;
# }
# .sml-font {
#     font-size:70px ;
# }
#
# </style>
# """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: white;'> X-RAY IMAGE CLASSIFICATION</h1>", unsafe_allow_html=True)
# st.write('<p class="sml-font">CLASSIFICATION</p>', unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center; color: white;'> X-RAY IMAGE CLASSIFICATION</h1>", unsafe_allow_html=True)

file = st.file_uploader("Please upload an file", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)


def import_and_predict(image_data, model):
    size = (150, 150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.

    img_reshape = img[np.newaxis, ...]

    prediction = model.predict(img_reshape)

    return prediction


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)

    with st.columns(3)[1]:
        st.image(image, width=300, use_column_width=True)

    # st.image(image, width=300, use_column_width=False)
    prediction = import_and_predict(image, model)
    #     st.write(prediction)
    if prediction[0][0] == 1:
        st.markdown("<h1 style='text-align: center;'>COVID</h1>", unsafe_allow_html=True)
    elif prediction[0][1] == 1:
        st.markdown("<h1 style='text-align: center;'>NORMAL</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center;'>PNEUMONIA</h1>", unsafe_allow_html=True)
