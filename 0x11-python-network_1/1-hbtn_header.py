#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys


def send():
    """sends a request to the url"""
    with urllib.request.urlopen(sys.argv[1]) as req:
        x_request_id = req.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    send()
