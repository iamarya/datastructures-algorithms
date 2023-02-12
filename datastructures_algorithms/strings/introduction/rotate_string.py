"""
Problem Statement
You are given a string 'str' and an integer 'D'. Your task is to rotate the given string left (anticlockwise) and right (clockwise)
by 'D' units from the starting index. You are required to return the rotated string.
Ex: abcde, 2 => cdeab deabc
Note: need consider what will hapen if number of character rotation is greater than string length
"""


def leftRotate(strr, d):
    actual = d % len(strr)
    return strr[actual:] + strr[:actual]


def rightRotate(strr, d):
    actual = len(strr) - d % len(strr)
    return strr[actual:] + strr[:actual]


assert leftRotate("abcd", 2), rightRotate("abcd", 2) == ("abcd", "abcd")
assert leftRotate("abc", 4), rightRotate("abc", 4) == ("bca", "cab")

# string as index inclusive and ending index as excluding
assert "abcd"[1:3] == "bc", f'Got abcd"[0:3]" as {"abcd"[1:3]}'

# -1 is the index of last character, so exclusing the last character
assert "abcd"[:-1] == "abc"
