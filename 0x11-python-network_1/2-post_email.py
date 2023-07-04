#!/usr/bin/python3
"""
A script that takes ina URL and an email,
sends a POST request to the passed URL
the email as a parameter
displays the body of the response (decoded in utf-8)

the email must be sent in the email variable
must use the packages urllib and sys
use the with statement
"""

if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
