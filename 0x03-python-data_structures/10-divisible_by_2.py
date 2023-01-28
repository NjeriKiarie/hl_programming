#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    multiples = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    retur (multiples)
