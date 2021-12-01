#!/usr/bin/python3
import random

def main():
    dict_color = {}

    for _ in range(10):
        hex_color = '{:06x}'.format(random.randint(0, 0xFFFFFF))
        dict_color[hex_color] = hex_to_rgb(hex_color)
    
    print(dict_color)

def hex_to_rgb(color):
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

main()