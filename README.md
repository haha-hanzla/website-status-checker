# Website Status Checker

A simple Python program that checks if websites are **UP** or **DOWN**.
It shows the status code and how fast each website responds, and saves
the results in a log file.

> This project is for learning purposes. Only check websites you are allowed to test.

## Features

- Check many websites in one run
- Read websites from a file (`websites.txt`) or from the command line
- Shows status code (200, 404, 500, etc.) and response time
- Detects timeouts and connection errors
- Adds `https://` automatically if you forget it
- Saves every result with date and time in `status_log.txt`

## What You Need

- Python 3
- The `requests` library

## Installation

```bash
git clone https://github.com/your-username/website-status-checker.git
cd website-status-checker
pip install -r requirements.txt
```

## How to Use

**Option 1: Check the websites listed in `websites.txt`**

```bash
python website_checker.py
```

**Option 2: Type the websites in the command line**

```bash
python website_checker.py google.com github.com
```

## Example Output

```
============================================================
WEBSITE STATUS CHECKER
Time: 2026-10-09 18:30:00
============================================================
https://google.com
   Status: UP | Code: 200 | Time: 0.21s
https://thiswebsitedoesnotexist12345.com
   Status: DOWN | Code: No connection | Time: 0s
============================================================
Total checked: 2
UP: 1  DOWN: 1
Results saved in status_log.txt
```

## How It Works

1. The program gets a list of websites.
2. For each website it sends a request using `requests.get()`.
3. If the status code is below 400, the website is **UP**. Otherwise it is **DOWN**.
4. If the website does not answer in 5 seconds, it is marked **DOWN** (Timeout).
5. The result is printed and saved in the log file.

## Common Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK, website is working |
| 301 / 302 | Redirect |
| 403 | Forbidden |
| 404 | Page not found |
| 500 | Server error |

## Project Files

```
website-status-checker/
├── website_checker.py   # main program
├── websites.txt         # list of websites to check
├── requirements.txt     # libraries needed
├── .gitignore
└── README.md
```

## What I Learned

- Sending HTTP requests with the `requests` library
- Understanding HTTP status codes
- Handling errors with `try` and `except`
- Reading and writing files in Python

## Future Ideas

- Check websites again every few minutes
- Send an email when a website goes down
- Save results in a CSV file

## License

MIT License
