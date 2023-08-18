#!/usr/bin/python3
# 6-print_comb3.py

""a program that prints all possible different combinations of two digits.""

for digit_x in range(0, 10):
    for digit_y in range (digit_x + 1, 10):
        if digit_x == 8 and digit_y == 9:
            print("{}{}".format(digit_x, digit_y))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
