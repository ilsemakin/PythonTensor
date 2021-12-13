#!/usr/bin/python3
import functions as fn

test_string = fn.input_string('Enter the string: ')

control = fn.is_int(test_string)
print(f'Is the string an integer?: {control}')

control = fn.is_float(test_string)
print(f'Is the string a floating point number?: {control}')

control = fn.is_positive(test_string)
print(f'Is the number positive?: {control}')

control = fn.is_zero(test_string)
print(f'Is the number zero?: {control}')
