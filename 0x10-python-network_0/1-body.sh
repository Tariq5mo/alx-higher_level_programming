#!/bin/bash
# Displays the body of the response
if [[ "$(curl -s -w '%{http_code}' -o >(cat > tmpfile) "$1")" == "200" ]]; then curl -s -f "$@"; fi; rm tmpfile
