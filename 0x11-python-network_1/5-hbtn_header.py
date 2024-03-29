#!/usr/bin/python3
"""sends a request to the URL and displays the
value of the variable X-Request-Id"""
import requests
import sys


def send():
    """print X-Request-Id"""
    res = requests.get(sys.argv[1])
    id = res.headers.get('X-Request-Id')
    print(id)


if __name__ == '__main__':
    send()
