from PIL import Image
import random
import streamlit as st
import base64

st.markdown("# Generate a random NFT or avatar")

# encode the image
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download Image</a>'
    return href

if st.button('Random generate'):
    background = Image.open(r'png/background/background_%s.png' % random.randint(1, 5))
    poster = Image.open(r'./png/poster/poster_%s.png' % random.randint(1, 4))
    balloon = Image.open(r'./png/balloon/balloon_%s.png' % random.randint(1, 4))
    face = Image.open(r'./png/face/face_%s.png' % random.randint(1, 8))
    decoration = Image.open(r'./png/decoration/decoration_%s.png' % random.randint(1, 4))
    hat = Image.open(r'./png/hat/hat_%s.png' % random.randint(1, 5))

    first_step = Image.alpha_composite(background, decoration)
    second_step = Image.alpha_composite(first_step, poster)
    third_step = Image.alpha_composite(second_step, balloon)
    fourth_step = Image.alpha_composite(third_step, hat)
    final = Image.alpha_composite(fourth_step, face)

    final.save('./collection/random.png')
    st.image(Image.open("./collection/random.png"))
    st.markdown(imagedownload('./collection/random.png'), unsafe_allow_html=True)
