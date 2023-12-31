#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    "" prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.""

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz",end ="")
    elif numbers % 5 == 0:
        print("Buzz",end="")
    elif numbers % 3 == 0:
        print("Fizz",end="")
    else:
        print("{} ".format(numbers), end="")
