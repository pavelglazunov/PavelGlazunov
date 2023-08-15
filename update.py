import datetime
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
    # with open("README.md", "a", encoding="utf-8") as file:
    create_bg_image()
#         file.write(f"""
# [bg](https://github.com/pavelglazunov/PavelGlazunov/blob/main/bg_with_time.jpg)
# """)

    os.system("git add ./bg_with_time.jpg")
    os.system(f"git commit -m \"{datetime.datetime.now()}")
    os.system("git push -u origin main")

    time.sleep(60)
#