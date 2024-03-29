#!/usr/bin/python3
"""handle error code"""
import requests
import sys


def send():
    """send request"""
    req = requests.get(sys.argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))


if __name__ == "__main__":
    send()
