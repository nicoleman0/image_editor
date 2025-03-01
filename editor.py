from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    # sharpens image and rotates by 90 degrees
    edit = img.filter(ImageFilter.SHARPEN).rotate(-90) 
    
    # contrast enhance
    contrast_factor = 2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(contrast_factor)

    # isolates name of file without extension
    clean_name = os.path.splitext(filename)[0] 

    edit.save(f".{pathOut}/{clean_name}_edited.jpg")