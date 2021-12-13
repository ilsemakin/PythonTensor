#!/usr/bin/python3

up = ['up', 'вверх']
down = ['down', 'вниз']
right = ['right', 'вправо']
left = ['left', 'влево']

def main():
    """Modifies and prints coordinate parameters."""
    x = y = 0

    command = input_command('Enter the command: ')

    movement = command[0]
    step = command[1]

    _x, _y = x, y

    if movement in up: y += step
    elif movement in down: y -= step
    elif movement in right: x += step
    elif movement in left: x -= step

    print(f'({_x}; {_y}) -> ({x}; {y})\n')

def input_command(message):
    """Returns the correct command.
    
    Parameters
    ----------
    message : str
        A message to the user when entering data

    Returns
    -------
    list
        a list in the format [command, number]
    """
    movements = up + down + right + left
    
    while True:
        command = input(message).split(' ')
        movement = command[0]

        if movement not in movements or len(command) != 2:
            print('Command not defined!\n')
            continue

        try:
            command[1] = float(command[1])
        except ValueError:
            print('The input is not a number!\n')
        else:
            return command

if __name__ == '__main__':
    main()