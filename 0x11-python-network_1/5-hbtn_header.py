#!/usr/bin/python3
"""
a python script thats makes a url send a request to the URL
and display the value of the value of the variable X-Request-Id
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
