#!/usr/bin/python3
"""
a script that fetches https://alx-intranet.hbtn.io/status
must use a with statement
use the package url
"""

import urllib.request
with urllib.request.urlopen('https:alx-intranet.hbtn.io/status') as response:
        html = response.read()

print('Body response:\n\t- type: {}'.format(type(html))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.formart(html.decode('utf-8')))
