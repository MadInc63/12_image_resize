import argparse
import os
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description='Resize image')
    parser.add_argument(
        'input',
        type=str,
        help='path to open original image file'
    )
    parser.add_argument(
        '-output',
        type=str,
        help='path to save resized image file'
    )
    parser.add_argument(
        '-width',
        type=int,
        help='width image in pixel'
    )
    parser.add_argument(
        '-height',
        type=int,
        help='height image in pixel'
    )
    parser.add_argument(
        '-scale',
        type=int,
        help='scale image in percent'
    )
    return parser.parse_args()


def calculate_aspect_ratio(original_image, new_width, new_height):
    width, height = original_image.size
    if new_height and new_width:
        return new_width, new_height
    elif new_width is None:
        return int(width/(height/new_height)), new_height
    elif new_height is None:
        return new_width, int(height/(width/new_width))


def scaling_image(image, percent):
    return [int((size * percent/100)) for size in image.size]


def resize_image(original_image, new_image_size):
    return original_image.resize(new_image_size, Image.ANTIALIAS)


def generates_file_name_for_save(
        path_to_original,
        path_to_resized,
        image_for_save
):
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
    accuracy = 100
    args = parse_args()
    opened_image = Image.open(args.input)
    if args.scale and (args.width or args.height):
        raise RuntimeError(
            'Use only the scale argument or the width/height change argument'
        )
    elif not args.scale and not args.width and not args.height:
            raise RuntimeError(
                'There is no argument to change image'
            )
    elif args.scale:
            new_size = scaling_image(
                opened_image,
                args.scale
            )
    else:
        new_size = calculate_aspect_ratio(
            opened_image,
            args.width,
            args.height
        )
        aspect_ratio = (opened_image.size[0] / opened_image.size[1])
        aspect_ratio_new = (new_size[0] / new_size[1])
        if int(aspect_ratio * accuracy) != int(aspect_ratio_new * accuracy):
            print(
                'Not proportional scaling for the specified width and height'
            )
    resized_image = resize_image(opened_image, new_size)
    file_name_for_save = generates_file_name_for_save(
        args.input,
        args.output,
        resized_image
    )
    save_image(resized_image, file_name_for_save)
