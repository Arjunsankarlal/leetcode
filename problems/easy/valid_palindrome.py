"""
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


def valid_palindrome(text):
    """
    Cleans up the string by only considering digits and characters, then
    actual string == reverse string would do the trick.
    :param text:
    :return:
    """
    modified = ""
    for i in text:
        if i.isalpha() or i.isdigit():
            modified += i.lower()
    print(modified)
    if modified == modified[::-1]:
        return True
    else:
        return False


print(valid_palindrome("mad249aM"))
