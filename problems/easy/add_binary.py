"""
https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a, b):
    """
    Convert the string to list of int and reverse them, add padding for smaller list
    Add one by one, maintain carry and at last check carry and add accordingly
    Reverse the list, int to str, join and return

    :param a:
    :param b:
    :return:
    """
    a = [int(i) for i in a][::-1]
    b = [int(i) for i in b][::-1]
    print(a, b)
    carry = 0
    if len(a) > len(b):
        b += (len(a) - len(b)) * [0]
    elif len(a) < len(b):
        a += (len(b) - len(a)) * [0]

    ans = []
    for x, y in zip(a, b):
        if x + y + carry == 3:
            ans.append(1)
            carry = 1
        elif x + y + carry == 2:
            ans.append(0)
            carry = 1
        elif x + y + carry == 1:
            ans.append(1)
            carry = 0
        else:
            ans.append(0)
            carry = 0
    if carry:
        ans.append(1)
    return "".join([str(i) for i in ans[::-1]])


print(add_binary("1111", "001"))
print(add_binary("11", "1"))
print(add_binary("1010", "1011"))
print(add_binary("1", "111"))
