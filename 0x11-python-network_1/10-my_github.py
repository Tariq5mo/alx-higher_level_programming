#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
from requests import get
from sys import argv
response = get("https://api.github.com/user", auth=(argv[1], argv[2]))
print(response.json().get("id"))
