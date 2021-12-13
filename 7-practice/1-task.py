#!/usr/bin/python3
from os import name, getlogin, listdir

print(f'Operating system name: {name}')
print(f'Terminal username: {getlogin()}')
print(f'Files and folders of the current directory: {listdir(path=".")}')