# https://cs50.harvard.edu/python/2022/psets/6/shirt/
import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command=line arguments')
    elif os.path.splitext(sys.argv[2])[1] not in ['.jpg', '.jpeg', '.png']:
        sys.exit('Invalid output')
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit('Input and output have different extensions')
    else:
        try:
            photo = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit('Input does not exist')
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = ImageOps.fit(photo, size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])


if __name__ == '__main__':
    main()
