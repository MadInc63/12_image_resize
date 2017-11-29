import argparse
from PIL import Image


def image_open(path_to_original):
    img = Image.open(path_to_original)
    return img


def calculates_the_aspect_ratio(resize_width, resize_heigth, img):
    width, heigth = img.size
    if resize_heigth == 0:
        resize_heigth = int(round(heigth/(float(width) / resize_width)))
    elif resize_width == 0:
        resize_width = int(round(width/(float(heigth) / resize_heigth)))
    print(width, heigth)
    print(resize_width, resize_heigth)


def resize_image(path_to_original, path_to_result):
    img = Image.open(path_to_original)
    width, heigth = img.size
    resized_img = img.resize((200, 200))
    resized_img.save(path_to_result)
    print(width, heigth)

if __name__ == '__main__':
    path_to_original = 'python.png'
    path_to_result = 'python_resize.png'
    resize_width = 0
    resize_heigth = 200
    img = image_open(path_to_original)
    calculates_the_aspect_ratio(resize_width, resize_heigth, img)

