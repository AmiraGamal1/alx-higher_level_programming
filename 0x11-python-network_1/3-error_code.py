#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the
response
"""
import sys
from urllib import request, error


def send():
    """send a request to the url and handle error"""
    try:
        with request.urlopen(sys.argv[1]) as req:
            res = req.read().decode('utf-8')
            print(res)
    except error.HTTPError as e:
        print('Error code: ' + str(e.code))


if __name__ == '__main__':
    send()
