#!/usr/bin/python3
"""fetches The url https://alx-intranet.hbtn.io/status
"""
from urllib import request
if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:")
        print("\t" + "- type:" + " {}".format(type(data)))
        print("\t" + "- content:" + " {}".format(data))
        print("\t" + "- utf8 content:" + " {}"
              .format(data.decode("UTF-8")))
