#!/usr/bin/python3

"""module give a function that prints say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'my name is' followed by the
    first name and last name(optional)
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
