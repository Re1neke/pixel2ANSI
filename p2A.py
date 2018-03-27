#!/usr/bin/env
"""pixel to ANSI - is for convert your picture to ANSI characters.

The tiny script that translates image into chain of ANSI escape sequences and
char blocks. In the result you will get text file that will form enough pretty
picture in your terminal.

Copyright (c) 2018, Max Reineke
"""

from sys import argv
from PIL import Image
from os.path import basename, splitext


def get_image_info(image_path):
    image = Image.open(image_path)
    rgba_image = image.convert('RGBA')
    pixel_list = [[rgba_image.getpixel((x, y))
                   for x
                   in range(rgba_image.width)]
                  for y
                  in range(rgba_image.height)]
    if rgba_image.height % 2:
        pixel_list.append([(0, 0, 0, 0) for i in range(rgba_image.height)])
    image.close()
    return pixel_list


def get_esc_seq(filler, fg_color, bg_color=None):
    fg_seq_template = "\033[38;2;{0[0]};{0[1]};{0[2]}m{1}\033[0m"
    bg_seq_template = "\033[48;2;{0[0]};{0[1]};{0[2]}m"
    esq_seq = fg_seq_template.format(fg_color, filler)
    if bg_color is not None:
        esq_seq = bg_seq_template.format(bg_color) + esq_seq
    return esq_seq


def select_block_colors(top_pixel, bot_pixel):
    if top_pixel == bot_pixel and top_pixel[3] != 0:
        return get_esc_seq('█', top_pixel[:3])
    elif top_pixel[3] == 0 and bot_pixel[3] == 0:
        return " "
    elif top_pixel[3] != 0 and bot_pixel[3] != 0:
        return get_esc_seq('▄', bot_pixel[:3], top_pixel[:3])
    else:
        if top_pixel[3] == 0:
            return get_esc_seq('▄', bot_pixel[:3])
        else:
            return get_esc_seq('▀', top_pixel[:3])


def pixel_list_to_str(pixel_list):
    row = ""
    for row_num, pixel_row in enumerate(pixel_list):
        if row_num % 2:
            continue
        for pixel_num, pixel in enumerate(pixel_row):
            row += select_block_colors(
                                       pixel,
                                       pixel_list[row_num + 1][pixel_num]
                                      )
        row += '\n'
    return row


if len(argv) <= 1 or len(argv) > 3:
    print("Usage: %s image_name [result_file_name]" % argv[0])
    exit(1)

result = pixel_list_to_str(get_image_info(argv[1]))
if len(argv) == 3:
    res_file_name = argv[2]
else:
    res_file_name = splitext(basename(argv[1]))[0] + "_result"
res_file = open(res_file_name, 'w')
res_file.write(result)
res_file.close()
