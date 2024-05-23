"""
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote
 can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
from collections import Counter


def is_ransom(ransom, magazine):
    mc = Counter(magazine)
    rc = Counter(ransom)
    for key, val in rc.items():
        if key in mc:
            if mc[key] >= val:
                continue
            else:
                return False
        else:
            return False
    return True


print(is_ransom("a", "b"))
print(is_ransom("a", "a"))
print(is_ransom("aa", "aab"))
