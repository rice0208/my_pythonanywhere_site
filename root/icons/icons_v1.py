from PIL import Image
from random import shuffle

def rectangle(image: Image, color: tuple, offset: tuple,):
    image.paste(color, offset)

def generate_icon_v1(number: int):
    h = bin(number)
    h = (h[2:] * 64)[:64]
    if h[0] == "0":
        b = (1, int(h[0]))
    else:
        b = (0, int(h[0]))
    color = [
        int(
            h[1:6],
            2,
        )
        + 84,
        int(
            h[7:12],
            2,
        )
        + 84,
        int(
            h[13:18],
            2,
        )
        + 84,
    ]
    if h[1:4] == "000":
        color[0] += 76
    elif h[1:4] == "001" or h[1:4] == "110":
        color[1] += 76
    elif h[1:4] == "010" or h[1:4] == "111":
        color[2] += 76
    elif h[1:4] == "011":
        color[0] += 76
        color[1] += 76
    elif h[1:4] == "100":
        color[0] += 76
        color[2] += 76
    elif h[1:4] == "101":
        color[1] += 76
        color[2] += 76
    if b == (
        0,
        0,
    ):
        image = Image.new("RGB", (1200, 1200), tuple(color))
        color = [i + 75 for i in color]
    elif b == (
        0,
        1,
    ):
        image = Image.new("RGB", (1200, 1200), tuple([i + 144 for i in color]))
    elif b == (
        1,
        0,
    ):
        image = Image.new("RGB", (1200, 1200), (255, 255, 255))
    else:
        image = Image.new("RGB", (1200, 1200), tuple(color))
        color = [255, 255, 255]
    color = tuple(color)
    c = h[25:31] if b[0] == 0 else h[25:35]
    if b[0] == 0:
        for i in [
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],
            [(4, 0), (3, 0), (2, 0), (4, 1), (3, 1), (2, 1)],
            [(0, 4), (1, 4), (2, 4), (0, 3), (1, 3), (2, 3)],
            [(4, 4), (4, 3), (4, 2), (3, 4), (3, 3), (3, 2)],
        ]:
            for j in range(6):
                if c[j] == '0':
                    rectangle(image, color, tuple([200 * p + 100 for p in i[j]] + [200 * p + 300 for p in i[j]]))
        if h[31]:
            image.paste(color, (400, 400, 200, 200))
    else:
        for i in [
            [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (1, 0),
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
            ],
            [
                (4, 0),
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 4),
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (3, 4),
            ],
        ]:
            for j in range(10):
                if c[j] == "0":
                    image.paste(
                        color,
                        tuple(
                            [200 * p + 100 for p in i[j]]
                            + [200 * p + 300 for p in i[j]]
                        ),
                    )
        for i in [[(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]]:
            for j in range(5):
                if h[35:40][j] == "0":
                    image.paste(
                        color,
                        tuple(
                            [200 * p + 100 for p in i[j]]
                            + [200 * p + 300 for p in i[j]]
                        ),
                    )
    return image
