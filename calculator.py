"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    first_token = tokens[0]
    other_tokens = tokens[1:]
    i = 0
    arg_dict = {}
    try:
        while i < len(other_tokens):
            for token in other_tokens:
                arg_dict[i] = float(token)
                i += 1
    except:
        print "Please enter valid numbers."
    finally:
        try:
            if tokens[0] == 'q':
                break
            elif tokens[0] == '+':
                print add(arg_dict[0], arg_dict[1])
            elif tokens[0] == '-':
                print subtract(arg_dict[0], arg_dict[1])
            elif tokens[0] == '*':
                print multiply(arg_dict[0], arg_dict[1])
            elif tokens[0] == '/':
                print divide(arg_dict[0], arg_dict[1])
            elif tokens[0] == "square":
                print square(arg_dict[0])
            elif tokens[0] == "cube":
                print cube(arg_dict[0])
            elif tokens[0] == "pow":
                print power(arg_dict[0], arg_dict[1])
            elif tokens[0] == "mod":
                print mod(arg_dict[0], arg_dict[1])
            else:
                print "Not a recognized operation."
        except:
            print "Enter numbers:"