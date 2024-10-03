"""
1071_greatest_common_divisor_of_strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

"""


def is_str_repeated(unit, string):
    j = len(unit)
    initial = unit
    for k in range(0, len(string), j):
        if string[k:k + j] != initial:
            return False
    return True


def gcd_of_strings(str1: str, str2: str) -> str:
    output = ""
    smaller = str1 if len(str1) < len(str2) else str2
    larger = str1 if len(str1) >= len(str2) else str2
    i = 1
    while i <= len(smaller):
        j = len(smaller) // i
        if len(smaller) % j == 0 and len(larger) % j == 0:
            unit = smaller[0:j]
            if is_str_repeated(unit, smaller) and is_str_repeated(unit, larger):
                output = unit
                break
        i = i + 1
    return output


if __name__ == "__main__":
    assert gcd_of_strings("ABCABC", "ABC") == "ABC"
    assert gcd_of_strings("ABABAB", "ABAB") == "AB"
    assert gcd_of_strings("LEET", "CODE") == ""
    assert gcd_of_strings("NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM",
                          "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM") == "NLZGM"
