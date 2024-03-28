#!/usr/bin/python3
""" takes in a URL and an email and sends a POST request"""
from urllib import request, parse
import sys


def post():
    """take in a url and email and send post request"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({"email": email}).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        out = res.read().decode('utf-8')
        print(out)


if __name__ == "__main__":
    post()
