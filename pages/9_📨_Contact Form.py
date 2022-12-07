import base64
from pathlib import Path
from PIL import Image
import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_icon="📨", 
    page_title="MLM - Contact", 
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
    <div id="contact_filler">display:none</div>
    ''', unsafe_allow_html=True)

# CONTACT
with st.container():
    st.write("---")
    st.markdown('<div id=title>Contact</div>', unsafe_allow_html=True)
    st.write("##")
    l_col, r_col = st.columns((4, 1))
    with l_col:
        selected_item = st.selectbox(
            "Subject",
            ("General Question", "Android Malware Detection Model", "Code Classification Model", "Code Clone Detection Model", "Vulnerability Detection Model"))
        st.markdown("""
            <form action="https://formsubmit.co/seemedunrun@gmail.com" method="POST">
            Name
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_subject" value= "Bachelor Project - Subject: """ + selected_item + """">
            <input type="text" name="Name" placeholder="Name Surname" required>
            Email
            <input type="email" name="Email" placeholder="example@domain.com" required>
            Message
            <textarea class="message" name="Message" style="height:240px" placeholder="How can we help you?" required></textarea>
            <button class="right_pos">Send</button>
            </form>
        """, unsafe_allow_html=True)
    with r_col:
        st.empty() #"Bachelor Project - Subject: "

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