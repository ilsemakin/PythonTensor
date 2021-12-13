#!/usr/bin/python3

def main():
    """Reads atoms from a file and outputs
    the number of molecules to another file."""
    input_file = 'input.txt'
    output_file = 'output.txt'

    data = read_file(input_file)
    if data is not None:
        write_file(output_file, calc_molecules(data))

def calc_molecules(data):
    """Calculates how many alcohol molecules can be composed of atoms.

    Parameters
    ----------
    data : list
        List of the number of atoms
    
    Returns
    -------
    int
        minimum number of molecules
    """
    return min([data[0] // 3, data[1] // 6, data[2]])

def read_file(name):
    """Reads data from a file.

    Parameters
    ----------
    name : str
        File name to read
    
    Returns
    -------
    str
        string of file data
    None
        if the file is not found
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = check_data(file.readline())
    except FileNotFoundError:
        print('File not found!')
        return None
    else:
        return data

def write_file(name, data):
    """Writes data to a file.

    Parameters
    ----------
    name : str
        File name to write
    data : int
        Number of molecules
    """
    with open(name, 'w') as file:
        file.write(str(data))

def check_data(data):
    """Checks read data.

    Parameters
    ----------
    data : str
        String from file
    
    Returns
    -------
    list
        a list of integers
    None
        if there were errors when checking
    """
    data = [_data for _data in data.split(' ') if _data]

    try:
        data = [int(_data) for _data in data]
    except ValueError:
        print('A non-natural number was read!')
        return None
    else:
        if len(data) >= 3:
            return data[0:3]
        else:
            print('There is not enough data in the file!')
            return None

if __name__ == '__main__':
    main()