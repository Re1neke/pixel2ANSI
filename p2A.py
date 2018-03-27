#!/usr/bin/env python3

from sys import argv
from PIL import Image

image = Image.open(argv[1])
rgba_image = image.convert('RGBA')

pixel_list = [[rgba_image.getpixel((x, y))
               for x
               in range(rgba_image.width)]
              for y
              in range(rgba_image.height)]

row = ""


def get_esc_seq(filler, fg_color, bg_color=None):
    fg_seq_template = "\033[38;2;{0[0]};{0[1]};{0[2]}m{1}\033[0m"
    bg_seq_template = "\033[48;2;{0[0]};{0[1]};{0[2]}m"
    esq_seq = fg_seq_template.format(fg_color, filler)
    if bg_color is not None:
        esq_seq = bg_seq_template.format(bg_color) + esq_seq
    return esq_seq


for row_num, pixel_row in enumerate(pixel_list):
    if row_num % 2:
        continue
    for pixel_num, pixel in enumerate(pixel_row):
        if pixel == pixel_list[row_num + 1][pixel_num]:
            if pixel[3] == 0:
                row += " "
            else:
                row += get_esc_seq('█', pixel[:3])
        elif pixel[3] != 0 and pixel_list[row_num + 1][pixel_num][3] != 0:
            row += get_esc_seq('▄', pixel_list[row_num + 1][pixel_num][:3], pixel[:3])
        else:
            if pixel[3] == 0:
                row += get_esc_seq('▄', pixel_list[row_num + 1][pixel_num][:3])
            else:
                row += get_esc_seq('▀', pixel[:3])
    row += '\n'

print(row)
