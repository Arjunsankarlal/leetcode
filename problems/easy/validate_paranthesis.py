"""
https://leetcode.com/problems/valid-parentheses/description/
"""


def validate_parentheses(text):
    """
    This is a classic problem with classic solution, stack is the only way to go here.

    :param text:
    :return:
    """
    stack = []
    if len(text) == 0:
        return True
    for i in text:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop(-1)
            if (x == "{" and i != "}") or (x == "(" and i != ")") or (x == "[" and i != "]"):
                return False
    if len(stack) != 0:
        return False
    return True


print(validate_parentheses("{}"))
print(validate_parentheses("{}()[]"))
print(validate_parentheses("[}"))
print(validate_parentheses("{([])}"))
print(validate_parentheses("{([[])}"))
