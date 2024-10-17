# 0x11. Python - Network #1

## What's the Deal?

In this project, we’re diving into Python networking. We’ll be using `urllib` and `requests` to fetch internet stuff, decode responses, and make all kinds of HTTP requests. By the end, we’ll be pros at grabbing JSON data and using it.

## What We Need to Know

- How to fetch internet resources with `urllib`
- Decoding `urllib` body responses
- Using `requests` for simpler HTTP requests
- Making GET, POST, PUT, etc. requests
- Fetching and using JSON data
- Handling data from external services

## Requirements

- Editors: `vi`, `vim`, `emacs`
- Python version: 3.8.5 on Ubuntu 20.04 LTS
- Style: Follow `pycodestyle` (version 2.8.*)
- Files must end with a new line and be executable
- First line: `#!/usr/bin/python3`
- Document all modules
- Use `get` for dictionary values
- Code shouldn’t run when imported (use `if __name__ == "__main__":`)

## Tasks

1. **What's my status? #0**
   - Fetch `https://alx-intranet.hbtn.io/status` with `urllib`
   - Show the response body
   - Use a `with` statement

2. **Response header value #0**
   - Send a request and display `X-Request-Id` from the response header
   - Use `urllib` and `sys`

3. **POST an email #0**
   - Send a POST request to a URL with an email param
   - Show the response body

4. **Error code #0**
   - Send a request and handle `urllib.error.HTTPError`
   - Print error code if status is ≥ 400

5. **What's my status? #1**
   - Fetch `https://alx-intranet.hbtn.io/status` with `requests`

6. **Response header value #1**
   - Send a request and display `X-Request-Id` with `requests`

7. **POST an email #1**
   - Send a POST request with an email param using `requests`

8. **Error code #1**
   - Send a request and show the response
   - Print `Error code: <status_code>` if status is ≥ 400

9. **Search API**
   - Send a POST request to `http://0.0.0.0:5000/search_user` with a letter param
   - Handle and display JSON responses

10. **My GitHub!**
    - Use GitHub API to display user ID with Basic Auth and a personal access token

11. **Time for an interview! (advanced)**
    - List 10 commits of the `rails` repo by the `rails` user using GitHub API

## How to Run It

Run the scripts with:

```bash
./<script_name> <arguments>
```

Make sure scripts are executable:

```bash
chmod +x <script_name>
```

Author
Tariq Omer
 touch!
