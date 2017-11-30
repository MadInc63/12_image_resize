# Image Resizer

The script allows you to change the size of the specified image and save the result to the specified file.

# How to use

The script requires the installed Python interpreter version 3.5 To call the help, run the script with the -h or --help option.

```Bash
>python image_resize.py -h
usage: image_resize.py [-h] [-output OUTPUT] [-width WIDTH] [-height HEIGHT]
                       [-scale SCALE]
                       input

Resize image

positional arguments:
  input           path to open original image file

optional arguments:
  -h, --help      show this help message and exit
  -output OUTPUT  path to save resized image file
  -width WIDTH    width image in pixel
  -height HEIGHT  height image in pixel
  -scale SCALE    scale image in percent
```

To change the size of the image, you must specify the file name and arguments:

If you specify the width or height of the new file, then the script automatically calculates the correct proportion.

```Bash
>python image_resize.py pic.jpg -output new_pic.jpg -width 500
```

If you specify the width and height of the new file, the script displays a warning if the entered width and height are not proportional to the original image and creates a file with the specified parameters.

```Bash
>python image_resize.py pic.jpg -output new_pic.jpg -width 500 -height 200
Not proportional scaling for the specified width and height
```

If you specify a scaling option, the script will change the size according to the scaling of the image scale.

```Bash
>python image_resize.py pic.jpg -output new_pic.jpg -scale 80
```

If you specify the scaling option and the width / height of the new image, the corresponding message will be displayed and the new file will not be saved.

```Bash
>python image_resize.py pic.jpg -output new_pic.jpg -width 500 -height 200 -scale 80
Use only the scale argument or the width / height change argument
```

If you do not specify more than one size change option, the program displays a message.

```Bash
>python image_resize.py pic.jpg -output new_pic.jpg
There is no argument to change image
```

The result of the program. To a new file name is added suffix `__WIDTHxHEIGTH` if the name was not specified then the program will take the name of the source file and add it to it suffix `__WIDTHxHEIGTH`.

```Bash
30.11.2017  15:39            25 026 new_pic__500x200.jpg
30.11.2017  15:38            30 314 new_pic__500x250.jpg
30.11.2017  15:44            62 122 new_pic__768x384.jpg
30.11.2017  08:13           159 429 pic.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
