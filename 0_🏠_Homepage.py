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
img_missing = Image.open("images/missing.png")

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
file_ = open(Path.cwd() / 'images/missing.png', "rb")
contents = file_.read()
data_url_m2 = base64.b64encode(contents).decode("utf-8")
file_.close()

# BODY - MODELS
with st.container():
    st.write("---")
    st.markdown('<div id=title>All the Models</div>', unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    l_col, r_col = st.columns(2)
    with l_col:
        st.markdown(f'''
        <div id="mbox_left" class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m1}">
            <h2 class="title_mbox">Android Malware Detection</h2>
            <div class="description_mbox">It's a simple and effective Deep Learning Approach to detect malware 
            based on Image Representation of Bytecode.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/Android_Malware_Detection" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(f'''
        <div class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m2}">
            <h2 class="title_mbox">Missing Model 2</h2>
            <div class="description_mbox">It's a simple and effective Deep Learning Approach to detect malware 
            based on Image Representation of Bytecode.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/Model_2" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
st.write("##")
with st.container():
    l_col, r_col = st.columns(2)
    with l_col:
        st.markdown(f'''
        <div id="mbox_left" class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m2}">
            <h2 class="title_mbox">Missing Model 3</h2>
            <div class="description_mbox">It's a simple and effective Deep Learning Approach to detect malware 
            based on Image Representation of Bytecode.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/Android_Malware_Detection" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(f'''
        <div class="mbox">
            <img class="img_mbox" src="data:image/jpg;base64,{data_url_m2}">
            <h2 class="title_mbox">Missing Model 4</h2>
            <div class="description_mbox">It's a simple and effective Deep Learning Approach to detect malware 
            based on Image Representation of Bytecode.</div>
            <div class="link_placeholder">
                <a class="link_mbox" href="http://localhost:8501/Android_Malware_Detection" target="_self">Try the DEMO out</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)

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
            unsafe_allow_html=True,
        )