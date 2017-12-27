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


def calculate_aspect_ratio(image, new_width, new_height):
    width, height = image.size
    if new_height and new_width:
        return new_width, new_height
    elif new_width is None:
        return int(width/(height/new_height)), new_height
    elif new_height is None:
        return new_width, int(height/(width/new_width))


def scaling_image(image, percent):
    return [int((size * percent/100)) for size in image.size]


def resize_image(image, size):
    return image.resize(size, Image.ANTIALIAS)


def build_file_name(path, image):
    file_name, file_extension = os.path.splitext(path)
    generated_name = '{}__{}x{}{}'.format(
        file_name,
        *image.size,
        file_extension)
    return generated_name


def get_file_name_for_save(
        path_to_original,
        path_to_resized,
        image
):
    if path_to_resized:
        return build_file_name(path_to_resized, image)
    else:
        return build_file_name(path_to_original, image)


def save_image(image_for_save, path_to_result):
    image_for_save.save(path_to_result)


if __name__ == '__main__':
    accuracy = 100
    args = parse_args()
    opened_image = Image.open(args.input)
    width_original, height_original = opened_image.size
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
        aspect_ratio = (width_original / height_original)
        width_resized, height_resized = new_size
        aspect_ratio_new = (width_resized / height_resized)
        if int(aspect_ratio * accuracy) != int(aspect_ratio_new * accuracy):
            print(
                'Not proportional scaling for the specified width and height'
            )
    resized_image = resize_image(opened_image, new_size)
    file_name_for_save = get_file_name_for_save(
        args.input,
        args.output,
        resized_image
    )
    save_image(resized_image, file_name_for_save)
