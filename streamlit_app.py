from PIL import Image
import random
import streamlit as st
import base64
import os

st.title("Foxiez")

# enable image download
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download Image</a>'
    return href

unique = st.checkbox('One-of-one')
if not unique:
    list_background = [os.path.splitext(f)[0] for f in os.listdir('./png/foxie/background')]
    list_expressions = [os.path.splitext(f)[0] for f in os.listdir('./png/foxie/expressions')]
    list_hats = [os.path.splitext(f)[0] for f in os.listdir('./png/foxie/hats')]
    list_clothings = [os.path.splitext(f)[0] for f in os.listdir('./png/foxie/clothings')]

    col1, col2 = st.columns(2)
    option_expressions = col1.selectbox('Expressions', list_expressions)
    option_hats = col1.selectbox('Hats', list_hats)
    option_clothings = col1.selectbox('Clothes', list_clothings)
    option_background = col1.selectbox('Background', list_background)

    if col2.button('Randomize'):
        option_expressions = list_expressions[random.randint(0, len(list_expressions)-1)]
        option_hats = list_hats[random.randint(0, len(list_hats)-1)]
        option_clothings = list_clothings[random.randint(0, len(list_clothings)-1)]
        option_background = list_background[random.randint(0, len(list_background)-1)]

    background = Image.open(r'png/foxie/background/%s.png' % option_background)
    clothes = Image.open(r'png/foxie/clothings/%s.png' % option_clothings)
    hat = Image.open(r'png/foxie/hats/%s.png' % option_hats)
    expression = Image.open(r'png/foxie/expressions/%s.png' % option_expressions)
    head = Image.open(r'png/foxie/default-head.png')
    ear = Image.open(r'png/foxie/default-ears.png')

    step1 = Image.alpha_composite(background, clothes)
    step2 = Image.alpha_composite(step1, ear)
    step3 = Image.alpha_composite(step2, head)
    step4 = Image.alpha_composite(step3, expression)
    final = Image.alpha_composite(step4, hat)

    final.save('./foxie.png')
    col2.image(Image.open("./foxie.png"))
    col2.write(imagedownload('./foxie.png'), unsafe_allow_html=True)

else:
    list_unique = [os.path.splitext(f)[0] for f in os.listdir('./png/foxie/unique')]
    col1, col2 = st.columns(2)
    option_unique = col1.selectbox('Select One-of-one', list_unique)
    col2.image(Image.open(r'png/foxie/unique/%s.png' % option_unique))
    col2.write(imagedownload(r'png/foxie/unique/%s.png' % option_unique), unsafe_allow_html=True)
