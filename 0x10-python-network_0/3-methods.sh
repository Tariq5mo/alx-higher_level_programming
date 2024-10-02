#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -s -L -X OPTIONS -I "$1" | grep Allow | cut -d " " -f 2-
