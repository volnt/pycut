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
    return ((x, y), image.getpixel((x, y)))

def pycut(image_name, width, height, fmt=lambda x: "{}-".format(chr(ord('a') + x)), factor=10):
    image = Image.open(image_name)
    image.thumbnail((1920, 1080), Image.ANTIALIAS)
    filename = path.basename(image_name)
    dirname = path.dirname(image_name)
    blur = image.filter(ImageFilter.GaussianBlur(100))
    blur.save(path.join(dirname, "zblured-{}".format(filename)))

    if not (width > 0 and height > 0):
        return 0

    rparts = range(width * height * factor ** 2)
    pw, ph = image.size[0] / (width * factor), image.size[1] / (height * factor)
    images = [blur.copy()]
    shuffle(rparts)

    ipart = 0
    for i, part in enumerate(rparts):
        for x in xrange(pw):
            for y in range(ph):
                images[ipart].putpixel(*get_pos_color_pixel(x + pw * (part % (width * factor)), 
                                                            y + ph * (part / (width * factor)), 
                                                            image))
                
        if not (i + 1) % 2 ** (ipart + 3):
            print i
            images[ipart].save(path.join(dirname, fmt(ipart) + filename))
            images.append(images[ipart].copy())
            ipart += 1
    images[ipart].save(path.join(dirname, fmt(ipart) + filename))

    return images

def main():
    image_name, width, height = parse_args()
    pycut(image_name, width, height)
    

if __name__ == "__main__":
    main()
