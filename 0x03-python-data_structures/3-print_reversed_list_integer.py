#!/usr/bin/python3
new_list = []


def print_reversed_list_integer(my_list=[]):
    for number in my_list:
        new_list.append(number)
    my_list = new_list[::-1]

    for number in my_list:
        print("{:d}".format(number))
