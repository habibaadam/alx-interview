#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (
if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys


def process_input():

    lines_read = 0
    possible_stat_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    total_size = 0

    try:
        # Read input from stdin line by line
        for line in sys.stdin:
            line = line.split(" ")  # split each line according to spaces
            if len(line) > 4:
                status_code = int(line[-2])

                # checking existence of status code in possible status code
                # increment the count of that status code
                if status_code in possible_stat_codes.keys():
                    possible_stat_codes[status_code] += 1

                file_size = int(line[-1])
                total_size += file_size

                # increment or count number of lines read
                lines_read += 1

            if lines_read == 10:
                lines_read = 0
                print(f"File size: {total_size}")

                for key, value in possible_stat_codes.items():
                    if value != 0:
                        print('{}: {}'.format(key, value))

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass

    finally:
        for key, value in possible_stat_codes.items():
            if value != 0:
                print('{}: {}'.format(key, value))


if __name__ == "__main__":
    process_input()
