#!/usr/bin/python3
"""post an email"""
import requests
import sys


def send():
    """post an email"""
    req = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(req.text)


if __name__ == '__main__':
    send()
