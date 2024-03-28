#!/usr/bin/python3
"""fetch url"""
import urllib.request


def fetch():
    """print fetched url"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url:
        r = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode('utf8')))


if __name__ == "__main__":
    fetch()
