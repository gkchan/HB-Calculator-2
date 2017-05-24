"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    try:
        arg1, arg2 = float(tokens[1]), float(tokens[2])
    except IndexError:
        arg1 = float(tokens[1])
    finally:
        if tokens[0] == 'q':
            break
        elif tokens[0] == '+':
            print add(arg1, arg2)
        elif tokens[0] == '-':
            print subtract(arg1, arg2)
        elif tokens[0] == '*':
            print multiply(arg1, arg2)
        elif tokens[0] == '/':
            print divide(arg1, arg2)
        elif tokens[0] == "square":
            print square(arg1)
        elif tokens[0] == "cube":
            print cube(arg1)
        elif tokens[0] == "pow":
            print power(arg1, arg2)
        elif tokens[0] == "mod":
            print mod(arg1, arg2)
        else:
            print "Not a recognized operation."