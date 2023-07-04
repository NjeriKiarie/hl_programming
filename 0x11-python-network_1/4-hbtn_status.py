#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
must use the package requests
the response display must be in tabulation
"""

if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    response = req.text

    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
