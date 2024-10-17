#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {"email": email}
    encoded_data = parse.urlencode(data)
    byte_data = encoded_data.encode("UTF-8")
    with request.urlopen(url,) as resp:
        data = resp.read()
        print(data.decode("UTF-8"))
