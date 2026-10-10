# Website Status Checker
# This program checks if websites are UP or DOWN.
# It sends a request to each website and shows the status code
# and how long the website took to respond.
#
# NOTE: Use this only for learning and on websites you are allowed to test.

import sys
import time
from datetime import datetime

import requests  # install it with: pip install requests

# If you don't give any websites, the program reads them from this file
WEBSITES_FILE = "websites.txt"

# How many seconds to wait before we say the website is not responding
TIMEOUT = 5


def read_websites_from_file(filename):
    """Read websites from a text file (one website per line)."""
    websites = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()  # remove spaces and the newline

                # skip empty lines and comment lines that start with #
                if line == "" or line.startswith("#"):
                    continue

                websites.append(line)
    except FileNotFoundError:
        print("Error: file '" + filename + "' was not found.")
        sys.exit(1)

    return websites


def add_http_if_missing(url):
    """If the user typed 'google.com', change it to 'https://google.com'."""
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url


def check_website(url):
    """
    Check one website.
    Returns a tuple: (status, status_code, response_time)
    """
    try:
        start_time = time.time()
        response = requests.get(url, timeout=TIMEOUT)
        end_time = time.time()

        response_time = round(end_time - start_time, 2)
        status_code = response.status_code

        # Status codes below 400 mean the website worked
        # (200 = OK, 301/302 = redirect)
        if status_code < 400:
            return "UP", status_code, response_time
        else:
            # 404 = not found, 500 = server error, etc.
            return "DOWN", status_code, response_time

    except requests.exceptions.Timeout:
        return "DOWN", "Timeout", TIMEOUT

    except requests.exceptions.ConnectionError:
        return "DOWN", "No connection", 0

    except requests.exceptions.RequestException:
        return "DOWN", "Error", 0


def save_to_log(line):
    """Add one line to the log file so we can see the results later."""
    with open("status_log.txt", "a") as log_file:
        log_file.write(line + "\n")


def main():
    # If the user gave websites in the command line, use them.
    # Example: python website_checker.py google.com github.com
    if len(sys.argv) > 1:
        websites = sys.argv[1:]
    else:
        websites = read_websites_from_file(WEBSITES_FILE)

    if len(websites) == 0:
        print("No websites to check.")
        return

    print()
    print("WEBSITE STATUS CHECKER")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print()

    up_count = 0
    down_count = 0

    for website in websites:
        url = add_http_if_missing(website)
        status, code, response_time = check_website(url)

        print(url)
        print("   Status: " + status + " | Code: " + str(code) + " | Time: " + str(response_time) + "s")

        # Count the results
        if status == "UP":
            up_count = up_count + 1
        else:
            down_count = down_count + 1

        # Save the result in the log file
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_log(now + " | " + url + " | " + status + " | " + str(code) + " | " + str(response_time) + "s")

    print()
    print("Total checked:", len(websites))
    print("UP:", up_count, " DOWN:", down_count)
    print("Results saved in status_log.txt")


main()
