import datetime
import sys
import time
import os

from PIL import Image, ImageDraw, ImageFont


def create_bg_image():
    image = Image.open("bg.jpg")
    size = image.size
    draw = ImageDraw.Draw(image)

    font_path = r"C:\Users\HP\AppData\Local\Microsoft\Windows\Fonts\SourceCodePro-Bold.ttf"
    font_size = 500

    font = ImageFont.truetype(font_path, size=font_size)

    text = str(datetime.datetime.now().strftime("%H:%M"))

    draw.text((100, 2100), text, fill="white", font=font)

    image.save("bg_with_time.jpg")


while True:
    time.sleep(60 - datetime.datetime.now().second)

    create_bg_image()

    os.system("git add .")
    os.system(f"git commit -m \"{datetime.datetime.now()}\"")
    os.system("git push -u origin main")

    time.sleep(60)
#