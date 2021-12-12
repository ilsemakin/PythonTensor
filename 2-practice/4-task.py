#!/usr/bin/python3
from math import pi as PI

try:
    radius = float(input('Input the radius: '))
except ValueError:
    print('Error: You input not a number!')
else:
    print(f'Area of circle = {PI * radius**2}')