from PIL import Image
import random
import imageio
import os

count = 0
while count <= 29:
    background = Image.open(r'png/background/background_%s.png' % random.randint(1, 5))
    poster = Image.open(r'./png/poster/poster_%s.png' % random.randint(1, 4))
    balloon = Image.open(r'./png/balloon/balloon_%s.png' % random.randint(1, 4))
    face = Image.open(r'./png/face/face_%s.png' % random.randint(1, 8))
    decoration = Image.open(r'./png/decoration/decoration_%s.png' % random.randint(1, 4))
    hat = Image.open(r'./png/hat/hat_%s.png' % random.randint(1, 5))

    first_step = Image.alpha_composite(background, decoration)
    second_step = Image.alpha_composite(first_step, poster)
    third_step = Image.alpha_composite(second_step, balloon)
    fourth_step = Image.alpha_composite(third_step, face)
    final = Image.alpha_composite(fourth_step, hat)

    count += 1
    final.save('./collection/generated-%s.png' % count)

images = []
generated_dir = './collection'
for filename in sorted(os.listdir(generated_dir)):
    file_path = os.path.join(generated_dir, filename)
    images.append(imageio.imread(file_path))
imageio.mimsave('./collection.gif', images, duration=0.5)
