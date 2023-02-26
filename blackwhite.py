from PIL import Image, ImageOps
import os

path = "./images"
pathOut = "./bwImages"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageOps.grayscale)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_bwImage.jpg')

