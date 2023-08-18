#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    ""a function that prints a string in uppercase""
    for x in str:
        if ord(c) >= 97 and ord(c) <= 122:
            x = chr(ord(c) - 32)
            print("{}".format(x), end="")
            print("")
