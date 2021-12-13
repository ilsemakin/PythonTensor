def input_string(message):
    """Returns a non-empty string.
    
    Parameters
    ----------
    message : str
        A message to the user when entering data

    Returns
    -------
    str
        a string if not empty
    """
    while True:
        string = input(message)
        if not string:
            print('The input is an empty string!')
        else:
            return string

def is_int(number):
    """Checks if a string is an integer.
    
    Parameters
    ----------
    number : str
        String to check

    Returns
    -------
    True
        if the string is an integer
    False
        otherwise
    """
    try:
        int(number)
    except ValueError:
        return False
    else:
        return True

def is_float(number):
    """Checks if a string is a floating point number.
    
    Parameters
    ----------
    number : str
        String to check

    Returns
    -------
    True
        if the string is a floating point number
    False
        otherwise
    """
    try:
        float(number)
    except ValueError:
        return False
    else:
        return True if not number.isdigit() else False 

def is_positive(number):
    """Checks if a string is a positive number.

    Parameters
    ----------
    number : str
        String to check
    
    Returns
    -------
    True
        if the number is positive
    False
        if it is not a number or the number is negative
    """
    if (is_int(number) or is_float(number)):
        if float(number) > 0:
            return True
    
    return False

def is_zero(number):
    """Checks whether a string is zero.

    Parameters
    ----------
    number : str
        String to check
    
    Returns
    -------
    True
        if string is number zero
    False
        otherwise
    """
    if (is_int(number) or is_float(number)):
        if float(number) == 0:
            return True
    
    return False