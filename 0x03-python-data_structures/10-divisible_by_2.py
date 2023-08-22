#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for count, d in enumerate(my_list):
        if d % 2 == 0:
            boolist[count] = True
        else:
            boolist[count] = False
    return(boolist)
