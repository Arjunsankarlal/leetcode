"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
"""

from collections import Counter


def valid_anagram(s, t):
    """
    Get the word count mapping for both string and compare it.

    :param s:
    :param t:
    :return:
    """
    sc = Counter(s)
    st = Counter(t)
    return sc == st


print(valid_anagram("arjun", "nujra"))
