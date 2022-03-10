from PIL import Image
import random
import streamlit as st
import base64

st.title("Generate your own avatar :dog:")

# enable image download
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download Image</a>'
    return href

project_names = ['Crazy Balloon', 'Tennis Ball']
project = st.radio("Project Select", project_names)

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
    st.markdown(imagedownload('./random.png'), unsafe_allow_html=True)

if project == 'Tennis Ball':
    st.subheader(project)



