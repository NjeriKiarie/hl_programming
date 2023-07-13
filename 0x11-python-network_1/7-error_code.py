#!/usr/bin/python3
"""
A python scriptthat takes in a URL, sends a request to the URL
and displays the body of the response
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.statu_code))
    else:
        print(response.text)
