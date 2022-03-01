from PIL import Image
import random

count = 0
samples = [1, 2, 3, 4]

while count <= 29:
    rand_arr = random.choices(samples, k=4)
    background = Image.open(r'png/background/background_%s.png' % rand_arr[0])
    poster = Image.open(r'./png/poster/poster_%s.png' % rand_arr[1])
    balloon = Image.open(r'./png/balloon/balloon_%s.png' % rand_arr[2])
    face = Image.open(r'./png/face/face_%s.png' % rand_arr[3])

    first_step = Image.alpha_composite(background, poster)
    second_step = Image.alpha_composite(first_step, balloon)
    final = Image.alpha_composite(second_step, face)

    count += 1
    final.save('./collection/generated-%s.png' % count)