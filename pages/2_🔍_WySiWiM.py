import base64
from pathlib import Path
from PIL import Image
import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_icon="🔍", 
    page_title="MLM - WySiWiM", 
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
        st.markdown('<div id=title>WySiWiM Model</div>', unsafe_allow_html=True)
        st.markdown('''
        <div id="content">WYSIWIM ("What You See Is What It Means") is a novel approach 
        to learning semantic representations of code via transfer learning, based on 
        visual representations of source code.
        <br>
        <br>
        In the demo, choose a mode and insert your code to check it out.
        </div>
        ''', unsafe_allow_html=True)
        st.write("##")
        st.markdown('<div id=title>DEMO</div>', unsafe_allow_html=True)
    with r_col:
        st.empty()
    l_col, r_col = st.columns((1, 4))
    with l_col:
        mode = st.radio(
            "Select a mode",
            ('Classification', 'Comparison', 'Vulnerability', 'Analysis'))

    with r_col:
        if mode == 'Classification':
            txt1 = st.text_area('Paste your code below')
            st.button('Classify')
        if mode == 'Comparison':
            txt1 = st.text_area('Paste your first code below')
            txt2 = st.text_area('Paste your second code below')
            st.button('Compare')
        if mode == 'Vulnerability':
            txt1 = st.text_area('Paste your code below')
            st.button('Check for vulnerability')
        if mode == 'Analysis':
            txt1 = st.text_area('Paste your code below')
            st.button('Analyse')

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