#!/usr/bin/python3
"""
a function that determines if a box can be opened with a list of keys
stored in boxes containing list of lists
"""


def canUnlockAll(boxes):
    """
    Function checking if boxes can be unlocked
    Args:
    boxes: list of lists
    Returns: True or False
    """
    startpoint = 0
    unlocked = {}

    for everybox in boxes:
        if len(everybox) == 0 or startpoint == 0:
            unlocked[startpoint] = "unlocked"
        for key in everybox:
            if key < len(boxes) and key != startpoint:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        startpoint += 1
    return False
