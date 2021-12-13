#!/usr/bin/python3

def main():
    """Prints an encoded and decoded list of strings."""
    encoded_strings = encode_list(input_list('Enter a list of strings: '))
    decoded_strings = decode_list(encoded_strings)

    print(f'Encoded strings: {encoded_strings}')
    print(f'Decoded strings: {decoded_strings}')

def encode_list(strings):
    """Returns an encoded list of strings as a list of tuples.

    Parameters
    ----------
    strings : list
        Source string list
    
    Returns
    -------
    list
        encoded list of tuples
    """
    return [tuple(ord(symbol) for symbol in string) for string in strings]

def decode_list(strings):
    """Returns a list of strings after decoding a list of tuples.

    Parameters
    ----------
    strings : list
        List of encoded tuples
    
    Returns
    -------
    list
        a list of strings
    """
    return [''.join([chr(code) for code in string]) for string in strings]

def input_list(message):
    """Returns a list of strings without spaces.

    Parameters
    ----------
    message : str
        A message to the user when entering data
    
    Returns
    -------
    list
        a list of strings without spaces
    """
    return [string for string in input(message).split(' ') if string]

if __name__ == '__main__':
    main()