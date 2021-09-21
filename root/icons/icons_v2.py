from .icons_v1 import rectangle
from PIL import Image, ImageDraw

def circle(image: Image, color: tuple, offset: tuple, r: int):
    draw = ImageDraw.Draw(Image)
    draw.ellipse((offset[0]-r, offset[1]-r, offset[0]+r, offset[1]+r), fill=tuple(
        list(color) + [255,]
    ))

def generate_circle_icon(image: Image, string: str, offset: tuple, color: tuple, r: int):
    hex = string.encode('utf-8').hex()
    h = bin(int(hex, 16))
    circle(image, color, offset, r - 10)
    numbers = int(h[:3], 2)
    for i in range(numbers):
        color_ = (255, 255, 255) if i % 2 == 0 else color
        r_ = int(h[:i+1], 2) * r / 5
        circle(image, color_, offset, r_)

def generate_icon_v2(string: str):
    hex = string.encode('utf-8').hex()
    h = bin(int(hex, 16))