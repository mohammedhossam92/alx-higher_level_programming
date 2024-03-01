#!/usr/bin/python3
new_list = []


def new_in_list(my_list, idx, element):
    for (index, old_element) in enumerate(my_list):

        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        else:
            if index == idx:
                new_list.append(element)
            else:
                new_list.append(old_element)
    return new_list
