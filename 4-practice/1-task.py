#!/usr/bin/python3
import sys

def main():
    print(buble_sort(input_list('Enter a list of numbers: ')))


def buble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def input_list(message):
    while True:
        try:
            numbers = input(message).split(' ')
            for index, number in enumerate(numbers):
                numbers[index] = float(number)
        except ValueError:
            print('Input not a number!\n')
        else:
            return numbers
        
main()