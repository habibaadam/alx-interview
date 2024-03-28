#!/usr/bin/python3
"""This script reads stdin line by line
and computes metrics
"""

import sys
import re

status_code_count = {}
total_file_size = 0
num_of_read = 0

try:
    for line in sys.stdin:
        num_of_read += 1
        r = re.search(
            '^\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3}\\s-\\s\\[[\\d -:.]*\
\\]\\s"GET\\s\\/projects\\/260\\sHTTP\\/1.1"\\s\\d{1,3}\\s\\d{1,4}$',
            line)
        if r:
            status = re.search("(?<=1.1\" )\\d{1,3}", line)
            file_size = re.search("\\d{1,4}$", line)
            if status_code_count.get(status.group()):
                status_code_count[status.group()] = status_code_count.get(
                    status.group()) + 1
            else:
                status_code_count[status.group()] = 1
            total_file_size = total_file_size + int(file_size.group())
        else:
            continue

        if num_of_read % 10 == 0:
            print(f"File size: {total_file_size}")
            for status in sorted(status_code_count):
                print(f"{status}: {status_code_count[status]}")

finally:
    print(f"File size: {total_file_size}")
    for status in sorted(status_code_count):
        print(f"{status}: {status_code_count[status]}")
