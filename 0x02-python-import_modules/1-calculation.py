#!/usr/bin/python3

if __name == "__main__":
    """Print the sum, difference, quotient & multiple of 10 and 5."""
    from calculator_1 import add, sub, div, mul

    b = 5
    a = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
