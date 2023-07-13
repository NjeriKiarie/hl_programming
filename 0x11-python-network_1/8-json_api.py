#!/usr/bin/python3
"""
A Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
the letter must be ssent in the variable q.

If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 2:
        q = argv[1]
    else:
        q == ''
    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': q})
    try:
        response_dict = response.json()
        id = response_dict.get('id')
        name = response_dict.get('name')
        if len(response_dict) == 0 or not id or not name:
            print('No Result')
        else:
            print('[{}] {}'.format(response_dict.get('id'),
                                   response_dict.get('name')))
    except:
        print('Not a valid JSON')
