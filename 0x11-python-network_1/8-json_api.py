#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import sys, requests
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        j = resp.json()
        print(j)
        if len(j) == 0:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
    except ValueError:
        print("Not a valid JSON")
