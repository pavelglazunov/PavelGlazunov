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

    image.save(f"bg_with_time_{switcher}.jpg")


switcher = 1
# for i in range(10):
#     print(switcher)


# sys.exit()
while True:
    # time.sleep(60 - datetime.datetime.now().second)
    # os.remove(f"bg_with_time_{switcher}.jpg")
    # switcher = (switcher + 1) % 2
    create_bg_image()

    time.sleep(1)
    os.system(f"git add .")
    os.system(f"git commit -m \"time\"")
    os.system("git push -u origin main")

    time.sleep(60)
#
