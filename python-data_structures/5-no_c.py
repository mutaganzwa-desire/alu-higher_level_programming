#!/usr/bin/python3
def no_c(my_string):
    new_string = "".join(char for char in my_string if char not in ('c', 'C'))
    return new_string
