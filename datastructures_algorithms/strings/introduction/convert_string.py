"""
Problem Statement:
You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.
For example:
If the given string 'STR' = ”I am a student of the third year” so you have to transform this string to ”I Am A Student Of 
The Third Year"

Intuition:
Describe your first thoughts on how to solve this problem.

Approach:
Describe your approach to solving the problem.

Time complexity:

Space complexity:

"""


def convert_string(str_value):
    '''Write your code here'''
    newstr = ""
    next_to_be_cap = True
    for c in str_value:
        if c == " ":
            next_to_be_cap = True
            newstr = newstr + " "
            continue
        if c != " " and next_to_be_cap:
            newstr = newstr + c.upper()
            next_to_be_cap = False
        else:
            newstr = newstr + c
    return newstr


assert convert_string("I love programming") == "I Love Programming"
