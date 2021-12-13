#!/usr/bin/python3
from random import randint

def main():
    """Displays a dictionary of matches between
    random HEX colors and RGB colors."""
    dict_color = {}

    for _ in range(10):
        hex_color = '{:06x}'.format(randint(0, 0xFFFFFF))
        dict_color[hex_color] = hex_to_rgb(hex_color)
    
    for key, value in dict_color.items():
        print(f'Hex color: {key} --> RGB color: {value}')

def hex_to_rgb(color):
    """Returns a color to the RGB from HEX.

    Parameters
    ----------
    color : str
        Hexadecimal string

    Returns
    -------
    tuple
        a tuple of 3 base color values
    """
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

if __name__ == '__main__':
    main()