#!/usr/bin/python3
"""fetches url use requests"""
import requests


def fetch():
    """fetch url"""
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == '__main__':
    fetch()
