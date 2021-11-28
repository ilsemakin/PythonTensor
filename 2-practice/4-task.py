#!/usr/bin/python3
import math

try:
    radius = float(input('Input the radius: '))
except ValueError:
    print('Error: You input not a number!')
else:
    print(f'Area of circle = {math.pi * math.pow(radius, 2)}')