#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys, requests
if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = {"q": sys.argv[1]}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        j = resp.json()
        if len(j) == 0:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
    except ValueError:
        print("Not a valid JSON")
