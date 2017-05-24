"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    user_input = raw_input("")
    tokens = user_input.split(" ")
    if tokens[0] == 'q':
        break
    else:
        arg1, arg2 = float(tokens[1]), float(tokens[2])
        if tokens[0] == '+':
            print add(arg1, arg2)
        elif tokens[0] == '-':
            print subtract(arg1, arg2)

