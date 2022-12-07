import base64
from pathlib import Path
from PIL import Image
import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_icon="🏠", 
    page_title="MLM - Homepage", 
    layout="wide"
    )

# IMAGES
img_snt_logo = Image.open("images/snt_logo_header.png")

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style/style.css")

# HEADER
with st.container():
    st.image(img_snt_logo, use_column_width=True)
    st.markdown(f'''
    <a href="Contact_Form" target="_self" id="contact"><div>Contact</div></a>
    ''', unsafe_allow_html=True)

# Convert jpg file to base64
file_ = open(Path.cwd() / 'images/malware.jpg', "rb")
contents = file_.read()
data_url_m1 = base64.b64encode(contents).decode("utf-8")
file_.close()

# Convert jpg file to base64
file_ = open(Path.cwd() / 'images/literally.jpg', "rb")
contents = file_.read()
data_url_m2 = base64.b64encode(contents).decode("utf-8")
file_.close()

# BODY - MODELS 
with st.container():
    st.write("---")
    st.markdown('''
        <div id="content_hp">What is a machine learning model?</div>
        <div id="content"><br>A machine learning model is an application that makes 
        a prediction by receiving an input, where the accuracy given in percentage 
        indicates the probability of the prediction being a correct result. To 
        improve the accuracy of the model, it is trained with unseen dataset during 
        the training runs.<br><br>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('<div id=title>All the Models<br><br></div>', unsafe_allow_html=True)
    l_col, r_col = st.columns(2)
    with l_col:
        st.markdown(f'''
        <div id="mbox_left" class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m1}">
            <h2 class="title_mbox">DexRay</h2>
            <div class="description_mbox">DexRay is a simple and effective Android Malware Detection Model that detects whether an APK file is malware or safe, based on image representation.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/DexRay" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(f'''
        <div class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m2}">
            <h2 class="title_mbox">WySiWiM</h2>
            <div class="description_mbox">WySiWiM consists of 3 Models with their own results that uses visualization and transfer learning to show the opportunities of code semantics learning.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/WySiWiM" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
st.write("##")

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
        SnT is a research and innovations centre with a meaningful impact on an international scale by developing great solutions for secure, reliable and trustworthy information and communication technology systems and services. It achieves his goals by working with talented people around the world, who are chosen on a selective way to guarantee diversity.</p>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(
            f'<a href="https://twitter.com/SnT_uni_lu"><img class="center_pos" src="data:image/png;base64,{data_url}"></a>',
            unsafe_allow_html=True,
        )