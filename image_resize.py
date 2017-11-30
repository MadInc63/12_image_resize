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
                        type=float,
                        help='width image in pixel')
    parser.add_argument('-height',
                        type=float,
                        help='height image in pixel')
    parser.add_argument('-scale',
                        type=float,
                        help='scale image in percent')
    return parser.parse_args()


def calculate_apect_ratio(width, height, new_width, new_height):
    if new_width is None:
        new_width = width / (height / new_height)
    elif new_height is None:
        new_height = height / (width / new_width)
    return new_width, new_height


def calculate_after_scaling(width, height, scale):
    return (width * (scale / 100)), (height * (scale / 100))


def scale_validation(width, height, width_scale, height_scale):
    if int((width/height)*100) != int((width_scale / height_scale)*100):
        return True
    else:
        return False


def file_name_for_save_image(path_to_original, path_to_resized,
                             width, height):
    path_to_original = os.path.basename(path_to_original)
    if path_to_resized is None:
        path_to_resized = os.path.splitext(path_to_original)[0] + '__' + str(
            int(width)) + 'x' + str(int(
                height)) + os.path.splitext(path_to_original)[1]
    else:
        path_to_resized = os.path.basename(arg.output)
        path_to_resized = os.path.splitext(path_to_resized)[0] + '__' + str(
            int(width)) + 'x' + str(int(
                height)) + os.path.splitext(path_to_original)[1]
    return path_to_resized


def resize_image(width, height, image, path_to_save_image):
    resized_image = image.resize((int(width), int(height)))
    resized_image.save(path_to_save_image)


if __name__ == '__main__':
    arg = arg_parser()
    path_to_open = arg.input
    path_to_save = arg.output
    resize_width = arg.width
    resize_height = arg.height
    resize_scale = arg.scale
    opened_image = Image.open(path_to_open)
    image_width, image_height = opened_image.size
    if resize_scale is None:
        if resize_width is None and resize_height is None:
            print('There is no argument to change image')
        else:
            if resize_width is not None and resize_height is not None:
                if scale_validation(image_width, image_height,
                                    resize_width, resize_height):
                    print('Not proportional scaling for the '
                          'specified width and height')
            resize_width, resize_height = calculate_apect_ratio(image_width,
                                                                image_height,
                                                                resize_width,
                                                                resize_height)
            path_to_save = file_name_for_save_image(path_to_open,
                                                    path_to_save,
                                                    resize_width,
                                                    resize_height)
            resize_image(resize_width, resize_height,
                         opened_image, path_to_save)
    else:
        if resize_width is None and resize_height is None:
            resize_width, resize_height = calculate_after_scaling(image_width,
                                                                  image_height,
                                                                  resize_scale)
            path_to_save = file_name_for_save_image(path_to_open,
                                                    path_to_save,
                                                    resize_width,
                                                    resize_height)
            resize_image(resize_width,
                         resize_height,
                         opened_image,
                         path_to_save)
        else:
            print('Use only the scale argument or the '
                  'width / height change argument')
