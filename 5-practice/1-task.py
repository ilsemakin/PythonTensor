#!/usr/bin/python3

def main():
    """Prints password strength."""
    if input_password('Enter password: '):
        print('Good password!')
    else:
        print('Password does not meet requirements!')

def input_password(message):
    """Checks the strength of the password.
    
    Parameters
    ----------
    message : str
        A message to the user when entering data
    
    Returns
    -------
    True
        if the password meets all the conditions
    False
        if the password does not match the conditions
    """
    black_list = 'password'
    password = input(message)
    
    if len(password) >= 6:
        if password.isdigit() or black_list in password.lower():
            return False
        
        for index in range(len(password)):
            if password[index].isdigit():
                return True     
    else:
        return False

if __name__ == '__main__':
    main()