"""
Problem Statement
Given a string "pattern", which contains only two types of characters ‘(’, ‘)’.
Your task is to find the minimum number of parentheses either ‘(’, ‘)’ we must add the parentheses in string ‘pattern’ and the resulted string is valid.
Condition for valid string-
Every opening parenthesis ‘(’ must have a correct closing parenthesis ‘)’.
Example - ‘(()(()))’, ‘()()()’, ‘((()))’ are valid string, and ‘(((’, ‘(()’, ‘)(())’ are invalid string.
Testcase: For )((() output will be 3
"""

# Return the minimum number of parentheses required.
def minimumParentheses(pattern: str):
    while "()" in pattern:
        pattern = pattern.replace("()", "")
    return len(pattern)


# In separate way use a stack to put parenthesis and remove '(' whenever a ')' is encountered. Whenever a required
# '(' is not available increase the counter by 1.

assert minimumParentheses("(((((") == 5
assert minimumParentheses("))(") == 3
assert minimumParentheses(")((()") == 3

