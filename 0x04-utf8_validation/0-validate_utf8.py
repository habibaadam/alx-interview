#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Checks if a given data set represents a valid UTF-8 encoding.

    This function iterates through each byte in the data and analyzes
    its binary representation to determine if it follows the UTF-8 encoding
    rules. It tracks the expected number of continuation bytes for
    multi-byte characters and checks for invalid sequences or byte formats.

    Args:
        data: A byte sequence representing the text to be validated.

    Returns:
        True if the data represents a valid UTF-8 encoding,
        False otherwise.
    """
    bytes = 0
    for n in data:
        byte = format(n, '#010b')[-8:]
        if bytes == 0:
            if byte[0] == '1':
                bytes = len(byte.split('0')[0])
            if bytes > 4 or bytes == 1:
                return False
            if bytes == 0:
                continue
        else:
            if not byte.startswith('10'):
                return False
        bytes -= 1
    return bytes == 0
