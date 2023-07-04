#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request to the URL
Displays the body of the response(decoded in utf-8).
manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code.
"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    from sys import argv

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as httperror:
        print('Error code: {}'.format(httperror.code))
