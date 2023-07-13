#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
must use the packages requests and sys
not allowed to import packages other than requests and sys
don’t need to check arguments passed to the script (number or type)
"""
if __name__ == '__main__':
    impoert requests
    from sys import argv
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(argv[2], argv[1]))
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
