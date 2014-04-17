from sys import argv, stderr
from PIL import Image, ImageFilter

def usage():
    stderr.write(("Usage : pycut IMAGE [OPTIONS]...\n"
                  "Try 'pycut --help' for more information.\n"))
    exit(1)
    

def parse_args():
    if len(argv) != 2:
        usage()
    else:
        return argv[1]

def pycut():
    image_name = parse_args()
    image = Image.open(image_name)
    blur = image.filter(ImageFilter.GaussianBlur(75))
    blur.save("blured-{}".format(image_name))

if __name__ == "__main__":
    pycut()
