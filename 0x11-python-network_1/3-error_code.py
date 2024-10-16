#!/usr/bin/python3
"""a Python script that manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""
from urllib import request
from sys import argv
from urllib.error import HTTPError
if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as resp:
            data = resp.read()
            print(data.decode("UTF-8"))
    except HTTPError as e:
        print("Error code: " + str(e.code))
