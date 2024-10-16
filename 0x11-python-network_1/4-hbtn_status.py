#!/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status by requests
"""
import requests
if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.text
        print("Body response:")
        print("\t" + "- type:" + " {}".format(type(data)))
        print("\t" + "- content:" + " {}".format(data))
