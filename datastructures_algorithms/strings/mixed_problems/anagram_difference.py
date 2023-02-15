"""
roblem Statement
You have been given two strings, let's say 'STR1' and 'STR2' of equal lengths.
You are supposed to return the minimum number of manipulations required to make the two strings anagrams.
Note:
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase. 
We can generalise this in string processing by saying that an anagram of a string is another string with the same quantity of each character in it, in any order.
Example:
String “eat” and “ate” are anagram to each other but string “buy” and “bye” are not.
Test Case:
For input as except, accept; output will be 2
"""

import math


def getMinimumAnagramDifference(str1, str2):
    count = 0
    for c in str1:
        if c in str2:
            str2 = str2.replace(c, "", 1)
        else:
            count += 1
    return count


assert getMinimumAnagramDifference("except", "accept") == 2

assert getMinimumAnagramDifference("buy", "bye") == 1
