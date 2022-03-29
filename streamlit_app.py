from PIL import Image
import random
import streamlit as st
import base64
import os

st.title("Generate your own avatar :dog:")

# enable image download
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download Image</a>'
    return href

project_names = ['Foxiez', 'Tennis Ball', 'Crazy Balloon']
project = st.radio("Project Select", project_names)

if project == 'Foxiez':
    st.subheader(project)

    list_background = ['rice', 'pink', 'yellow', 'green', 'blue-dots', 'green-dots', 'yellow-dots', 'snow']
    list_expressions = ['default-smile', 'eyes-closed', 'frown', 'kawaii-smile', 'pipe', 'sad', 'sleepy', 'sophisticated', 'wink']
    list_hats = ['none', 'brim-bucket', 'bucket', 'mushroom', 'strawhat']
    list_clothings = ['default-body', 'apron', 'blue-collar-shirt', 'blue-tie', 'fish-tshirt', 'red-collar-shirt', 'scarf']
    list_hats = ['none', 'brim-bucket', 'bucket', 'birthday-hat', 'chef-hat', 'crown', 'flower', 'gentleman-hat',
                 'mushroom', 'pink-bow', 'poop', 'propeller-hat', 'straw-hat']
    list_clothings = ['default-body', 'apron', 'stripe-apron', 'blue-collar-shirt', 'blue-hoodie', 'blue-tie',
                      'fish-tshirt', 'pink-hoodie', 'poop-tshirt', 'red-collar-shirt', 'scarf', 'vest-and-bowtie', 'vest-and-tie']

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
    step4 = Image.alpha_composite(step3, hat)
    final = Image.alpha_composite(step4, expression)

    final.save('./foxie.png')
    col2.image(Image.open("./foxie.png"))
    col2.write(imagedownload('./foxie.png'), unsafe_allow_html=True)

if project == 'Tennis Ball':
    st.subheader(project)

    list_background = ['pink', 'green', 'blue', 'rice', 'yellow']
    list_body = ['default']
    list_effect = ['default', 'fire', 'fly', 'puddle', 'court-line']
    list_face = ['smile', 'cry', 'dizzy', 'kawaii-smile', 'cool', 'surprised']

    col1, col2 = st.columns(2)

    option_face = col1.selectbox('face', list_face)
    option_body = col1.selectbox('ball', list_body)
    option_effect = col1.selectbox('effect', list_effect)
    option_background = col1.selectbox('background', list_background)

    if col2.button('Randomize'):
        option_face = list_face[random.randint(0, len(list_face)-1)]
        option_body = list_body[random.randint(0, len(list_body)-1)]
        option_effect = list_effect[random.randint(0, len(list_effect)-1)]
        option_background = list_background[random.randint(0, len(list_background)-1)]

    background = Image.open(r'png/tennis-ball/background/%s.png' % option_background)
    effect = Image.open(r'png/tennis-ball/effect/%s.png' % option_effect)
    body = Image.open(r'png/tennis-ball/body/%s.png' % option_body)
    face = Image.open(r'png/tennis-ball/face/%s.png' % option_face)

    first_step = Image.alpha_composite(background, effect)
    second_step = Image.alpha_composite(first_step, body)
    final = Image.alpha_composite(second_step, face)

    final.save('./tennis.png')
    col2.image(Image.open("./tennis.png"))
    col2.write(imagedownload('./tennis.png'), unsafe_allow_html=True)

if project == 'Crazy Balloon':
    st.subheader('Crazy Balloon')
    if st.button('Generate Image'):
        background = Image.open(r'png/crazy-balloon/background/background_%s.png' % random.randint(1, 5))
        poster = Image.open(r'./png/crazy-balloon/poster/poster_%s.png' % random.randint(1, 4))
        balloon = Image.open(r'./png/crazy-balloon/balloon/balloon_%s.png' % random.randint(1, 4))
        face = Image.open(r'./png/crazy-balloon/face/face_%s.png' % random.randint(1, 8))
        decoration = Image.open(r'./png/crazy-balloon/decoration/decoration_%s.png' % random.randint(1, 4))
        hat = Image.open(r'./png/crazy-balloon/hat/hat_%s.png' % random.randint(1, 5))

        first_step = Image.alpha_composite(background, decoration)
        second_step = Image.alpha_composite(first_step, poster)
        third_step = Image.alpha_composite(second_step, balloon)
        fourth_step = Image.alpha_composite(third_step, hat)
        final = Image.alpha_composite(fourth_step, face)

        final.save('./random.png')
    st.image(Image.open("./random.png"))
    st.write(imagedownload('./random.png'), unsafe_allow_html=True)
