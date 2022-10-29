import base64
from pathlib import Path
from PIL import Image
import streamlit as st

from models.wysiwim.vis_ast.ast_alg import from_to_file_ast
from models.wysiwim.vis_color.color_alg import from_to_file_color
from models.wysiwim.vis_geometric.geometric_alg import from_to_file_geometric
from models.wysiwim.vis_st.st_alg import from_to_file_st

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

    # We generate the code here, because if they stay blank, the user will be informed to put some valid code inside
    text = ""
    text2 = ""
    l_col, r_col = st.columns((2, 7))
    with l_col:
        # User needs to choose the programming language of his code
        prog_lang = st.selectbox(
            "Select a programming language",
            ('Java', 'Python'))

        # User can choose between 4 different ways to generate an image
        method = st.radio(
            "Select a rendering method",
            ('AST', 'Geometric', 'Textual', 'Color'))

        # User can choose, which approach will happen with his code
        approach = st.radio(
            "Select an approach",
            ('Code classification', 'Code clone detection', 'Vulnerability detection'))

    with r_col:
        # If the approach is 'Code clone detection', we have 2 areas of code
        if approach == 'Code clone detection':
            text = st.text_area('Paste your first code below')
            text2 = st.text_area('Paste your second code below')
        # For approach: 'Code classification' and 'Vulnerability detection'
        else:
            text = st.text_area('Paste your code below')

        # Button uses the code for the model, if there
        if st.button(approach):
            # Check whether the first textarea has some input, otherwise the user must provide some
            if text != "":
                # Enter the correct method provided by the user
                if method == 'AST':
                    images_dir_ast = Path.cwd() / 'models/wysiwim/vis_ast/generated_images'
                    image = from_to_file_ast(text, images_dir_ast, prog_lang)
                if method == 'Geometric':
                    images_dir_geometric = Path.cwd() / 'models/wysiwim/vis_geometric/generated_images'
                    image = from_to_file_geometric(text, images_dir_geometric, prog_lang)
                if method == 'Textual':
                    images_dir_st = Path.cwd() / 'models/wysiwim/vis_st/generated_images'
                    image = from_to_file_st(text, images_dir_st, prog_lang)
                if method == 'Color':
                    images_dir_color = Path.cwd() / 'models/wysiwim/vis_color/generated_images'
                    image = from_to_file_color(text, images_dir_color, prog_lang)
                # Enter the 'Code clone detection' approach
                if approach == 'Code clone detection':
                    # Check whether the second textarea has some input, otherwise the user must provide some
                    if text2 != "":
                        # Enter the same method as for the first code
                        if method == 'AST':
                            images_dir_ast = Path.cwd() / 'models/wysiwim/vis_ast/generated_images'
                            image2 = from_to_file_ast(text2, images_dir_ast, prog_lang)
                        if method == 'Geometric':
                            images_dir_geometric = Path.cwd() / 'models/wysiwim/vis_geometric/generated_images'
                            image2 = from_to_file_geometric(text2, images_dir_geometric, prog_lang)
                        if method == 'Textual':
                            images_dir_st = Path.cwd() / 'models/wysiwim/vis_st/generated_images'
                            image2 = from_to_file_st(text2, images_dir_st, prog_lang)
                        if method == 'Color':
                            images_dir_color = Path.cwd() / 'models/wysiwim/vis_color/generated_images'
                            image2 = from_to_file_color(text2, images_dir_color, prog_lang)
                        #INSERT MODEL PREDICT FROM APPROACH 2

                    else:
                        st.write("You must provide some valid code for the " + approach + ".")
                else:
                    # Enter the 'Code classification' approach
                    if approach == 'Code classification':
                        st.write('')
                        #INSERT MODEL PREDICT HERE FROM APPROACH 1

                    # Enter the 'Vulnerability detection' approach
                    else:
                        st.write('')
                        #INSERT MODEL PREDICT HERE FROM APPROACH 3

            else:
                st.write("You must provide some valid code for the " + approach + ".")

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