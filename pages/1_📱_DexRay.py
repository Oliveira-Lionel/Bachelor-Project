import base64
import math
from pathlib import Path
from PIL import Image
import streamlit as st

from models.dexray.apktoimage import apktoimage
from models.dexray.DexRay import decode_img

import tensorflow as tf
import tensorflow_addons as tfa

# PAGE CONFIG
st.set_page_config(
    page_icon="📱", 
    page_title="MLM - DexRay", 
    layout="wide"
    )

# IMAGES
img_snt_logo = Image.open("images/snt_logo_header.png")

# CSS
def local_css(f_name):
    with open(f_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style/style.css")

# HEADER
with st.container():
    st.image(img_snt_logo, use_column_width=True)
    st.markdown(f'''
    <a href="Contact_Form" target="_self" id="contact"><div>Contact</div></a>
    ''', unsafe_allow_html=True)
    

# MODELS
with st.container():
    st.write("---")
    l_col, r_col = st.columns((4, 1))
    with l_col:
        st.markdown('<div id=title>DexRay Model</div>', unsafe_allow_html=True)
        st.markdown('''
        <div id="content">DexRay is an Android Malware Detection model published at 
        MLHat 2021. It's a simple and effective Deep Learning Approach to detect malware 
        based on Image Representation of Bytecode.
        <br>
        <br>
        In the demo, insert an apk file to check for malware. 
        </div>
        ''', unsafe_allow_html=True)
        st.write("##")
        st.markdown('<div id=title>DEMO</div>', unsafe_allow_html=True)

        # Loading the model
        model_file_dir = Path.cwd() / 'models/dexray/model1'
        model = tf.keras.models.load_model(model_file_dir, custom_objects={"metrics": ['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall(), tfa.metrics.F1Score(num_classes=2, average="micro", threshold=0.5)]})

        # Upload a file of apk type
        apk_file = st.file_uploader("File Uploader", type="apk")
        with st.spinner('Checking the file..'):
            if apk_file is not None:
                # Get the content of the file in bytes
                bytes_data = apk_file.getvalue()

                # Path for the folder of the new apk file
                apk_file_dir = Path.cwd() / 'models/dexray/apk_files/'
                apk_file_path = apk_file_dir / apk_file.name

                # In the new Path of the apk file, the file is opened as a binary file
                # Now the content of bytes_data is written to the binary file
                # ('with' closes the file automatically, after the function ends)
                with open(apk_file_path, "wb") as binary_f:
                    binary_f.write(bytes_data)
                
                # Path for the folder of the new generated images
                images_dir = Path.cwd() / 'models/dexray/generated_images'

                # Generate an image of the apk file with the apktoimage(..) function
                apktoimage(str(apk_file_path), str(images_dir))

                # Adjust Image (Size) with the decode_img(..) function
                images_path = str(images_dir / apk_file.name) + ".png"
                image = decode_img(images_path)

                # Check the apk file with the model
                image = tf.expand_dims(image, axis=0)
                prediction = model.predict(image)

                print(prediction)

                # Get result of variable prediction and check if it's a malware or a goodware
                prediction = prediction[0][0]
                result = None
                if prediction > 0.5:
                    result = "malware"
                    prediction = int(prediction*10000) / 100

                if prediction <= 0.5:
                    result = "goodware"
                    prediction = int((1-prediction)*10000) / 100

                # Text box with the result of the checked apk file (if only 1 got checked)
                # This is called when the result is still None, a mistake has probably occured
                if result == None:
                    st.markdown('''<div id="box" class="mistake">
                    <h2>Something went wrong. Let's get in touch by the Contact Form.</h2>
                    </div>''', unsafe_allow_html=True)
                # This is called when the result is "goodware"
                if result == "goodware":
                    st.markdown("""<div id="box" class="safe">
                    <h2>This file is safe to be used on your device.</h2></div>
                    <br>
                    <div id="content">This result has a """ + str(prediction) + """% probability to be correct.</div>
                    """, unsafe_allow_html=True)
                # This is called when the result is "malware"
                if result == "malware":
                    st.markdown("""<div id="box" class="malicious">
                    <h2>This file contains malware that may harm your device.</h2></div>
                    <br>
                    <div id="content">This result has a """ + str(prediction) + """% probability to be correct.</div>
                    """, unsafe_allow_html=True)
    with r_col:
        st.empty()

# FOOTER
# Convert png file to base64
file_ = open(Path.cwd() / 'images/follow_us_twitter.png', "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

# Display SnT Information & Have a Twitter Link of SnT as Logo
with st.container():
    st.write("---")
    l_col, r_col = st.columns((4, 1))
    with l_col:
        st.markdown('''
        <p class="snt_text"><span class="bold_text">&#160SnT</span>
        <br>
        SnT is an internationally leading research and innovations centre that together with partners works to establish Luxembourg as a European centre of excellence for secure, reliable, and trustworthy ICT systems and services. In this context SnT achieves excellence by targeting research topics that create high impact, well beyond the academic community.</p>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(
            f'<a href="https://twitter.com/SnT_uni_lu"><img class="center_pos" src="data:image/png;base64,{data_url}"></a>',
            unsafe_allow_html=True)