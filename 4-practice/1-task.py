#!/usr/bin/python3

def main():
    """Outputs a sorted list."""
    print(buble_sort(input_list('Enter a list of numbers: ')))


def buble_sort(array):
    """Returns a list sorted by bubble sort.

    Parameters
    ----------
    array : list
        Unsorted list

    Returns
    -------
    list
        sorted list
    """
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def input_list(message):
    """Returns a list of floating point numbers that
    were obtained by converting a list of strings.

    Parameters
    ----------
    message : str
        A message to the user when entering data

    Returns
    -------
    list
        a list of float numbers
    """
    while True:
        try:
            numbers = input(message).split(' ')
            for index, number in enumerate(numbers):
                numbers[index] = float(number)
        except ValueError:
            print('Input not a number!\n')
        else:
            return numbers

if __name__ == '__main__':
    main()