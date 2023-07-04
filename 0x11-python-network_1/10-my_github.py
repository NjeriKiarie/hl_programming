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

if __name__ == '__main__':
    import requests
    from sys import argv

    response = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(response.json().get('id'))
