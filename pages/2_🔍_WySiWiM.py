import base64
from pathlib import Path
from PIL import Image
import streamlit as st

from models.wysiwim.vis_ast.ast_alg import from_to_file_ast
from models.wysiwim.vis_color.color_alg import from_to_file_color
from models.wysiwim.vis_geometric.geometric_alg import from_to_file_geometric
from models.wysiwim.vis_st.st_alg import from_to_file_st

from torchvision.io import read_image
from torchvision.models import resnet50

import torch
from torchvision import transforms
import torch.nn as nn

import time

from guesslang import Guess

# Loads image
def load_img(image_path):
    return Image.open(image_path).convert('RGB')

# Transforms an image to a vector (tensor) with the correct size for the model
def imagetovector(image_path):
    data_transforms = transforms.Compose([
            transforms.Resize(230),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    img = load_img(image_path)
    img = data_transforms(img)
    return img

# Check if the given text is a supported programming language
def guessLang(text):
    guess = Guess()
    language_name = guess.language_name(text)
    list = ["Assembly", "Batchfile", "C", "C#", "C++", "Clojure", "COBOL", "CoffeeScript", "Dart", "DM", "Elixir", "Erlang", "Fortran", "Go", "Groovy", "Haskell", "Java", "JavaScript", "Julia", "Kotlin", "Lisp", "Lua", "Matlab", "Objective-C", "OCaml", "Pascal", "Perl", "PHP", "Prolog", "Python", "R", "Ruby", "Rust", "Scala", "Swift", "TypeScript", "Visual Basic"]
    guessed = False

    if text != "":
        for i in list:
            if i == language_name:
                guessed = True
    
    return guessed

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
        <div id="content">WYSIWIM ("What You See Is What It Means") is an approach that 
        makes use of visualization and transfer learning to present the opportunities of 
        code semantics learning.<br><br>
        It consists of three different models with their own result:<br></div>
        <div id="content2">• The code classification model associates a class from a set 
        of possible labels to the given code.<br>
        • The code clone detection model compares the two given codes with each other to 
        check whether they are semantic clones.<br>
        • The vulnerability detection model checks if the given code has a vulnerability 
        problem.<br><br></div>
        It also uses four different rendering methods to convert the given code to a 
        specific image:<br>
        <div id="content2">• AST can only convert Java code into an image. It is a method 
        that renders the code to an optimized abstract syntax tree while giving geometric 
        shapes to certain types of nodes.<br>
        • Geometric renders the language keywords of a code to a certain geometric shape.
        <br>
        • Textual renders a code simply without highlighting any language construct.<br>
        • Color renders a code with coloring language keywords with a certain color.<br>
        <br></div>
        This image is then resized and transformed to a vector (tensor) before going into 
        the chosen model.<br><br>
        The Demo below gives the possibility to choose between these different options.
        <br><br></div>
        ''', unsafe_allow_html=True)
        st.markdown('<div id=title>DEMO</div>', unsafe_allow_html=True)
    with r_col:
        st.empty()

    # We generate the code here, so that if the text area stays blank, the user will be informed to put some valid code inside
    text = ""
    text2 = ""
    button_pressed = 0
    l_col, r_col = st.columns((2, 7))
    with l_col:
        # User can choose between 4 different ways to generate an image
        method = st.radio(
            "Select a rendering method",
            ('AST (only Java code)', 'Geometric', 'Textual', 'Color'))

        # User can choose, which approach will happen with his code
        approach = st.radio(
            "Select a model",
            ('Code classification', 'Code clone detection', 'Vulnerability detection'))
    with r_col:
        # If the approach is 'Code clone detection', we have 2 areas of code
        if approach == 'Code clone detection':
            text = st.text_area('Paste your first code below')
            text2 = st.text_area('Paste your second code below')
            text_c = 'codes'

        # For approach: 'Code classification' and 'Vulnerability detection'
        else:
            text = st.text_area('Paste your code below')
            text_c = 'code'

        # Button uses the code for the model, if there
        if st.button(approach):

            # Start timer for the execution, when uploading a file
            start = time.time()

            # Loading Animation
            with st.spinner('Checking the ' + text_c + '..'):
                # Check whether the first textarea has some input, otherwise the user must provide some
                if guessLang(text):
                    img_name = 'image.png'
                    images_dir = Path.cwd() / 'models/wysiwim/generated_images'
                    images_dir.mkdir(parents=True, exist_ok=True)

                    # Enter the correct method provided by the user
                    if method == 'AST (only Java code)':
                        try:
                            image = from_to_file_ast(text, images_dir, 'java', img_name)
                        except:
                            button_pressed = -1
                    if method == 'Geometric':
                        image = from_to_file_geometric(text, images_dir, 'any', img_name)
                    if method == 'Textual':
                        image = from_to_file_st(text, images_dir, 'any', img_name)
                    if method == 'Color':
                        image = from_to_file_color(text, images_dir, 'any', img_name)

                    # Check if an error occured, if it's the case, we end the with st.spinner(..)
                    if button_pressed != -1:
                        # Enter the 'Code clone detection' approach
                        if approach == 'Code clone detection':
                            # Check whether the second textarea has some input, otherwise the user must provide some
                            if guessLang(text2):
                                img2_name = 'image2.png'
                                # Enter the same method as for the first code
                                if method == 'AST (only Java code)':
                                    try:
                                        image2 = from_to_file_ast(text2, images_dir, 'java', img2_name)
                                    except:
                                        button_pressed = -1
                                if method == 'Geometric':
                                    image2 = from_to_file_geometric(text2, images_dir, 'any', img2_name)
                                if method == 'Textual':
                                    image2 = from_to_file_st(text2, images_dir, 'any', img2_name)
                                if method == 'Color':
                                    image2 = from_to_file_color(text2, images_dir, 'any', img2_name)

                                # Check if an error occured, if it's the case, we end the with st.spinner(..)
                                if button_pressed != -1:
                                    button_pressed = 2
                                    # Model Prediction Approach 2
                                    model_file_dir = Path.cwd() / 'models/wysiwim/clone_feature_extraction_model'
                                    image_path = images_dir / img_name
                                    image2_path = images_dir / img2_name

                                    input_ = imagetovector(str(image_path))
                                    input_ = torch.unsqueeze(input_, 0)
                                    input2_ = imagetovector(str(image2_path))
                                    input2_ = torch.unsqueeze(input2_, 0)

                                    # Loading the model
                                    model = torch.load(str(model_file_dir))

                                    # Check the inputs with the model
                                    model.eval()
                                    img1_features_vector = model(input_)
                                    img2_features_vector = model(input2_)
                                    cos = nn.CosineSimilarity(dim=1, eps=1e-6)
                                    preds = cos(img1_features_vector, img2_features_vector)
                            else:
                                button_pressed = -1
                        else:
                            button_pressed = 1

                            # Enter the 'Code classification' approach
                            if approach == 'Code classification':
                                # Model Prediction Approach 1
                                model_file_dir = Path.cwd() / 'models/wysiwim/cc_model'
                                image_path = images_dir / img_name

                                input_ = imagetovector(str(image_path))
                                input_ = torch.unsqueeze(input_, 0)

                                # Loading the model
                                model = torch.load(str(model_file_dir))

                                # Check the input with the model
                                model.eval()
                                outputs = model(input_)
                                _, preds = torch.max(outputs, 1)

                            # Enter the 'Vulnerability detection' approach
                            else:
                                # Model Prediction Approach 3
                                model_file_dir = Path.cwd() / 'models/wysiwim/vul_model'
                                image_path = images_dir / img_name

                                input_ = imagetovector(str(image_path))
                                input_ = torch.unsqueeze(input_, 0)

                                # Loading the model
                                model = torch.load(str(model_file_dir))

                                # Check the input with the model
                                model.eval()
                                outputs = model(input_)
                                _, preds = torch.max(outputs, 1)
                else:
                    button_pressed = -1
    
            # End timer for the execution, when uploading a file
            end = time.time()
            running_time = str((int)(end-start))
    
    st.write("##")
    if button_pressed == 1:
        l_col, r_col = st.columns((1, 1))
        with l_col:
            st.write("Generated image from code")
            img_interface = Image.open("models/wysiwim//generated_images/image.png")
            st.image(img_interface, use_column_width=True)
        with r_col:
            st.empty()
        l_col, r_col = st.columns((1, 1))
        with l_col:
            st.write("Result:")
            # Result of Approach 1
            if approach == 'Code classification':
                preds = preds[0].numpy()
                list = [[30, 't1'], [100, 't2']] #The List of the classes (only an example right now)

                # Associate a class to the model's prediction
                class_name = ''
                for i in list:
                    if i[0] == preds:
                        class_name = i[1]

                if class_name != '':
                    st.markdown("""<div id="box" class="safe">
                    <h2>Class of the given code: """ + class_name + """</h2></div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""<div id="box" class="malicious">
                    <h2>We can't associate a class to the given code.</h2></div>
                    """, unsafe_allow_html=True)
            # Result of Approach 3
            else:
                preds = preds[0].numpy()

                if preds == 0:
                    st.markdown("""<div id="box" class="safe">
                    <h2>This code has no vulnerability problems.</h2></div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""<div id="box" class="malicious">
                    <h2>This code has some vulnerability problems.</h2></div>
                    """, unsafe_allow_html=True)
            st.markdown("""<br>
                <div id="content">The running time of this computation was """ + running_time + """s.</div>
                """, unsafe_allow_html=True)
        with r_col:
            st.empty()
    elif button_pressed == 2:
        l_col, r_col = st.columns((1, 1))
        with l_col:
            st.write("Generated image from first code")
            img_interface = Image.open("models/wysiwim//generated_images/image.png")
            st.image(img_interface, use_column_width=True)
        with r_col:
            st.write("Generated image from second code")
            img2_interface = Image.open("models/wysiwim//generated_images/image2.png")
            st.image(img2_interface, use_column_width=True)
        l_col, r_col = st.columns((1, 1))
        with l_col:
            st.write("Result:")
            # Result of Approach 2
            preds = preds[0][0][0].detach().numpy()
            print(preds)

            if preds >= 0.7:
                st.markdown("""<div id="box" class="safe">
                <h2>The two given codes have a 93% similarity to be semantic clones.</h2></div>
                """, unsafe_allow_html=True)
            elif preds >= 0.5:
                st.markdown("""<div id="box" class="malicious">
                <h2>The two given codes are not similar enough to be semantic clones.</h2></div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""<div id="box" class="malicious">
                <h2>The two given codes are definitely not semantic clones.</h2></div>
                """, unsafe_allow_html=True)
        with r_col:
            st.empty()
    elif button_pressed == -1:
        l_col, r_col = st.columns((2, 7))
        with l_col:
            st.empty()
        with r_col:
            st.markdown("""<div id="box" class="malicious">
            <h2>You must provide some valid code</h2></div>
            """, unsafe_allow_html=True)
    else:
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
        SnT is a research and innovations centre with a meaningful impact on an international scale by developing great solutions for secure, reliable and trustworthy information and communication technology systems and services. It achieves his goals by working with talented people around the world, who are chosen on a selective way to guarantee diversity.</p>
        ''', unsafe_allow_html=True)
    with r_col:
        st.markdown(
            f'<a href="https://twitter.com/SnT_uni_lu"><img class="center_pos" src="data:image/png;base64,{data_url}"></a>',
            unsafe_allow_html=True,
        )