import argparse
import os
from PIL import Image


def arg_parser():
    parser = argparse.ArgumentParser(description='Resize image')
    parser.add_argument('input',
                        type=str,
                        help='path to open original image file')
    parser.add_argument('-output',
                        type=str,
                        help='path to save resized image file')
    parser.add_argument('-width',
                        type=int,
                        help='width image in pixel')
    parser.add_argument('-height',
                        type=int,
                        help='height image in pixel')
    parser.add_argument('-scale',
                        type=int,
                        help='scale image in percent')
    return parser.parse_args()


def calculate_aspect_ratio(original_image, new_width, new_height):
    width, height = original_image.size
    if new_height and new_width:
        if int((width/height)*100) != int((new_width/new_height)*100):
            print('Not proportional scaling for the '
                  'specified width and height')
        return new_width, new_height
    elif new_width is None:
        return int(width/(height/new_height)), new_height
    elif new_height is None:
        return new_width, int(height/(width/new_width))


def calculate_after_scaling(original_image, scale):
    return [int((size * scale/100)) for size in original_image.size]


def resize_image(original_image, new_image_size):
    return original_image.resize(new_image_size, Image.ANTIALIAS)


def file_name_for_save_image(path_to_original,
                             path_to_resized,
                             image_for_save):
    if path_to_resized:
        file_name = os.path.splitext(path_to_resized)[0]
        file_extension = os.path.splitext(path_to_original)[1]
        path_to_resized = '{}__{}x{}{}'.format(
            file_name,
            *image_for_save.size,
            file_extension)
        return path_to_resized
    else:
        file_name, file_extension = os.path.splitext(path_to_original)
        created_path = '{}__{}x{}{}'.format(
            file_name,
            *image_for_save.size,
            file_extension)
        return created_path


def save_image(image_for_save, path_to_result):
    image_for_save.save(path_to_result)


if __name__ == '__main__':
    new_size = [0, 0]
    arg = arg_parser()
    path_to_save = arg.output
    opened_image = Image.open(arg.input)
    if arg.scale is None:
        if arg.width is None and arg.height is None:
            raise RuntimeError('There is no argument to change image')
        elif arg.width or arg.height:
            new_size = calculate_aspect_ratio(opened_image,
                                              arg.width,
                                              arg.height)
    else:
        if arg.width or arg.height:
            raise RuntimeError('Use only the scale argument or the '
                               'width / height change argument')
        elif arg.width is None and arg.height is None:
            new_size = calculate_after_scaling(opened_image, arg.scale)
    resized_image = resize_image(opened_image, new_size)
    file_name_for_save = file_name_for_save_image(arg.input,
                                                  arg.output,
                                                  resized_image)
    save_image(resized_image, file_name_for_save)
