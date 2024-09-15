#!/bin/bash
# Displays the size of the body of the response
curl -I -s "$1" | grep Content-Length | cut -d " " -f 2
