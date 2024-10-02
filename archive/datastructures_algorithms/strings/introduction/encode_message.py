"""Problem Statement
You have been given a text message. You have to return the Run-length Encoding of the given message.
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to
represent repeated successive characters as the character and a single count. For example,
the string "aaaabbbccdaa" would be encoded as "a4b3c2d1a2"."""

from collections import *
from math import *
from os import *
from sys import *


def encode(message):
    # Write your code here.
    ans = ""
    count = 1
    for i in range(len(message)):
        if i < len(message) - 1 and message[i] == message[i + 1]:
            count += 1
        else:
            ans += message[i] + str(count)
            count = 1
    return ans


assert encode("abbdcaas") == "a1b2d1c1a2s1"
