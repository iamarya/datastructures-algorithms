# Problem Statement
# You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.
# For example:
# If the given string 'STR' = ”I am a student of the third year” so you have to transform this string to ”I Am A Student Of The Third Year"

from os import *
from sys import *
from collections import *
from math import *


def convertString(str):
    # Write your code here
    newstr = ""
    nextToBeCap = True
    for c in str:
        if c == ' ':
            nextToBeCap = True
            newstr = newstr+" "
            continue
        if c != ' ' and nextToBeCap:
            newstr = newstr+c.upper()
            nextToBeCap = False
        else:
            newstr = newstr + c
    return newstr


assert convertString('I love programming') == 'I Love Programming'
