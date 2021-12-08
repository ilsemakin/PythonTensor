#!/usr/bin/python3

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    data = read_file(input_file)
    if data is not None:
        write_file(output_file, calc_molecules(data))

def calc_molecules(data):
    return min([data[0] // 3, data[1] // 6, data[2]])

def read_file(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return check_data(file.readline())
    except FileNotFoundError:
        print('File not found!')
        return None

def write_file(name, data):
    with open(name, 'w') as file:
        file.write(str(data))

def check_data(data):
    try:
        data = [int(data) for data in [data for data in data.split(' ') if data]]
    except ValueError:
        print('A non-natural number was read!')
        return None
    else:
        if len(data) >= 3:
            return data[0:3]
        else:
            print('There is not enough data in the file!')
            return None

main()