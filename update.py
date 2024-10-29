from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont

import datetime

app = Flask(__name__)


@app.route("/time")
def get_image_with_current_time():
    image = Image.open("main_background.jpg")
    draw = ImageDraw.Draw(image)

    font_path = r"/root/GitHubUpdater/SourceCodePro-Bold.ttf"
    font_size = 200

    font = ImageFont.truetype(font_path, size=font_size)

    text = str(datetime.datetime.now().strftime("%H:%M"))

    draw.text((50, 820), text, fill="white", font=font)

    image.save(f"result.jpg")

    return send_file("result.jpg")


# app.run(host="127.0.0.1", port=8080)
app.run(host="94.198.216.152", port=50000)

