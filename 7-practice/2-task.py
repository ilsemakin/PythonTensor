#!/usr/bin/python3
from numpy.random import randint
from numpy import transpose

array = randint(-10, 10, (3, 3))

print(f'Source array:\n{array}')
print(f'Transposed:\n{transpose(array)}')