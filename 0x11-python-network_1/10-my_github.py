#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
must use Basic Authentication with a personal access token
as password to access to your information
(only read:user permission is needed)
The first argument will be your username
The second argument will be your password
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.orgv[1], sys.argv[2])
    response = get('https://api.github.com/user', auth=auth)
    print(response.json().get('id'))
