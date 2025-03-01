from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(-90)

    clean_name = os.path.splitext(filename)[0] # isolates name of file without extension

    edit.save(f".{pathOut}/{clean_name}_edited.jpg")