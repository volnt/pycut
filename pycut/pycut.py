from sys import argv, stderr
from random import shuffle
from PIL import Image, ImageFilter
from os import path

def usage():
    stderr.write(("Usage : pycut IMAGE [WIDTHxHEIGHT]\n"))
    exit(1)

def parse_args():
    if not 1 < len(argv) < 4:
        usage()
    if len(argv) == 2:
        return argv[1], -1, -1
    try:
        w, h = map(int, argv[2].split("x"))
    except:
        usage()
    return argv[1], w, h

def get_pos_color_pixel(x, y, image):
    # print x, y
    return ((x, y), image.getpixel((x, y)))

def pycut(image_name, width, height, fmt=lambda x: "{}-".format(chr(ord('a') + x)), factor=10):
    image = Image.open(image_name)
    image.thumbnail((1920, 1080), Image.ANTIALIAS)
    filename = path.basename(image_name)
    dirname = path.dirname(image_name)
    blur = image.filter(ImageFilter.GaussianBlur(125))
    blur.save(path.join(dirname, "blured-{}".format(filename)))

    if not (width > 0 and height > 0):
        return 0

    width *= factor
    height *= factor
    rparts = range(width * height)
    pw, ph = image.size[0] / (width), image.size[1] / (height)
    images = [blur.copy()]
    shuffle(rparts)

    for i, part in enumerate(rparts):
        for x in xrange(pw):
            for y in range(ph):
                images[i / factor ** 2].putpixel(*get_pos_color_pixel(x + pw * (part % (width)), 
                                                                 y + ph * (part / (width)), 
                                                                 image))

        if not (i + 1) % factor ** 2:
            images[i / factor ** 2].save(path.join(dirname, fmt(i / factor ** 2) + filename))
            images.append(images[i / factor ** 2].copy())

    return images

def main():
    image_name, width, height = parse_args()
    pycut(image_name, width, height)
    

if __name__ == "__main__":
    main()
