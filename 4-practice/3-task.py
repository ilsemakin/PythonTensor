#!/usr/bin/python3
from random import randint

set_1 = set(randint(-50, 50) for _ in range(20))
set_2 = set(randint(-50, 50) for _ in range(20))

print(f'set1 = {set_1}\nset2 = {set_2}\n')

print(f'Intersection = {set_1 & set_2}')
print(f'Difference set1 and set2 = {set_1 - set_2}')
print(f'Difference set2 and set1 = {set_2 - set_1}')
print(f'Symmetric difference = {set_1 ^ set_2}')