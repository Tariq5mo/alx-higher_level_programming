#!/bin/bash
# Set A header variable X-School-User-Id to the value 98
curl -sL -H "X-School-User-Id: 98" "$1"
