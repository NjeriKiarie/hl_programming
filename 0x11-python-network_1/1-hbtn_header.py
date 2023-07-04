#!/usr/bin/python3
"""
a script that takes in a url, sends a request to the url
displays the value of the x-Request-Id.
Variable found in the header of the response.

use pacjages otherthan urllib and sys
must use a with statement
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    req = request.Request(argv[1])

    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
