"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

print "This calculator currently takes a max of 2 numbers per operation."

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    operator = tokens[0]
    other_tokens = tokens[1:]
    try:
        args = [float(token) for token in other_tokens]

        # while i < len(other_tokens):
        #     for token in other_tokens:
        #         args[i] = float(token)
        #         i += 1

    except ValueError:
        print "Please enter valid numbers."
    else:
        if operator == 'q':
            break
        elif operator == '+':
            print reduce(add, args)
        # elif operator == '-':
        #     print subtract(*args)
        # elif operator == '*':
        #     print multiply(*args)
        # elif operator == '/':
        #     print divide(*args)
        # elif operator == "square":
        #     print square(*args)
        # elif operator == "cube":
        #     print cube(*args)
        # elif operator == "pow":
        #     print power(*args)
        # elif operator == "mod":
        #     print mod(*args)
        # else:
        #     print "Not a recognized operation."


# user_input = raw_input("> ")
# tokens = user_input.split(" ")
# operator = tokens[0]
# other_tokens = tokens[1:]
# reduce(add(), other_tokens)
