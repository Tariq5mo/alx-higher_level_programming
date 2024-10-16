#!/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    with request.urlopen(url) as resp:
        request.Request(url=url, data={"email", email})
        data = resp.read()
        print(data.decode("UTF-8"))
