# pip3 install pytesseract

import pytesseract
import os
from PIL import Image

def convert():
    img = Image.open('img.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()