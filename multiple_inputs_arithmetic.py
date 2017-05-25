"""Math functions for calculator."""


def add(*args):
    """Return the sum of a list of input numbers."""

    answer = 0

    for i in range(len(args)):

        answer += args[i]

    return answer


def subtract(*args):
    """Return the difference of a list of input integers by subtracting
    each successive number from the first (ex. - 5 3 1 = 1)."""

    answer = args[0]

    for i in range(1, len(args)):

        answer -= args[i]

    return answer


def multiply(*args):
    """Return product of all inputs together."""

    answer = 1

    for i in range(len(args)):

        answer *= args[i]

    return answer


def divide(*args):
    """Return the quotient of the first number divided by each subsequent number."""

    answer = args[0]

    for i in range(1, len(args)):

        answer /= args[i]

    return answer


def square(*args):
    """Return the list of squares of the inputs."""

    return [num**2 for num in args]


def cube(*args):
    """Return the cubes of the inputs."""

    return [num**3 for num in args]


def power(*args):
    """Raise num1 to the power of each successive number and return the value."""

    answer = args[0]

    for i in range(1, len(args)):

        answer **= args[i]

    return answer


def mod(*args):
    """Return a list of the remainders of the first input divided by all the others."""

    return [(args[0] % num) for num in args[1:]]


def add_mult(num1, num2, num3):
    """Return the product of num3 and the sum of num1 and num2."""

    return (num1 + num2) * num3


def add_cubes(num1, num2):
    """Return the sum of the cubes of num1 and num2."""

    return num1 ** 3 + num2 ** 3
