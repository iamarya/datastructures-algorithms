"""
Problem Statement
You are given a string STR of length N. Your task is to remove all the vowels present in that string and print the modified string.
English alphabets ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ are termed as vowels. All other alphabets are called consonants.
"""


def remove_vowels(input_string: str):
    output = ""
    for c in input_string:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            output = output + c
    return output


assert remove_vowels("CodeGeek") == "CdGk"

# one liner way
def remove_vowels_v2(input_string: str):
    return "".join(
        [c for c in input_string if c.lower() not in ["a", "e", "i", "o", "u"]]
    )


assert remove_vowels_v2("CodeGeek") == "CdGk"
