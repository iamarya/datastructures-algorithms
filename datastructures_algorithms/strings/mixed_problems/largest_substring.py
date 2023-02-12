"""
Problem Statement
You are given a string 'S' of length 'N' consisting of lowercase English alphabet letters. You are also given a positive integer 'K'.
Now, a substring of this string is good if it contains at most 'K' distinct characters. A string 'X' is a substring of string 'Y' 
if it can be obtained by deletion of several continuous elements(possibly zero) from the beginning and the end from the string 'Y'.
Your task is to return the maximum size of any good substring of the string 'S'.
Example:
‘S’ = “bacda” and ‘K’ = 3.

So, the substrings having at most ‘3’ distinct characters are called good substrings. Some possible good substrings are:
1. “bac”
2. “acd”
3. “acda”

The substring “acda” is the largest possible good substring, as we cannot get any other substring of length 5 or more having distinct 
characters less than or equal to ‘3’. Thus, you should return ‘4’ as the answer.
"""


def getLengthofLongestSubstring(s, k):
    max_count = 0
    count_distinct_char = 0
    for i in range(len(s)):
        temp_string = s[i]
        count_distinct_char = 1
        for j in range(i + 1, len(s)):
            if s[j] not in temp_string:
                # i+=1 is the same as i=i+1, whereas i=+1 just means i=(+1).
                count_distinct_char += 1
            if s[j] in temp_string or count_distinct_char <= k:
                temp_string = temp_string + s[j]
            if count_distinct_char > k or j == len(s) - 1:
                break
        max_count = max(max_count, len(temp_string))
    return max_count


assert (
    getLengthofLongestSubstring("abcbc", 2) == 4
), f'But value is {getLengthofLongestSubstring("abcbc", 2)}'

assert (
    getLengthofLongestSubstring("k", 1) == 1
), f'But value is {getLengthofLongestSubstring("k", 1)}'
