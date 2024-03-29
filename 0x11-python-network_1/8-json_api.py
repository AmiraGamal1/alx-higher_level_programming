#!/usr/bin/python3
"""search API"""
import requests
import sys


def send():
    """post request"""
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res = req.json()
        if bool(res) is False:
            print("NO result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except:
        print("Not a valid JSON")


if __name__ == '__main__':
    send()
